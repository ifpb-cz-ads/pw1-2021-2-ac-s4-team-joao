dias = int(input('Digite os dias: '))
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

calDias = ((dias * 24) * 60) * 60
calHoras = (horas * 60) * 60
calMinutos = minutos * 60

soma =  calDias + calHoras + calMinutos + segundos

print(soma, 'segundos')