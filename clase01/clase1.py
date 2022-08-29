#25-08-22

#Entrada
##############################
#COMENTARIOS
#comentario de 1 liena = #
#comentarios en varias lineas ='''

#Variables, tipos, funciones, salidas, librerias


#Salida
#f(x,y,z) -> variables
from ctypes.wintypes import INT
from numbers import Integral
from operator import truediv
from pickle import FLOAT
from pickletools import float8
from tkinter.tix import INTEGER
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
inta=1001 
floating=2.0
string="pranayama mucho mucho para no caer en el serruco" # string
verdad=True #bool o bolean
vacio=None  # NoneType

print(inta,type(int)) # type() muestra el tipo de dato de la prop que se le pasa
print(floating,type(float))
print(string,type(str))
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

###########################
#Ejercicios

#1.1. 
'''Desarrollar un programa que solicite por pantalla(consola) el ingreso de un numero entero. 
Luego el programa debe mostrar por pantalla (consola) el numero ingresado.'''

numeroIngresado =input("Ingrese Numero: ")
print("Usted Ingreso: ", numeroIngresado)

#1.2
'''Desarrollar un programa que solicite por teclado dos lados de un rectangulo. Luego calcular el perimetro y area del mismo. Mostrar los resultados de la siguiente forma:'''
# Area: num...
#Perimetro: num...

lado1     = int(input("Ingresar Lado 1: "))
lado2     = int(input("Ingresar Lado 2: "))
area      = lado1*lado2
perimetro = lado1+lado2
print("Área: ", area)
print("Perímetro", perimetro)

#1.3
'''Desarrollar un programa que solicite el ingreso de dos numeros enteros. Luego el programa debera mostrar por pantalla el resultado de sumar, restar, multiplar y dividir dichos numeros ingresados.
'''

num1 =int(input("Ingresar Numero 1: "))
num2 =int(input("Ingresar Numero 2: "))

print("Los resultados para 4 y 2 son: ")
print("La suma: ", (num1+num2))
print("La resta: ", (num1-num2))
print("La división: ", int(num1/num2))
print("La multiplicación: ", (num1*num2))

#1.4
'''
Desarrollar un programa que solicite el ingreso de un número real. Luego el programa deberá mostrar la descomposición del número real en su parte entera y su parte decimal.
'''

numero = float(input("Ingrese Numero: "))
print("Los resultados para ",numero," son:")
print("parte entera", int(numero))
decimales = round((numero-int(numero)),4)
print("Parte decimal: ", decimales)
