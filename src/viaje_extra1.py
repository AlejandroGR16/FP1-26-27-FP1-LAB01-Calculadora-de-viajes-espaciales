distancia = int(input('Introduce la distancia total en km:'))
paradas = distancia // 150000
if distancia <= 150000:
    print('Puedes llegar sin hacer ninguna parada')
else:
    for i in range(1,paradas+1):
        print(f'Parada en el km {i*150000}')
    print(f'Total de paradas para respostar: {paradas}')