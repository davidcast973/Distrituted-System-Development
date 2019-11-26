import threading
import time
import random
import datetime
#creamos la clase Reloj.
#Reloj extiende (hereda de la clase threading.Thread)
class Reloj(threading.Thread):
	#Se crean los atributos de la clase
	printable = False
	nombre = ""
	hora = -1
	mins = -1
	segs = -1
	ritmo = 1
	paused = False

	#El constructor de la clase recibe el nombre que tendrá el reloj.
	def __init__(self,nombre, hora=None, mins=None, segs=None):
		threading.Thread.__init__(self)
		#Se asigna el nombre al hilo
		self.nombre= nombre
		if(hora!=None and mins!=None and segs!=None):
			self.hora=hora - 1
			self.mins=mins - 1
			self.segs=segs - 1
		else:
			if(self.nombre=="#1"):
				t = datetime.datetime.now()
				self.hora = t.hour -1
				self.mins = t.minute -1 
				self.segs = t.second -1
				print("Hora de este:", self )
			else:
				self.hora=random.randint(0,24)
				self.mins=random.randint(0,60)
				self.segs=random.randint(0,60)

	#Se sobreescribe el método run para poder correlo como hilo
	def run(self):
		"""En este bloque se realiza todo el proceso del reloj.
		No es más que un grupo de while's anidados.
		"""
		while True:
			while self.hora < 23 and not self.paused:
				self.hora += 1
				while self.mins < 59 and not self.paused:
					self.mins+= 1
					while self.segs < 59 and not self.paused:
						self.segs+= 1
						#Se imprime el valor del reloj para verificar su funcionalidad
						if self.printable:
							print("reloj:",self.nombre,"->",self)
						time.sleep(self.ritmo)
					if not self.paused:
						self.segs= -1
				if not self.paused:
					self.mins= -1
			if not self.paused:
				self.hora= -1
		
	def cambiaRitmo(self, nuevoRitmo):
		self.ritmo=nuevoRitmo
	
	def pausa(self):
		self.paused=True

	#Se sobreescribe su método __repr__
	def __repr__(self):
		"""Sirve para representar al objeto cuando se manda a imprimir
		Algo así como el @Override de toString() en Java para objetos."""
		return "Hilo: "+self.nombre+" | "+str(self.hora)+":"+str(self.mins)+":"+str(self.segs)
