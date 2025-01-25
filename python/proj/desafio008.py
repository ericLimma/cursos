metro = float(input('Digite um valor em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro / 10
cm = metro * 100
mm = metro * 1000

print(f'A medida em quilômetros é: {km}km\n'
      f'A medida em hectômetro é: {hm}hm\n'
      f'A meduida em decâmetros é: {dam}da,\n'
      f'A medida em centímetros é: {cm}cm\n'
      f'A medida em milímetros é: {mm}mm')
