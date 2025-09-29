# Criar uma variável de temperatura, se estiver frio, temp. ambiente ou quente, é exibido
localizacao_atual = str(input("\nMe diga sua localização atual: ").strip())
temperatura_atual = int(input("\nDigite qual temperatura atual: "))

temperatura = 30

if temperatura > temperatura_atual:
    print(f"\nHoje ta frio ai em {localizacao_atual}, ta fazendo {temperatura_atual} ºC! Cê é louco.")
elif temperatura == temperatura_atual:
    print(f"\nCara, tanto aqui como ai em {localizacao_atual}, ta ambiente né, com seus {temperatura} ºC!")
else:
    print(f"\nRapaz, é {localizacao_atual} ou o inferno? rsrsrs! {temperatura_atual} ºC é quente viu?")