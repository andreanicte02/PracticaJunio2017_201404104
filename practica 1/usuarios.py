import commands

class usuario(object):
	"""docstring for usuario"""
	def __init__(self, nombre, usuario, contra):
		self.nombre = nombre
		self.usuario = usuario
		self.contra = contra
		self.siguente = None
		self.anterior = None

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

	def recorrer(self):
		
		temporal = self.primero
		while temporal.siguente!= self.primero:
			print 'el nombre es:'+ str(temporal.nombre)
			temporal = temporal.siguente
		print 'el nombre es:' + str(temporal.nombre)

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

	def graficar(self):
		archi = open('usuarios.dot','w')
		archi.write('digraph Ilustrasion5{\n')
		archi.write('node [shape=record fontsize=10 fontname=\" Verdana\"style=filled];\n')
		contador = 0
		temporal = self.primero
		while temporal.siguente != self.primero:
			contador = contador +1
			archi.write('node'+str(temporal.usuario)+'[label="' + str(temporal.usuario)+ '"];\n')
			temporal= temporal.siguente
		archi.write('node'+str(temporal.usuario)+'[label="' + str(temporal.usuario)+ '"];\n')
		
		temporal = self.primero
		while temporal.siguente != self.primero:
			archi.write('node'+str(temporal.usuario)+'->node'+ str(temporal.siguente.usuario)+ ';\n')
			archi.write('node'+str(temporal.usuario)+'->node'+ str(temporal.anterior.usuario)+ ';\n')
			temporal= temporal.siguente
		archi.write('node'+str(temporal.usuario)+'->node'+ str(temporal.siguente.usuario)+ ';\n')
		archi.write('node'+str(temporal.usuario)+'->node'+ str(temporal.anterior.usuario)+ ';\n')
		
		archi.write('\n}')
		archi.close()	
		commands.getoutput('dot -Tpng usuarios.dot -o usuarios.png')

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
