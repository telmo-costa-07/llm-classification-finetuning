# LLM Classification Finetuning

- Kaggle: https://www.kaggle.com/competitions/llm-classification-finetuning
- Objetivo: prever qual de duas respostas de modelos é preferida por uma pessoa, ou se existe empate.
- Tipo: classificação multiclasse com três resultados.
- Métrica: log loss multiclasse; um valor menor é melhor.

## Dados

O treino inclui:

- `id`: identificador da observação;
- `model_a` e `model_b`: modelos que produziram as respostas;
- `prompt`: pedido apresentado aos modelos;
- `response_a` e `response_b`: respostas a comparar;
- `winner_model_a`, `winner_model_b` e `winner_tie`: resultado em formato one-hot.

O teste contém `id`, `prompt`, `response_a` e `response_b`. A submissão deve conter o `id` e uma probabilidade para cada um dos três resultados. As três probabilidades de cada linha devem somar aproximadamente 1.

## Primeiro objetivo

Construir um baseline local reproduzível:

1. validar os ficheiros e as colunas;
2. analisar valores ausentes, duplicados, distribuição dos resultados e comprimentos dos textos;
3. criar uma validação estratificada;
4. treinar TF-IDF com regressão logística;
5. medir log loss;
6. gerar uma primeira submissão válida.

Modelos Transformer e fine-tuning ficam para uma fase posterior, depois de o pipeline completo estar validado.

