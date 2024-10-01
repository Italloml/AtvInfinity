class animal:
    def falar():
        print("Esse animal faz um som")

class cachorro(animal):
    def falar(self):
        print("O cachorro late")

class gato(animal):
    def falar(self):
        print("Esse gato mia.")


ani1 = cachorro()
ani1.falar()

ani2 = gato()
ani2.falar()

