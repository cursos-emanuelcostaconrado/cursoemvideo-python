# Exercício Python 008: Escreva um programa que leia um valor em metros e
# o exiba convertido em centímetros e milímetros.

medida = float(input('Uma distância em metros: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {} m corresponde a \n'
      '{:.3f} km\n'
      '{:.3f} hm\n'
      '{:.3f} dam\n'
      '{:.2f} dm\n'
      '{:.2f} cm\n'
      '{:.2f} mm'.format(medida, km, hm, dam, dm, cm, mm))
