import pandas as pd

data = {
    'Jogo': [
        'Flamengo vs Time A', 'Flamengo vs Time B', 'Flamengo vs Time C',
        'Flamengo vs Time D', 'Flamengo vs Time E', 'Flamengo vs Time F',
        'Flamengo vs Time G', 'Flamengo vs Time H', 'Flamengo vs Time I',
        'Flamengo vs Time J'
    ],
    'Faltas Feitas': [15, 12, 18, 10, 14, 11, 13, 16, 9, 17],
    'Faltas Recebidas': [10, 14, 9, 13, 16, 12, 11, 15, 18, 14]
}

df = pd.DataFrame(data)

print("Dados dos jogos do Flamengo na temporada de 2023:")
print(df)

total_faltas_feitas = df['Faltas Feitas'].sum()
total_faltas_recebidas = df['Faltas Recebidas'].sum()

media_faltas_feitas = df['Faltas Feitas'].mean()
media_faltas_recebidas = df['Faltas Recebidas'].mean()

print("\nAnálise de Dados:")
print(f"Total de faltas feitas pelo Flamengo na temporada: {total_faltas_feitas}")
print(f"Total de faltas recebidas pelo Flamengo na temporada: {total_faltas_recebidas}")
print(f"Média de faltas feitas pelo Flamengo por jogo: {media_faltas_feitas:.2f}")
print(f"Média de faltas recebidas pelo Flamengo por jogo: {media_faltas_recebidas:.2f}")

jogo_mais_faltas_feitas = df.loc[df['Faltas Feitas'].idxmax()]['Jogo']
jogo_mais_faltas_recebidas = df.loc[df['Faltas Recebidas'].idxmax()]['Jogo']

print(f"Jogo com o maior número de faltas feitas pelo Flamengo: {jogo_mais_faltas_feitas}")
print(f"Jogo com o maior número de faltas recebidas pelo Flamengo: {jogo_mais_faltas_recebidas}")
