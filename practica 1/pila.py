import commands

class nodopila(object):
	"""docstring for nodopila"""
	def __init__(self, valor):

		self.valor=valor
		self.siguiente=None


class lpila(object):
	"""docstring for lpila"""
	def __init__(self):
		self.primero= None

	def insertar(self, elemento):
		if self.primero == None:
			self.primero = elemento

		else:
			elemento.siguiente=self.primero
			self.primero = elemento

	def recorrer(self):

		temporal = self.primero
		cadena = ''
		while temporal!= None:
			#print str(temporal.valor)
			cadena = str(cadena) + str (temporal.valor) + ' '
			temporal = temporal.siguiente

		print cadena

		
	def pop(self):



			dato = self.primero.valor

			self.primero = self.primero.siguiente

			return dato



"""prueba= '5 + 6 + 9'.split()
print prueba[1]"""


"""ld= lpila()
ld.insertar(nodopila(1))
ld.insertar(nodopila(2))
ld.insertar(nodopila(3))
ld.insertar(nodopila(4))
ld.recorrer()"""


		

		