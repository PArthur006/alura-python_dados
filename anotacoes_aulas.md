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

# Aula 3: Crie Gráficos e Conte Histórias com os Dados

Nesta aula, exploramos diversas bibliotecas de visualização de dados em Python para criar gráficos informativos e atraentes. O objetivo é transformar dados brutos em insights visuais que contam uma história.

## Bibliotecas de Visualização

-   **Matplotlib**: A biblioteca fundamental para criar gráficos estáticos em Python. Oferece controle granular sobre todos os elementos do gráfico.
-   **Seaborn**: Construída sobre o Matplotlib, o Seaborn simplifica a criação de gráficos estatísticos complexos com menos código e um visual mais agradável por padrão.
-   **Plotly Express**: Uma biblioteca de alto nível que facilita a criação de gráficos interativos e dinâmicos. Ideal para dashboards e análises exploratórias onde a interatividade é desejada.

## Comandos e Métodos Essenciais

### 1. Configuração do Matplotlib para Interatividade

Para que o Matplotlib exiba gráficos em janelas interativas (em ambientes com interface gráfica), é necessário configurar o backend.

```python
import matplotlib
matplotlib.use('TkAgg') # 'TkAgg' é um backend comum para exibir janelas
import matplotlib.pyplot as plt
```
*   **`matplotlib.use('TkAgg')`**: Define o backend que o Matplotlib usará para renderizar os gráficos. `TkAgg` é uma boa escolha para ambientes de desktop. Se você estiver em um ambiente sem interface gráfica (como um servidor), esta linha pode ser comentada, e você deve optar por salvar os gráficos como arquivos (HTML ou imagem).

### 2. Gráficos com Matplotlib

#### Gráfico de Barras (`.plot(kind='bar')`)
Usado para mostrar a distribuição de frequência de categorias.

```python
plt.figure(figsize=(10, 6)) # Define o tamanho da figura (largura, altura)
ax = df_limpo['senioridade'].value_counts().plot(kind='bar')

# Personalização: Título, rótulos dos eixos e anotações nas barras
ax.set_title('Distribuição de Senioridade', fontsize=16)
ax.set_xlabel('Nível de Senioridade', fontsize=12)
ax.set_ylabel('Número de Profissionais', fontsize=12)

# Adiciona os rótulos de dados em cada barra
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.tight_layout() # Ajusta o layout para evitar sobreposição de elementos
plt.show() # Exibe o gráfico
```

### 3. Gráficos com Seaborn

#### Gráfico de Barras (`sns.barplot()`)
Ideal para comparar valores numéricos entre diferentes categorias.

```python
import seaborn as sns
# Calcula a média de USD por senioridade e ordena para o gráfico
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem, palette='viridis')
plt.title('Salário Médio por Nível de Senioridade', fontsize=14)
plt.xlabel('Senioridade', fontsize=12)
plt.ylabel('Salário Médio Anual (USD)', fontsize=12)
plt.tight_layout()
plt.show()
```
*   **`palette='viridis'`**: Define a paleta de cores a ser usada no gráfico.

#### Histograma (`sns.histplot()`)
Mostra a distribuição de uma variável numérica, agrupando valores em "bins" (intervalos).

```python
plt.figure(figsize=(10, 5))
sns.histplot(df_limpo['usd'], bins=50, kde=True, color='skyblue')
plt.title('Distribuição de Salários Anuais', fontsize=14)
plt.xlabel('Salário Anual (USD)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.tight_layout()
plt.show()
```
*   **`bins`**: Número de intervalos para agrupar os dados.
*   **`kde=True`**: Adiciona uma estimativa de densidade de kernel (curva suave) que representa a distribuição dos dados.

#### Boxplot (`sns.boxplot()`)
Exibe a distribuição de dados numéricos para diferentes categorias, mostrando mediana, quartis e outliers.

```python
# Define a ordem manual das categorias para exibição no gráfico
ordem_senioridade = ['Júnior', 'Pleno', 'Sênior', 'Executivo']

plt.figure(figsize=(8, 5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade', legend=False)
plt.title('Boxplot de Salários Anuais por Nível de Senioridade', fontsize=14)
plt.xlabel('Nível de Senioridade', fontsize=12)
plt.ylabel('Salário Anual (USD)', fontsize=12)
plt.tight_layout()
plt.show()
```
*   **`order`**: Controla a ordem das categorias no eixo x.
*   **`palette='Set2'`**: Outra opção de paleta de cores.
*   **`hue`**: Divide os dados por uma variável categórica, criando boxplots separados para cada grupo.
*   **`legend=False`**: Remove a legenda, pois o `hue` está usando a mesma variável do eixo x.

### 4. Gráficos Interativos com Plotly Express

Plotly Express (`px`) é uma interface de alto nível para o Plotly, ideal para criar rapidamente gráficos interativos.

#### Gráfico de Pizza (`px.pie()`)
Usado para mostrar a proporção de cada categoria em relação ao todo.

```python
import plotly.express as px
# Prepara os dados para o gráfico de pizza (contagem de tipos de trabalho)
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
                names='tipo_trabalho',
                values='quantidade',
                title='Proporção dos Tipos de Trabalho',
                hole=0.5 # Cria um gráfico de rosca (donut chart)
)

# Personaliza a exibição de texto dentro das fatias
fig.update_traces(textposition='inside', textinfo='percent+label')

# Opções de visualização/salvamento do gráfico Plotly:
# 1. Exibir em uma janela do navegador (requer ambiente gráfico e navegador configurado)
# fig.show()

# 2. Salvar como arquivo HTML (mantém a interatividade, pode ser aberto em qualquer navegador)
fig.write_html("grafico_proporcao_trabalho.html")

# 3. Salvar como imagem estática (requer a instalação da biblioteca 'kaleido': pip install kaleido)
# fig.write_image("grafico_proporcao_trabalho.png")
```
*   **`names`**: Coluna para os rótulos das fatias.
*   **`values`**: Coluna para os tamanhos das fatias.
*   **`hole`**: Cria um gráfico de rosca (donut chart) se o valor for > 0 e < 1.
*   **`fig.update_traces(textposition='inside', textinfo='percent+label')`**: Configura o texto exibido dentro das fatias (percentual e rótulo).
*   **`fig.show()`**: Tenta abrir o gráfico em uma nova aba do navegador. Pode não funcionar em ambientes CLI sem um navegador configurado.
*   **`fig.write_html("nome_do_arquivo.html")`**: Salva o gráfico interativo como um arquivo HTML.
*   **`fig.write_image("nome_do_arquivo.png")`**: Salva o gráfico como uma imagem estática (PNG, JPEG, SVG, etc.). Requer a instalação da biblioteca `kaleido` (`pip install kaleido`).

#### Gráfico de Barras (`px.bar()`)
Versão interativa do gráfico de barras, permitindo zoom, pan e tooltips.

```python
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
```
*   **`color`**: Mapeia uma coluna para a cor das barras.
*   **`template`**: Define um tema visual para o gráfico (ex: 'plotly_white', 'plotly_dark').
