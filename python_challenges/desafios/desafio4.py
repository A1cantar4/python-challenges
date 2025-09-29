# Revisão no Código: 28/07/2025

# Estoque de cada pão
estoque = {
    'bolachão': 20,
    'frances': 30,
    'baiano': 25,
    'doce': 15
}

# Preço dos pão
precos_pao = {
    'bolachão': 0.5,
    'frances': 0.33,
    'baiano': 0.5,
    'doce': 0.5
}

# lista de devedores (Se for comprado fiado)
devedores = []

# Cardápio de pães
print("¨¨¨ CARDÁPIO DE PÃES ¨¨¨")
for idx, pao in enumerate(estoque.keys(), 1):
    print(f"{idx}- {pao.capitalize()} (R${precos_pao[pao]:.2f})")

# Tipo do pão
opcao = input("\nQual pão você deseja meu nobre (Digite o nome ou o número)? ").strip().lower()

# Se o número for digitado vai ser convertido
lista_paes = list(estoque.keys())
if opcao.isdigit() and 1 <= int(opcao) <= len(lista_paes):
    tipo_pao = lista_paes[int(opcao) - 1]
elif opcao in lista_paes:
    tipo_pao = opcao
else:
    print("Pão inexistente!")
    exit()

# Verificador de quantidade desejada
quantidade = int(input(f"\nQuantos pão de {pao} você quer meu nobre?"))
if quantidade > estoque[tipo_pao]:
    print(f"Foi mal, só temos {estoque[tipo_pao]} {tipo_pao}(s) no estoque.")
    exit()
    
# Preço do pão escolhido
pao = precos_pao[tipo_pao]

# Seleção de método de pagamento
print("\nMétodos de pagamento:")
print("1- Pix")
print("2- Débito")
print("3- Crédito")
print("4- Dinheiro (À vista)")
print("5- MODO POBRE: fiado")

pagamento_opcao = input("Qual vai ser o método de pagamento chefe?: ").strip().lower()


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