import os #Manipulación de consola
import sympy as sp  #Algebráica

x = sp.symbols('x') #letra de la incognita

while True :
    os.system('cls') #limpiamos pantalla

    a = input("ingrese el valor de ""a"" hacia donde tiende su limite aqui:")

    print("ejemplos de formato para ingresar una funcion racional \n (x**2 + 5*x + 4) / (x**3 - 2*x + 7)\n")
    funcion_usuario = input ("ingrese aqui:")

    f_x_usuario = sp.sympify(funcion_usuario)#Convertimos texto en una expresión simbólica
    
    limite_usuario = sp.limit(f_x_usuario, x, a)#Calculamos el límite cuando x → a

    print(f"El límite de la función ingresada cuando x → {a} es: {limite_usuario}")#Mostramos el resultado

    repetir = input("Desea ingresar otra función (Y/N)")
    if repetir == 'N':
        print("Programa finalizado")
        break