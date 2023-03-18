def calc_almento(porcentagem, salario_recebido): 
    media_calculada = salario_recebido * (porcentagem / 100)
    total_almento = media_calculada + salario_recebido 
    print(f'''
        Total almento: {total_almento}
        Media calculada: {media_calculada}
    ''')

salario = float(input('Informer o salario do funcionario: '))
#vars estaticas
media_calculo = 1250

if salario > media_calculo:
    calc_almento(10, salario) 
else: 
    calc_almento(15, salario)