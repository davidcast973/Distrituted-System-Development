#!"C:/Program Files/Python37/python.exe"
from flask import Flask, jsonify, send_file, request, render_template ,render_template_string, make_response, send_from_directory
from flask_cors import CORS, cross_origin
import flask
import threading
import time

#Includes de práctica:
from classes.Reloj import Reloj

app = Flask(__name__)

hilo = 1
relojes = []

#Esta ruta predeterminada lo redirije a /relojes
@app.route("/")
def goToMain():
	return flask.redirect("/relojes", code=302)

#Es la ruta principal, la que inicia los relojes
@app.route("/relojes")
def main():
	global hilo
	for a in range(4):
		h = Reloj("#"+str(hilo))
		###Pensé que esto funcionaría :
		###h = threading.Thread(target=createHilos, name="Hilo "+str(hilo), args=("#"+str(hilo),) )
		### :(
		relojes.append(h)
		relojes[a].start()
		print("Inició hilo:",hilo)
		hilo+=1
		
	#Regresa un json dummy de relojes desplegados
	return jsonify({'ok':True, 'description':'Deployed'})

#Retorna un json 
@app.route("/relojes/getTime/<int:idReloj>/")
def getTimeFromClock(idReloj):
	try:
		return jsonify({'ok':True, 'description':relojes[idReloj]})
	except Exception as ex:
		return jsonify({'ok':False, 'description': str(ex)})

#Esta ruta/función será la que edite los relojes
@app.route("/relojes/edit/<int:idReloj>/<int:hora>/<int:mins>/<int:segs>", methods=['GET', 'POST'])
def editaReloj(idReloj,hora, mins, segs):
	try:
		relojes[idReloj].hora = hora
		relojes[idReloj].mins = mins
		relojes[idReloj].segs = segs
		#Regresa el json de edición correcta
		return jsonify({'ok':True, 'description':str(relojes[idReloj]) } )
	except Exception as ex:
		return jsonify({'ok':False, 'description': str(ex)})

if __name__ == "__main__":
	app.run(port=80, debug=True)

