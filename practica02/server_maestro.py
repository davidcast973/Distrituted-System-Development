#!"C:/Program Files/Python37/python.exe"
from flask import Flask, jsonify, send_file, request, render_template ,render_template_string, make_response, send_from_directory
from flask_cors import CORS, cross_origin
import flask
import threading
import time
import requests
import json
import datetime

#Includes de práctica:
from classes.Reloj import Reloj

app = Flask(__name__)

hilo = 1
relojes = []

#Esta ruta predeterminada lo redirije a /relojes
@app.route("/")
def goToMain():
	#Regresa un json dummy de relojes desplegados
	#return jsonify({'ok':True, 'description':'Deployed'})
	
	return flask.redirect("/reloj_maestro", code=302)

#Es la ruta principal, la que inicia los relojes
@app.route("/reloj_maestro")
def main():
	return render_template("reloj_maestro.html")

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

#Esta ruta/función será la que edite los relojes
@app.route("/relojes/edit/<int:idReloj>/<int:hora>/<int:mins>", methods=['POST'])
def editaReloj(idReloj,hora, mins):#, segs):
	try:
		relojes[idReloj].hora = hora 
		relojes[idReloj].mins = mins 
		#Regresa el json de edición correcta
		return jsonify({'ok':True, 'description': {'reloj_afectado':idReloj, 'nuevo_valor':str(relojes[idReloj])} } )
	except Exception as ex:
		return jsonify({'ok':False, 'description': str(ex)})

@app.route("/relojes/pausa/<int:idReloj>/<opcion>")
def pausaReloj(idReloj, opcion):
	if opcion == "pausa":
		relojes[idReloj].paused = True
	else:
		relojes[idReloj].paused = False
	return jsonify({'ok':True, 'description':{'reloj':idReloj, 'pausado':relojes[idReloj].paused}})

@app.route("/relojes/<int:idReloj>/<opcion>")
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

#Esta ruta/función, será el detonador que actualizará a los demás servidores
@app.route("/relojes/sendUpdate", methods=['POST'])
def sendUpdateTo():

	response = {'ok':False, 'description':""}
	actualizados = {}
	now = datetime.datetime.now()
	try:
		#Petición para actualizar principal
		principal = requests.post("http://localhost:90/relojes/refresh_hour")
		salida = json.loads(principal.text)
		actualizados['principal'] = {'updated':salida['ok'] }
	except Exception as ex:
		actualizados['principal'] = {'updated':False, 'error':str(ex) }
	
	try:
		#Petición para actualizar secundario 1
		srv_sec_1 = requests.post("http://localhost:100/relojes/refresh_hour")
		salida = json.loads(srv_sec_1.text)
		actualizados['secundario_01'] = {'updated':salida['ok'] }
	except Exception as ex:
		actualizados['secundario_01'] = {'updated':False, 'error':str(ex) }
	
	try:
		#Petición para actualizar secundario 2
		srv_sec_2 = requests.post("http://localhost:120/relojes/refresh_hour")
		salida = json.loads(srv_sec_2.text)
		actualizados['secundario_02'] = {'updated':salida['ok']}
	except Exception as ex:
		actualizados['secundario_02'] = {'updated':False, 'error':str(ex)}

	response['ok'] = actualizados['principal']['updated'] and \
						actualizados['secundario_01']['updated'] and \
						actualizados['secundario_02']['updated']
	#Formatear la respuesta con la info de exito o fracaso de update en 
	#cada servidor
	end = datetime.datetime.now()
	response['description'] = actualizados
	response['timing'] = str(end - now)
	return jsonify( response )


if __name__ == "__main__":
	now = datetime.datetime.now()
	h = Reloj("Maestro", hora=now.hour, mins=now.minute, segs=now.second)
	
	###Pensé que esto funcionaría :
	###h = threading.Thread(target=createHilos, name="Hilo "+str(hilo), args=("#"+str(hilo),) )
	### :(
	relojes.append(h)
	relojes[0].start()
	print("Inició hilo:",hilo)
	hilo+=1
	app.run(port=80, debug=True)

