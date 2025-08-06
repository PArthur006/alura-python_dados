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
