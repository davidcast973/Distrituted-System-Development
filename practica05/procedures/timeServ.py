import datetime
import ntplib
import socket
import sys
import time
sys.path.append("./libs")
from sqlBd import Bd

def guardaDatosHoraEnBd(reloj, ipServer, offset, horaServer, latencia):
	host_name = socket.gethostname() 
	host_ip = socket.gethostbyname(host_name)
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
	bd = Bd("reloj_utc", hostname='localhost', username='root', password='')

	#print("Hoy:", hoy, "| horaRef:", horaReferencia)
	horaReferencia = datetime.datetime.now().timestamp()

	a = bd.doQuery("INSERT INTO hora_central(hora_previa, hora_utc) VALUES ('{}', '{}');".
		format(hoy, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(horaReferencia)))
	)

	lastId = bd.doQuery("SELECT * from hora_central ORDER BY id DESC LIMIT 1;", returnAsDict=True)[0]['id']

	idServer = bd.doQuery("SELECT id FROM servidores WHERE ip = '{}' LIMIT 1;".format(ipServer), returnAsDict=True)[0]['id']

	#print("LastId y IdServer:", lastId,",", idServer)

	if horaServer >= now.timestamp():
		ralentiza = 6
	else:
		ralentiza = 1

	bd.doQuery("INSERT INTO hora_servidores(idHoraCentral, idServidor, ajuste, ralentizar) VALUES ('{}', '{}', '{}', '{}');".
		format(lastId, idServer, offset, ralentiza)
	)

	bd.doQuery("UPDATE servidores SET latencia = '{}' WHERE id = '{}';".format(latencia, idServer))


	