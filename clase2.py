########### CLASE 2 #########
'''
FUNCIONES 
'''
# from random import randint # solo trae randint
import random##### importar librerias frameworks de funciones


#palabra reservada + nombre de funcion + (dos parametros) + dos puntos :
def sumar(a,b):
    res=a+b
    print("la suma es:", res)

sumar(3,4) ### punto de ejecucion pegado al borde

def restar(a,b):
    res=a-b
    return res

restar(3,4) ### retorna el resultado para utilizarlo

'''PROGRAMA PRINCIPAL'''

'''def main():##### codigo limpio solo se ejecuta la funcion main( siempre llamarla main)
    num1= random.randint(10,100) # int(input("Ingrese num1: ")) # radint(numMIn,numMax) da un numero random entre el minimo y maximo pasado
    num2= random.randint(10,100) # int(input("Ingrese num2: "))
    sumar(num1,num2)#####parametros
    print("La resta es: ", restar(num1,num2))
    
main()'''


####################################################
###### FORMAT ######
# formatear los string para imprimirlos bien

def main():
    print("Juan", "Lopez", 33355235)
    print("Carla", "Lopez", 25262523)
    cadenaFormateada="{:8} {:8} {:8}".format("Juan", "Lopez", 33355235)### formateador de codigo
    print(cadenaFormateada) # www.pyformat.info

main() 

################################################
## CONDICIONALES

def maxi(a,b): # me retorna el maximo de dos
    res=None
    if a>b:
        res=a
    else:
        res=b
    return res

def mini(a,b): #me retorna el minimo
    res=b
    if a<b:
        res=a
    return res

def maxi3(a,b,c): # imprime el maximo de tres
    res=None
    if a>=b and a>=c:
        res=a
    else: 
        if b>=a and b>=c:
            res=b
        else:
            res=c
    return res

def traduce(num):
    if num==1:
        res="UNO"
    elif num2==2:
        res="DOS"
    elif num==3:
        res="TRES"
    else:
        res="ERROR!!"
    return res

################################################
## FUNCION BOOLEANA

def esMul7(num):
    return num%7==0

esMul7(8) ###False

def esPar(num):
    return num%2==0

esPar(8) # True

def esParYMult7(num):
    return esMul7(num) and esParYMult7(num)

'''Si un año es divisible entre 100, pero no entre 400, entonces "no" es un año bisiesto''' 

### operador de MEMBRESIA in # ve si un caracter esta en la cadena o un conjunto de caracteres iguales


"h" in "hola" ##true
"hl" in "hola" ## False
"hol" in "hola" ## True