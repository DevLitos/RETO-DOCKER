alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]

def calcular_media(lista_alumnos):
    """
    Metodo que calcula la media de una lista de alumnos
    """
    notas = 0.0
    if len(lista_alumnos) == 0:
        return 0 
    else: 
        for alumno in alumnos:
            notas += alumno['nota']
        return round(notas / len(lista_alumnos), 2)


aprobados: int = 0
notas = 0.0
for alumno in alumnos:
    notas += alumno['nota']
    if alumno["nota"] >= 5.0:
        print(f"{alumno['nombre'].upper()} ha aprobado con una nota de {alumno['nota']}.")
        aprobados += 1
    else:
        print(f"{alumno['nombre'].upper()} ha suspendido con una nota de {alumno['nota']}.")

suspendidos: int = len(alumnos) - aprobados
media = calcular_media(alumnos)
print(f"Resumen: Numero alumnos: {len(alumnos)}. Numero aprobados: {aprobados}. Numero suspendidos: {suspendidos}. Media: {media}")


