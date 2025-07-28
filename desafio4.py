# Revisão no Código: 15/07/2025

# Lista de Pão
TIPOS_DE_PÃO = ['bolachão', 'frances', 'baiano', 'doce']
pao = 0

# Cardápio de pães
print("¨¨¨ CARDÁPIO DE PÃES ¨¨¨")
print("\n1- Bolachão")
print("2- Frances")
print("3- Baiano")
print("4- Doce")

# Seleção de pães
tipos_de_pao = str(input("\nQual pão você deseja? ").strip())
if tipos_de_pao == "1":
    pao = 0.5
elif tipos_de_pao == "2":
    pao = 0.33
elif tipos_de_pao == "3":
    pao = 0.5
else:
    pao = 0.5

quantos_pao = str(input("\nQuantos pães você quer meu nobre? "))

dinheiro = float(input("\nDiga quanto você tem em R$: "))

print("\nMétodos de pagamento:")
print("1- Pix")
print("2- Débito")
print("3- Crédito")
print("4- Dinheiro (À vista)")
print("5- MODO POBRE: fiado")
pagamento = str(input("Qual vai ser o método de pagamento chefe?:"))


# Calculo para saber quantidade de pão e troco
posso_comprar = round(dinheiro / pao)
troco = dinheiro - (posso_comprar * pao)


print(f"\nO pão é R${pao}!")

if dinheiro == pao or troco == 0:
    print(f"\nTome seus {posso_comprar} pão, sem troco meu chapa!")
elif dinheiro > pao:
    print(f"\nTome seus {posso_comprar} pão, e seu troco é: R${troco:.2f}.")
else:
    print(f"\nCara, sem pão hoje, o pão é R${pao}")