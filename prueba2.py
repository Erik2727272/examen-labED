#Implemente un programa para convertir un número decimal a hexadecimal
# ejm. el número 8642 en forma hexadecimal es: 21C2


#creamos la variable que pide el numero 
num = int(input("Escriba un numero Entero para pasarlo a Hexadecimal: "))
x = num
#mientras sea verdadero
while True:
    if x%16>9 and x%16<16: 
        if x%16==10:                      #configuramos los caracteres para el sistema hexadecimal
            acumulador = "A"+acumulador 
        if x%16==11:
            acumulador = "B"+acumulador
        if x%16==12:
            acumulador = "C"+acumulador
        if x%16==13:
            acumulador = "D"+acumulador
        if x%16==14:
            acumulador = "E"+acumulador
        if x%16==15:
            acumulador = "F"+acumulador
    else:
            acumulador = str(x%16)+acumulador
    x = int(x/16)
    if x<=1: break
    #usamos la condicional 
if x>0:
    acumulador = str(x)+acumulador
    #imprimimos
print(num," Decimal = ",acumulador," en Hexadecimal")
