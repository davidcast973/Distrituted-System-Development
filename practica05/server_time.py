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
from Reloj import Reloj

numeroServidor = int(sys.argv[1])
env = json.loads(open("./config/settings.json", "r").read())['server_clock_'+str(numeroServidor)]

app = Flask(__name__)

hilo = 1
relojes = []

#Esta ruta predeterminada lo redirije a /numeros
@app.route("/")
def goToMain():
	#Regresa un json dummy de relojes desplegados
	#return jsonify({'ok':True, 'description':'Deployed'})
	
	return flask.redirect("/coordinador", code=302)

#Es la ruta de la vista del coordinador
@app.route("/time")
def main():
	#En esta vista se reflejarán los envíos de cada servidor jugador (3 srvrs jugadores)
	return render_template("server_coordinador.html", servidor = numeroServidor)


@app.route("/time/get-current-time/", methods=['POST'])
def obtieneTiempoUTC():
	from datetime import timezone
	solicitud = request.json
	ipServer = solicitud['ip_server']
	start_timing_client = datetime.datetime.now()
	r = requests.post("http://{}/time/prueba-timing-time".format(ipServer))
	end_timing_client = datetime.datetime.now()

	c = ntplib.NTPClient()
	# Provide the respective ntp server ip in below function
	response_utc_time = c.request('3.mx.pool.ntp.org', version=3)
	response_utc_time.offset 
	# UTC timezone used here, for working with different timezones you can use [pytz library][1]
	#print("Timestamp:", response_utc_time.tx_time)

	#print ("Date UTC:",datetime.datetime.fromtimestamp(response_utc_time.tx_time, timezone.utc))

	timeDif = end_timing_client-start_timing_client

	miliSecs = timeDif.microseconds / 1000
	end_all = datetime.datetime.now()

	resta_final = end_all - start_timing_client

	sumaFinal = ((timeDif.microseconds)/2)+resta_final.microseconds
	secondsSumaFinal = sumaFinal/(1000000)



	return jsonify(ok=True, description={"UTC-time":response_utc_time.tx_time, "ajuste":secondsSumaFinal})

#Retorna un json 
@app.route("/time/getTime/<int:idReloj>/")
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


if __name__ == "__main__":
	global database
	
	puertoServer = env['puerto']
	database = env['database']
	
	now = datetime.datetime.now()
	app.run(port=puertoServer, debug=True, host='0.0.0.0')