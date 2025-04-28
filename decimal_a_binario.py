def decimal_a_binario(decimal):
    if decimal < 0:
        return "El número debe ser positivo."
    
    binario = ""
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    
    return binario

def binario_a_decimal(binario):
    if not all(c in '01' for c in binario):
        return "Número binario inválido."
    
    decimal = 0
    for i in range(len(binario)):
        exponente = len(binario) - 1 - i
        digito = int(binario[i])
        decimal += digito * 2 ** exponente
    return decimal

while True:
    print("\nSeleccione opción:")
    print("1. Decimal a binario")
    print("2. Binario a decimal")
    print("3. Salir")

    try:
        option = int(input("Opción: "))
        
        if option == 1:
            decimal = int(input("Ingrese un número decimal: "))
            resultado = decimal_a_binario(decimal)
            print(f"El número en binario es: {resultado}")
        
        elif option == 2:
            binario = input("Ingrese un número binario: ")
            resultado = binario_a_decimal(binario)
            print(f"El número en decimal es: {resultado}")
        
        elif option == 3:
            print("Saliendo...")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")