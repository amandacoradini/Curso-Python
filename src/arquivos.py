# importação de arquivos
# o 2 param é o mode, w é escrever
# gerou um arquivo teste vazio
arquivo = open('teste.txt', 'w')  # pode gerar o arquivo em qualq dir
# o write sobrepõe o q está escrito
arquivo.write('Minha primeira escrita, 1')
arquivo.close()
# se o arq já existe e vc n quer sobrescrever, usa o a no mode
arquivo = open('teste.txt', 'a')
# o write sobrepõe o q está escrito
arquivo.write('\nMinha segunda escrita, 2')
arquivo.close()
# para ler o arquivo
arquivo = open('teste.txt', 'r')
texto = arquivo.read()
# print(texto)
# transformando o txt em uma lista
# qnd ele achar o \n ele vai separar em um termo da lista
texto2 = texto.split('\n')
# print(texto2)

txt = []
txt2 = []
for x in texto2:
    texto3 = x.split(',')
    primeira_frase = texto3.pop(0)
    txt.append({primeira_frase: texto3})
    for j in texto3:
        txt2.append(int(j))

# print(texto3)
print(txt)
print(txt2)
