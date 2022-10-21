######### ARCHIVOS DE TEXTO
# los archivos son secuencias de byts, el archivo no sabe cuanto es su tamaño, lo maneja el so, pero tienen un tipo de estructura
# ARCHIVOS DE TEXTO se agrupan los byts de a uno, que contiene caracteres
# podemos hacer APERTURAS y CIERRES

##### Apertura de un archivo
#     - "r" -> de lectura. Requiere que exista el archivo
#     - "w" -> de Escritura. Si no existe archivo, entonces lo crea, y si existe entonces borra su contenido. Y escribis arriba.
#     - "a" -> de apendice(agregado). Si no existe archivo, entonces lo crea; y si existe deja el puntero al final para escribir (no borra contenido)

# APERTURA --> open
#ejemplo

def leerArch():
    arch=open("datos_01.txt", "r")### apertura
    #procesar
    lsArch=arch.readlines()
    print(lsArch)
    arch.close() ### cierre
##### Cierre de un archivo
# CIERRE --> <nombre del archivo logico>.close()


## LEER archivo
#    .readline() ->str
#    .readlines() ->list de str (un str por linea)

leerArch()

### ESCRIBIR un archivo
#    .write

'''def escribir():
    arch=open("datos_02.txt", "w")### apertura
    #procesar
    contenido="Estoy escribiendo\n"
    contenido+="desde python\n"
    contenido+="chau...\n"
    arch.write(contenido)
    arch.close() ### cierre

escribir()'''

# APENDICE 

def agregar():
    arch=open("datos_02.txt", "a")### apertura
    contenido="Agregando texto....\n"
    arch.write(contenido)
    arch.close() ### cierre

agregar()

#############################
## .csv coma separate value

def leerArchCSV(nomArch):
    arch=open(nomArch, "r")### apertura
    lsArch=arch.readlines()
    ##print(lsArch)
    arch.close() ### cierre
    return lsArch

def obtenerLista(nomArch):
    lsRes=[]
    ## <pass> ### comodin para poder compilar
    ls=leerArchCSV("datos_csv_01.csv")
    for linea in ls:
        linea=linea[:-1]
        lslinea=linea.split(",") ##-1 le saca el ultimo elemnto a cada linea , y split es un separador, en esta caso usamos coma
        lslinea[0]=int(lslinea[0])
        lslinea[3]=float(lslinea[3])
        lsRes.append(lslinea)
    return lsRes

def mostrarTable(nomArch):
    ls=obtenerLista(nomArch)
    titulo="{:6}{:12}{:12}{:6}".format("DNI","APELLIDO","NOMBRE","ESTATURA")
    print(titulo)

    for lsLin in ls:
        dato="{:<6}{:12}{:12}{:6}".format(lsLin[0],lsLin[1],lsLin[2],lsLin[2])
        print(dato)


mostrarTable("datos_csv_01.csv")