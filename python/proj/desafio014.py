#converter ºC em ºF

celsius = float(input('Informe a temperatura em ºC ('
                      'celsius): '))
print(f'A temperatura de '
      f'{celsius} ºC corresponde a {((celsius*9/5)+32)}ºF'
      f' e a {celsius + 273.15 :.2f} K')