salario = int(input('Digite seu salário: '))
aumento = int(input('Digite a porcentagem do seu aumento de salário: '))

ajuste = (salario + (salario * aumento / 100))

print('O seu salário de', salario ,'foi ajustado para', ajuste)