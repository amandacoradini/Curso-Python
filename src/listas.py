# pode ter tipos diferentes em uma lista
lista = [1, 2, 3, 4, 5, 6, 'papagaio']
lista2 = [10, 2, 8, 4, 5, 6]
lista_animais = ['Cão', 'gato', 'passaro', 'leão']
print(lista_animais[1])

# percorrre a lista de animais
for x in lista_animais:
    print(x)
# funções de lista
print(sum(lista2))
print(min(lista2))
# printa o nome com a maior letra
print(max(lista_animais))

if 'lobo' in lista_animais:
    print('existe um gato na lista')
else:
    print('n existe gato na lista')
    # add um novo elemento a lista
    lista_animais.append('lobo')
# retira o elemento da lista
lista_animais.pop(0)
lista_animais.remove('passaro')

# multiplicando uma lista (reprete 3 vezes a lista)
lista_nova = lista_animais*3
print(lista_nova)
lista_nova2 = lista2*3
print(lista_nova2)

# ordenar uma lista
lista2.sort()
print(lista2)
# ordena de forma reversa
lista2.reverse()
print(lista2)

# tupla é imutável, a lista n(pode add, ordenar, remover)
# tupla é entre parênteses (n consegue alterar um objeto da tupla)
tupla = (1, 10, 12, 14)
# len retorna o número de elementos na lista
len(tupla)
# consegue converter lista p tupla através do tuple
tupla_animal = tuple(lista_animais)
print(tupla_animal)
# converter tupla em lista
lista_numerica = list(tupla)
lista_numerica[0] = 100
print(lista_numerica)
