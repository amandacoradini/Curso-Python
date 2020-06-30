# criando e manipulando conjuntos em py (ele fica como tipo 'set = conjunto)
# n permite duplicidade, se tiver dois 4 só vai aparaecer um
conjunto = {1, 2, 3, 4, 5}
# add e removendo elemento ao conjunto
conjunto.add(6)
conjunto.discard(3)
print(conjunto)

# união dos conjuntos
conj1 = {1, 2, 3, 4}
conj2 = {4, 5, 6}
conjunto_uniao = conj1.union(conj2)
print(conjunto_uniao)

# intersecção = td q tem no conj um e no conj 2
conj_intersec = conj1.intersection(conj2)
print(conj_intersec)

# diferença entre os conjutos (mostra os números q só tem no conjunto 1 e n
#  tem no 2, se fosse) ao contrário mostrari o do 2
conj_dife = conj1.difference(conj2)
print(conj_dife)

# diferença simétrica(td q n tem nos dois-aquilo q só tem no 1 e q só tem no 2)
conj_dife_sim = conj1.symmetric_difference(conj2)
print(conj_dife_sim)

# pertinência
# sub set vai retornar se um conjunto é subconjunto do outro
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)  # retorna true pq ele é um subconjunto

# verifica se ele é um subconjunto
# smp q um conjA é subocnj de um conjB, o conjB é um superconj
# (B tem tds os ele de A)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

# converter uma lista p conjunto (queremos tirar a duplicidade dela)
# conjunto_animais = set(lista)
# lista_animais = list(conjunto_animais)
