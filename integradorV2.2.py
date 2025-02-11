import os #Manipulación de consola
import sympy as sp  #Algebráica

x = sp.symbols('x') #letra de la incognita

while True :
    # Mostrar un cuadro de diálogo en la consola
    os.system('cls')
    print("\n" + "="*40)
    print("      CÁLCULO DE LÍMITES      ")
    print("="*40)
    print("[1] Calcular el límite de una función")
    print("[2] Ver ejemplo de función")
    print("[3] Salir")
    print("="*40)

    opcion = input("Seleccione una opción: ")

    if opcion == '1':

        while True :

            os.system('cls')

            a = input("ingrese el valor de ""a"" hacia donde tiene su limite aqui:")

            print("ejemplos de formato para ingresar una funcion racional \n (x**2 + 5*x + 4) / (x**3 - 2*x + 7)\n")
            funcion_usuario = input ("ingrese su función aqui:")

            f_x_usuario = sp.sympify(funcion_usuario)#Convertimos texto en una expresión simbólica
            
            limite_usuario = sp.limit(f_x_usuario, x, a)#Calculamos el límite cuando x → a

            print("\n" + "="*40)
            print(f"\nEl límite de la función ingresada cuando x → {a} es: {limite_usuario}")#Mostramos el resultado
            print("\n" + "="*40)

            repetir = input("Desea ingresar otra función (Y/N)")
            if repetir == 'N':
                print("Programa finalizado")
                break
    
    elif opcion == '2':  # Opción para ver un ejemplo de función
        os.system('cls')
        print("\n" + "="*40)
        print("\nEjemplo de formato para ingresar una función:")
        print("\nf(x) = (2*x**2 + 3*x + 1) / (x**3 + 5)")
        print("\nComo puede observar...\nEl producto debe estar explícito\n")
        print("Resultado esperado:\nSi x → ∞, el límite es 0.")
        print("\n" + "="*40)
        input("\nPresione ENTER para continuar...")