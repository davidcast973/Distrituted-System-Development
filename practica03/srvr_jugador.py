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
resultados = [None]*3

#Esta ruta predeterminada lo redirije a /numeros
@app.route("/")
def goToMain():
	#Regresa un json dummy de relojes desplegados
	#return jsonify({'ok':True, 'description':'Deployed'})
	
	return flask.redirect("/reloj_maestro", code=302)

#Es la ruta de la vista del coordinador
@app.route("/coordinador")
def main():
	#En esta vista se reflejarán los envíos de cada servidor jugador (3 srvrs jugadores)
	return render_template("interfaz_coordinador.html")

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
		relojes[idReloj].paused = True
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

#Esta función enviará el archivo .txt al coordinador
def enviaTxt2Coordinador(datosRequest):
	pass

#Esta ruta/función, será la que recibirá el .txt de los front
#del servidor jugador
@app.route("/numeros/", methods=['POST'])
def sendNumbers():
	response = {'ok':False, 'description':""}
	datos = request
	enviaTxt2Coordinador(datos)
	return jsonify( response )


if __name__ == "__main__":
	now = datetime.datetime.now()
	h = Reloj("Jugador", hora=now.hour, mins=now.minute, segs=now.second)

	relojes.append(h)
	relojes[0].start()
	print("Inició hilo:",hilo)
	hilo+=1
	print("Inició Jugador X")
	app.run(port=80, debug=True, host='0.0.0.0')

