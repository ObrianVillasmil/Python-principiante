def materias():
	return ['química','física','biología','matemática','catellano','ingles']

materias = materias()
x = 1

print ('Materias dispuestas: ')

for i in materias:
	print (str(x) +") " + i)
	x +=1

materia_escogida = input('ingrese la materia que escogerá : ')

if materia_escogida.lower() in materias:
	print('materia ' + materia_escogida + ' escogida con exito')
else:
	print('La materia ' + materia_escogida + ' no existe')