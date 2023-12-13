# Arquivo com código de testa da classe Veículo

from veiculo import Veiculo

minhaCaranga = Veiculo('Fiat', '147', 'Amarelo', 0)

# Exibindo minha caranga
print('\n\t\t\t -- Minha Caranga --')
print(minhaCaranga)

# Acelerando a minha caranga
for i in range(0, 200):
    minhaCaranga.acelerar()

# Exibindo minha caranga acelerada
print('\n\t\t\t -- Minha Caranga Acelerada --')
print(minhaCaranga)

# Freando a minha caranga
for i in range(0, 200):
    minhaCaranga.frear()

# Exibindo minha caranga freando
print('\n\t\t\t -- Minha Caranga Freando --')
print(minhaCaranga)