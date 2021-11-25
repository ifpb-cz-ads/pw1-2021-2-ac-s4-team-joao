carro = int(input('Digite quantos km/s você percorreu com o carro: '))

dias = int(input('Digite quantos dias você ficou com o carro: '))

calKm = carro * 0.15
calDias = dias * 60
aluguel = calKm + calDias

print('O Total a pagar pelo aluguel será : R$', aluguel)