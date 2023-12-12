# Arquivo com código de testa da classe Veículo

from veiculo import Veiculo

minhaCaranga = Veiculo(marca='Fiat', modelo='147', cor='Amarelo', velocidade=8)

# Exibindo minha caranga
print('\n\t\t\t -- Minha Caranga -- \n')
print(minhaCaranga)

# Acelerando a minha caranga
for i in range(0, 200):
    minhaCaranga.acelerar()

# Exibindo minha caranga acelerada
print('\n\t\t\t -- Minha Caranga Acelerada -- \n')
print(minhaCaranga)