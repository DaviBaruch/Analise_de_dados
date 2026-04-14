import pandas as pd
dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba'],
    'Salario': [5000, 6000, 7000, 8000]

}

df = pd.DataFrame(dados)
print(df)
# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)
df = pd.read_csv('dados.csv')
print(df)
idade = df['Idade']






