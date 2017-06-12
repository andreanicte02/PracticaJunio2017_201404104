import commands
import os
from xml.etree import ElementTree
from lxml import etree
import usuarios
import matriz
import operaciones
import os.path as path
import pila




	

class inicio(object):
	def __init__(self):
		self.arg = None
		self.users = usuarios.lusuario()
		self.auxus = None


	def lectura(self, ruta, cola, mat, trans):

		doc = etree.parse(str(ruta))
		#print etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")
		raiz = doc.getroot()
		#print raiz.tag
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
						#print child2.text
						#insertar en cola
						cola.insertar(operaciones.noperacion(child2.text))


		

		if cola.estado == False:

			topex = 0
			topey = 0
			mat.estado= True
			trans.estado = True


			while topey < y: #crear matriz
			
				while topex < x:

					mat.insertar(topex,topey,str(topex)+ '-' +str(topey))
					#print topex

					topex = topex +1	

 				#print topey
 				topex = 0
				topey = topey +1


			topex = 0
			topey = 0
			while topey < x: #crear matriz
			
				while topex < y:

					trans.insertar(topex,topey,str(topex)+ '-' +str(topey))
					#print topex

					topex = topex +1	

 				#print topey
 				topex = 0
				topey = topey +1
			cola.estado = True






		




	def crearusuarios(self):

		print '--------------Crear usuarios-----------'

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


	def operarmatriz(self, mat, trans):

		man = True
		while man==True:			
			print '-------------opear matriz--------------'
			print '1. ingresar dato'
			print '2. operar tranpsuesta'
			print '3. mostrar matriz original'
			print '4. mostrar matriz tranpsuesta'
			print '5. regresar \n'

			selec= raw_input()

			if selec == '5':
				man=False
			elif selec == '1':
				x = 0
				y = 0 

				print 'Ingrese la pos en x:'
				x=raw_input()
				print 'Ingrese la pos en y:'
				y=raw_input()
				x= int(x)
				y= int(y)

				nodo = mat.verificar(x,y)
				if nodo != None:
					print 'Ingrese el dato:'
					f= raw_input()
					nodo.valor = f
					

				else:
					print 'la matriz no cuenta con esas posiciones'



			elif selec == '2': #operar tarnaspuesta
	
				nodoy = mat.ladoy.primero

				while nodoy!= None:
					temporal = nodoy.listah.primero

					while temporal != None:

						aux=trans.verificar(temporal.y, temporal.x)
						if aux!= None:
							aux.valor = temporal.valor
						#trans.insertar(int(temporal.y), int(temporal.x), temporal.valor)

						temporal = temporal.siguiente
			
					nodoy = nodoy.abajo		

			elif selec == '3':
				print mat.recorrer()

			elif selec == '4':	
				print trans.recorrer()

	def ResOpe(self, cola):
		
		if cola.primero != None:
			opera= cola.dequeque()
			print 'se va resolver la siguiente operacion:' + opera
			opera2 = opera.split(' ')
			lip = pila.lpila()


			
			i = 0
			while i < len(opera2):


				chun = opera2[i]
				lip.insertar(pila.nodopila(chun))
				primero = 0
				segundo = 0

				if lip.primero != None:

					if chun == '*' or chun == '+' or chun == '-':
						
						print 'los datos en la pila son los siguientes:------------\n'
						lip.recorrer()

						signo = lip.pop()
						segundo = lip.pop()
						primero = lip.pop()
						result = 0

						print 'la operacion que se va realizar es:' + str(primero) + ' '+str(signo) + ' '+str(segundo)
						if signo == '*':
							result = int(primero) * int(segundo) 
							lip.insertar(pila.nodopila(result))
						elif signo == '+':
							result  = int (primero) + int (segundo)
							lip.insertar(pila.nodopila(result))

						elif signo == '-':
							result = int(primero) - int(segundo)
							lip.insertar(pila.nodopila(result))		

						print 'el resultado es: '+ str(result)		

				i = i + 1

			print '----------El resultado FINAL es:----------'
			lip.recorrer()

		
		

	def ingresaralsistema(self):
		if self.users.primero == None:
			print 'no hay ningun usuario registrado en el sistema'
			return 0

		print 'ingrese el usuario'
		us = raw_input()
		print 'ingrese la contrasena'
		contra = raw_input()
		nodo = self.users.buscar(us,contra) #nodo con el que se ingreso

		if nodo != None:
			auxus = nodo
			
			man = True
			while man == True:
				print '\n\n----------Ingreso al sistema---------------'
				print '1. Leer archivo'
				print '2. Resolver Operaciones'
				print '3. Operar Matriz'
				print '4. Mostrar Usuarios'
				print '5. Mostrar Cola'
				print '6. Cerrar sesion'
				des = raw_input()

				if des =='1':

					print 'ingrese la ruta del archivo'
					ruta = raw_input()
					if path.exists(ruta):
						print 'existe la rtua'
						self.lectura(ruta, nodo.loper, nodo.matiz, nodo.trans)
						#print nodo.matiz.recorrer()

					else:
						print 'ruta equivocada'

				elif des =='2':
					if nodo.matiz.estado == True: 
						self.ResOpe(nodo.loper)
					else:
						print '---no se ha cargado ningun archivo---'

				elif des =='3':

					if nodo.matiz.estado ==True:

						self.operarmatriz(nodo.matiz, nodo.trans)
					else: 
						print '---no se ha cargado ningun archivo---'

				elif des =='4':
					self.users.recorrer()


				elif des =='5':
					nodo.loper.recorrer()
					if nodo.loper.primero == None:
						print 'la cola de operaciones esta vacia'

				elif des =='6':
					auxus= None
					man = False




		else:
			print 'usuario o contrasena incorrectas'





	def paso1(self):
		des=''
		fin = 0

		while fin == 0:
			print '--------menu principal: 201404104--------'
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
					#self.users.recorrer()
					pass

			else:
				pass

		
		


i = inicio()
i.paso1()
