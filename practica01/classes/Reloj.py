import threading
import time
#creamos la clase Reloj.
#Reloj extiende (hereda de la clase threading.Thread)
class Reloj(threading.Thread):
	#Se crean los atributos de la clase
	nombre = ""
	hora = -1
	mins = -1
	segs = -1

	#El constructor de la clase recibe el nombre que tendrá el reloj.
	def __init__(self,nombre):
		threading.Thread.__init__(self)
		#Se asigna el nombre al hilo
		self.nombre= nombre

	#Se sobreescribe el método run para poder correlo como hilo
	def run(self):
		"""En este bloque se realiza todo el proceso del reloj.
		No es más que un grupo de while's anidados.
		"""
		while True:
			while self.hora< 12:
				self.hora +=1
				while self.mins< 60:
					self.mins+= 1
					while self.segs< 60:
						self.segs+= 1
						#Se imprime el valor del reloj para verificar su funcionalidad
						print("reloj:",self.nombre,"->",self)
						time.sleep(1)
					self.segs= -1
				self.mins= -1
			self.hora= -1

	#Se sobreescribe su método __repr__
	def __repr__(self):
		"""Sirve para representar al objeto cuando se manda a imprimir
		Algo así como el @Override de toString() en Java para objetos."""
		return "Hilo: "+self.nombre+" | "+str(self.hora)+":"+str(self.mins)+":"+str(self.segs)
