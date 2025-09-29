from assets.static.styles import c_amarelo, c_vermelho, c_magenta, c_verde

class Quadrado():
    """ Classe para calcular o quadrado de um número """
    def __init__(self, valor: int):
        """ Inicializa o objeto capturando o valor do quadrado """
        self.valor = valor
        
    def calcula_quadrado(self) -> int:
        """ Realiza o cálculo do quadrado """
        return self.valor * self.valor
    
    def __str__(self) -> str:
        """
        Retorna a representação em string do cálculo já formatada com cores.
        """
        return (c_amarelo(f"O quadrado de ") + 
                c_vermelho(f"{self.valor}") + 
                c_amarelo(" é ") + 
                c_verde(f"{self.calcula_quadrado()}"))
        

pergunta = Quadrado(int(input(c_magenta(f"\nOlá, qual número você quer calcular? ").strip())))
print(pergunta)