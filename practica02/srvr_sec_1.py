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
	return render_template("reloj.html")

#Es la ruta principal, la que inicia los relojes
@app.route("/refresh_hour/<from>")
def getHourFromMaster():
    response = {'ok':False, 'description':""}
    #Solicitará la hora al maestro
    #Solicitará ritmo de reloj al maestro
	
    #Regresa el json de que se ha actualizado el reloj
    return jsonify( response )

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
	global hilo
	app.run(port=80, debug=True)
    h = Reloj("#"+str(hilo))
	relojes.append(h)
	relojes[0].start()
	print("Inició hilo:",hilo)
