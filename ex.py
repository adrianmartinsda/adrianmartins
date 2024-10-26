class vendedor ():
    def __int__(self, nome):
        self.nome= nome

vendedor1= vendedor(input("nome do vendedor:"))
print("vendedor: ",vendedor1.nome)

class pessoa():
    def __init__(self,nome,sobrenome,idade,cidade):
        self.nome = nome
        self.sobrenome= sobrenome
        self.idade= idade
        self.cidade= cidade

nome_inp = input("qual o seu nome?")
sobrenome_inp=input("qual o seu sobrenome?")
idade_inp= input("qual a sua idade?")
cidade_inp= input("qual a sua cidade?")

pessoa= pessoa(nome_inp,sobrenome_inp, idade_inp, cidade_inp)
print(f"\nome:{pessoa.nome}\nsobrenome: {pessoa.sobrenome}\nidade: {pessoa.idade}\ncidade:{pessoa.cidade}")
    





