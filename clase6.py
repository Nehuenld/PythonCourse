# Listas, la ultima clase
# Ordenar una lista

'''ls =[23,6,31,98,7,62]
def ordenarLst(ls):
    for i in range(0,len(ls)-1):
        for j in range(i+1,len(ls)):
            if ls[i]<ls[j]:
                aux   = ls[i]
                ls[i] = ls[j]
                ls[j] = aux
    print(ls)

ordenarLst(ls)

ls2=ls # hace referencia a la misma lista en memoria
ls2=[]+ls # crea una nueva lista en memoria
'''

## TUPLAS
# Secuencia de cualquier tipo de dato valido.
# Inmutable(no acepta modificacion desde su interior)
# No tiene metodos

'''def fun() :
    tu=(1, (), "hola") ## Tuple de tres elementos
    tu2=()               # Tuple vacia
    tu3=(1,)             # Tuple de un solo elemento
    # Una Tuple sirve para retornar mas de un solo elemento
    tu4=("abc",True)
    tu5=tu4+tu
    ## Indice 
    print(tu5[1])
    ## slicing
    print(tu5[1:4])

fun()

def fun2():
    num=1234
    nombre="juancito"
    print (num,nombre) ## retorna una Tupla, mejor metodo para evitar que la modifiquen

fun2()'''

######################
## DICCIONARIO
## '''key:value'''
# key  # es un identificador que no se repite
# value # es un valor asociado a una clave
# Metodos:
#          .get()
#          .keys()
#          .values()
#          .pop()
def fun():
    di={  20:"Juan", 32:"Laura", 12:"Julieta", "abc":"choco" }
    print(di[20]) # accede a la posicion 20
    di2={} # diccionario vacio

    di.get(20) #devuelve el valor
    di.get(1000) # devuelve None, no hace falta manejo de error

    di.pop(20) #devuelve el elemento que borra y lo saca de el diccionario

    di.keys() # devuelve datos keys, lista de las keys del diccionario

    di.values() # devuelve la lista de valores del diccionario

    # recorrido del diccionario
    for clave in di:
        print("{:<4} {:10}".format(clave,di[clave]))

    # recorrido
    lsClaves=di.keys()
    for clave in lsClaves:
        print("{:<4} {:10}".format(clave,di[clave]))

# como hago para ordenar la biblioteca por key

fun()
