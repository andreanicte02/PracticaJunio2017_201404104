import commands

class noperacion(object):
	"""docstring for operacion"""
	def __init__(self,operacion):
		self.operacion = operacion
		self.siguiente = None

class listaopera(object):
	"""docstring for listaopera"""
	def __init__(self):
		self.primero = None

	def insertar(self, elemento):

		if self.primero == None:

			self.primero = elemento

		else:
			temporal = self.primero
			while temporal.siguiente!= None:
				
				temporal = temporal.siguiente

			temporal.siguiente = elemento




	def dequeque(self):

		if self.primero.siguiente== None:
			opera = self.primero.operacion
			self.primero = None
			return opera
		else :
			opera = self.primero.operacion
			self.primero = self.primero.siguiente
			return opera

	def recorrer(self):
		
		temporal = self.primero

		while temporal!= None:

			print str(temporal.operacion)

			temporal = temporal.siguiente




'''lista = listaopera()
lista.insertar(noperacion('hi'))
lista.insertar(noperacion('h2'))
lista.insertar(noperacion('h3'))
print lista.dequeque() + '-------- saco'
print lista.dequeque() + '-------- saco'
print lista.dequeque() + '-------- saco'
lista.recorrer()'''


		

