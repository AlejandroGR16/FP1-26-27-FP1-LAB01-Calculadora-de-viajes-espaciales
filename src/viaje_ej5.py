repetir = True
while repetir:
    distancia_km = int(input('¿Cuál es la distancia en km?'))  # distancia Tierra - Luna
    velocidad_kmh = int(input('¿Cuál es la velocidad en km/h?'))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    respuesta = input('¿Quieres hacer otra simulación? (s/n)')
    if respuesta == 's':
        repetir = True
    else: repetir = False