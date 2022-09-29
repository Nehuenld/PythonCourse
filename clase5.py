#29/9/22
#cadena de caracteres (2 parte)

'''def estaEn(sCad,cad):
    # retorna True si sCad se encuentra dentro de 'cad'
    # sCad: Subcadena
    # cad: cadena
    return sCad in cad'''

'''def estaEn2(sCad,cad):
    # encontro: el resultado del encuentro
    encontro=False
    i=0
    while i<len(cad) and not encontro :
        if sCad==cad[i] :
            encontro=True
        i+=1
    return encontro'''

'''def estaEn3(sCad,cad):
    # retorna True si 'sCad' (cadena) se encuentra en 'cad'
    # encontro: el resultado del encuentro
    encontro=False
    i=0
    while i<(len(cad)-len(sCad)+1) and not encontro :
        if sCad==cad[i:i+len(sCad)]: #slicing [1:4]
            encontro=True
        i+=1
    return print(encontro)'''

'''def contar(sCad,cad):
    # retorna la cantiodad de veces que aparece sCad en Cad
    # cp: contador de sCad
    i=0
    cp=0
    while i<(len(cad)-len(sCad)+1):
        if sCad==cad[i:i+len(sCad)]: #slicing [1:4]
            cp+=1
            i+=len(sCad)
        else:
            i+=1
    return print(cp)'''
'''def extrae(palabra,txt):
    # retorna la cantiodad de veces que aparece sCad en Cad
    # cp: contador de sCad
    # palabra: es una secuencia de caracteres letra
    # separador: es una secuencia de caracteres no letra [, ! ?]
    # retorna : una cadena con las palabras con las palabras q se encontraron en txt separadas por coma
    # usar un while y adentro 2 while
    i=0
    cp=0
    retorno=[]
    while i<(len(txt)-len(palabra)+1):
        if palabra==txt[i:i+len(palabra)]: #slicing [1:4]
            cp+=1
            i+=len(palabra)
            #retorno[] ???
           # while
             #while 
        else:
            i+=1
    return print(cp)'''

'''def main():
    contar("aa","aaaa")

main()'''


############TRABAJO para el HOGAR
#desarrollar la funcion que extrae palabras que la retorna una cadena de las palabras que se encuentran en un texto 'txt'



#####################################
#LISTAS
#################################
# son secuencias de cualquier tipo de dato valido en python
# vale todo lo visto hasta ahora en cadema, con algunas salvedades
# Lista es mutable
# Puedo acceder por su indice
# Puedo hacer slicing
# Puedo agregar elementos al final -> .append
# Puedo insertar elementos en posicion especifica -> .insert
# Puedo borrar elementos ( x contenido )-> .remove
# Puedo borrar posciones ( x posicion) -> .pop
# Puedo asignar valores a una posicion -> ls[i]=valor
# Una lista se pasa por referencia a una funcion 


def fun():
    ls=[] # crea una lista vacia
    ls2=[1234,"abcd",True,None] # lista completa
    
    print(ls2)
    print("........................")

    ls2.append("Yinsolina")
    ls2.insert(1,"TANTRA")
    print(ls2)
    print("........................")
    ls2.remove(True) # debe existir para que no falle
    ls2.pop(2) # debe existir la posicion a borrar, sino ERROR
    print(ls2)
    print("........................")
    ls2[0]="Falta poco!"
    print(ls2)
def imprimirLs(ls):
    i=0
    while i<len(ls) :
        print(ls[i])
        i+=1


fun()