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

sys.path.append("./classes")
sys.path.append("./procedures")
#Includes de práctica:
from Reloj import Reloj
from timeServ import *
from coordinador import *



UPLOAD_FOLDER = './static/uploads/coordinador'
numeroServidor = int(sys.argv[1])
#env = json.loads(open("./config/settings.json", "r").read())['server_clock_'+str(numeroServidor)]
env = json.loads(open("./config/settings.json", "r").read())['server_'+str(numeroServidor)]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
PRIORIDAD = env['time_priority']


hilo = 1
relojes = []
resultados = [None]*3
finalizo = [None]

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
	 while True:
		  c = ntplib.NTPClient()
		  # Provide the respective ntp server ip in below function
		  
		  #Parece ser que está bloqueado en la red de ESCOM
		  #response_utc_time = c.request('uk.pool.ntp.org', version=3)

		  relojUtc = datetime.datetime.now()

		  if relojUtc.microsecond/1000 > 0.5:
			  suma = 1
		  else:
			  suma = 0

		  relojes[0].hora = relojUtc.hour
		  relojes[0].mins = relojUtc.minute
		  relojes[0].segs = relojUtc.second + suma


		  time.sleep(30)

#-------------------------------------------------------------------------
'''
-------------------------------
Funciones server coordinador sumas
'''

def get_ip():
	 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	 try:
		  # doesn't even have to be reachable
		  s.connect(('10.255.255.255', 1))
		  IP = s.getsockname()[0]
	 except:
		  IP = '127.0.0.1'
	 finally:
		  s.close()
	 return IP

def verificaHoraServerTime():
	host_ip = get_ip()
	#print("Socket name info:",host_ip)

	while True:
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
		print("Estoy pidiendo la nueva hora...")
		r = requests.post("http://10.100.70.115/time/get-current-time/", json=detalles_servidor)
		try:
			json_resp = json.loads(r.text)
		except:
			continue
		if json_resp['ok'] == True:
			tiempo = json_resp['description']['UTC-time']+json_resp['description']['ajuste']
			utc_time = datetime.datetime.fromtimestamp( tiempo )

			#print("Hora UTC:", utc_time)
			#print("Hora Hilo:", horaLocal)
			print("Hora local:", reloj_local.strftime("%Y-%m-%d %H:%M:%S"), "| Hora UTC:", utc_time.strftime("%Y-%m-%d %H:%M:%S"))
			print("Hora local:", reloj_local.strftime("%Y-%m-%d %H:%M:%S"), "| Hora UTC:", utc_time.strftime("%Y-%m-%d %H:%M:%S"))
			print("Hora local:", reloj_local.strftime("%Y-%m-%d %H:%M:%S"), "| Hora UTC:", utc_time.strftime("%Y-%m-%d %H:%M:%S"))
			if reloj_local < utc_time:
				print("SOLO SETEARÁ HORA!")
				print("SOLO SETEARÁ HORA!")
				print("SOLO SETEARÁ HORA!")
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
				print("Va a ralentizar")
				print("Va a ralentizar")
				print("Va a ralentizar")
				relojes[0].ritmo += 5
		time.sleep(10)



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
	
	return flask.redirect("/coordinador", code=302)

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
	datos = request.json
	
	ip_origen = datos['ip_origin']
	numeroServer = datos['num_jugador_origin'] 
	suma = datos['resultado_suma']
	nombreEquipoOrigen = datos['nombre_equipo_origin']
	guardado = guardaEnBd( ip_origen, numeroServer, suma, relojes[0], nombreEquipoOrigen, dbName=database)

	return jsonify( guardado )
	

@app.route("/numeros/getResultOf/<int:idJugador>", methods=['GET'])
def exponeSumaDeJugador(idJugador):
	if idJugador in [0,1,2]:
		return jsonify(ok=True, description=resultados[idJugador])
	else:
		return jsonify(ok=False, description="Jugador Inexistente")

@app.route("/numeros/getUtcTime", methods=['GET'])
def obtieneTiempoUTC():
	global finalizo, relojes, hiloTime
	host_name = socket.gethostname() 
	host_ip = socket.gethostbyname(host_name)
	print("Socket name info:",host_ip)
	now = datetime.datetime.now()
	
	reloj_local = datetime.datetime(
		now.year,now.month, now.day,
		#relojes[0].hora, relojes[0].mins, relojes[0].segs,tzinfo=datetime.timezone.utc
		relojes[0].hora, relojes[0].mins, relojes[0].segs
	)

	tiempo = {
		"ip_server" : host_ip,
		"hora_server" : reloj_local.timestamp()
	}

	r = requests.post("http://10.100.70.115/time/get-current-time/", json=tiempo)

	json_resp = json.loads(r.text)

	if json_resp['ok'] == True:
		tiempo = json_resp['description']['UTC-time']+json_resp['description']['ajuste']
		#utc_time = datetime.datetime.fromtimestamp( tiempo, datetime.timezone.utc)
		utc_time = datetime.datetime.fromtimestamp( tiempo )
		reloj_local = datetime.datetime(
			now.year,now.month, now.day,
			#relojes[0].hora, relojes[0].mins, relojes[0].segs,tzinfo=datetime.timezone.utc
			relojes[0].hora, relojes[0].mins, relojes[0].segs
		)
		print("Hora UTC:", utc_time)
		print("Hora Hilo:", reloj_local)
		if utc_time >= reloj_local:
			print("UTC es mayor")
			relojes[0].hora = utc_time.hour
			relojes[0].mins = utc_time.minute
			relojes[0].segs = utc_time.second
			relojes[0].ritmo = 1
		else:
			print("Local es mayor")
			dif = utc_time-reloj_local
			relojes[0].ritmo += 5
			#hiloTime = threading.Thread(target=verificaHoraServerTime, name="Verifica_tiempo", args=(reloj_local,))
			#hiloTime.start()
	
	return flask.redirect("/", 302)


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
	#En esta vista se verá reflejada la hora del servidor de tiempo
	return render_template("server_time.html")

@app.route("/time/get-current-time/", methods=['POST', 'GET'])
def sendCurrentTime():
	global lastConnectToUTCServer
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
					(timeDif.microseconds/2)
			)
	)
	hiloGuardadp.start()

	return jsonify(ok=True, description={"UTC-time":response_utc_time, "ajuste":secondsSumaFinal})

'''
Fin servidor tiempo
----------------------------------------------------------
'''

'''
------------------------------------------------------------------------
------------------------------------------------------------------------
FIN RUTAS Y HANDLERS
------------------------------------------------------------------------
------------------------------------------------------------------------
'''


if __name__ == "__main__":
	global database	

	puertoServer = env['puerto']
	database = env['database']

	#now = datetime.datetime.now()
	#h = Reloj("Maestro", hora=now.hour, mins=now.minute, segs=now.second)
	h = Reloj("Maestro")
	
	relojes.append(h)
	print("Inició hilo:",hilo)
	relojes[0].start()
	hilo+=1
	
	for a in range(0, len(resultados)):
		resultados[a] = {'idJugador': a, 'suma':'-'}

	
	now = datetime.datetime.now()
	
	reloj_local = datetime.datetime(
		now.year,now.month, now.day,
		#relojes[0].hora, relojes[0].mins, relojes[0].segs,tzinfo=datetime.timezone.utc
		relojes[0].hora, relojes[0].mins, relojes[0].segs
	)
	hiloTiempo = threading.Thread(target=verificaHoraServerTime, name="Estabiliza tiempo")
	hiloTiempo.start()
	print("Inició coordinador")
	from coordinador import allowed_file, leeArchivoTxt, guardaEnBd, connectToBd,sendResultToOtherServer
	app.run(port=puertoServer, debug=True, host='0.0.0.0')