class veiculo:
    def movimentar(self):
        print("Veiculo está em movimento.")

class carro(veiculo):
    def movimentar(self):
        print("O carro dirigindo.")

class moto(veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

transporte = veiculo()
transporte.movimentar()

transpCar = carro()
transpCar.movimentar()

transpMoto = moto()
transpMoto.movimentar()