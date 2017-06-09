import commands
class nododisperso(object):
    """docstring for nododisperso; nodo de la matriz"""
    def __init__(self, x,y,valor):
        self.x = x
        self.y = y
        self.valor = valor
        self.siguiente = None
        self.anterior = None
        self.arriba= None
        self.abajo = None

class listaHo(object):

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tam = 0

    def insertar(self, elemento):
        self.tam = 0
        if self.primero == None:

            self.primero = elemento
            self.ultimo = elemento

        elif elemento.x < self.primero.x :

            self.primero.anterior = elemento
            elemento.siguiente = self.primero
            self.primero = self.primero.anterior

        elif elemento.x > self.ultimo.x :


            temporal = self.primero

            while temporal.siguiente!=None:
                temporal = temporal.siguiente

            temporal.siguiente = elemento
            elemento.anterior = temporal
            self.ultimo = elemento

        else :

            temp1 = self.primero

            while temp1.x < elemento.x:

                temp1 = temp1.siguiente

            temp2 = temp1.anterior

            temp2.siguiente = elemento
            temp1.anterior = elemento
            elemento.siguiente = temp1
            elemento.anterior = temp2
        self.tam=self.tam+1


class listaVe():

    def __init__(self):

        self.tam = 0
        self.primero= None
        self.ultimo= None


    def insertar(self, elemento):

        if self.primero == None:

            self.primero = elemento
            self.ultimo = elemento

        elif elemento.y < self.primero.y :

            self.primero.arriba = elemento
            elemento.abajo = self.primero
            self.primero = self.primero.arriba

        elif elemento.y > self.ultimo.y :

            temporal = self.primero
            while temporal.abajo!= None:
                temporal = temporal.abajo

            temporal.abajo=elemento
            elemento.arriba= temporal
            self.ultimo= elemento

        else :

            temp1 = self.primero

            while temp1.y < elemento.y:

                temp1 = temp1.abajo

            temp2 = temp1.arriba

            temp2.abajo = elemento
            temp1.arriba = elemento
            elemento.abajo = temp1
            elemento.arriba = temp2
        self.tam=self.tam+1



#cabeceras xxxxxxxxxxxxxxxxxxxxxxxxxxx

class nodox():

    def __init__(self, x):
        self.x = x
        self.listav = listaVe()
        self.siguiente = None
        self.anterior = None

class nodoy():

    def __init__(self, y):
        self.y = y
        self.listah = listaHo()
        self.arriba = None
        self.abajo = None

#Lista de cabeceras del eje X
class listax():


    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tam  =0

    def insertar(self, elemento):

        if self.primero == None:

            self.primero = elemento
            self.ultimo = elemento

        elif elemento.x < self.primero.x :

            self.primero.anterior = elemento
            elemento.siguiente = self.primero
            self.primero = self.primero.anterior

        elif elemento.x > self.ultimo.x :

            temporal= self.primero
            while temporal.siguiente!=None:
                temporal=temporal.siguiente

            temporal.siguiente=elemento
            elemento.anterior=temporal
            self.ultimo=elemento

        else :

            temp1 = self.primero

            while temp1.x < elemento.x:

                temp1 = temp1.siguiente

            temp2 = temp1.anterior

            temp2.siguiente = elemento
            temp1.anterior = elemento
            elemento.siguiente = temp1
            elemento.anterior = temp2

        self.tam= self.tam+1





    def existe(self,x):

        if self.primero == None:
            return None
        else:
            temporal = self.primero

            while temporal != None :

                if temporal.x == x :
                    return temporal

                temporal = temporal.siguiente
        return None

#Lista de cabeceras del lado Y eje vertical
class listay():

    def __init__(self):

        self.primero= None
        self.ultimo= None
        self.tam=0


    def insertar(self, elemento):

        if self.primero == None:

            self.primero = elemento
            self.ultimo = elemento

        elif elemento.y < self.primero.y :

            self.primero.arriba = elemento
            elemento.abajo = self.primero
            self.primero = self.primero.arriba

        elif elemento.y > self.ultimo.y :
            temporal = self.primero
            while temporal.abajo!=None:
                temporal=temporal.abajo

            temporal.abajo=elemento
            elemento.anterior=temporal
            self.ultimo=elemento


        else :

            temp1 = self.primero

            while temp1.y < elemento.y:

                temp1 = temp1.abajo

            temp2 = temp1.arriba

            temp2.abajo = elemento
            temp1.arriba = elemento
            elemento.abajo = temp1
            elemento.arriba = temp2

        self.tam = self.tam +1


    def existe(self,y):

        if self.primero == None:
            return None
        else:
            temporal = self.primero

            while temporal != None :

                if temporal.y == y :
                    return temporal

                temporal = temporal.abajo
        return None


#-------------- Matriz

class matriz(object):
    """docstring for matriz dispersa"""
    def __init__(self):
        self.ladox= listax()
        self.ladoy= listay()

    def verificar(self, x, y): #verifica si existe un nodo en la matriz/buscar
        nodoyy = self.ladoy.primero

        while nodoyy != None:
            temporal = nodoyy.listah.primero

            while temporal != None:
                if temporal.x == x and temporal.y == y:
                    return temporal

                temporal = temporal.siguiente

            nodoyy = nodoyy.abajo

        return None

    def insertar(self,x,y,valor):

       #si existe no deberia de insertar nada
        if self.verificar(x,y) == None:

            if self.ladox.existe(x) == None:

                self.ladox.insertar(nodox(x))

            if self.ladoy.existe(y)== None:

                self.ladoy.insertar(nodoy(y))

            temx = self.ladox.existe(x)
            temy = self.ladoy.existe(y)

            elemento = nododisperso(x,y,valor)


            temx.listav.insertar(elemento)
            temy.listah.insertar(elemento)

            return elemento

    def recorrer(self): #recorre la matriz -->>>>>>>>>>>>>>ESTEEE RECORRE LA MATRIZ
        juntar=''
        temp= self.ladoy.primero
        while temp != None :
            temp2= temp.listah.primero
            juntar = str(juntar)+'|'
            while temp2!= None:
                juntar=str(juntar)+str(temp2.valor)+'   '
                temp2 = temp2.siguiente

            juntar = str(juntar) + '|\n'
            temp=temp.abajo

        return juntar









"""mat = matriz()
for y in range(0,3):

    for x in range (0,2):
        mat.insertar(str(x),str(y),'dato'+str(x)+str(y))

print mat.recorrer()"""
