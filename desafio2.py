# Revisão no Código: 26/09/2025
# Projeto: Inserir (Pelo Input) informações em String e Inteiro (com método Strip) 
# e exibe os valores formatado em F-String.
from assets.static.styles import c_verde, c_ciano, c_magenta

idade = int(input(c_verde("\nQuantos anos você tem? ")).strip())
nome = str(input(c_ciano("\nQual seu nome ? ")).strip().title())

# Adicionado identação para facilitar manutenção das cores
print(str(c_magenta("\n Você se chama " + 
                    c_verde(f"{nome}") + 
                    c_magenta(", e tem ") + 
                    c_ciano(f"{idade}") +
                    c_magenta(" anos!"))))