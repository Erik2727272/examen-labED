#Convertir un Número Entero a Cualquier Base Numérica,
# El programa debe pedir al usuario que ingrese un número n, y un número p

#pedimos que ingrese un dato para la variable n
n=int(input("Ingrese un valor numerico(n): "))
#pedimos que ingrese el valor de p 
p=int(input("Ingrese el valor del sistema numerico al que quiere convertir\n1.binario \n2.base 8 \n"))


def n_a_binario(n):
    if n <= 0:
        return "0"    # Aquí almacenamos el resultado
    # Mientras se pueda dividir...
    while n > 0:
            # Saber si es 1 o 0
        residuo = int(n % 2)
            # E ir dividiendo el n
        n = int(n / 2)
            # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario
binario = n_a_binario(n)

def n_a_octal(n):  #creamos la funcion que tranforma a la base 8 u octal 
    while n > 0:
        residuo = n % 8
        octal = str(residuo) + octal
        n = int(n / 8)
    return octal

octal = n_a_octal(n)
print(n_a_binario(p))
print(n_a_octal(p))

print("El número ",n" es ",binario" en binario")
print("El numero",n" es ",octal" en octal")



