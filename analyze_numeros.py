numero_1 = int(input('Iformer o primeiro numero: '))
numero_2 = int(input('Iformer o primeiro segundo: '))

maior = max(numero_1, numero_2)
menor = min(numero_1, numero_2) 

if numero_2 > numero_1:
    print(numero_2, 'é o maior numero')
else:
    if numero_2 == numero_1:
        print('Os numeros são iguais')
    else: 
        print(numero_1, 'É o maior numero')

print(f'''
    O maior numero é {maior}
    O menor numero é {menor}
''')