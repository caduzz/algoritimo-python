def calc_bonus (anos, bonus):
    result = anos * bonus
    return result

total_ano = int(input('Informe o total de anos servidos: '))
bonus_ano = int(input('Bonus por ano: '))

calculo = calc_bonus(total_ano, bonus_ano)

print('O bonus calculado foi de', calculo)