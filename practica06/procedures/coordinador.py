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
import server_coordinador

ALLOWED_EXTENSIONS = {'txt'}

respuestas = []

def avisa_soy_nuevo_coordinador(tipoServer, equipo_destino, myIP, myPriority, location_array):
	global respuestas
	url_avisa_coord = "/coordinacion/nuevo-coordinador"
	datos = {
		'nuevo_coordinador' : myIP,
		'tipo_servidor': tipoServer,
		'prioridad' : myPriority

	}
	r = requests.post( equipo_destino['direccion'] + url_avisa_coord, json=datos)
	if r.status_code == 200:
		response = json.loads( r.text )
		respuestas[ location_array ] = response['description']['accepted']

def confirma_soy_nuevo_coordinador(tipoServer, equipo_destino, myIP):
	global respuestas
	url_confirma_coord = "/coordinacion/confirma-coordinador"
	datos = {
		'nuevo_coordinador' : myIP,
		'tipo_servidor': tipoServer
	}
	r = requests.post( equipo_destino['direccion'] + url_confirma_coord, json=datos)
	if r.status_code == 200:
		response = json.loads( r.text )
		print("Respuesta confirmación de coordinador:", response)
	#	respuestas[ location_array ] = response['description']['accepted']
	#pass

def iniciaEleccionNuevoCoordinador( tipoServer , prioridadEquipos, myIP, myPriority):
	global respuestas
	respuestas = [None]*len(prioridadEquipos)
	a = 0
	for equipo in prioridadEquipos:
		a+=1
		if equipo['direccion'] == myIP:
			continue
		if equipo['prioridadEquipos']>myPriority:
			h = threading.Thread(target=avisa_soy_nuevo_coordinador, name="Avisa nuevo coord", args=(tipoServer, equipo,myIP,myPriority,a) ) 
			h.start()
	try:	
		h.join()
	except Exception as ex:
		#print(ex)
		pass
		
	print("Valor de las respuestas de los dema´s para Bully:",respuestas)
	if False in respuestas:
		return False
	else:
		for equipo in prioridadEquipos:
			if equipo['direccion'] == myIP:
				continue
		if equipo['prioridadEquipos']>myPriority:
			h = threading.Thread(target=confirma_soy_nuevo_coordinador, name="Avisa nuevo coord", args=(tipoServer, equipo, myIP) ) 
			h.start()

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

def sendResultToOtherServer(ip_origen, numeroServer, suma, nombreEquipoOrigen):
	from server_coordinador import env
	print("Llegó a función de hilo")
	destino = env['send_to']
	data_to_send = {
		'ip_origin' : ip_origen,
		'num_jugador_origin' : numeroServer,
		'resultado_suma' : suma,
		'nombre_equipo_origin' : nombreEquipoOrigen
	}
	r = requests.post("http://"+destino+"/numeros/save-result-peer", json=data_to_send)
	print("Hizo petición de hilo y regresará")
	return r.text

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