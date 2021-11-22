produto = int(input('Digite o valor do produto: '))
desconto = int(input('Digite o valor do desconto: '))

ajuste = (produto - (produto * desconto / 100))

print('O produto de', produto ,'reais recebeu um desconto de', desconto ,'por cento, o valor a ser pago é ', ajuste)