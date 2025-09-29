# Revisão no Código: 26/09/2025
# Projeto: Programa para exibir: Valor de Variável e Seu Tipo.
# [Adicionado verificador para exibir o tipo de forma personalizada].
from assets.static.styles import c_magenta, c_ciano, c_verde, c_amarelo

msg = 'Sou um texto!'
print(msg)
print(c_magenta(type(msg)))

if type(msg) == str:
    print(c_ciano('Olá, sou uma String!'))
elif type(msg) == int:
    print(c_verde('Olá, sou um número Inteiro!'))
elif type(msg) == float:
    print(c_verde('Olá, sou um número "Flutuante"!'))
elif type(msg) == bool:
    print(c_verde('Olá, posso ser Verdadeiro ou Falso!'))
else:
    print(c_amarelo('Olá, pena que não sou uma String!'))