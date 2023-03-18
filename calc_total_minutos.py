quantiade_minutus = float(input('Informe a quantidade de minutos usado: '))

if quantiade_minutus < 200:
    valor_mutiplicar = 0.20
else:
    if quantiade_minutus >= 200 and quantiade_minutus <= 400:
        valor_mutiplicar = 0.18
    else:
        valor_mutiplicar = 0.15

total_pagar = valor_mutiplicar * quantiade_minutus

print(total_pagar, valor_mutiplicar)