#1
'''def fun (cad,c):
    res=""
    i=0
    while i<len(cad):
        res=res+cad[i]+c
        i+=1
    return res
def main():
    cad="Domingo"
    nuevaCadena=fun(cad,"-")
    print(nuevaCadena)
main()'''

#2

'''def fun (cad):
    band=True
    res=""
    for i in range(0,len(cad)):
        if band:
            res=res+"-"+cad[i]
            band=False
        else:
            res+="+"+cad[i]
            band=True
    return res
def main():
    cad="246"
    nuevaCadena=fun(cad)
    print(nuevaCadena)
main()
'''

#3
'''def fun (cad,a,b):
    encontro=False
    res=""
    for i in range(0,len(cad)):
        aux=cad[i]
        if aux==a and not encontro:
            aux=b
            encontro=True
        res+=aux
    return res
def main():
    cad="Hola, hoy es un dia de frio y lluvia"
    nuevaCadena=fun(cad,"a","A")
    print(nuevaCadena)
main()'''

#4

'''def fun (d,c,b,a):
    largo=len(a)
    r=""
    i=0
    while i<largo and i<3:
        r=r+a[i]
        i+=1
    txt="{} {} de {} de {}"
    txt = txt.format(r,b,c,d)
    return txt
def main():
    res=fun(2022,"Mayo",30,"Lunes")
    print(res)
main()'''

#5

'''def extrae (txt,pos,sep):
    cont=0
    i=0
    res=""
    while i<len(txt) and cont!=pos :
        if txt[i]==sep:
            cont+=1
        i+=1
    while i<len(txt) and txt[i]!=sep:
        res+= txt[i]
        i+=1
    return res

def main():
    meses="""
enero,febrero,marzo,abril,mayo,
junio,julio,agosto,septiembre,
octubre,noviembre,diciembre
"""
    res=extrae(meses,0,",")
    print(res)
    res=extrae(meses,6,",")
    print(res)
    res=extrae(meses,11,",")
    print(res)

main()'''

#6

'''def fun(txt):
    i=len(txt)-1
    while i>=0:
        txt += txt[i]
        i-=1
    return txt
def main():
    print(fun("hola"))
main()'''

#7

'''def fun(txt,x):
    i=0
    desp=len(x)
    band=False
    while i<len(txt) and not band:
        if txt[i:i+desp]==x:
            band=True
        i+=1
    return band
def main():
    print(fun("pruebas","ba"),fun("hola","Ba"))
main()'''

#8

def f(p):
    v="aeiou"
    c="bcdfghjklmñpqrstvwxyz"
    r=""
    for x in p:
        if (x in v) or (x in c):
            r=r + chr(ord(x)-32)
        else:
            r=r + x 
    return r

def main():
    print(f("ab"),("92"),f("2d"))
main()