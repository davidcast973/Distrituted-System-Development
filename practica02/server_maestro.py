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

# Reloj maestro crea su propio Hilo


#Esta ruta predeterminada lo redirije a /relojes
@app.route("/")
def goToMain():
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
	#return jsonify({'ok':True, 'description':'Deployed'})
	
	return flask.redirect("/relojes", code=302)

#Es la ruta principal, la que inicia los relojes
@app.route("/relojes")
def main():
	return render_template("relojes.html")

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

#Esta ruta/función será la que edite los relojes
@app.route("/relojes/edit/<int:idReloj>/<int:hora>/<int:mins>", methods=['GET', 'POST'])
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
    			relojes[idReloj].ritmo -= 0.1
		if opcion == "D":
			relojes[idReloj].ritmo += 1
		response['ok'] = True
		response['description'] = "ritmo modificado: "+str(relojes[idReloj].ritmo)+" cambios/seg"
	except Exception as ex:
		print("Excepción en cambiaRitmo:", ex)
		response['description'] = str(ex)
	return jsonify( response )
if __name__ == "__main__":
	app.run(port=80, debug=True)

