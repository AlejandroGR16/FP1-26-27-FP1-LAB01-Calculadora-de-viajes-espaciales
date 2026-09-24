velocidad:int
tiempo:float
for i in range(1,6):
    velocidad=10000*i
    tiempo=(225000000/velocidad)/24
    print(f'Velocidad: {velocidad} km/h -> Tiempo: {tiempo} días')