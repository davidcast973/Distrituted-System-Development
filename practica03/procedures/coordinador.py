import sys
import os
import datetime

sys.path.append("./libs")
from sqlBd import Bd

ALLOWED_EXTENSIONS = {'txt'}


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
def guardaEnBd(ip_origen, numeroServer, suma, relojObject, nombreEquipo):
	resultado = {'ok':True, 'description':suma}

	now = datetime.datetime.now()
	datetimeServer = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" "

	datetimeServer += str(relojObject.hora)+":"+str(relojObject.mins)+":"+str(relojObject.segs)

	bd = connectToBd()
	a = bd.doQuery("""
	INSERT INTO resultados_envios(date_added, ip_origen, nombre_equipo, num_jugador, resultado_suma) 
	VALUES('{}', '{}', '{}', '{}', '{}');""".format(
			datetimeServer, ip_origen, nombreEquipo, numeroServer, suma
		)
	)

	resultado['description'] = "Resultado almacenado"

	return resultado

def connectToBd():
	#La conexión conla BD
	return Bd(	
		hostname = 'localhost',
		username = 'root',
		password = '',
		database = 'resguardo_sumas'
	)