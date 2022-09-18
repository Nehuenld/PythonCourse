import math
from tkinter import W

'''def main():
    print(math.sqrt(math.pi))

main()'''

''''def fun(a,b):
    a = b + 1 
        x = 2 + W
    return a + b

print(fun(1,10))'''

'''def fun(num,p):
    res = num**p
    return res

print(fun(2,8))'''

'''def fun2(a,c):
    return a+c
def fun(a,b):
    a+b+1
    b=2
    fun2(a,b)

print(fun(1,10))'''

'''def fun(val):
    res = val % 2 == 0
    print(res)

fun(20)'''

import random
'''def saludo(val):
    msjA="Hola"
    msjB="Chau"
    res = msjA*(val)+ msjB*(1-val)
    return res

def main():
    ale = random.randint(0,1)
    print(saludo(ale))

main()'''

'''def areaRectangulo (base,altura):
    res = base * altura
    print(res)
    return res
    

areaRectangulo(10,15)'''

import math
def areaTriangulo(base,altura):
    # calcula y retorna el area de un triangulo
    res = (base * altura) / 2
    return res

def areaCirculo(radio):
    #calcula y retorna el area de un circulo
    # obsercar que se recibe por parametro el
    # radio y NO el diametro
    res = math.pi * radio**2
    return res

def areaNegra(diametro):
    #calcula y retorna el area negrra de la figura
    #y asignarlo a la varriable ... DEBERA invocar a las
    #funciones respectivas delclaradas arriba
 
    area_triangulo = areaTriangulo(diametro,diametro/2)
    
    area_circulo = areaCirculo(diametro/2)

    area_negra = area_triangulo+((area_circulo/2)-area_triangulo)

    return area_negra

def main():
    #Desde main se invoca a areaNegra

    diametro = int(input("Ingresar diametro: "))
    res = areaNegra(diametro)


    print("Para diametro: {:.2f}".format(diametro))
    print("El area negra ess: {:.2f}".format(res))

main()