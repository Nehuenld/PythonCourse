#1
'''def cicloW(msj):
    i= 1
    while(i < 5 ):
        print(msj, end="|")
        i = i+1
    
def main():
    cicloW("hola")
main()'''

#2
'''def cicloF(msj):
    for x in "abc":
        print(msj,end="|")
    
def main():
    cicloF("hola")

main()
'''
#3
'''def fun(ini,inf,sup):
    sum = ini
    for d in range(inf, sup):
        sum += d
    return sum
def main():
    print(fun(0,0,4))
main()
'''

# 4
'''def fun2():
    res = "*"
    for x in "lamarestabaserena":
        res = res +"*"+x
    return res

def main():
    print(fun2())

main()'''

# 5 
'''def fun2(pal,y):
    res=None
    n=len(pal)-1
    for x in pal:
        if x ==y:
            res=n 
        n-=1
    return res

def main():
    print(fun2("hola","o"))
main()'''

# 6
#import random
'''def aleatorio (inf,sup):
    return random.randint(inf,sup)
def condicion(num):
    return num %2==0 or num %3==0
def imprimirLinea(cant,inf,sup):
    imprimio=0
    numAle = aleatorio (inf,sup)

    while imprimio < cant:
        if condicion(numAle):
            print("{:5d}".format(numAle), end="" )
            imprimio = imprimio + 1
        numAle = aleatorio(inf,sup)

def main():
    cantidad = 6 # Vria segun la salida que se quiera obterner
    limInf = 100 # Varia segun la salida que se quiera obtener
    limSup = 300
    imprimirLinea(cantidad,limInf,limSup)

main()'''

#7
#7.1 ||| --> True
#7.2 \ -> f==c 
#7.3 _\ -> f==c or f==b-1
#7.4 x -> f==c or f+c==b-1
#7.5 --> f==c or f+c>=b-1
#7.6 --> (f<=c and f+c<=b-1) or c==b//2
def figura (b,car):
    for f in range(0,b):
        for c in range(0,b):
            if f+3<=c  or (f+3)+c<=b-1 or f-3>=c or (f-3)+c>=b-1:
                print(car,end="")
            else:
                print(end="  ")
        print()
def main():
    figura (7, " *")
main()

