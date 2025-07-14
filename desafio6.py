# Criar uma variável de horas e minutos com sistema de detecção de erro de digitação

while True: # Loop para caso erre a digitação 
    try:
        hora = int(input("\nMeu nobre, que horas são? (0 a 23) "))
        minutos = int(input("Que minutos são por gentileza? (0 a 59) "))

        if not (0 <= hora <= 23) or not (0 <= minutos <= 59):
            print("Hora ou minutos fora do relógio. Tente outra vez!")
            continue

        horario_formatado = f"{hora}:{minutos:02d}"

        if 6 < hora < 12:
            print(f"\nBom dia capitão, são {horario_formatado} da manhã!")
        elif 12 <= hora < 18:
            print(f"\nMarujo, hora de almoçar, são {horario_formatado} da tarde!")
        elif 18 <= hora < 22:
            print(f"\nAnoiteceu comandante, uma jantinha cai bem agora de {horario_formatado}, certo?")
        elif 22 <= hora <= 23:
            print(f"\nPassou do horário de dormir senhor, já são {horario_formatado}!")
        elif 0 <= hora <= 6:
            print(f"\nMadrugar às {horario_formatado} faz bem pra reflexionar, porém, atitudes somente pela manhã hein?")

        break

    except ValueError:
        print("Problemas a vista! Recite apenas números inteiros para hora e minutos marujo!")

print("Até depois marinheiro!")
