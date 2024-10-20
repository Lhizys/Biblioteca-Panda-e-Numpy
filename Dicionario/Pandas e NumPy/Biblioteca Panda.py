import pandas as pd

dados = {
    'Nome': ['Joao', 'Lucas', 'Gabi'],
    'Idade': [25, 36, 33],
    'Cidade': ['Niteroi', 'Caxias', 'Bangu']
}

df = pd.DataFrame(dados)
print(f'/n {df}')
print(30*'=')

# Idade
print(df['Idade'])
print(30*'=')

# Cidade
print(df['Cidade'])
print(30*'=')
