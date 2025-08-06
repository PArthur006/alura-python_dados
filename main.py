# Importação de bibliotecas
import os
import pandas as pd

# --- CARREGAMENTO E INSPEÇÃO INICIAL DOS DADOS ---

# Limpa o terminal para uma visualização mais limpa ao executar o script
os.system('clear')

# Carrega o DataFrame a partir de um arquivo CSV online
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Comandos de inspeção (comentados para não poluir a saída final)
# print(df.head(5))  # Mostra as 5 primeiras linhas
# df.info()  # Resumo técnico do DataFrame (tipos de dados, valores nulos)
# linhas, colunas = df.shape
# print(f"O arquivo possui {linhas} linhas e {colunas} colunas.")
# print(df.columns) # Lista as colunas originais


# --- TRADUÇÃO E RENOMEAÇÃO DAS COLUNAS ---

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

# Aplica a renomeação ao DataFrame
df.rename(columns=renomear_colunas, inplace=True)


# --- TRADUÇÃO DOS VALORES DAS COLUNAS CATEGÓRICAS ---

# Dicionários de tradução para cada coluna
traducao_senioridade = {
    'SE': 'Sênior',
    'MI': 'Pleno',
    'EN': 'Júnior',
    'EX': 'Executivo'
}

traducao_contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Meio Período',
    'CT': 'Contrato',
    'FL': 'Freelance'
}

traducao_remoto = {
    100: 'Remoto',
    50: 'Híbrido',
    0: 'Presencial'
}

traducao_tamanho_empresa = {
    'L': 'Grande',
    'M': 'Média',
    'S': 'Pequena'
}

# Aplica as traduções usando o método .map()
df['senioridade'] = df['senioridade'].map(traducao_senioridade)
df['contrato'] = df['contrato'].map(traducao_contrato)
df['remoto'] = df['remoto'].map(traducao_remoto)
df['tamanho_empresa'] = df['tamanho_empresa'].map(traducao_tamanho_empresa)


# --- EXIBIÇÃO DOS DADOS PROCESSADOS ---

# Imprime a contagem de valores para verificar as traduções
print("--- DADOS PROCESSADOS ---")
print("\nSENIORIDADE:\n", df["senioridade"].value_counts())
print("\nTIPOS DE CONTRATO:\n", df["contrato"].value_counts())
print("\nTAXA DE TRABALHO REMOTO:\n", df["remoto"].value_counts())
print("\nTAMANHO DA EMPRESA:\n", df["tamanho_empresa"].value_counts())
print("\n-------------------------\n")
print("Tradução e limpeza concluídas. Amostra do resultado final:")
print(df.head())