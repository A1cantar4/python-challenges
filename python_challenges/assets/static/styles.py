from colorama import Fore, Style, init

# 'Inicia' o auto reset do framework
init(autoreset=True)

# Lista para selecionar as cores das strings.
C_STYLES = {
    "branco": Fore.WHITE,
    "vermelho": Fore.RED,
    "ciano": Fore.CYAN,
    "verde": Fore.GREEN,
    "amarelo": Fore.YELLOW,
    "magenta": Fore.MAGENTA,
}

def styled(text, c_style="branco"):
    """
    Retorna o estilo de 'C_STYLES', e o texto herda o estilo, após,
    reseta para não passar (o estilo) para o próximo texto
    """
    return f"{C_STYLES.get(c_style, Fore.WHITE)}{text}{Style.RESET_ALL}"

# Funções para simplificar uso direto nas strings
def c_branco(text): return styled(text, "branco")
def c_vermelho(text): return styled(text, "vermelho")
def c_ciano(text): return styled(text, "ciano")
def c_verde(text): return styled(text, "verde")
def c_amarelo(text): return styled(text, "amarelo")
def c_magenta(text): return styled(text, "magenta")