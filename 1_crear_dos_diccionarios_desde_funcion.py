def crear_curso(lista_curso, lista_vacantes):
    codigo         = input("Ingrese el codigo del curso: ").upper()
    nombre         = input("Ingrese el nombre del curso: ")
    lenguaje       = input("Ingrese el lenguaje del curso: ").lower()
    duracion_meses = int(input("Ingrese la duracion en meses del curso: "))
    certificacion  = bool(input("Tiene certificacion? (true/False): ").lower)
    modalidad      = input("Ingrese la modalidad: (presencial/online)").lower()

    precio         = int(input("Ingrese el precio del curso: "))
    vacantes       = int(input("Ingrese la cantidad de vacantes del curso: "))

    diccionario_curso = {
        codigo: [
            nombre,
            duracion_meses,
            lenguaje,
            certificacion,
            modalidad
        ]
    }

    diccionario_vacante = {
        codigo: [
            precio,
            vacantes
        ]
    }

    lista_curso.append(diccionario_curso)
    lista_vacantes.append(diccionario_vacante)
    print("Curso agregado")



#Ejecución del programa....
#Creamos ambas listas para ambos diccionarios
lista_cursos   = []
lista_vacantes = [] 

#Llamamos al método y le pasamos ambas listas como parametro
crear_curso(lista_cursos, lista_vacantes)

