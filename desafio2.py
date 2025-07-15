# Revisão no Código: 15/07/2025
# Projeto: Inserir (Pelo Input) informações em String e Inteiro (com método Strip) 
# e exibe os valores formatado em F-String.
idade = int(input("\nQuantos anos você tem? ").strip())
nome = str(input("\nQual seu nome ? ").strip())

print(f"\n Você se chama {nome}, e tem {idade} anos!")