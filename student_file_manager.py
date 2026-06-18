alumnos = ["rojas", "chema", "celeste","sara","dilan con i", "carlos"]


with open("lista_alumnos.txt", "w", encoding="utf-8") as archivo:
    for alumno in alumnos:
        archivo.write(alumno + ",")
