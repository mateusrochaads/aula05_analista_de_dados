quantidade =  int(input("quantas pessoas deseja cadastrar?"))
resultado = []
for i in range (quantidade):
    print("\ncadastro", i + 1)
    nome = input("digite o seu nome: ")
    salario_bruto = float(input("digite o seu salario: R$"))
    if salario_bruto >= 5000:
        percentual = 0.14
    elif salario_bruto >- 4000:
        percentual = 0.12
    else: 
        percentual = 0.99
    desconto = salario_bruto * percentual 
    salario_final = salario_bruto - desconto 
    resultado
    print(f"nome: {nome}")
    print(f"bruto: {salario_bruto}")
    print(f"desconto: {desconto}")
    print(f"final: {salario_final}")
    print("\n== relatorio final ===")

                        