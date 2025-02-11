import sympy as sp  # Importamos sympy
import os

# Definimos la variable simbólica x
x = sp.symbols('x')

while True:  # Bucle infinito hasta que el usuario decida salir
    # Mostrar un cuadro de diálogo en la consola
    os.system('cls')
    print("\n" + "="*40)
    print("      CÁLCULO DE LÍMITES      ")
    print("="*40)
    print("[1] Calcular el límite de una función")
    print("[2] Ver ejemplo de función")
    print("[3] Salir")
    print("="*40)
    
    opcion = input("Seleccione una opción: ").strip()

    if opcion == '1':  # Opción para calcular un límite
        os.system('cls')
        print("\nEjemplo de función: \n f(x) = (2*x**2 + 3*x + 1) / (x**3 + 5)")

         a = input("ingrese el valor de ""a"" hacia donde tiene su limite aqui:")
        funcion_usuario = input("\nIngrese una función en términos de x: ")

        # Convertimos la entrada en una expresión simbólica
        f_x_usuario = sp.sympify(funcion_usuario)

        # Calculamos el límite en el punto ingresado
        limite_usuario = sp.limit(f_x_usuario, x, a)

        # Mostramos el resultado en un cuadro de diálogo
        print("\n" + "-"*40)
        print(f"  Límite de f(x) cuando x → {a}")
        print(f"  Resultado: {limite_usuario}")
        print("-"*40)

        input("\nPresione ENTER para continuar...")

    elif opcion == '2':  # Opción para ver un ejemplo de función
        os.system('cls')
        print("\nEjemplo de formato \npara ingresar una función:")
        print("  f(x) = (2*x**2 + 3*x + 1) / (x**3 + 5)")
        print("  Si x → ∞, el límite es 0.")
        input("\nPresione ENTER para continuar...")


    elif opcion == '3':  # Opción para salir
        os.system('cls')
        print("\nSaliendo del programa... ¡Hasta luego!")
        break  # Termina el bucle

    else:  # Si la opción no es válida
        os.system('cls')
        print("\n⚠️ Opción no válida. Intente nuevamente.")
