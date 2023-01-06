#Implemente un algoritmo, usando una función recursiva, que resuelva la
# siguiente
# sumatoria: K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + ... + n ∗ p
# ● El programa debe pedir al usuario que ingrese un número n, y un número P,
# ● Luego debe calcular el valor de K(n, p) usando una función recursiva,
# ● Debe imprimir el resultado de K(n, p)



#pedimos que ingrese un dato para la variable p
p=int(input('Ingrese un valor numerico(p): '))
#pedimos que ingrese un dato para la variable n
n=int(input('Ingrese otro valor numerico(n): '))
 
def recursividad(n,p,recolectado): #creamos una fucnion que tenga como parametros n,p,recolectado
  while n>0 :                   #mientras el numero sea mayor a 0 podemos ejecutar la linea de codigo siguiente 
    recolectado += n*p           #le sumamos a la variable de entrada "recolectado" el producto que salio de n*p
    n-=1
    recursividad(n,p,recolectado) 
  return recolectado                   #retornamos el valor de la variable recolectado 
 
print(recursividad(n,p,0)) #finalmente imrprimimos el valor 
