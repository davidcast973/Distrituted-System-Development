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
import ntplib

sys.path.append("./classes")
sys.path.append("./procedures")
#Includes de práctica:
from classes.Reloj import Reloj
from procedures.timeServ import *
from procedures.coordinador import *

numeroServidor = int(sys.argv[1])
envGral = json.loads(open("./config/settings.json", "r").read())
try:
	env = envGral['server_clock_'+str(numeroServidor)]
except:
	env = envGral['server_'+str(numeroServidor)]

MI_PRIORIDAD = env['priority']


app = Flask(__name__)

prioridad_equipos = []
hilo = 1
relojes = []
date_time_str = '2019-10-13 15:00:27'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')


def get_ip(getPort = False):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
	finally:
		s.close()
	if getPort == True:
		return {'ip':IP, 'port':env['puerto']}
	return IP


#Esta ruta predeterminada lo redirije a /time
@app.route("/")
def goToMain():
	#Regresa un json dummy de relojes desplegados
	#return jsonify({'ok':True, 'description':'Deployed'})
	
	return flask.redirect("/time", code=302)

#Es la ruta de la vista del servidor de tiempo
@app.route("/time")
def main():
	#En esta vista se verá reflejada la hora del servidor de tiempo
	return render_template("server_time.html")

@app.route("/numeros/pausa/<int:idReloj>/<opcion>")
def pausaReloj(idReloj, opcion):
	if opcion == "pausa":
		relojes[idReloj].paused = False
	else:
		relojes[idReloj].paused = False
	return jsonify({'ok':True, 'description':{'reloj':idReloj, 'pausado':relojes[idReloj].paused}})

@app.route("/time/get-current-time/", methods=['POST', 'GET'])
def obtieneTiempoUTC():
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

def obtenUTCTime():
	 while True:
		  #c = ntplib.NTPClient()
		  # Provide the respective ntp server ip in below function
		  #response_utc_time = c.request('3.mx.pool.ntp.org', version=3)
		  relojUtc = datetime.datetime.now()
		  #return {'ok':True, 'description':{'UTC-Time':response_utc_time.tx_time, 'offset':response_utc_time.offset}}

		  #relojUtc = datetime.datetime.fromtimestamp(response_utc_time.tx_time)

		  if relojUtc.microsecond/1000 > 0.7:
			  suma = 1
		  else:
			  suma = 0

		  relojes[0].hora = relojUtc.hour
		  relojes[0].mins = relojUtc.minute
		  relojes[0].segs = relojUtc.second + suma
		  time.sleep(30)

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


'''
Eleccion de nuevo coordinador:
'''

@app.route("/coordinacion/nuevo-coordinador", methods=['POST'])
def valida_merecimiento():
	data = request.json
	print("Alguien quiere ser coordinador:", data)
	print("Alguien quiere ser coordinador:", data)
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


@app.route("/coordinacion/inicia-eleccion")
def inicia_eleccion_coord():
	my_ip = get_ip(getPort=True)
	my_address = my_ip['ip']+":"+str(my_ip['port'])
	a = iniciaEleccionNuevoCoordinador('tiempo', prioridad_equipos, my_address, MI_PRIORIDAD)
	if a == True:
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
			hiloUtc.join()
		except Exception as ex:
			#print(ex)
			pass
	return flask.redirect('/', code=302)

if __name__ == "__main__":
	global database

	for equipo in envGral:
		if 'server' in equipo:
			ip_server = envGral[equipo]['location']+':'+str(envGral[equipo]['puerto'])
			prioridad = envGral[equipo]['priority']

			prior_equipo = { 'direccion': ip_server, 'prioridad': prioridad }
			prioridad_equipos.append( prior_equipo )
	
	puertoServer = env['puerto']
	database = env['database']
	
	now = datetime.datetime.now()
	h = Reloj("Tiempo")
	
	relojes.append(h)
	print("Inició hilo:",hilo)
	relojes[0].start()
	hilo+=1

	hiloUtc = threading.Thread(target=obtenUTCTime, name="Obtiene hora de UTC Server")
	hiloUtc.start()

	app.run(port=puertoServer, debug=True, host='0.0.0.0')