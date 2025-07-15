# Revisão no Código: 15/07/2025
# Projeto: Inserir um número float, calcula o "troco" e informa a quantidade do troco com pão
# Usa Condicionais para cada situação e F-STRING formatada no print.
cliente1 = float(input("\nDiga quanto você tem em R$: "))
pao = 0.50
print(f"\nO pão é R${pao}!")

troco = cliente1 - pao

if cliente1 > pao:
    print(f"\nTome seu pão, o troco é: R${troco}")
elif cliente1 == pao:
    print(f"\nTome seu pão, sem troco meu chapa!")
else:
    print(f"\nCara, sem pão hoje, o pão é R${pao}")