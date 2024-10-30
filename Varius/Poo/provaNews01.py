class ContaBancaria:
    def __init__(self, titular: str):
        self._titular = titular
        self._saldo = 0.0  # Inicializa o saldo como zero

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor: float):
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self._titular}: R${self._saldo:.2f}")

# Exemplo de uso:
if __name__ == "__main__":
    conta = ContaBancaria("")
    conta.exibir_saldo()  
    conta.depositar()   
    conta.exibir_saldo() 
    conta.sacar()        
    conta.exibir_saldo() 
    conta.sacar()
