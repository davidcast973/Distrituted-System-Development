import datetime
import ntplib
import socket
import sys
import time
sys.path.append("./libs")
from sqlBd import Bd

def get_ip(getPort = False):
	from practica06.server_time import env
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

def guardaDatosHoraEnBd(reloj, ipServer, offset, horaServer, latencia, bd_srvr_tiempo=None):
	host_ip = get_ip()
	now = datetime.datetime.now()
	#hora = -1
	#mins = -1
	#segs = -1
	if reloj.hora < 10:
		strHora = "0"+str(reloj.hora)
	else:
		strHora=str(reloj.hora)
	
	if reloj.mins < 10:
		strMins = "0"+str(reloj.mins)
	else:
		strMins=str(reloj.mins)
	
	if reloj.segs < 10:
		strSecs = "0"+str(reloj.segs)
	else:
		strSecs=str(reloj.segs)
	
	hoy = now.strftime("%Y-%m-%d") +" "+ strHora+":"+strMins+":"+strSecs

	now = datetime.datetime.now()

	#time = obtenUTCTime(date_time_obj, relojes[0])
	reloj_local = datetime.datetime(
		now.year,now.month, now.day,
		#relojes[0].hora, relojes[0].mins, relojes[0].segs,tzinfo=datetime.timezone.utc
		reloj.hora, reloj.mins, reloj.segs
	)

	hora = reloj_local.timestamp()

	#bd = Bd("reloj_utc", hostname='localhost', username='root', password='12345')
	bd = conectaBd(bd_srvr_tiempo)

	#print("Hoy:", hoy, "| horaRef:", horaReferencia)
	horaReferencia = datetime.datetime.now().timestamp()

	a = bd.doQuery("INSERT INTO hora_central(hora_previa, hora_utc) VALUES ('{}', '{}');".
		format(hoy, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(horaReferencia)))
	)

	lastId = bd.doQuery("SELECT * from hora_central ORDER BY id DESC LIMIT 1;", returnAsDict=True)[0]['id']

	queryArmada = "SELECT id FROM servidores WHERE ip = '{}' LIMIT 1;".format(ipServer)
	#print("Query armada para obtener ip:",queryArmada)
	idServer = bd.doQuery(queryArmada, returnAsDict=True)[0]['id']

	#print("LastId y IdServer:", lastId,",", idServer)

	if horaServer >= now.timestamp():
		ralentiza = 6
	else:
		ralentiza = 1

	bd.doQuery("INSERT INTO hora_servidores(idHoraCentral, idServidor, ajuste, ralentizar) VALUES ('{}', '{}', '{}', '{}');".
		format(lastId, idServer, offset, ralentiza)
	)

	bd.doQuery("UPDATE servidores SET latencia = '{}' WHERE id = '{}';".format(latencia, idServer))


def conectaBd(bd_srvr_tiempo):
	if bd_srvr_tiempo is None:
		return Bd("reloj_utc", hostname='localhost', username='root', password='')
	elif "C" in bd_srvr_tiempo:
		return Bd("reloj_utc_"+bd_srvr_tiempo, hostname='localhost', username='root', password='')