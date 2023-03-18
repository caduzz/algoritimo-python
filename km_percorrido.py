while_reapeat = True

while while_reapeat:
    distancia_percorrida = input('Distancia percorrida: ')

    distancia_max = 200

    if distancia_percorrida == 'sair':
        while_reapeat = False
        print('''Sair''')
    elif int(distancia_percorrida) >= distancia_max:
        total_pagar = int(distancia_max) * 0.5
        print(f'''Você vai pagar o total {total_pagar}''')
    else:
        total_pagar = int(distancia_max) * 0.45
        print(f'''Você vai pagar o total {total_pagar}''')