print("===== Modificar nombre. =====")

diccionario_cursos       =  { "C001": ['Inglés Inicial','ingles',4,True,'online'] } 
diccionario_cursos_dos   =  { "C002": ['Francés Básico','frances',6,False,'presencial'] }

lista_cursos   = []

lista_cursos.append(diccionario_cursos)
lista_cursos.append(diccionario_cursos_dos)

codigo_modificar = input("Ingrese el código del curso: ")
nuevo_nombre = input("Ingrese el nuevo nombre del curso: ")

for elemento_curso in lista_cursos:
    clave = list(elemento_curso.keys())[0]  # Obtener la primera clave
   
    if clave == codigo_modificar:
        elemento_curso[clave][1] = nuevo_nombre
        print("El nombre fue modificado....")
        break