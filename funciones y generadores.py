persona = []
datosPersona = []
preguntas = ["ingrese la edad: " ,"Ingrese el sexo: ","Ingrese la nacionalidad: "]
anucios = ['Su edad es: ','Su sexo es: ','Su nacionalidad es: ']
nombre = input("Ingrese el nombre de la persona: ")

persona.append(nombre)

for i in preguntas:
	res = input(i)
	datosPersona.append(res)

persona.append(datosPersona)

def funcionGeneradora(persona):
	for i in persona[1]:
		yield i

datos = funcionGeneradora(persona)

print("Su nomrbe es "+ persona[0])

z=0
for x in datos:
	print(anucios[z] + x)
	z+=1