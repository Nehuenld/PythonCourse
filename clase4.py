##################### FIGURAS #############

# diagonal principal  f==c
# diagonal secundaria f+c==b-1
# tapa de cuadrado f==0
# fondo del cuadrado f==b-1
# tapa izquierda c==0
# tapa del medio c==b//2
# tapa horizontal f==b//2
# f>=c sudoeste
# f<=c noreste
# f+c>=b-1 sudeste
# f+c<=b-1 noroeste
# if f==c -b//2 or f==c +b//2 #parte del rombo
# and solo trae el resultado de las dos condiciones
# or suma y trae las dos condiciones
# hacer una x f==c or f+c==b-1
# f>=c and f+c>=b 
# (f>=c and f+c>=b-1) or c==b//2 or f==b//2 
'''def figura(b,car,esp): 
    for f in range(0,b):
        for c in range(0,b):
            if f==c and f+c==b-1:
                print(car,end="")
            else:
                print(esp,end="")
        print()

figura(5," *"," ")'''

#######################################
## CADENA DE CARACTERES

#Es una secuencia de caracteres
# Las secuencias son iterables.
# lo puedo poner al lado derecho de un for y funciona
# son inmutables: no puede cambiar un elemento dentro de una secuencia
## Se acceden con el indice
# s="abcdef123"
# s[1] == b
## puedo saber el tama;o, la cantidad de elemento   # len(s)


#"DG5&@? \n"

### slicing
s="abcdef123"
#s[ini:fin] # : separa dos numeros un  rango
print(s[2:6])

### acceso con indice positivo y indice negativo

print(s[1]) # de adelante para el final
print(s[-2]) # del final para adelante
print("bc" in s) # membresia, pertenece

############### ALGORITMO TAREA
'''
1) Desarollar una funcion y implementarla desde el main()
que retorno True si una subsecuencia str se encuentra dentro de otra secuencia
2) desarrollarlo con un while
3) desarrollarlo sin usar in, con un for


'''
#1 con in
'''def membresia(x,y):
    x in y
'''
#2 con while
'''def membresia(x,y):
    x = input("ingrese subsecuencia a buscar")
    y = input("Ingrese secuencia donde buscar")
    while x in y:
        True
    '''

#3 con for
'''def membresia(x,y):
    for i=0:
        
        print(True)
    else:
        print("no coincide la secuencia")

def main():
    membresia("abc","holabc123")

main()
'''