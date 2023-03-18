km = float(input("Quantos km percorrido: "))
dias = int(input("Quantidade de dias pelos quais o carro foi alugado: "))

total = 60 * dias + 0.15 * km

print(f'''
    Você alugou o carro por `{dias}`dias, 
    e andou `{km}`km,
    total a pagar = {total}
''')
