# Se o atleta tiver entre 18 a 35 anos, aptidão e atestado médico, pode participar da competição
nome = str(input("\nOlá, qual seu nome? ").strip())
atleta = int(input("\nJovem atleta, qual sua idade? ").strip())

while True:
    aptidao = str(input("\nVocê possui aptdão física? (S/N) ").strip().lower())
    if aptidao in ("s", "n"):
        break
while True:
    atestado = str(input("\nPossui também permissão médica? (S/N) ").strip().lower())
    if atestado in ("s", "n"):
        break    
    
if 18 <= atleta <= 35 and (aptidao == "s" or atestado == "s"):
    print(f"Parabéns, você poderá participar da competição! Bem-vindo(a) {nome}!")
else:
    print(f"Infelizmente você não poderá partipar {nome}!")