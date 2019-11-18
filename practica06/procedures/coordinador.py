import sys
import os
import datetime
import requests
import json
import pymysql
import time
import socket
import threading


sys.path.append("./libs")
sys.path.append("./../")
from sqlBd import Bd

ALLOWED_EXTENSIONS = {'txt'}

respuestas = []

hiloUtc = ""

def avisa_soy_nuevo_coordinador(tipoServer, equipo_destino, myIP, myPriority, location_array):
	global respuestas
	print("Le estoy avisando a {}, que quiero ser el coordinador".format(equipo_destino))
	url_avisa_coord = "/coordinacion/nuevo-coordinador"
	datos = {
		'nuevo_coordinador' : myIP,
		'tipo_servidor': tipoServer,
		'prioridad' : myPriority
	}
	try:
		r = requests.post("http://"+ equipo_destino['direccion'] + url_avisa_coord, json=datos)
		if r.status_code == 200:
			response = json.loads( r.text )
			respuestas[ location_array ] = response['description']['accepted']
	except Exception as ex:
		#print(ex)
		print("No le pude avisar a:", equipo_destino)
		respuestas[ location_array ] = None

def confirma_soy_nuevo_coordinador(tipoServer, equipo_destino, myIP):
	global respuestas
	url_confirma_coord = "/coordinacion/confirma-coordinador"
	print("Se va a setear al nuevo coordinador ubicado en:", myIP)
	datos = {
		'nuevo_coordinador' : myIP,
		'tipo_servidor': tipoServer
	}
	try:
		print("Haré petición de confirmación a:", "http://"+equipo_destino['direccion'] + url_confirma_coord)
		r = requests.post("http://"+ equipo_destino['direccion'] + url_confirma_coord, json=datos)
		#print("RESPUESTA DE confirmación que soy el coordinador:", r.text, "estatus:", r.status_code)
		if r.status_code == 200:
			response = json.loads( r.text )
		#	respuestas[ location_array ] = response['description']['accepted']
		#pass
	except Exception as ex:
		print("No se pudo hacer petición de confirmación a ", equipo_destino)
		pass

def iniciaEleccionNuevoCoordinador( tipoServer , prioridadEquipos, myIP, myPriority):
	global respuestas, hiloUtc
	print("Estoy iniciando proceso de elección")
	respuestas = [None]*len(prioridadEquipos)
	a = 0
	for equipo in prioridadEquipos:
		if equipo['direccion'] == myIP:
			print("Estoy haciendo skip para avisar :", equipo)
			print("Estoy haciendo skip para avisar :", equipo)
			print("Estoy haciendo skip para avisar :", equipo)
			print("Estoy haciendo skip para avisar :", equipo)
			print("Estoy haciendo skip para avisar :", equipo)
			print("Estoy haciendo skip para avisar :", equipo)
			print("Estoy haciendo skip para avisar :", equipo)
			print("Estoy haciendo skip para avisar :", equipo)
			continue
		if equipo['prioridad']>myPriority:
			#print("Le voy a avisar a {}, que quiero ser el coordinador".format(equipo))
			print("Iniciando hilo para avisarles")
			h = threading.Thread(target=avisa_soy_nuevo_coordinador, name="Avisa nuevo coord", args=(tipoServer, equipo,myIP,myPriority,a) ) 
			h.start()
			h.join()
		a+=1
		
	print("Valor de las respuestas de los demás para Bully:",respuestas)
	#input(".-.-.-.-.-.-")
	if False in respuestas:
		return False
	else:
		for equipo in prioridadEquipos:
			#print("Le estoy confirmando a {}, que seré el coordinador".format(equipo))
			if equipo['direccion'] == myIP:
				print("Estoy haciendo skip de mi dirección:", equipo)
				print("Estoy haciendo skip de mi dirección:", equipo)
				print("Estoy haciendo skip de mi dirección:", equipo)
				print("Estoy haciendo skip de mi dirección:", equipo)
				print("Estoy haciendo skip de mi dirección:", equipo)
				print("Estoy haciendo skip de mi dirección:", equipo)
				print("Estoy haciendo skip de mi dirección:", equipo)
				continue
			#Le avisa a todo mundo que él es el nuevo coordinador
			h = threading.Thread(target=confirma_soy_nuevo_coordinador, name="Avisa nuevo coord", args=(tipoServer, equipo, myIP) ) 
			h.start()
			h.join()
		return True

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def leeArchivoTxt(pathFilename):
	archivo = open(pathFilename, "r")
	numsStr = archivo.readlines()
	numsList = []
	for num in numsStr:
		numsList.append( int(num.strip()) )
	return numsList

#Esta función guardará los datos recibidos en la Base de datos
def guardaEnBd(ip_origen, numeroServer, suma, relojObject, nombreEquipo, dbName=None):
	resultado = {'ok':True, 'description':suma}

	now = datetime.datetime.now()
	datetimeServer = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" "

	datetimeServer += str(relojObject.hora)+":"+str(relojObject.mins)+":"+str(relojObject.segs)

	bd = connectToBd(dbName=dbName['name'])

	a = bd.doQuery("""
	INSERT INTO resultados_envios(date_added, ip_origen, nombre_equipo, num_jugador, resultado_suma) 
	VALUES('{}', '{}', '{}', '{}', '{}');""".format(
			str(datetimeServer), str(ip_origen), str(nombreEquipo), str(numeroServer), str(suma)
		)
	)
	resultado['description'] = "Resultado almacenado"

	return resultado

# def sendResultToOtherServer(ip_origen, numeroServer, suma, nombreEquipoOrigen):
# 	from server_coordinador import env
# 	print("Llegó a función de hilo")
# 	destino = env['send_to']
# 	data_to_send = {
# 		'ip_origin' : ip_origen,
# 		'num_jugador_origin' : numeroServer,
# 		'resultado_suma' : suma,
# 		'nombre_equipo_origin' : nombreEquipoOrigen
# 	}
# 	r = requests.post("http://"+destino+"/numeros/save-result-peer", json=data_to_send)
# 	print("Hizo petición de hilo y regresará")
# 	return r.text

def connectToBd(dbName=None):

	bd_name=dbName
	if dbName is None:
		bd_name = "resguardo_sumas_1"

	return Bd(	
		hostname = "10.100.70.115",
		username = "root",
		password = "12345",
		database = bd_name
	)