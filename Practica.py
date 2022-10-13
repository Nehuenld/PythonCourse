#########################
# ENTRADA / SALIDA / VARIABLES / OPERADORES

#1.1
#Desarrolllar un programa que solicite por pantalla el ingreso de un numero entero. Luego el programa debe mostrar por pantalla el numero ingresado

'''num = int(input("Ingrese Numero: "))
print("Usted ingreso: ", num)'''

# 1.2
# Desarrollar un programa que solicite por teclado dos lados de un rectangulo. Luego calcular el perimetro y area del mismo. Mostrar los resultados de la siguiente forma:

'''lado1 = int(input("Ingresar Lado 1: "))
lado2 = int(input("Ingrese Lado 2: "))

area = lado1 * lado2
perimetro = (lado1 * lado2)/2

print("Area: ", area)
print("Perimetro: ",60)'''

# 1.3

# Desarrollar un programa que solicite el ingreso de dos numeros enteros. Luego el programa debera mostrar por pantalla el resultado de sumar, restar multiplicar y dividir dichos numeros ingresados.

'''num1 = int(input("Ingrese Numero 1: "))
num2 = int(input("Ingrese Numero 2: "))

suma=num1+num2
resta=num1-num2
division=num1/num2
multiplicacion=num1*num2

print("Los resultados para ",num1, " y ",num2," son:")

print("La suma: ",suma)
print("La resta: ",resta)
print("La division: ",int(division))
print("La multiplicacion: ",multiplicacion)'''

## Desarrollar un programa que solicite el ingreso de un numero real. Luego el programa debera mostrar la decomposicion del numero real en su parte entera y su parte decimal como bien muestr el ejemplo.

num = float(input("Ingrese un Numero: "))
entera=int(num)
decimal=round(num-entera, 4)

print("Los resultados para", num,"son:")
    
print("Parte entera: ", entera)
print("Parte decimal: ", decimal)
