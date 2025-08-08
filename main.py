# Importação de bibliotecas
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 
import matplotlib

# --- CONFIGURAÇÕES INICIAIS ---
# Limpa o terminal para uma visualização mais limpa ao executar o script
os.system('clear')

# --- AULA 01: CARREGAMENTO E TRADUÇÃO DOS DADOS ---

# Carrega o DataFrame a partir de um arquivo CSV online
# O dataset contém informações sobre salários em diferentes cargos de tecnologia.
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Dicionário para renomear as colunas para o português
# Isso facilita a compreensão e manipulação dos dados para falantes de português.
renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns=renomear_colunas, inplace=True)

# Dicionários de tradução para os valores das colunas categóricas
# Isso padroniza e torna os valores mais legíveis.
traducao_senioridade = {'SE': 'Sênior', 'MI': 'Pleno', 'EN': 'Júnior', 'EX': 'Executivo'}
traducao_contrato = {'FT': 'Tempo Integral', 'PT': 'Meio Período', 'CT': 'Contrato', 'FL': 'Freelance'}
traducao_remoto = {100: 'Remoto', 50: 'Híbrido', 0: 'Presencial'}
traducao_tamanho_empresa = {'L': 'Grande', 'M': 'Média', 'S': 'Pequena'}

# Aplica as traduções usando o método .map()
# O .map() é eficiente para substituir valores em uma série com base em um dicionário.
df['senioridade'] = df['senioridade'].map(traducao_senioridade)
df['contrato'] = df['contrato'].map(traducao_contrato)
df['remoto'] = df['remoto'].map(traducao_remoto)
df['tamanho_empresa'] = df['tamanho_empresa'].map(traducao_tamanho_empresa)

# --- AULA 02: LIMPEZA E PREPARAÇÃO DOS DADOS ---

# A função .dropna() remove linhas que contêm valores nulos (NaN).
# É uma forma direta de lidar com dados ausentes, garantindo que o DataFrame
# não tenha buracos que possam atrapalhar análises ou modelos futuros.
df_limpo = df.dropna()

# O método .assign() permite criar ou modificar múltiplas colunas de uma vez.
# Aqui, ele está sendo usado para converter os tipos de dados (dtypes) de várias colunas.
# A conversão de tipos é crucial para otimizar o uso de memória e garantir
# que as operações em cada coluna sejam computacionalmente eficientes e corretas.
df_limpo = df_limpo.assign(
    # Converte a coluna 'ano' para o tipo inteiro.
    ano = df_limpo['ano'].astype('int64'),
)

# --- AULA 03: CRIE GRÁFICOS E CONTE HISTÓRIAS COM OS DADOS ---
# Esta seção demonstra a criação de diferentes tipos de gráficos usando Matplotlib, Seaborn e Plotly.

# Configura o backend do Matplotlib para ser interativo (necessário para exibir gráficos em janelas)
# Se você estiver em um ambiente sem interface gráfica (como um servidor), pode comentar esta linha
# e usar fig.write_html() ou fig.write_image() para salvar os gráficos.
matplotlib.use('TkAgg')

# --- Gráfico de Barras com Matplotlib (Distribuição de Senioridade) ---
# Este gráfico mostra a contagem de profissionais por nível de senioridade.
plt.figure(figsize=(10, 6)) # Define o tamanho da figura
ax = df_limpo['senioridade'].value_counts().plot(kind='bar')

# Adiciona título e rótulos aos eixos para clareza
ax.set_title('Distribuição de Senioridade', fontsize=16)
ax.set_xlabel('Nível de Senioridade', fontsize=12)
ax.set_ylabel('Número de Profissionais', fontsize=12)

# Adiciona os rótulos de dados em cada barra para mostrar os valores exatos
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.tight_layout() # Ajusta o layout para evitar sobreposição
plt.show() # Exibe o gráfico em uma janela

# --- Gráfico de Barras com Seaborn (Salário Médio por Senioridade) ---
# Este gráfico compara o salário médio em USD para cada nível de senioridade.
# A ordem das barras é definida pelo salário médio, do menor para o maior.
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem, palette='viridis') # 'viridis' é uma paleta de cores
plt.title('Salário Médio por Nível de Senioridade', fontsize=14)
plt.xlabel('Senioridade', fontsize=12)
plt.ylabel('Salário Médio Anual (USD)', fontsize=12)
plt.tight_layout()
plt.show()

# --- Histograma com Seaborn (Distribuição de Salários Anuais) ---
# Mostra a distribuição de frequência dos salários anuais em USD.
plt.figure(figsize=(10, 5))
sns.histplot(df_limpo['usd'], bins=50, kde=True, color='skyblue') # 'bins' define o número de barras, 'kde' adiciona a curva de densidade
plt.title('Distribuição de Salários Anuais', fontsize=14)
plt.xlabel('Salário Anual (USD)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.tight_layout()
plt.show()

# --- Boxplot com Seaborn (Salários Anuais por Senioridade) ---
# Este gráfico mostra a distribuição (mediana, quartis, outliers) dos salários
# para cada nível de senioridade.
# A ordem é definida manualmente para garantir uma sequência lógica.
ordem_senioridade = ['Júnior', 'Pleno', 'Sênior', 'Executivo']

plt.figure(figsize=(8, 5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade', legend=False)
plt.title('Boxplot de Salários Anuais por Nível de Senioridade', fontsize=14)
plt.xlabel('Nível de Senioridade', fontsize=12)
plt.ylabel('Salário Anual (USD)', fontsize=12)
plt.tight_layout()
plt.show()

# --- Gráfico de Pizza Interativo com Plotly (Proporção dos Tipos de Trabalho) ---
# O Plotly cria gráficos interativos que podem ser visualizados em navegadores.
# Calcula a contagem de cada tipo de trabalho (Remoto, Híbrido, Presencial).
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

# Cria o gráfico de pizza
fig = px.pie(remoto_contagem,
                names='tipo_trabalho',
                values='quantidade',
                title='Proporção dos Tipos de Trabalho',
                hole=0.5 # Cria um gráfico de rosca (donut chart)
)

# Atualiza os traços para exibir o percentual e o rótulo dentro das fatias
fig.update_traces(textposition='inside', textinfo='percent+label')

# Opções de visualização/salvamento do gráfico Plotly:
# 1. Exibir em uma janela do navegador (requer ambiente gráfico e navegador configurado)
# fig.show() 

# 2. Salvar como arquivo HTML (mantém a interatividade, pode ser aberto em qualquer navegador)
fig.write_html("grafico_proporcao_trabalho.html")

# 3. Salvar como imagem estática (requer a instalação da biblioteca 'kaleido': pip install kaleido)
# fig.write_image("grafico_proporcao_trabalho.png")

# --- Gráfico de Barras Interativo com Plotly (Salário Médio por Senioridade) ---
# Reutiliza os dados de salário médio por senioridade para um gráfico interativo.
senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig_bar_plotly = px.bar(senioridade_media_salario,
                x='senioridade',
                y='usd',
                title='Salário Médio por Nível de Senioridade (Interativo)',
                labels={'usd': 'Salário Anual (USD)', 'senioridade': 'Nível de Senioridade'},
                color='senioridade', # Colore as barras por senioridade
                template='plotly_white' # Define um tema visual
)

# Opções de visualização/salvamento do gráfico Plotly:
# fig_bar_plotly.show()
fig_bar_plotly.write_html("grafico_salario_senioridade_interativo.html")
# fig_bar_plotly.write_image("grafico_salario_senioridade_interativo.png")