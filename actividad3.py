'''def fun(a,b):
    res = 0
    if (a<b):
        res = a+b
    return res

def main():
    print(fun(2,2))

main()'''

'''def fun (nombre):
    msj = "hola"
    if nombre!="":
        msj = msj +" "+nombre
        return msj
def main():
    print(fun("")+", ",end="")

    print(fun("Augusto"))

main()'''
'''def fun(num):
    if (num>=0):
        res = "+"
    else:
        res ="-"
    return res

def main():
    print(fun(1),fun(3),fun(-1))
main()'''

#6
'''def fun(num):
    if(num<=-10):
        res = "#"
    elif(num == 0):
        res = "@"
    elif(num>0 and num<=10):
        res = "&"
    else:
        res = "?"
    
    return res

def main():
    print(fun(11), fun(0), fun(-30), fun(-1), fun(0))

main()'''

#7

'''def fun(num):
    if (num>=0):
        if (num == 0):
            res = "|"
        else:
            res = "+"
    else:
        res = "-"
    return res

def main():
    print(fun(1), fun(0), fun(-3), fun(-1), fun(0))

main()'''

#8 
'''def mayorDeTres(a,b,c):
    if (a>=b):
        if (a>c):
            maxi = a
        else: 
            maxi = b
    else:
        if (b>=c):
            maxi = b
        else:
            maxi = c
    return maxi
    

def main():
    print(mayorDeTres(1,4,3))

main()'''

#9
'''La función 'fVal' valida si la fecha es válida retornando True.  Caso contrario retorna False. 'fVal' Recibe un número 'mmdd' de tres o cuatro cifras que representa una fecha donde la parte del número mm representa el número de mes y la parte dd representa el número de día.
# Ejemplos: 'fechasVálidas'->(valorNúmericoRecibido):
# 'jul-01'->(701)
# 'dic-24'->(1224)
# 'dic-24'->(1224)
# 'oct-7'->(1007),
# 'ene-1'->(101)

# Aclaración: Tomar a febrero como que siempre tiene 28 días máximo.'''

'''def getDia(mmdd):
    return mmdd%100

def getMes(mmdd):
    return mmdd//100

def fval(mmdd):
    res=None
    mes = getMes(mmdd)
    dia = getDia(mmdd)
    if (dia<=31 and (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12)):
        res = True
    elif (dia<=30 and (mes==4 or mes==6 or mes==9 or mes==11)):
        res = True
    elif (dia<=28 and (mes==2)):
        res= True
    else:
        res= False
    return res

def main():
    # PRUEBAS
    mmdd=1224 #dic-24
    print(mmdd, "->",fval(mmdd)) # True
    mmdd=1130 #nov-30
    print(mmdd, "->",fval(mmdd)) # True
    mmdd=701 #jul- 1
    print(mmdd, "->",fval(mmdd)) # True

    mmdd=3106 #jun-31
    print(mmdd, "->",fval(mmdd)) # False
    mmdd=2513 # mes 13 no existe
    print(mmdd, "->",fval(mmdd)) # False
    mmdd=230 #feb-30
    print(mmdd, "->",fval(mmdd)) # False

main()'''
 
 
# 10 

'''def fun(val, n):
    return n!=0 and val % n == 0

def main():
    print(fun(10,3))

main()'''

#11

def fun(num):
    return num>=0 and num<=9

def main():
    print(fun(10))

main()



