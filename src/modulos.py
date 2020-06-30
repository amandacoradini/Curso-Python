# Módulos são os arquivos .py (esses módulos podem interagir entre si)
# qnd importa o arquivo, vai td q tem nele, para esconder o q
# n quer mostrar usa if __name__ == '__main__': e coloca
# o q vc n quer q aparecça nesse if (significa q o q ta lá só)
# vai aparecer caso o arquivo q o import seja ele msm
from funcoes_met_cla import Calculadora
calc = Calculadora(5, 2)
print(calc)

# lambda é uma função anônima - uma função genérica q
# pode ser utilizada em outros módulos
# nome da função - lambda - o parâmetroq ela vai receber
# ela é eficiente p funções q podem ser resolvidas com 1 linha
# ela fica dentro de uma variável, ela n tem nome


def contador_letras(lista): return [len(x) for x in lista]


# ele retorna uma lista []
# vai pegar o len de x para cada x da lista
lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))


def soma(a, b): return a + b


print(soma(1, 5))

# dicionario feito com funções lambda
Calculadora3 = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
}
# soma recebe a função anonima através dessa atribuição
soma = Calculadora3['soma']
subtracao = Calculadora3['subtracao']
print(soma(10, 5))
print(subtracao(10, 5))
