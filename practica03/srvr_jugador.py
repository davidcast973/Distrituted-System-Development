#!"C:/Program Files/Python37/python.exe"
from flask import Flask, jsonify, send_file, request, render_template ,render_template_string, make_response, send_from_directory
from flask_cors import CORS, cross_origin
import flask
import threading
import time
import requests
import json

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
	#return render_template("reloj.html")
	return render_template("reloj_srvr_principal.html")

#Es la ruta principal, la que inicia los relojes
@app.route("/relojes/refresh_hour", methods=['POST'])
def getHourFromMaster():
	r = requests.get("http://10.100.76.68/relojes/getTime/0/")
	salida = json.loads(r.text)
	horaSrvMaster = salida['description']['tiempo']
	if r.status_code == 200 and salida['ok'] == True:
		relojes[0].hora = horaSrvMaster['hora']
		relojes[0].mins = horaSrvMaster['mins']
		relojes[0].segs = horaSrvMaster['segs']
		relojes[0].ritmo = salida['description']['velocidad_segundero']
		relojes[0].paused = salida['description']['pausado']

	#Solicitará la hora al maestro
	#Solicitará ritmo de reloj al maestro
	
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
				},
				"velocidad_segundero" : relojes[idReloj].ritmo,
				"pausado" : relojes[idReloj].paused
			}
		})
	except Exception as ex:
		return jsonify({'ok':False, 'description': str(ex)})



if __name__ == "__main__":
		#Pide la hora al servidor maestro
	#Instancia el reloj de este servidor con la del maestro
	r = requests.get("http://10.100.76.68/relojes/getTime/0/")
	salida = json.loads(r.text)
	relojes=[]
	if r.status_code == 200 and salida['ok'] == True:
		horaSrvMaster = salida['description']['tiempo']
		h = Reloj("Principal #"+str(hilo), 
			hora=horaSrvMaster['hora'], 
			mins=horaSrvMaster['mins'],
			segs=horaSrvMaster['segs']
		)
		relojes.append(h)
		relojes[0].start()
		print("Inició hilo:",hilo)
	app.run(port=80, debug=True, host='0.0.0.0')
	