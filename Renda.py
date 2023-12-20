import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import random as random

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

#Carregando os dados
df = pd.read_csv('C:/ProjetosNovos/Renda/dados.csv')
print(df.describe())



#Análise Exploratória
df["UF"] = df["UF"].astype(str)
df["UF"] = df["UF"].map(
    {"11": "RO", "12": "AC", "13": "AM", "14": "RR", "15": "PA", "16": "AP", "17": "TO", "21": "MA", "22": "PI", "23": "CE", "24": "RN", "25": "PB", "26": "PE", "27": "AL", "28": "SE", "29": "BA", "31": "MG", "32": "ES", "33": "RJ", "35": "SP", "41": "PR", "42": "SC", "43": "RS", "50": "MS", "51": "MT", "52": "GO", "53": "DF"},
    na_action=None,
)
df["Sexo"] = df["Sexo"].astype(str)
df["Sexo"] = df["Sexo"].map(
    {"0": "Masculino", "1": "Feminino"},
    na_action=None,
)
df = df.rename(columns={'Cor': 'Cútis'})
df["Cútis"] = df["Cútis"].astype(str)
df["Cútis"] = df["Cútis"].map(
    {"0": "Indígena", "2": "Branca", "4": "Preta", "6": "Amarela", "8": "Parda", "9": "Sem Declaração"},
    na_action=None,
)
df["Altura"] = df["Altura"].round(2)

#1 - Demonstração da Correlação entre as variáveis
f,ax = plt.subplots(figsize=(12, 12))
sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt=".2f", ax=ax)

#2 - UF´s por anos de estudo?
plt.figure(figsize=(20,15))
renda_por_uf = sns.barplot(data = df,
                           x = 'UF',
                           y = 'Anos de Estudo',
                           errorbar=('ci', False)
                           )
plt.grid(color = 'black', linestyle = '--', linewidth = 0.3)
plt.show()

#3 - UF´s por renda?
plt.figure(figsize=(20,15))
renda_por_uf = sns.barplot(data = df,
                           x = 'UF',
                           y = 'Renda',
                           errorbar=('ci', False)
                           )
plt.grid(color = 'black', linestyle = '--', linewidth = 0.3)
plt.show()


#4 - Número de pessoas por altura e sexo(feminino e masculino) nas UF´s
g = sns.FacetGrid(df, col= 'UF', hue='Sexo', col_wrap=1)
g.map(sns.histplot, 'Altura')
plt.xlim(xmin=1.5, xmax = 2.0)
g.add_legend()


#5 - Número de pessoas por altura e Cútis nas UF´s
g = sns.FacetGrid(df, col= 'UF', hue='Cútis', col_wrap=1)
g.map(sns.histplot, 'Altura')
plt.xlim(xmin=1.5, xmax = 2.0)
g.add_legend()

#6 - Quais os 10 Estados que mais responderam o estudo
quantidade_pop_estudo = df['UF'].value_counts()

plt.figure(figsize=(15,5))
plt.plot(quantidade_pop_estudo.head(10), linestyle='none', markersize=15, marker='h')
plt.title('Os 10 estados que mais responderam a pesquisa', fontsize=20)
plt.xticks(rotation=45)
plt.xlabel('UF', fontsize=15)
plt.ylabel('Quantidade', fontsize=15)
plt.grid(alpha=.3)
plt.margins(.05)
plt.show()

#7 - Quais os 10 Estados que menos responderam o estudo
quantidade_pop_estudo = df['UF'].value_counts()

plt.figure(figsize=(15,5))
plt.plot(quantidade_pop_estudo.tail(10), linestyle='none', markersize=15, marker='h')
plt.title('Os 10 estados que mais responderam a pesquisa', fontsize=20)
plt.xticks(rotation=45)
plt.xlabel('UF', fontsize=15)
plt.ylabel('Quantidade', fontsize=15)
plt.grid(alpha=.3)
plt.margins(.05)
plt.show()

