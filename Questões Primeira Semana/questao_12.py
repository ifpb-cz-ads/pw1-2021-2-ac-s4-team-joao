distancia = int(input('Digite a distância do percurso: '))
velMedia = int(input('Digite a velocidade média: '))

viagem = distancia / velMedia

print('Sua viagem de', distancia, 'km com uma velocidade média de', velMedia, 'km/h %5.2f horas' % viagem)