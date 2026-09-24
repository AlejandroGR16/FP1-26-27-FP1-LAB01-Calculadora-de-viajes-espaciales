# Ejercicio 1
distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
tiempo_semanas = tiempo_dias // 7
dias_restantes = tiempo_dias % 7
print(f"Tardarías {tiempo_semanas} semanas y {dias_restantes} días en llegar.")

# Ejercicio 2
distancia_km = int(input('¿Cuál es la distancia en km?'))  # distancia Tierra - Luna
velocidad_kmh = int(input('¿Cuál es la velocidad en km/h?'))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
tiempo_semanas = tiempo_dias // 7
dias_restantes = tiempo_dias % 7
print(f"Tardarías {tiempo_semanas} semanas y {dias_restantes} días en llegar.")

# Ejercicio 4
velocidad:int
semanas:int
dias:float
for i in range(1,6):
    velocidad=10000*i
    semanas=((225000000/velocidad)/24)//7
    dias=((225000000/velocidad)/24)%7
    print(f'Velocidad: {velocidad} km/h -> Tiempo: {semanas} semanas y {dias} días')

# Ejercicio 5
repetir = True
while repetir:
    distancia_km = int(input('¿Cuál es la distancia en km?'))  # distancia Tierra - Luna
    velocidad_kmh = int(input('¿Cuál es la velocidad en km/h?'))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_semanas = (tiempo_horas // 24)//7
    dias_restantes = (tiempo_horas // 24)%7
    print(f"Tardarías {tiempo_semanas} semanas y {dias_restantes} días en llegar.")
    respuesta = input('¿Quieres hacer otra simulación? (s/n)')
    if respuesta == 's':
        repetir = True
    else: repetir = False