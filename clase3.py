'''######
# OPERADORES LOGICOS
# and -> y
#  or -> o
# not -> negacion

"a" in "hola" and 10>6 
"a" in "hola" or "l" in "lado"
"a" not in "hola"


######################
# CICLOS

# while
# for

#### while #####

def cicloW(ini, fin):
    i=ini
    while i<fin:
        print("hola")
        i+=i ## contador
    
cicloW(1,5)

###break ### esta mal usado mala practica
### fundamentos distra
### return ### no tiene que estar en cualquier lado porque rompe el ciclo, siempre al final


####### ciclo for #####

def cicloF1(sec):
    for x in sec:
        print(x, end="-") 

cicloF1("hola")

# range()  #funcion de python que permite poner secuencias de numeros

# list()  combierte en un array
def cicloF2():
    for i in range(0,5):
        print(i, "hola")

def prueba(sec):
    for i in sec:
        print(i)

prueba(range(2,20,2))

###################
# GENERADOR DE NUMEROS

def gene1(ini,fin):
    res = ""
    sep = "\n"
    for i in range(ini, fin):
        if res=="":
            res = str(i)
        else:
            res = res+ sep + str(i)
    print(res)

gene1(203,206)
'''

import random
def gene2(inf, sup, cant):
    res = ""
    sep = ","
    i=0
    ale = random.randint(inf,sup)
    mini = ale
    maxi = ale
    while i<cant:
        if ale>maxi:
            maxi=ale
        if ale<mini:
            mini=ale
        if res=="":
            res = str(ale)
        else:
            res = res+ sep + str(ale)
        i+=1
        ale = random.randint(inf,sup)
    return res+"["+str(mini)+","+str(maxi)+"]"

gene2(103,206,6)

#### Pendiente de trabajo para la semana que viene

'''Desarrollar una funcion que recibe una cadena de numeros separados por coma. La funcion debera imprimir el numero mas grande y el numero mas chico'''

# 3805,3807,704, 555000, 201

# el minimo es : 201
# el Maximo es : 555000


#### mas ejercicios de la guia hasta el 4.6