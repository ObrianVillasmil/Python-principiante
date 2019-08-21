def getValor(val1,val2):
	if 0<val1>val2:
		return val1+val2
	else:
		print("El valor 1 tiene que ser mayor a 0 y mayor al valor 2")

val1 = int(input("Escribe el valor 1: "))
val2 = int(input("Escribe el valor 2: "))

resultado = getValor(val1,val2)
print (resultado)


