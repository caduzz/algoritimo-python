#constate
velocidade = int(input('Informe a velocidade: '))
limite_via = 80
mutiplicador_multa = 5

total_multa = velocidade * mutiplicador_multa

if velocidade > limite_via:
    print(f'''
        *Mutado*
        Voce ultrapassou o limite de {limite_via}km/h da via, 
        Velocidade: {velocidade}Km/h
        Valor da multa: {total_multa}R$
    ''')
else:
    print('Voce respeitou as regras boa gerreiro paciente *BOA*')