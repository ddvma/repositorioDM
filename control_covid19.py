global childlist, adultlist, elderlist, deadlist
childlist= list()
adultlist= list()
elderlist= list()
deceasedlist= list()

class Paciente:
    def __init__(self, nombre, apellido, id, fecha_nacimiento, edad, genero, pais, status):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.genero = genero
        self.pais = pais
        self.status = status

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("id: ", self.id)
        print("Fecha de nacimiento: ", self.fecha_nacimiento)
        print("Edad: ", self.edad)
        print("Genero: ", self.genero)
        print("Status: ", self.status, "\n")


def menu():
    global opcion
    while True:
        print("\n--Bienvenido al menu principal--")
        print("\n1.Añadir al sistema")
        print("2. Cambiar status")
        print("3. Ver casos")
        print("4. Buscar casos")
        print("5. Determinar covid-19")
        print("\n6. Salir")
        try:
            opcion = int(input("Elige una opcion (1-6): "))

        except:
            print("escoge una opcion valida")
            continue

        if opcion in range(1, 6):

            proceso(opcion)

        elif opcion == 6:
            break

        else:
            print("escoge una opcion valida")


def menu1():
    global opcion1
    print("\n--Añadir al sistema--")
    print("\n1. Niño")
    print("2. Adulto")
    print("3. Tercera Edad")
    print("4. Decesos")
    print("\n5. Return")

    try:
        opcion1 = int(input("escoge una opcion(1-5): "))
    except:
        print("escoge una opcion valida")

    if opcion1 in range(1, 5):
        proceso1(opcion1)

    elif opcion1 == 5:
        menu()

    else:
        print("escoge una opcion valida")

def buscarcaso():
    id= input("id: ")
    for a in childlist:
        if a.id == id:
            print("\nNombre: ",a.nombre)
            print("Apellido: ",a.apellido)
            print("id: ",a.id)
            print("Fecha de nacimiento: ",a.fecha_nacimiento)
            print("Edad: ",a.edad)
            print("Genero ",a.genero, "\n")

    for a in adultlist:
        if a.id == id:
            print("\nNombre: ",a.nombre)
            print("Apellido: ",a.apellido)
            print("id: ",a.id)
            print("Fecha de nacimiento: ",a.fecha_nacimiento)
            print("Edad: ",a.edad)
            print("Genero ",a.genero, "\n")

    for a in elderlist:
        if a.id == id:
            print("\nNombre: ",a.nombre)
            print("Apellido: ",a.apellido)
            print("id: ",a.id)
            print("Fecha de nacimiento: ",a.fecha_nacimiento)
            print("Edad: ",a.edad)
            print("Genero ",a.genero, "\n")

    menu()
        
def menu3():
    while True:
        print("\n--Ver casos--")
        print("\n1. Infectados")
        print("2. A salvo")
        print("3. Decesos")
        print("4. Niño")
        print("5. Adulto")
        print("6. Tercera Edad")
        print("\n7. return")
        try:
            opcion3 = int(input("escoge una opcion (1-7): "))
        except:
            print("escoge una opcion valida")
            continue

        if opcion3 in range(1, 7):
            proceso3(opcion3)

        elif opcion3 == 7:
            menu()

        else:
            print("escoge una opcion valida")


def addtosystemchild():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    id = input("id: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    edad = int(input("Edad: "))
    genero = input("Genero: ")
    pais = input("Pais: ")
    status = input("Status? (infectado/a salvo): ")
    newchild = Paciente(nombre, apellido, id, fecha_nacimiento, edad, genero, pais, status)
    childlist.append(newchild)
    menu()


def addtosystemadult():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    id = input("id: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    edad = int(input("Edad: "))
    genero = input("Genero: ")
    pais = input("Pais: ")
    status = input("status? (infectado/a salvo): ")
    newadult = Paciente(nombre, apellido, id, fecha_nacimiento, edad, genero, pais, status)
    adultlist.append(newadult)
    menu()


def addtosystemelder():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    id = input("id: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    edad = int(input("Edad: "))
    genero = input("Genero: ")
    pais = input("Pais: ")
    status = input("status? (infectado/a salvo): ")
    newelder = Paciente(nombre, apellido, id, fecha_nacimiento, edad, genero, pais, status)
    elderlist.append(newelder)
    menu()

def addtosystemedead():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    id = input("id: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    edad = int(input("Edad: "))
    genero = input("Genero: ")
    pais = input("Pais: ")
    status = "Muerto"
    newdead = Paciente(nombre, apellido, id, fecha_nacimiento, edad, genero, pais, status)
    deceasedlist.append(newdead)
    menu()


def showchildcases():
    for childs in childlist:
        childs.mostrar()
    menu()

def showelderscases():
    for elders in elderlist:
        elders.mostrar()
    menu()


def showadultcases():
    for adults in adultlist:
        adults.mostrar()
    menu()

def showdeceasedcases():
    for deads in deadlist:
        deads.mostrar()
    menu()

def showinfectedcases():
    status="infectado"
    for a in childlist:
        if a.status == status:
            print("\nNombre: ", a.nombre)
            print("Apellido: ", a.apellido)
            print("id: ", a.id)
            print("Fecha de nacimiento: ", a.fecha_nacimiento)
            print("Edad: ", a.edad)
            print("Genero: ", a.genero, "\n")

    for a in adultlist:
        if a.status == status:
            print("\nNombre: ", a.nombre)
            print("Apellido: ", a.apellido)
            print("id: ", a.id)
            print("Fecha de nacimiento: ", a.fecha_nacimiento)
            print("Edad: ", a.edad)
            print("Genero: ", a.genero, "\n")

    for a in elderlist:
        if a.status == status:
            print("\nNombre: ", a.nombre)
            print("Apellido: ", a.apellido)
            print("id: ", a.id)
            print("Fecha de nacimiento: ", a.fecha_nacimiento)
            print("Edad: ", a.edad)
            print("Genero: ", a.genero, "\n")

    menu()

def showsafecases():
    status="a salvo"
    for a in childlist:
        if a.status == status:
            print("\nNombre: ", a.nombre)
            print("Apellido: ", a.apellido)
            print("id: ", a.id)
            print("Fecha de nacimiento: ", a.fecha_nacimiento)
            print("Edad: ", a.edad)
            print("Genero: ", a.genero, "\n")

    for a in adultlist:
        if a.status == status:
            print("\nNombre: ", a.nombre)
            print("Apellido: ", a.apellido)
            print("id: ", a.id)
            print("Fecha de nacimiento: ", a.fecha_nacimiento)
            print("Edad: ", a.edad)
            print("Genero: ", a.genero, "\n")

    for a in elderlist:
        if a.status == status:
            print("\nNombre: ", a.nombre)
            print("Apellido: ", a.apellido)
            print("id: ", a.id)
            print("Fecha de nacimiento: ", a.fecha_nacimiento)
            print("Edad: ", a.edad)
            print("Genero: ", a.genero, "\n")

    menu()

def proceso(opcion):
    if opcion == 1:
        menu1()

    elif opcion == 2:
        pass

    elif opcion == 3:
        menu3()

    elif opcion == 4:
        buscarcaso()
        
    elif opcion == 5:
        pass


def proceso1(opcion1):
    if opcion1 == 1:
        addtosystemchild()

    elif opcion1 == 2:
        addtosystemadult()

    elif opcion1 == 3:
        addtosystemelder()
        
    elif opcion1 == 4:
        addtosystemdead()


def proceso3(opcion3):
    if opcion3 == 1:
        showinfectedcases()

    elif opcion3 == 2:
        showsafecases()

    elif opcion3 == 3:
        showdeceasedcases()

    elif opcion3 == 4:
        showchildcases()

    elif opcion3 == 5:
        showadultcases()

    elif opcion3 == 6:
        showelderscases()


menu()
