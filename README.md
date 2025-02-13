# Análise de Evasão Acadêmica com Modelagem Bayesiana

## Sobre o Projeto
Este projeto tem como objetivo analisar os fatores relacionados à evasão acadêmica em um curso universitário, utilizando técnicas estatísticas e modelagem bayesiana. O conjunto de dados utilizado (`curso-55N-2024.csv`) contém informações sobre estudantes, incluindo variáveis como ano de ingresso, sexo, etnia, tipo de cota, período cursado e forma de evasão (formatura, desistência, desligamento, etc.).

O trabalho explora a relação entre essas variáveis por meio da matriz de correlação e ajusta um modelo bayesiano usando o framework `CmdStanPy` para identificar padrões que possam explicar ou prever a evasão.

## Estrutura do Projeto
Aqui estão os principais arquivos e sua descrição:

- **Makefile** : Automatiza as etapas de compilação e execução do projeto.
- **script.py** : Script Python responsável por carregar os dados, realizar a análise exploratória (matriz de correlação).
- **model.stan** : Modelo Stan utilizado para a análise bayesiana.
- **curso-55N-2024.csv** : Conjunto de dados original com informações dos alunos.

### Saídas Geradas :
- `correlation_matrix.csv`: Matriz de correlação entre as variáveis.
- `relatorio_correlacao.txt`: Relatório detalhado com interpretações das correlações encontradas.
- Arquivos temporários gerados durante a execução (removidos ao usar o comando `make clean`).

## Como Executar o Projeto

### Pré-requisitos
Certifique-se de que os seguintes softwares estão instalados no seu sistema:

- Python 3.x
- Bibliotecas Python necessárias:
  - `pandas`
  - `numpy`
  - `cmdstanpy`
- CmdStan (para executar modelos Stan)
- GNU Make (para usar o Makefile)

Instale as dependências Python com o seguinte comando:

```bash
pip install pandas numpy cmdstanpy
```

### Passos para Executar

1. **Baixe o repositório** :
   Certifique-se de que todos os arquivos necessários (`curso-55N-2024.csv`, `script.py`, `model.stan`, `Makefile`) estão no mesmo diretório.

2. **Execute o Makefile** :
   Use os seguintes comandos no terminal para executar o projeto:

   ```bash
   make        # Executa todas as etapas (compilação e execução)
   make clean  # Remove arquivos temporários e de saída
   ```

3. **Verifique as Saídas** :
   Após a execução, os seguintes arquivos serão gerados:
   - `correlation_matrix.csv`: Contém a matriz de correlação calculada.
   - `relatorio_correlacao.txt`: Relatório interpretativo com insights sobre as correlações encontradas.

## Resultados Esperados

### Matriz de Correlação
A matriz de correlação revela a relação linear entre as variáveis do conjunto de dados. Por exemplo:

- Variáveis como `ANO_INGRESSO` e `NUM_PERIODO_ALUNO` apresentam uma correlação negativa moderada, indicando que alunos que ingressaram mais recentemente tendem a ter menos períodos cursados.
- Outras variáveis, como `SEXO` e `ETNIA`, têm correlações próximas de zero, sugerindo pouca influência direta no número de períodos cursados.

### Relatório de Análise
O arquivo `relatorio_correlacao.txt` fornece uma interpretação detalhada dos resultados, destacando:

- As principais correlações encontradas.
- Insights sobre os fatores que mais impactam a evasão acadêmica.
- Conclusões gerais que podem orientar políticas de retenção e suporte aos alunos.

## Exemplo de Comandos

### Executar o Projeto
```bash
make
```

### Limpar Arquivos Temporários
```bash
make clean
```
