# Makefile para o projeto de análise de evasão com Stan

# Definição dos arquivos necessários
ARQUIVOENTRADA = curso-55N-2024.csv
COMPILACAO_TXT = compilacao.txt
ARQUIVOSAIDA = arquivosaida.txt
PYTHON_SCRIPT = script.py
STAN_MODEL = model.stan
OUTPUT_REPORT = relatorio_correlacao.txt
OUTPUT_IMAGE = output.png
CORRELATION_MATRIX = correlation_matrix.csv

# Regra principal: compila e executa o código
all: compila executa

# Compilação: verifica se os arquivos necessários estão presentes
compila:
	@echo "Verificando arquivos necessários..."
	@test -f $(ARQUIVOENTRADA) || (echo "Erro: O arquivo de entrada '$(ARQUIVOENTRADA)' não foi encontrado." && exit 1)
	@test -f $(STAN_MODEL) || (echo "Erro: O arquivo do modelo Stan '$(STAN_MODEL)' não foi encontrado." && exit 1)
	@test -f $(PYTHON_SCRIPT) || (echo "Erro: O script Python '$(PYTHON_SCRIPT)' não foi encontrado." && exit 1)
	@touch $(COMPILACAO_TXT)
	@echo "Compilação concluída com sucesso."

# Execução: executa o script Python e gera o relatório
executa:
	@echo "Executando o script Python..."
	python3 $(PYTHON_SCRIPT) > $(ARQUIVOSAIDA) 2>&1
	@test -f $(OUTPUT_REPORT) || (echo "Erro: O relatório '$(OUTPUT_REPORT)' não foi gerado." && exit 1)
	@test -f $(CORRELATION_MATRIX) || (echo "Erro: A matriz de correlação '$(CORRELATION_MATRIX)' não foi gerada." && exit 1)
	@echo "Execução concluída. Verifique o relatório em '$(OUTPUT_REPORT)' e a matriz de correlação em '$(CORRELATION_MATRIX)'."

# Limpeza: remove arquivos temporários e de saída
clean:
	rm -f $(COMPILACAO_TXT) $(ARQUIVOSAIDA) $(OUTPUT_REPORT) $(CORRELATION_MATRIX) $(OUTPUT_IMAGE)
	@echo "Arquivos temporários removidos."

.PHONY: all compila executa clean