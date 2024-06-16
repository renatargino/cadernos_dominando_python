import colorama

# print(help(colorama.Fore))

# carregar apenas o que vamos utilizar
from colorama import Fore

# podemos importar mais de um por vez
from colorama import Fore, Back

# import minhas_funcoes as mf

# print(mf.somar(10,20))
# print(mf.multiplicar(1,2,3,4))

from minhas_funcoes import somar
# quando importado assim, não precisamos colocar o nome antes de chamar a função

print(somar(50,30))