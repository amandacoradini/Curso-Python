# método chama definição e usa-se o def para criá-lo
# se tem retorno é uma função
def soma(a, b):
    return a + b


# print(soma(1, 2))

# classe


class Calculadora:
    def __init__(self, num1, num2):  # métodopinicializar(self ref o prop obj)
        # smp q instanciar a calculadora ele vai passar p esse método
        self.a = num1
        self.b = num2

    # método da classe
    def multiplica(self):  # serve p acessar os valores da classe
        return self.a * self.b

# caso n queira instanciar a classe


class Calculadora2:
    def __init__(self):
        pass  # pass n faz nada é apenas p n ficar vazio

    def multiplica1(self, a, b):
        return a * b


if __name__ == "__main__":
    pass
    # como instanciar uma classe
    calculadora = Calculadora(10, 2)
    # qnd instancia já chama o init, outros n
    print(calculadora.a, calculadora.b)
    print(calculadora.multiplica())  # chamando o método da classe

    calculadora2 = Calculadora2()  # n precisa inicializar agr
    print(calculadora2.multiplica1(10, 2))  # chamando o método da classe
    # pode fazer sem o init tb
    # if var - se a var fo true o if vai funcionar, n precisa escrever nada
    #  o método n precisa retornar nada
