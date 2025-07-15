# Revisão no Código: 15/07/2025
# Projeto: Digite 2 valores Inteiros, e é exibido as variáveis formatadas em F-String
# Tanto da soma, como da subtração dos valores.
numero1 = int(input("\nDiga um número: ").strip()) 
numero2 = int(input("\nDiga outro número: ").strip())

mais = numero1 + numero2
menos = numero1 - numero2

print(f"\nA soma desses números é: {mais}")
print(f"\nComo também, a subtração de {numero1} - {numero2} é: {menos}")