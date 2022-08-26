#25-08-22

#Entrada
##############################
#COMENTARIOS
#comentario de 1 liena = #
#comentarios en varias lineas ='''

#Variables, tipos, funciones, salidas, librerias


#Salida
#f(x,y,z) -> variables
from operator import truediv
from pickle import FLOAT
from tokenize import Floatnumber


print("Baboso le seca el pozo")
print("Baboso se la seca",end="") #elimina el salto de line end = nada
print("Baboso","le seca el","pozo",2022)
print(''' 1000, "inminencias", 
   1000, "pranayamas''') #/n salto de linea o '''
print("el tao nunca pierde")
print(1000,1001,1002,"1003", sep="")#sep ="" elimina los espacios de sep aracion

#tanto end como sep son metodos de print

#printito("imbecil eso no es python") error

#####################################
#VARIABLES

pranayamas=1001
print(pranayamas)

mantram="1000 inminencias"
print(mantram,pranayamas,"pranayamas", end= " - ") #end = " - " pone un menos y suma el print de abajo
#############################################
#TIPOS DE DATOS
int=1001 
float=2.0
str="pranayama mucho mucho para no caer en el serruco" # string
verdad=True #bool o bolean
vacio=None  # NoneType

print(int,type(int)) # type() muestra el tipo de dato de la prop que se le pasa
print(float,type(float))
print(str,type(str))
print(verdad,type(verdad))
print(vacio,type(vacio))

##############################################
#OPERACIONES

yin=10
yang=10

sumaTao=yin+yang
restaTao=yin*yang
producto=yin*yang
divisionTao=yin/yang
divisionEntera=yin//yang
resto=yin%yang
potencia=yin**yang

print(sumaTao)
print(restaTao)
print(producto)
print(divisionTao)
print(divisionEntera)
print(resto)
print(potencia)

# las computadoras hacen cuentas a travez de polinomios y no llegan a representar algunas operaciones, y hacen una aproximacion 

##########
#para cadenas

pranayama="cuando la respiracion se detiene,"
semen=" el semen se detiene"
suma= pranayama+semen

print(suma)

#el metodo + tiene una sobrecarga segun que variable reciba y un polimorfismo

#########################################
#CONVERSIONES


'''float(123) #convierte en float, si es una cadena tiene que tener un punto
int(1.2)# convierte a entero, si es una cadena no tiene que tener punto
str(1111)# convierte en string'''


##########################################
#ENTRADA Input

#El input siempre retorna un str
#hay que convertir el dato

yin = input("ingrese cantidad yin: ")## ingresa usuario por teclado 
yang = 10

print(sumaTao)


########################################
#FUNCIONES

def imprimir(nom,msj): 
   print(msj,end="")
   print(nom+": ")

imprimir("Nehuen ","Crack")

def suma(num1,num2):
   suma=num1+num2
   return suma

suma(1000,1001)