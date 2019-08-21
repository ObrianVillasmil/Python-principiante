nombre = "obrian"
lista = ["hola","mundo","empezando","python"]
#inserta el valor en la posicion que se le indique con el primer parametro
lista.insert(3,"aqui")
#agrega el elemento al final de la lista
lista.append("3.*")
lista2 = ['aun no se nada',200]
#mete un lista dentro de otra
lista.extend(lista2)
#agrega valor al final de la lista
lista.append(nombre)
#buscar si el "valor" esta en el arreglo
print ("hola" in lista) 
#elimna el elemento de la lista que se le pase 
print(lista.remove(nombre))
#imprime desde la posicion 2 la final de la lista
print(lista[2:])
#imprime desde el inicio a la posicion 1 de la lista
print(lista[:2])
#imprime la lista completa
print(lista[:])