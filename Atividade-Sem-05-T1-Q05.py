def compra(desconto, parcela, reajuste):
    return desconto, parcela, reajuste

compra = float(input())
desc = compra -(compra * 9 /100)
parcela = compra / 5
aumento = (compra / 10)
total = aumento + (aumento * 17 /100)
print('%2f'% desc)
print('%2f'% parcela)
print('%2f'% total)
