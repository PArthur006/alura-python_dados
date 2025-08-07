# Aula 1: Explore Dados com Pandas

Nesta aula, iniciamos nossa jornada na análise de dados com Python utilizando a biblioteca Pandas. O objetivo foi carregar, inspecionar e realizar as primeiras transformações em um conjunto de dados sobre salários na área de tecnologia.

## Comandos e Métodos Essenciais

### 1. Importando a Biblioteca
Sempre começamos importando o Pandas. A convenção é usar o alias `pd`.
```python
import pandas as pd
```

### 2. Carregando Dados
Para ler dados de um arquivo CSV (local ou de uma URL), utilizamos a função `pd.read_csv()`. O resultado é um objeto chamado **DataFrame**.
```python
df = pd.read_csv("url_do_seu_arquivo.csv")
```

### 3. Inspeção Inicial do DataFrame
Após carregar os dados, é crucial entendê-los.

- **`.head(n)`**: Exibe as primeiras `n` linhas do DataFrame (por padrão, 5). Ótimo para ter uma primeira impressão dos dados.
  ```python
  print(df.head())
  ```
- **`.info()`**: Fornece um resumo técnico, incluindo o tipo de dado de cada coluna (`Dtype`), a quantidade de valores não nulos e o uso de memória. Essencial para identificar tipos de dados incorretos ou valores ausentes.
  ```python
  df.info()
  ```
- **`.shape`**: Retorna uma tupla com o número de (linhas, colunas) do DataFrame.
  ```python
  linhas, colunas = df.shape
  print(f"O DataFrame tem {linhas} linhas e {colunas} colunas.")
  ```
- **`.columns`**: Lista todos os nomes das colunas.
  ```python
  print(df.columns)
  ```

### 4. Renomeando Colunas
Nomes de colunas claros facilitam a análise. O método `.rename()` com o parâmetro `columns` e um dicionário é a forma ideal.

- **Dicionário de renomeação**: `{ "nome_antigo": "nome_novo", ... }`
- **`inplace=True`**: Modifica o DataFrame diretamente, sem precisar atribuí-lo a uma nova variável.
```python
renomear_colunas = {
    'work_year': 'ano_de_trabalho',
    'experience_level': 'senioridade'
}
df.rename(columns=renomear_colunas, inplace=True)
```

### 5. Análise de Categorias
Para entender os valores de uma coluna categórica.

- **`.value_counts()`**: Conta a ocorrência de cada valor único em uma coluna. Muito útil para entender a distribuição das categorias.
  ```python
  print(df["senioridade"].value_counts())
  ```

### 6. Mapeamento e Tradução de Valores
Para substituir valores em uma coluna com base em um dicionário, o método `.map()` é a ferramenta mais direta e eficiente.

- **Dicionário de mapeamento**: `{ "valor_antigo": "valor_novo", ... }`
- **Como funciona**: O `map` percorre a coluna e substitui cada valor pela sua correspondência no dicionário.
```python
traducao_senioridade = {
    'SE': 'Sênior',
    'MI': 'Pleno'
}
df['senioridade'] = df['senioridade'].map(traducao_senioridade)
```

# Aula 2: Preparação e Limpeza de Dados

Nesta aula, focamos em técnicas para tratar dados ausentes e otimizar os tipos de dados (`dtypes`) das colunas, passos fundamentais para garantir a qualidade e a eficiência da análise.

## Comandos e Métodos Essenciais

### 1. Tratamento de Dados Ausentes (NaN)
Valores ausentes podem distorcer análises. A primeira decisão é se vamos removê-los ou preenchê-los.

- **`.dropna()`**: Remove todas as **linhas** que contêm pelo menos um valor nulo (NaN). É a abordagem mais simples, mas pode levar à perda de muitos dados se os valores ausentes estiverem espalhados.
  ```python
  df_sem_nulos = df.dropna()
  ```

### 2. Conversão de Tipos de Dados (`dtypes`)
A otimização dos tipos de dados é crucial para economizar memória e acelerar o processamento.

- **`.astype()`**: Converte uma coluna para um tipo específico.
- **`.assign()`**: Permite criar ou modificar várias colunas de uma vez. É uma forma elegante de encadear múltiplas transformações, incluindo a conversão de tipos.

**Tipos de Dados Comuns:**
- **`int64`**: Para números inteiros.
- **`float64`**: Para números com casas decimais.
- **`category`**: Ideal para colunas de texto com um número limitado de valores únicos (categorias). Reduz drasticamente o uso de memória e acelera operações como `groupby`.

```python
df_otimizado = df_limpo.assign(
    ano=df_limpo['ano'].astype('int64'),
    usd=df_limpo['usd'].astype('int64'),
    remoto=df_limpo['remoto'].astype('category'),
    tamanho_empresa=df_limpo['tamanho_empresa'].astype('category')
)
```

### 3. Salvando o DataFrame Processado
Após a limpeza e preparação, salvamos o resultado para uso futuro.

- **`.to_csv('nome_do_arquivo.csv', index=False)`**: Salva o DataFrame em um arquivo CSV.
  - **`index=False`**: Impede que o Pandas salve o índice do DataFrame como uma coluna no arquivo, o que geralmente é o comportamento desejado.

```python
df_otimizado.to_csv('dados_tratados.csv', index=False)
```