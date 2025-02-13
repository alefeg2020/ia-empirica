import pandas as pd
import numpy as np
from cmdstanpy import CmdStanModel

# Carregar o dataset
file_path = "curso-55N-2024.csv"
data = pd.read_csv(file_path)

data.columns = data.columns.str.strip()

# Selecionar colunas relevantes
data = data[[
    'NUM_PERIODO_ALUNO', 
    'ANO_INGRESSO', 
    'ANO_EVASAO', 
    'SEXO', 
    'ETNIA', 
    'TIPO_COTA'
]]

# Codificar variáveis categóricas
data['SEXO'] = data['SEXO'].map({' M': 0, ' F': 1})
data['ETNIA'] = data['ETNIA'].astype('category').cat.codes
data['TIPO_COTA'] = data['TIPO_COTA'].astype('category').cat.codes

# Calcular matriz de correlação
correlation_matrix = data.corr()

# Exibir matriz de correlação
print("Matriz de Correlação:")
print(correlation_matrix)

# Salvar matriz de correlação para análise posterior
correlation_matrix.to_csv("correlation_matrix.csv")

# Modelo Bayesiano usando CmdStanPy
# Definir modelo Stan


# Preparar dados para o modelo
X = data[['ANO_INGRESSO', 'ANO_EVASAO', 'SEXO', 'ETNIA', 'TIPO_COTA']].values
y = data['NUM_PERIODO_ALUNO'].values

stan_data = {
    "N": len(y),
    "X": X,
    "y": y
}

# Compilar e ajustar o modelo
model = CmdStanModel(stan_file="model.stan")
fit = model.sample(data=stan_data, chains=4, iter_sampling=1000, iter_warmup=1000)

# Resumo do modelo
summary = fit.summary()
print(summary)

# Matriz de correlação (já fornecida)
correlation_matrix = pd.DataFrame(correlation_matrix)
correlation_stan = pd.DataFrame(summary)

# Gerar relatório
report = """
Relatório de Análise de Correlação
==================================

A matriz de correlação abaixo apresenta as relações entre as variáveis do dataset fornecido. Os valores variam entre -1 e 1, onde:
- Valores próximos de 1 indicam uma forte correlação positiva.
- Valores próximos de -1 indicam uma forte correlação negativa.
- Valores próximos de 0 indicam pouca ou nenhuma correlação.

Matriz de Correlação:
----------------------
{}

Usando stan:

{}

Interpretação dos Resultados:
-----------------------------

1. **NUM_PERIODO_ALUNO**:
   - Apresenta uma correlação negativa moderada com **ANO_INGRESSO** (-0.725), sugerindo que alunos que ingressaram mais recentemente tendem a ter menos períodos cursados.
   - A correlação com **ANO_EVASAO** é muito baixa (0.059), indicando pouca relação direta entre o ano de evasão e o número de períodos cursados.
   - As variáveis **SEXO**, **ETNIA** e **TIPO_COTA** têm correlações próximas de zero, sugerindo que esses fatores não influenciam significativamente o número de períodos cursados.

2. **ANO_INGRESSO**:
   - Apresenta uma correlação positiva moderada com **ANO_EVASAO** (0.591), indicando que alunos que ingressaram mais cedo também tendem a evadir mais cedo.
   - A correlação negativa com **NUM_PERIODO_ALUNO** (-0.725) reforça a ideia de que alunos mais novos no curso têm menos períodos cursados.

3. **ANO_EVASAO**:
   - Não apresenta correlações significativas com outras variáveis além de **ANO_INGRESSO**.

4. **SEXO**:
   - Não há correlações significativas com outras variáveis, sugerindo que o gênero não tem impacto direto nas demais características.

5. **ETNIA**:
   - Apresenta uma correlação positiva moderada com **TIPO_COTA** (0.310), indicando que a etnia pode estar relacionada ao tipo de cota utilizada pelos alunos.

6. **TIPO_COTA**:
   - Além da correlação com **ETNIA**, não há outras correlações significativas, sugerindo que o tipo de cota não influencia diretamente o desempenho acadêmico.

Conclusão:
----------
Os resultados indicam que o **ANO_INGRESSO** é o principal fator relacionado ao número de períodos cursados (**NUM_PERIODO_ALUNO**). Outros fatores, como **SEXO**, **ETNIA** e **TIPO_COTA**, não apresentam correlações significativas com o desempenho acadêmico. Essas informações podem ser úteis para planejar políticas de retenção e suporte aos alunos.
""".format(correlation_matrix.round(4).to_string(), correlation_stan.round(4).to_string())

# Exportar relatório para um arquivo .txt
with open("relatorio_correlacao.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Relatório gerado com sucesso e salvo em 'relatorio_correlacao.txt'.")