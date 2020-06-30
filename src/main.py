# n precisa de ;
# o input retona uma string, então pra fazer uma soma tem q convertê-lo
a = int(input('Entre com o primero valor:'))
b = int(input('Entre com o segundo valor:'))
soma = a + b
print(type(a))
# soma é um float, mas posso converté-la em int (arredonda)
print(int(soma))
# da erro a variável receber seu tipo convertido se forem diferentes, se forem
# dois numéricos n da erro
# soma = str(soma)
# para conseguir printar uma string junto com um valor não
# string no print tem q converter esse número p uma string
# print(soma)
# convertendo um número em string e concatenando
print('soma:' + str(soma))
# da pra converter string em numeor
x = '1'
y = 1 + int(x)
print(y)
# o format consegue fazer a concaatenação dentro da string idependete
# do tipo da variável
print('soma: {} y: {}' .format(soma, y))
print('soma: {sum} \ny: {y2}' .format(sum=soma, y2=y))

# para fazer uma comparação desses números recebidos precisa converter p int
# o que está dentro do if é o q está identado, ele n usa {}
if a > b:
    print('O maior valor é: {}'.format(a))
else:
    print('O maior valor é: {}'.format(b))

# operadores unários &&==and ||==or !==not
c = int(input('entre com o terceiro valor: '))
if a > b and a > c:
    print('O maior valor é: {}'.format(a))
# elif é um else com if
elif b > a and b > c:
    print('O maior valor é: {}'.format(b))
else:
    print('O maior valor é: {}'.format(c))

# cria um loop de 1 a 9, vai smp do primeiro número até o último menos 1

for z in range(1, 10):
    print(z)
# é assim q faz o a++ no python
a += 1

w = 0
while w < 10:
    print(w)
    w += 1
