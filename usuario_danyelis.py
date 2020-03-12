class Usuario():
	def __init__(self,correo,contraseña,nombre,apellido):
		self.correo=correo
		self.contraseña=contraseña
		self.nombre=nombre
		self.apellido=apellido
		
	def registrar(self):
		Danyelis= open('usuarios.txt','a')
		Danyelis.write(f'''
Correo: {self.correo}
Contraseña: {self.contraseña}
Nombre: {self.nombre}
Apellido: {self.apellido}
''')
		Danyelis.close()
		
def BuscarUusarios(correo):
	Danyelis= open('usuarios.txt','a')
	Danyelis.close()
	Danyelis= open('usuarios.txt','r')
	Jop=Danyelis.readlines()
	Danyelis.close()
	for Pop in Jop:
		if (Pop == 'Correo: '+correo+'\n'): 
			print('El Correo Ingresado ya existe:"ERROR"')
			return False

Exit1=False
Val=False
while Exit1== False:
	print('''Bienvenido al Menu de Danyelis
1-Registrar Nuevo Usuario
2-Iniciar sesion
3-Salir''')
	opc1 =input('OPCION: ')
	if (opc1=="1"):
		print('Ingrese "Salir" para salir al menu')
		correo = input('Correo: ')
		if correo == 'salir' or BuscarUusarios(correo) == True:
			continue
		contraseña=input('contraseña :')
		nombre=input('nombre: ')	
		apellido=input('apellido: ')
		UsuarioCreado = Usuario(correo,contraseña,nombre,apellido)
		UsuarioCreado.registrar()
		print("Ha sido guardado el nuevo usuario")
	elif (opc1=="2"):
		Danyelis=open('usuarios.txt','r')	
		Pro=Danyelis.readlines()
		Danyelis.close()
		correo=input('Ingrese su Correo: ')
		if (correo=='admin'):
			contraseña=input('Ingrese la contraseña: ')
			if (contraseña=='admin'):
				Danyelis=open('usuarios.txt','r')
				print("Usuarios Registrados: ")
				print(Danyelis.read())
				Danyelis.close()
				continue
		for 	x in Pro:
			SesionI=False
			if (x == 'Correo: '+correo+'\n'):
				contraseña = input('Ingrese la contraseña: ')
				for x in Pro:
					if (x == 'Contraseña: '+contraseña+'\n'):
						salida = False
						SeccionI = True
				if SeccionI == True:
					print('Haz iniciado sesion correctamente!')
					while salida==False:
						print('Calculadora')
						print('1-Sumar:')
						print('2-Restar:')
						print('3-Multiplicar:')
						print('4-Dividir:')				
						opc = input('Opcion: ')
						try:
							n1 = int(input('primer numero: '))
							n2 = int(input('segundo numero: '))
							Val = True
						except:
							print('No se puede ingresar letras, ni caracteres ')			
						if (opc == '1'):
							resultado = n1+n2
						elif (opc == '2'):
							resultado = num1-num2
						elif (opc== '3'):
							resultado = n1*n2
						elif (opc == '4'):
							try: 
								resultado = n1/n2
							except:
									print('Imposible dividir entre cero')
									Val = False
									continue
						else:
							print("Opcion invalida")	
						print('El resutlado de su operacion es: ',resultado)
						print('Desea cerrar sesion S/N')
						cerrar=input()	
						if  (cerrar=='s'):
							salida=True
							break
						elif  (cerrar=='n'):
							continue
	
	elif (opcion=='3'):
		break
	else:
		print("Esta opcion no exite"+"\n")
		print("Ingrese otra opcion")
				
