# Importação de bibliotecas
import os
import pandas as pd
import numpy as np

# --- CONFIGURAÇÕES INICIAIS ---
# Limpa o terminal para uma visualização mais limpa ao executar o script
os.system('clear')

# --- AULA 01: CARREGAMENTO E TRADUÇÃO DOS DADOS ---

# Carrega o DataFrame a partir de um arquivo CSV online
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Dicionário para renomear as colunas para o português
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

# Dicionários de tradução para os valores das colunas
traducao_senioridade = {'SE': 'Sênior', 'MI': 'Pleno', 'EN': 'Júnior', 'EX': 'Executivo'}
traducao_contrato = {'FT': 'Tempo Integral', 'PT': 'Meio Período', 'CT': 'Contrato', 'FL': 'Freelance'}
traducao_remoto = {100: 'Remoto', 50: 'Híbrido', 0: 'Presencial'}
traducao_tamanho_empresa = {'L': 'Grande', 'M': 'Média', 'S': 'Pequena'}

# Aplica as traduções usando o método .map()
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
    # Converte o salário em USD para o tipo inteiro para facilitar cálculos.
    usd = df_limpo['usd'].astype('int64'),
    # Converte colunas textuais com um número limitado de valores únicos
    # para o tipo 'category'. Isso economiza memória e pode acelerar operações
    # de agrupamento e junção.
    remoto = df_limpo['remoto'].astype('category'),
    tamanho_empresa = df_limpo['tamanho_empresa'].astype('category'),
    contrato = df_limpo['contrato'].astype('category'),
    senioridade = df_limpo['senioridade'].astype('category')
)

# O método .to_csv() salva o DataFrame processado em um arquivo CSV.
# O parâmetro 'index=False' evita que o índice do DataFrame seja salvo como uma
# coluna extra no arquivo, mantendo os dados limpos.
# df_limpo.to_csv('salarios_tratados.csv', index=False)

# --- VERIFICAÇÃO FINAL ---
# Imprime informações do DataFrame limpo para confirmar as mudanças de tipo
# e a ausência de valores nulos.
print("--- Informações do DataFrame após a limpeza e conversão ---")
df_limpo.info()
