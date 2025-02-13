data {
    int<lower=0> N; // Número de amostras
    matrix[N, 5] X; // Variáveis independentes
    vector[N] y;    // Variável dependente (NUM_PERIODO_ALUNO)
}
parameters {
    vector[5] beta; // Coeficientes
    real<lower=0> sigma; // Desvio padrão
}
model {
    y ~ normal(X * beta, sigma); // Modelo linear
}