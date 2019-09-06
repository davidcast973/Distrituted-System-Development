#!"C:/Program Files/Python37/python.exe"
from flask import Flask, jsonify, send_file, request, render_template ,render_template_string, make_response, send_from_directory
from flask_cors import CORS, cross_origin
import flask
import threading
import time
import datetime
import json
import requests

#Includes de práctica:
from classes.Reloj import Reloj

app = Flask(__name__)

hilo = 1
relojes = []

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



#Esta ruta predeterminada muestra la hora de este servidor
@app.route("/")
def goToMain():
	return render_template("reloj_srvr_secundario_2.html")

#Es la ruta principal, la que inicia los relojes
@app.route("/relojes/refresh_hour", methods=['POST'])
def getHourFromMaster():
    #Solicitará la hora al principal
	#Solicitará ritmo de reloj al principal
	r = requests.get("http://localhost:90/relojes/getTime/0/")
	salida = json.loads(r.text)
	horaSrvrPrincipal = salida['description']['tiempo']
	if r.status_code == 200 and salida['ok'] == True:
		now = datetime.datetime.now()
		principal = datetime.datetime( now.year, now.month, now.day, (horaSrvrPrincipal['hora']), (horaSrvrPrincipal['mins']), (horaSrvrPrincipal['segs']) )
		#Le resta 90 mins
		hora_modif_mins= principal - datetime.timedelta(minutes=90)
		relojes[0].hora = hora_modif_mins.hour
		relojes[0].mins = hora_modif_mins.minute
		relojes[0].segs = hora_modif_mins.second
		relojes[0].ritmo = salida['description']['velocidad_segundero']
		relojes[0].paused = salida['description']['pausado']

	#Regresa el json de que se ha actualizado el reloj
	return flask.redirect("/relojes/getTime/0/")

#Retorna un json 
@app.route("/relojes/getTime/<int:idReloj>/")
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
				}
			}
		})
	except Exception as ex:
		return jsonify({'ok':False, 'description': str(ex)})

if __name__ == "__main__":
	#Solicitará la hora al principal
	#Solicitará ritmo de reloj al principal
	r = requests.get("http://localhost:90/relojes/getTime/0/")
	salida = json.loads(r.text)
	horaSrvrPrincipal = salida['description']['tiempo']
	if r.status_code == 200 and salida['ok'] == True:
		now = datetime.datetime.now()
		principal = datetime.datetime( now.year, now.month, now.day, (horaSrvrPrincipal['hora']), (horaSrvrPrincipal['mins']), (horaSrvrPrincipal['segs']) )
		#Le suma 1 hora
		hora_modif_mins= principal - datetime.timedelta(minutes=90)
		h = Reloj("Secundario_02 #"+str(hilo), 
			hora = hora_modif_mins.hour, 
			mins = hora_modif_mins.minute,
			segs = hora_modif_mins.second
		)
		relojes.append(h)
		relojes[0].start()
		print("Inició hilo:",hilo)

	app.run(port=120, debug=True)

