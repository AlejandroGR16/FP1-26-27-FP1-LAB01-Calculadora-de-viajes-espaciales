edad = int(input('¿Cuál es tu edad?'))
nivel_fisico = int(input('¿Cuál es tu nivel físico del 1 al 10?'))
if edad<18:
    print('Debes ser mayot de edad')
if nivel_fisico<5:
    print('Debes estar en mejor forma')
if edad>=18 and nivel_fisico>=5:
    print('¡Listo para despegar!')