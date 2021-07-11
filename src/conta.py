import cliente

class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite


    def deposita(self, valor):
        self.saldo += valor


if __name__ == '__main__':
    conta = Conta('123-4', 'João', 1000.0)
    conta.deposita(100.0)
    print(conta.numero)
    print(conta.titular)
    print(conta.saldo)
    print(conta.limite)
