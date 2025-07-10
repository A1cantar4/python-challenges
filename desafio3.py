# Diga 2 números, e exiba a soma e subtração deles.
numero1 = int(input("\nDiga um número: ").strip()) 
numero2 = int(input("\nDiga outro número: ").strip())

mais = numero1 + numero2
menos = numero1 - numero2

print(f"\nA soma desses números é: {mais}")
print(f"\nComo também, a subtração de {numero1} - {numero2} é: {menos}")