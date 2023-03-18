formato = input('Para qual você quer converter: [C, F]: ') 
temp = float(input('Converter °C em °F, informe o valor: '))

if formato == 'C' or formato == 'c':
    converter_temp = (temp * 9/5) + 32
    print(converter_temp, 'F')
elif formato == 'F' or formato == 'f':
    converter_temp = temp / (9/5) + 32
    print(converter_temp, 'C')
else :
    print('erro')