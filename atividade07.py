# Digite um valor e veja quantos dolares voce poderá comprar: R$

real = float(input("Digite o Valor em Real(is): "))
dolar = float(input("Digite a cotação do dia: "))

conv = real / dolar

print(f"""
    Seu Valor em Real(is): R${real}
    Cotação atual em Dólar: ${dolar}

    Valor de Convesão: ${conv}
""")