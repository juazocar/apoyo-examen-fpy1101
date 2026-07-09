print("===== Busqueda entre dos diccionarios. =====")

diccionario_cursos       =  { "C001": ['Inglés Inicial','ingles',4,True,'online'] } 
diccionario_cursos_dos   =  { "C002": ['Francés Básico','frances',6,False,'presencial'] }

diccionario_vacantes     = { "C001": [149990,20]}
diccionario_vacantes_dos = { "C002": [189990,10]}

lista_cursos   = []
lista_vacantes = []

lista_cursos.append(diccionario_cursos)
lista_cursos.append(diccionario_cursos_dos)

lista_vacantes.append(diccionario_vacantes)
lista_vacantes.append(diccionario_vacantes_dos)

#Buscar cupos por idioma

idioma_ingresado = input("Ingrese el idioma: ").lower().strip()

for elemento_curso in lista_cursos:
    clave = list(elemento_curso.keys())[0]  # Obtener la primera clave
   
    if elemento_curso[clave][1] == idioma_ingresado:
        #Encontramos la clave
        print(clave)
        #Ahora recorremos la otra lista
        for elemento_vacante in lista_vacantes:
            clave_vacante = list(elemento_vacante.keys())[0]
            #Preguntamos si la clave del elemento vacante, es igual a la clave encontrada previamente
            if clave_vacante == clave:
                print("Las vacantes para el curso", clave,"son de:", elemento_vacante[clave_vacante][1],"personas")