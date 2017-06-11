import commands
import matriz
import operaciones
import matriz

class usuario(object):
	"""docstring for usuario"""
	def __init__(self, nombre, usuario, contra):
		self.nombre = nombre
		self.usuario = usuario
		self.contra = contra
		self.siguente = None
		self.anterior = None
		self.loper = operaciones.listaopera()
		self.matiz = matriz.matriz()
		self.trans = matriz.matriz()

class lusuario(object):
	"""docstring for lusuario"""
	def __init__(self):
		self.primero = None
		self.anterior = None

	def insertar(self, elemento):
		
		if self.primero == None:
			self.primero = elemento
			elemento.siguente = elemento
			elemento.anterior = elemento
		else: 
			temporal = self.primero
			while temporal.siguente != self.primero:
				temporal = temporal.siguente

			self.primero.anterior= elemento
			temporal.siguente= elemento
			elemento.anterior = temporal
			elemento.siguente = self.primero


	def opt(self):
		nodoy = self.matiz.ladoy.primero

		while nodoy!= None:
			temporal = nodoy.listah.primero

			while temporal != None:

				self.trans(int(temporal.y), int(temporal.x), temporal.valor)

				temporal = temporal.siguente
			
			nodoy = nodoy.abajo

	def recorrer(self):
		
		reporte=''
		temporal = self.primero
		while temporal.siguente!= self.primero:
			reporte = str(reporte)+str(temporal.usuario)+'->'
			temporal = temporal.siguente

		reporte =str(reporte)+str(temporal.usuario)
		print 'Usuarios:'
		print reporte

		
		re = ''
		while temporal!= self.primero:
			re= str(re)+str(temporal.usuario)+'->'
			temporal = temporal.anterior

		re = str(re)+str(temporal.usuario)
		print re	

		#print 'el nombre es:' + str(temporal.nombre)

	def existe(self, nombre):
		temporal = self.primero
		while temporal.siguente!= self.primero:
			if str(temporal.usuario)== str(nombre):
				return True			
			temporal = temporal.siguente
		if str(temporal.usuario) == str(nombre):
			return True #si es true existe
		else:
			return False

	def buscar(self, nombre, contra):
		temporal = self.primero
		while temporal.siguente!= self.primero:
			if str(temporal.usuario)== str(nombre) and str(temporal.contra)== str(contra):
				return temporal			
			temporal = temporal.siguente
		if str(temporal.usuario) == str(nombre) and str(temporal.contra)== str(contra):
			return temporal #si es true existe
		else:
			return None
		




		
"""lista = lusuario()
lista.insertar(usuario('prueba1','dos','contra1'))
lista.insertar(usuario('prueba2','tres','contra2'))
lista.insertar(usuario('prueba3','cuatr','contra3'))
lista.insertar(usuario('prueba4','cincto','contra4'))
lista.insertar(usuario('prueba5','seis','contra5'))

print 'verifique si existe'
if (lista.buscar('dos','ew')== True):
	print 'LOL'"""
