import commands
import os
from xml.etree import ElementTree
from lxml import etree
import usuarios
import matriz





	

class inicio(object):
	def __init__(self):
		self.arg = None
		self.users = usuarios.lusuario()


	def lectura(self):
		print 'ingrese la ruta del archivo:'
		ruta = raw_input()
		doc = etree.parse(str(ruta))
		#print etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")
		raiz = doc.getroot()
		print raiz.tag
		libro = raiz[0]
		x=0
		y=0
		for child in raiz:
			#print child.tag
			if child.tag == 'matriz':
				for child2 in child:
					#print child2.tag
					if child2.tag == 'x':
						x = int(child2.text)
					elif child2.tag == 'y':
						y = int(child2.text)
			elif child.tag == 'operaciones':
				for child2 in child:
					if child2.tag == 'operacion':
						print child2.text


	def crearusuarios(self):


		if self.users.primero == None:
			print 'ingrese el usuario'
			us = raw_input()
			print 'ingrese el nombre'
			nombre = raw_input()
			print 'ingrese la contra'
			contra = raw_input()
			self.users.insertar(usuarios.usuario(nombre, us, contra))
			return True
		else:
			print 'ingrese el usuario'
			us = raw_input()
			if self.users.existe(us) == True:
				print 'el usuario ya existe'
				return False # fracaso crear usuarios
			print 'ingrese el nombre'
			nombre = raw_input()
			print 'ingrese la contra'
			contra = raw_input()
			self.users.insertar(usuarios.usuario(nombre, us, contra))

		return True #exito	
		#users.insertar(usuarios.usuario(nombre,nus,contra))

	def menusistmea(self):
		pass

	def ingresaralsistema(self):
		if self.users.primero == None:
			print 'no hay ningun usuario registrado en el sistema'
			return 0

		print 'ingrese el usuario'
		us = raw_input()
		print 'ingrese la contrasena'
		contra = raw_input()
		nodo = self.users.buscar(us,contra)

		if nodo != None:
			print 'Ingreso al sistema'
			man = True
			while man == True:
				print '\n\n-------------------------'
				print '1. Leer archivo'
				print '2. Resolver Operaciones'
				print '3. Operar Matriz'
				print '4. Mostrar Usuarios'
				print '5. Mostrar Cola'
				print '6. Cerrar sesion'
				des = raw_input()

				if des =='1':
					pass
				elif des =='2':
					pass

				elif des =='3':
					pass

				elif des =='4':
					pass

				elif des =='5':
					pass

				elif des =='6':
					man = False




		else:
			print 'usuario o contrasena incorrectas'





	def paso1(self):
		des=''
		fin = 0
		while fin == 0:
			print '1. Crear usuario'
			print '2. Ingresar al sistema'
			print '3. Salir del programa'
			des = input()
			if des == 3:
				fin = 1
			elif des == 2:
				self.ingresaralsistema()

			elif des == 1: #crear usuario
				if self.crearusuarios() == True:
					self.users.recorrer()

			else:
				pass

		
		


i = inicio()
i.lectura()

