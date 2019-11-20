#!"C:/Program Files/Python37/python.exe"
from flask import Flask, jsonify, send_file, request, render_template ,render_template_string, make_response, send_from_directory
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import flask
import threading
import time
import requests
import json
import datetime
import os
import sys
import socket
import ntplib

sys.path.append("./../")

#Includes de práctica:
from practica06.classes.Reloj import Reloj
from practica06.procedures.timeServ import *
from practica06.procedures.coordinador import *

UPLOAD_FOLDER = './static/uploads/coordinador'
INTENTOS_MAX_GET_HORA = 2

numeroServidor = int(sys.argv[1])
#env = json.loads(open("./config/settings.json", "r").read())['server_clock_'+str(numeroServidor)]
envGral = json.loads(open("./config/settings.json", "r").read())
env = envGral['server_'+str(numeroServidor)]

MI_PRIORIDAD = env['priority']

#Configuración FLASK
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
PRIORIDAD = env['priority']

#Variables "globales"
hilo = 1
relojes = []
resultados = [None]*3
finalizo = [None]
prioridad_equipos = []
voBos = []
equipos_vivos = []
intentos_get_hora = 0
address_direccion_server_tiempo = envGral['server_clock_1']['location']+":"+str(envGral['server_clock_1']['puerto'])
address_to_forward = ""

#hiloTiempo = ""

caracter="sumas"

'''
----------------------------------------------------------------
----------------------------------------------------------------
FUNCIONES:
----------------------------------------------------------------
----------------------------------------------------------------
'''

'''
---------------------------------
Funciones server tiempo
'''

def obtenUTCTime():
	global relojes
	t = threading.currentThread()
	while getattr(t, "do_run", True):
		#c = ntplib.NTPClient()
		# Provide the respective ntp server ip in below function

		#Parece ser que está bloqueado en la red de ESCOM
		#response_utc_time = c.request('uk.pool.ntp.org', version=3)

		relojUtc = datetime.datetime.now()

		if relojUtc.microsecond/1000 > 0.7:
			suma = 1
		else:
			suma = 0

		relojes[0].hora = relojUtc.hour
		relojes[0].mins = relojUtc.minute
		relojes[0].segs = relojUtc.second + suma


		time.sleep(30)

'''
------------------------------------------
'''

#-------------------------------------------------------------------------
'''
-------------------------------
Funciones server coordinador sumas
'''
def forward_to_sum_server(full_path):
	return flask.redirect("http://{}/{}".format(address_to_forward, full_path), code=307)

def am_i_a_sum_server():
	if caracter == 'sumas':
		return True
	return False



def verificaHoraServerTime():
	global intentos_get_hora, caracter, hiloTiempo
	host_ip = get_ip()
	#print("Socket name info:",host_ip)

	#while True:
	hiloTiempo = threading.currentThread()
	while getattr(hiloTiempo, "do_run", True):
		print("Está en hilo de verificaHoraServerTime")

		now = datetime.datetime.now()
		reloj_local = datetime.datetime(
			now.year,now.month, now.day,
			#relojes[0].hora, relojes[0].mins, relojes[0].segs,tzinfo=datetime.timezone.utc
			relojes[0].hora, relojes[0].mins, relojes[0].segs
		)
		detalles_servidor = {
			"ip_server" : host_ip,
			"hora_server" : reloj_local.timestamp()
		}
		
		aux = ""
		try:
			print("Estoy pidiendo la nueva hora a:", address_direccion_server_tiempo)
			r = requests.post("http://{}/time/get-current-time/".format(address_direccion_server_tiempo), json=detalles_servidor)
			aux = r
			json_resp = json.loads(r.text)
		except:
			print("Entré en excepción porque r=",aux, "caracter=", caracter)
			print("Entré en excepción porque r=",aux, "caracter=", caracter)
			
			intentos_get_hora +=1
			if intentos_get_hora >= INTENTOS_MAX_GET_HORA and caracter == 'sumas':
				#INICIA PROCESO DE ELECCION
				my_ip = get_ip(getPort=True)
				my_address = my_ip['ip']+":"+str(my_ip['port'])
				a = iniciaEleccionNuevoCoordinador('tiempo', prioridad_equipos, my_address, MI_PRIORIDAD)
				if a == True:
					print("Ahora seré un servidor de TIEMPO!")
					print("Ahora seré un servidor de TIEMPO!")
					print("Ahora seré un servidor de TIEMPO!")
					hiloUtc = threading.Thread(target=obtenUTCTime, name="Obtiene hora de UTC Server")
					hiloUtc.start()
					caracter ='tiempo'
					print("Valor de caracter:", caracter)
					print("Valor de caracter:", caracter)
					print("Valor de caracter:", caracter)
					try:
						hiloTiempo.do_run = False
						#hiloTiempo.join()
					except Exception as ex:
						print("Excepción al tratar de matar hiloTiempo", ex, ":::::::::::::")
						pass
					print("Trataré de romper el hilo")
					if numeroServidor == 1:
						address_to_forward = envGral['server_2']['location']+":"+str(envGral['server_2']['puerto'])
					else:
						address_to_forward = envGral['server_1']['location']+":"+str(envGral['server_1']['puerto'])
					return True
				else:
					try:
						hiloUtc.do_run = False
						hiloTiempo.do_run = True
						#hiloUtc.join()
					except Exception as ex:
						print("Excepción al tratar de matar hiloUtc", ex, ":::::::::::::")
						pass

			time.sleep(10)

			continue
		if json_resp['ok'] == True:
			tiempo = json_resp['description']['UTC-time']+json_resp['description']['ajuste']
			utc_time = datetime.datetime.fromtimestamp( tiempo )

			#print("Hora local:", reloj_local.strftime("%Y-%m-%d %H:%M:%S"), "| Hora UTC:", utc_time.strftime("%Y-%m-%d %H:%M:%S"))

			if reloj_local < utc_time:
				print("SOLO SETEARÁ HORA!")
				print("SOLO SETEARÁ HORA!")
				#if utc_time.microsecond/1000 > 0.7:
				#	suma = 1
				#else:
				#	suma = 0
				
				relojes[0].hora = utc_time.hour
				relojes[0].mins = utc_time.minute
				relojes[0].segs = utc_time.second
				relojes[0].ritmo = 1
				print("Ritmo final:", relojes[0].ritmo)
				#hiloTime.join()
			else:
				print("Va a ralentizar")
				print("Va a ralentizar")
				
				relojes[0].ritmo += 5
		time.sleep(10)

'''
------------------------------------------
'''

#-------------------------------------------------------------------------

'''
-------------------------------
Funciones concenso:
'''

def validaConcenso():
	# Al momento de confirmar un coordinador, se manda a llamar a esta llamada.
	# Primera parte del concenso... Decirle a todos quién es mi coordinador
	# Luego esta se encarga de comunicarle a todos quién es cu coordinador
	# 
	my_ip = get_ip(getPort=True)
	my_address = my_ip['ip']+":"+str(my_ip['port'])

	global voBos
	voBos = []
	for equipo in prioridad_equipos:
		if equipo['direccion'] == my_address:
			continue
		share_coordinator = threading.Thread(target=comunicaCoordinador, name="Hilo que va preguntando quién es el coord de cada equipo", args=(equipo,))
		share_coordinator.start()
		share_coordinator.join()

def comunicaCoordinador( equipo_a_preguntar ):
	global voBos
	ruta = "/coordinacion/tell-me-your-coordinator"
	datos = {
		'my_coordinator':address_direccion_server_tiempo
	}
	try:
		r = requests.post("http://"+equipo_a_preguntar['direccion']+ruta, json=datos)
		response = json.loads(r.text)
		if response['ok'] == True:
			return True
		else:
			return False
	except Exception as ex:
		return False


def pingCheckServersAlive(equipo_a_preguntar):
	#global equipos_vivos
	equipos_vivos = []
	ruta_ping = "/time/prueba-timing-time"
	try:
		r = requests.post("http://"+equipo_a_preguntar+ruta_ping)
		response = json.loads(r.text)
		if response['ok'] == True:
			equipos_vivos.append(True)
		else:
			equipos_vivos.append(False)
	except Exception as ex:
		print("Parece ser que el servidor:",equipo_a_preguntar, "está muerto...")
		equipos_vivos.append(False)

def valida_nuevo_coordinador():
	# Cuando alguien me dice quién es su coordinador, yo valido quién es el de los demás
	# Segunda parte del concenso... Elegir al que diga la mayoría
	my_ip = get_ip(getPort=True)
	my_address = my_ip['ip']+":"+str(my_ip['port'])
	global voBos, address_direccion_server_tiempo
	for equipo in prioridad_equipos:
		if equipo['direccion'] == my_address:
			continue
		share_coordinator = threading.Thread(target=pingCheckServersAlive, name="Hilo que va preguntando quién es el coord de cada equipo", args=(equipo,))
		share_coordinator.start()
		share_coordinator.join()

	#De todos los servidores, los que en verdad hayan dado señales de vida
	solo_vivos = [x for x in equipos_vivos if x == True]
	mayoria = (len(solo_vivos)//2)+1
	if len(voBos)>mayoria:
		#Obtiene el de mayor ocurrencia
		print("Se cambiará por el concenso el resultado de address_direccion_server_tiempo, val actual:", address_direccion_server_tiempo)
		print("Se cambiará por el concenso el resultado de address_direccion_server_tiempo, val actual:", address_direccion_server_tiempo)
		print("Se cambiará por el concenso el resultado de address_direccion_server_tiempo, val actual:", address_direccion_server_tiempo)
		address_direccion_server_tiempo = max( voBos, key=voBos.count )
		print("--------------------------------")
		print("Nuevo valor por concenso para server tiempo:", address_direccion_server_tiempo)
		print("Nuevo valor por concenso para server tiempo:", address_direccion_server_tiempo)
		print("Nuevo valor por concenso para server tiempo:", address_direccion_server_tiempo)
	else:
		print("No se obtuvo mayoría:", voBos)
		print("No se obtuvo mayoría:", voBos)
		print("No se obtuvo mayoría:", voBos)


'''
------------------------------------------------------------------------
------------------------------------------------------------------------
Fin Funciones
------------------------------------------------------------------------
------------------------------------------------------------------------
'''

#--------------------------------------------------------------------------------------------------


'''
------------------------------------------------------------------------
------------------------------------------------------------------------
RUTAS Y HANDLERS:
------------------------------------------------------------------------
------------------------------------------------------------------------
'''

'''
----------------------------------------
Funciones server coordinador sumas
'''

#Esta ruta predeterminada lo redirije a /numeros
@app.route("/")
def goToMain():
	#Regresa un json dummy de relojes desplegados
	#return jsonify({'ok':True, 'description':'Deployed'})
	if am_i_a_sum_server() == True:
		return flask.redirect("/coordinador", code=302)
	else:
		return flask.redirect("/time", code=302)

#Es la ruta de la vista del coordinador
@app.route("/coordinador")
def main_coordinador():
	#En esta vista se reflejarán los envíos de cada servidor jugador (3 srvrs jugadores)
	return render_template("server_coordinador.html", servidor = numeroServidor)

#Retorna un json 
@app.route("/numeros/getTime/<int:idReloj>/")
def getTimeFromClock(idReloj):
	try:
		return jsonify({
			'ok':True, 
			'description':{
				"id_reloj":idReloj,
				"tiempo":{
					'hora': relojes[idReloj].hora,
					'mins': relojes[idReloj].mins,
					'segs': relojes[idReloj].segs
				},
				"velocidad_segundero" : relojes[idReloj].ritmo,
				"pausado" : relojes[idReloj].paused
			}
		})
	except Exception as ex:
		return jsonify({'ok':False, 'description': str(ex)})

#Esta ruta/función será la que edite los relojes
@app.route("/numeros/edit/<int:idReloj>/<int:hora>/<int:mins>", methods=['POST'])
def editaReloj(idReloj,hora, mins):#, segs):
	try:
		relojes[idReloj].hora = hora 
		relojes[idReloj].mins = mins 
		#Regresa el json de edición correcta
		return jsonify({'ok':True, 'description': {'reloj_afectado':idReloj, 'nuevo_valor':str(relojes[idReloj])} } )
	except Exception as ex:
		return jsonify({'ok':False, 'description': str(ex)})

@app.route("/numeros/pausa/<int:idReloj>/<opcion>")
def pausaReloj(idReloj, opcion):
	if opcion == "pausa":
		relojes[idReloj].paused = False
	else:
		relojes[idReloj].paused = False
	return jsonify({'ok':True, 'description':{'reloj':idReloj, 'pausado':relojes[idReloj].paused}})

@app.route("/numeros/<int:idReloj>/<opcion>")
def cambiaRitmo(idReloj, opcion):
	if am_i_a_sum_server() == False:
		return jsonify(ok=True, description='Disabled function')
	response = {'ok':False, 'description':""}
	try:
		if opcion=="A":
			if(relojes[idReloj].ritmo > 0.1):#es un tope... al llegar a 0 fallaba
				relojes[idReloj].ritmo -= 0.2
		if opcion == "D":
			relojes[idReloj].ritmo += 1
		response['ok'] = True
		response['description'] = "ritmo modificado: "+str(relojes[idReloj].ritmo)+" cambios/seg"
	except Exception as ex:
		print("Excepción en cambiaRitmo:", ex)
		response['description'] = str(ex)
	return jsonify( response )

#Esta ruta/función, será la que recibirá los archivos de los jugadores
@app.route("/numeros/save-sum-numbers", methods=['POST'])
def saveSumNumbers():
	if am_i_a_sum_server() == False:
		return forward_to_sum_server(request.full_path)
	response = {'ok':False, 'description':"Check on the console :D"}
	formReq = request.form
	numeroServer = formReq.get('servidor',-1)
	nombreEquipoOrigen = formReq.get('equipo',-1)
	file = request.files['archivoTxt']
	ip_origen = request.remote_addr

	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		
		listaNums = leeArchivoTxt( os.path.join(app.config['UPLOAD_FOLDER'], filename) )
		suma = sum(listaNums)

		print("Hará hilo...")
		hilo = threading.Thread(target=sendResultToOtherServer, name="Hilo_envio_datos_server", args=(ip_origen, numeroServer, suma, nombreEquipoOrigen))
		hilo.start()
		hilo.join()
		print("Se supone que terminó hilo...")

		resultados[int(numeroServer)-1]['suma'] = suma
		#print("SE cambiaron los numeros:", resultados[int(numeroServer)-1])
		guardado = guardaEnBd( ip_origen, numeroServer, suma, relojes[0], nombreEquipoOrigen, dbName=database)
		

		return jsonify( guardado )
	else:
		return jsonify( response )

@app.route("/numeros/save-result-peer", methods=["POST"])
def guardaResultadoOtroServidor():
	if am_i_a_sum_server() == False:
		return forward_to_sum_server(request.full_path)

	datos = request.json
	
	ip_origen = datos['ip_origin']
	numeroServer = datos['num_jugador_origin'] 
	suma = datos['resultado_suma']
	nombreEquipoOrigen = datos['nombre_equipo_origin']
	guardado = guardaEnBd( ip_origen, numeroServer, suma, relojes[0], nombreEquipoOrigen, dbName=database)

	return jsonify( guardado )
	

@app.route("/numeros/getResultOf/<int:idJugador>", methods=['GET'])
def exponeSumaDeJugador(idJugador):
	if am_i_a_sum_server() == False:
		return forward_to_sum_server(request.full_path)

	if idJugador in [0,1,2]:
		return jsonify(ok=True, description=resultados[idJugador])
	else:
		return jsonify(ok=False, description="Jugador Inexistente")


@app.route("/time/prueba-timing-time", methods=['POST'])
def pruebaDeReboteParaTiming():
	return jsonify(ok=True, description="Eco for timing")


'''
Fin funciones server coordinador sumas
----------------------------------------
'''
#-------------------------------------------------------------------------
'''
----------------------------------------------------------
Servidor de tiempo:
'''

#Es la ruta de la vista del servidor de tiempo
@app.route("/time")
def main_time():
	if am_i_a_sum_server() == True:
		return jsonify(ok=False, description="I'm not a time server")

	#En esta vista se verá reflejada la hora del servidor de tiempo
	return render_template("server_time.html")

@app.route("/time/get-current-time/", methods=['POST', 'GET'])
def sendCurrentTime():
	if am_i_a_sum_server() == True:
		return jsonify(ok=False, description="I'm not a time server")
	#global lastConnectToUTCServer
	from datetime import timezone
	solicitud = request.json
	ipServer = solicitud['ip_server']
	horaServer = solicitud['hora_server']
	#print("Solicitud recibida:", solicitud)
	start_timing_client = datetime.datetime.now()
	r = requests.post("http://{}/time/prueba-timing-time".format(ipServer))
	end_timing_client = datetime.datetime.now()
	now = datetime.datetime.now()

	#time = obtenUTCTime(date_time_obj, relojes[0])
	reloj_local = datetime.datetime(
		now.year,now.month, now.day,
		#relojes[0].hora, relojes[0].mins, relojes[0].segs,tzinfo=datetime.timezone.utc
		relojes[0].hora, relojes[0].mins, relojes[0].segs
	)

	response_utc_time = reloj_local.timestamp()
	offsetUtc = 0
	
	timeDif = end_timing_client-start_timing_client

	miliSecs = timeDif.microseconds / 1000
	end_all = datetime.datetime.now()

	resta_final = end_all - start_timing_client

	sumaFinal = ((timeDif.microseconds)/2)+resta_final.microseconds
	secondsSumaFinal = sumaFinal/(1000000) + offsetUtc

	hiloGuardadp = threading.Thread(
			target=guardaDatosHoraEnBd, 
			name="Guardado de datos hora en bd", 
			args=(
					relojes[0], 
					ipServer, 
					secondsSumaFinal, 
					horaServer,
					(timeDif.microseconds/2),
					"C"+str(numeroServidor)
			)
	)
	hiloGuardadp.start()

	return jsonify(ok=True, description={"UTC-time":response_utc_time, "ajuste":secondsSumaFinal})

'''
Fin servidor tiempo
----------------------------------------------------------
'''

'''
Eleccion de nuevo coordinador:
'''

@app.route("/coordinacion/nuevo-coordinador", methods=['POST'])
def valida_merecimiento():
	data = request.json
	print("Alguien quiere ser coordinador:", data)


	if data['prioridad'] < MI_PRIORIDAD:
		my_ip = get_ip(getPort=True)
		my_address = my_ip['ip']+":"+str(my_ip['port'])
		h = threading.Thread(target=iniciaEleccionNuevoCoordinador, name="Inicia nueva eleccion", args=(data['tipo_servidor'] , prioridad_equipos, my_address, MI_PRIORIDAD,) )
		h.start()
		return jsonify(ok=True, description={'accepted':False})
	else:
		#FALTA Switch para ahora pedir el tiempo al nuevo servidor
		return jsonify(ok=True, description={'accepted':True})

@app.route("/coordinacion/confirma-coordinador", methods=['POST'])
def confirma_nuevo_coordinador():
	global address_direccion_server_tiempo, caracter, address_to_forward
	data = request.json
	
	print("Me hizo la petición el host:\n",request.headers)
	print("......................................................")
	print("YA ME AVISARON QUE HAY UN NUEVO COORDINADOR:", data)
	print("YA ME AVISARON QUE HAY UN NUEVO COORDINADOR:", data)
	print("YA ME AVISARON QUE HAY UN NUEVO COORDINADOR:", data)
	if data['tipo_servidor'] == 'tiempo':
		address_direccion_server_tiempo = data['nuevo_coordinador']
		print("La nueva dirección del servidor de tiempo:\n", address_direccion_server_tiempo)
		print("--------------------------------------------------------------------------------------")
		caracter = "sumas"
		
		#hiloTiempo = threading.Thread(target=verificaHoraServerTime, name="Estabiliza tiempo")
		#hiloTiempo.start()
		hiloTiempo.do_run = True
		#validaConcenso()
		return jsonify(ok=True, description={'server_changed':True, 'details':"Changed to {}".format(address_direccion_server_tiempo)})
	else:
		return jsonify(ok=False, description={'server_changed':False, 'details':"Servidor inesperado:{}".format(data['tipo_servidor'])})
	# FALTA Switch para ahora pedir el tiempo al nuevo servidor
	# elif data['tipo_servidor'] == 'coordinador':
	# 	Switch para coordinador

@app.route("/coordinacion/inicia-eleccion")
def inicia_eleccion_coord():
	global caracter
	my_ip = get_ip(getPort=True)
	my_address = my_ip['ip']+":"+str(my_ip['port'])
	a = iniciaEleccionNuevoCoordinador('tiempo', prioridad_equipos, my_address, MI_PRIORIDAD)
	if a == True:
		#Resultó este servidor elegido como coordinador
		hiloUtc = threading.Thread(target=obtenUTCTime, name="Obtiene hora de UTC Server")
		hiloUtc.start()
		caracter ='tiempo'
		try:
			hiloTiempo.join()
		except Exception as ex:
			pass
		print("Trataré de romper el hilo")
	else:
		try:
			hiloUtc.do_run = False
			hiloTiempo.do_run = True
		except Exception as ex:
			#print(ex)
			pass
	return jsonify(ok=True, caracter=caracter)
	#return flask.redirect("/", code=302)

@app.route("/get-caracter")
def returnCaracter():
	return jsonify(ok=True, caracter=caracter)

'''
Fin Elección de nuevo coordinador
----------------------------------------------------------
'''

'''
Concenso:
'''


@app.route("/coordinacion/tell-me-your-coordinator", methods=['POST'])
def checkNewCoordinator():
	global voBos
	data = request.json
	voBos.append( data['my_coordinator'] )
	#valida_nuevo_coordinador(  )
	return jsonify(ok=True, description= 'Coordinator received: {}'.format(data['my_coordinator']) )


'''
------------------------------------------------------------------------
------------------------------------------------------------------------
FIN RUTAS Y HANDLERS
------------------------------------------------------------------------
------------------------------------------------------------------------
'''


if __name__ == "__main__":
	global database, hiloTiempo

	for equipo in envGral:
		if 'server' in equipo:
			ip_server = envGral[equipo]['location']+':'+str(envGral[equipo]['puerto'])
			prioridad = envGral[equipo]['priority']

			prior_equipo = { 'direccion': ip_server, 'prioridad': prioridad }
			prioridad_equipos.append( prior_equipo )

	voBos = [None]*len(prioridad_equipos)
	puertoServer = env['puerto']
	database = env['database']
	
	for a in range(0, len(resultados)):
		resultados[a] = {'idJugador': a, 'suma':'-'}

	
	relojes.append( Reloj("Coordinador_"+str(numeroServidor)+"_"+str(hilo)) )
	print("Relojes:", relojes)

	#relojes[0].printable = True
	relojes[0].start()
	print("Inició hilo:",relojes[0])

	#my_ip = get_ip(getPort=True)
	#my_address = my_ip['ip']+":"+str(my_ip['port'])
	#a = iniciaEleccionNuevoCoordinador('tiempo', prioridad_equipos, my_address, MI_PRIORIDAD)

	hiloTiempo = threading.Thread(target=verificaHoraServerTime, name="Estabiliza tiempo")
	hiloTiempo.start()
	print("Inició coordinador")



	app.run(port=puertoServer, debug=True, host='0.0.0.0', use_reloader=False)
	