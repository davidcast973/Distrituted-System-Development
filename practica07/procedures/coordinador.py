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
ack_replicaciones = []

hiloUtc = ""


def avisa_soy_nuevo_coordinador(tipoServer, equipo_destino, myIP, myPriority, location_array):
	global respuestas
	print("Le estoy avisando a {}, que quiero ser el COORD d {}".format(equipo_destino, tipoServer))
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
	print("Se va a setear al nuevo coordinador {} ubicado en: {}".format(tipoServer,myIP))
	datos = {
		'nuevo_coordinador' : myIP,
		'tipo_servidor': tipoServer
	}
	try:
		print("Haré confirmación a:", "http://"+equipo_destino['direccion'] + url_confirma_coord)
		r = requests.post("http://"+ equipo_destino['direccion'] + url_confirma_coord, json=datos)
		#print("RESPUESTA DE confirmación que soy el coordinador:", r.text, "estatus:", r.status_code)
		if r.status_code == 200:
			response = json.loads( r.text )
		#	respuestas[ location_array ] = response['description']['accepted']
		#pass
	except Exception as ex:
		print("No pudo hacer confirmación a ", equipo_destino)
		pass

def iniciaEleccionNuevoCoordinador( tipoServer , prioridadEquipos, myIP, myPriority):
	"""
	Es el proceso que de elección de nuevo coordinador. Regresa verdadero si el equipo actual resulta
	coordinador o de tiempo. 
	Retornará Falso si queda como servidor de sumas
	"""
	global respuestas, hiloUtc
	print("Estoy iniciando proceso de elección")
	respuestas = [None]*len(prioridadEquipos)
	a = 0
	for equipo in prioridadEquipos:
		if equipo['direccion'] == myIP:
			print("Estoy haciendo skip para avisar :", equipo)
			print("Estoy haciendo skip para avisar :", equipo)
			
			continue
		if equipo['prioridad']>myPriority:
			#print("Le voy a avisar a {}, que quiero ser el coordinador".format(equipo))
			print("Iniciando hilo para avisarles")
			avisa_soy_nuevo_coordinador(tipoServer, equipo,myIP,myPriority,a)
		a+=1
		
	print("Valor de las respuestas de los demás para Bully:",respuestas)
	#input(".-.-.-.-.-.-")
	if False in respuestas:
		return False
	else:
		for equipo in prioridadEquipos:
			#print("Le estoy confirmando a {}, que seré el coordinador".format(equipo))
			#if equipo['direccion'] == myIP:
			#	print("Estoy haciendo skip de mi dirección:", equipo)
			#	print("Estoy haciendo skip de mi dirección:", equipo)
			#	
			#	continue
			#Le avisa a todo mundo que él es el nuevo coordinador
			confirma_soy_nuevo_coordinador(tipoServer, equipo, myIP) 
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

def get_ip(getPort = False):
	from practica06.server_coordinador import env
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
	finally:
		s.close()
	if getPort == True:
		return {'ip':IP, 'port':env['puerto']}
	return IP

#Esta función guardará los datos recibidos en la Base de datos
def guardaEnBd(ip_origen, numeroServer, suma, relojObject, nombreEquipo, dbName=None):
	resultado = {'ok':True, 'description':suma}

	now = datetime.datetime.now()
	datetimeServer = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" "

	datetimeServer += str(relojObject.hora)+":"+str(relojObject.mins)+":"+str(relojObject.segs)

	bd = connectToBd(dbName=dbName)

	a = bd.doQuery("""
	INSERT INTO resultados_envios(date_added, ip_origen, nombre_equipo, num_jugador, resultado_suma) 
	VALUES('{}', '{}', '{}', '{}', '{}');""".format(
			str(datetimeServer), str(ip_origen), str(nombreEquipo), str(numeroServer), str(suma)
		)
	)
	resultado['description'] = "Resultado almacenado"

	return resultado

def send_to_others_servers(ip_origen, numeroServer, suma, nombreEquipoOrigen, servidor_destino):
	my_address = get_ip()
	destino = servidor_destino['direccion']

	url_destino = "http://"+destino+"/numeros/save-result-peer"

	print("Replicando a:", url_destino)
	print("Replicando a:", url_destino)
	print("Replicando a:", url_destino)

	if destino == my_address:
		return True
	data_to_send = {
		'ip_origin' : ip_origen,
		'num_jugador_origin' : numeroServer,
		'resultado_suma' : suma,
		'nombre_equipo_origin' : nombreEquipoOrigen
	}
	try:
		r = requests.post(url_destino, json=data_to_send)
		response = json.loads(r.text)
		ack_replicaciones.append( response['ok'] )
	except Exception as ex:
		ack_replicaciones.append( True )
	
def sendResultToOtherServer(ip_origen, numeroServer, suma, nombreEquipoOrigen, equipos_a_enviar):
	print("Llegó a función de hilo")
	my_ip = get_ip(getPort=True)
	my_address = my_ip['ip']+":"+str(my_ip['port'])
	for equipo in equipos_a_enviar:
		if equipo['direccion'] == my_address:
			continue
		send = threading.Thread(target=send_to_others_servers, name="Envia a servidores", args=(ip_origen, numeroServer, suma, nombreEquipoOrigen, equipo,))
		send.start()
		send.join()
	#Si todos dieron su ack
	if all( x == True for x in ack_replicaciones ) == True:
		return True	


def connectToBd(dbName=None):
	bd_name=dbName
	#if dbName is None:
	#	bd_name = "resguardo_sumas_1"
	server_bd = "10.100.76.126"

	return Bd(	
		hostname = server_bd,
		username = "root",
		password = "12345",
		database = bd_name
	)