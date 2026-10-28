numero01 = float(input("digite o primeiro numero: "))
numero02 = float(input("digite o segundo numero"))
numero03 = float(input("digite o terceiro numero"))
if numero01 >= numero02 and numero01 >= numero03:
    maior = numero01
elif numero02 >= numero01 and numero02 >= numero03:
    maior = numero02
else:
    maior = numero03
print(f"o maior numero e: {maior}")