def sumar_2_numeros():
    num1 = validar_numero()
    num2 = validar_numero()
    total = num1+num2
    print("FUNCIÓn: El total de la suma es:",total)

def restar_2_numeros(p_num1: float, p_num2: float):
    total = p_num1 - p_num2 
    print("FUNCIÓN: El total de la resta es:",total)

def multiplicar_2_numeros():
    num1 = validar_numero()
    num2 = validar_numero()
    total = num1 * num2
    return total

def dividir_2_numeros(p_num1:int, p_num2:int):
    total = p_num1/p_num2
    return total

def validar_numero():
    while True:
        try:
            num = float(input("Ingrese número: "))
            break
        except:
            print("ERROR! DEEBE INGRESAR UN NÚMERO ENTERO!")
    return num

def menu():
    print("MENU")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multilicar 2 números")
    print("4. Dividir 2 números")

def validar_opciones(opciones):
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in opciones:
                break
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UNNÚMERO ENTERO!")
    return opc