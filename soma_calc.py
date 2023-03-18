typesCalc = ['+', '-', '*', '/']

print(f''' 
Tipos de contas
 ({typesCalc[0]})
 ({typesCalc[1]})
 ({typesCalc[2]})
 ({typesCalc[3]})
''')

typeCalc = input('escolha um valor acima: ')

if typesCalc[0] == typeCalc :
    typeSelecionada = '+'
    print('Voce celecionou (+)')
elif typesCalc[1] == typeCalc :
    typeSelecionada = '-'
    print('Voce celecionou (-)')
elif typesCalc[3] == typeCalc :
    typeSelecionada = '*'
    print('Voce celecionou (*)')
elif typesCalc[4] == typeCalc :
    typeSelecionada = '/'
    print('Voce celecionou (/)')
else:
    print('erro')
    return

numero1 = input('Informe o numero 1: ')
numero2 = input('Informe o numero 2: ')

montar_calc = numero1 + typeSelecionada + numero2
calc = eval(montar_calc)
print(calc)