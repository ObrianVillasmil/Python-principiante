from login import Login

login = Login()
usuarios = login.usuarios(True);

if login.usuario in usuarios:
	
	if usuarios[login.usuario]['contrasenna'] == login.contrasena:
	
		print("Bienvenido al sitema ", login.usuario)
		roles = login.roles(True)

		if usuarios[login.usuario]["rol"] in roles:
			
			if(roles[usuarios[login.usuario]["rol"]] == "Administrador"):
				alumn = login.getDataAlumno()
				print("Los alumnuos registrados son: ")
				for al in alumn:
					print(al," | ",end="")

				login.getPromedio()

			elif(roles[usuarios[login.usuario]["rol"]] == "Profesor"):
				pass

			else:
				login.getPromedioAlumno(login.usuario)

	else:
		print("La combinación de usuario y contraseña no exite")
else:
	print("El usuario no existe")