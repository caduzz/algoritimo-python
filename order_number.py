num1 = int(input('Informe um numero: '))
num2 = int(input('Informe um numero: '))
num3 = int(input('Informe um numero: '))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

if maior > menor:
    print("O maior número é:", maior)
    print("O menor número é:", menor)
else:
    print("Esses numeros são iguais")