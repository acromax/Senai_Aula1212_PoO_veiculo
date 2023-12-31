# Atividade sobre POO - Senai dia 12/12/2023

# Classe Veículo
class Veiculo(object):
    # Método Construtor
    def __init__(self, marca, modelo, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

    # Encapsulamento
    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo

    def setCor(self, cor):
        self.cor = cor
    def getCor(self):
        return self.cor

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade
    def getVelocidade(self):
        return self.velocidade

    # Retorno de dados da classe
    def __str__(self):
        return (
            ' Marca: ' + str(self.getMarca()) +
            '\n Modelo: ' + str(self.getModelo()) +
            '\n Cor: ' + str(self.getCor()) +
            '\n Velocidade: ' + str(self.getVelocidade()) + 'kmm/h'
        )

    # Método Acelerar
    def acelerar(self):
        if self.velocidade < 120:
            self.velocidade+=1

    # Método Frear
    def frear(self):
        if self.velocidade > 0:
            self.velocidade-=1
