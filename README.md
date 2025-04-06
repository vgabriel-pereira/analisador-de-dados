📊 Analisador de Dados de Desempenho Escolar
Este projeto foi desenvolvido como parte da disciplina de Aprendizagem de Máquinas, com o objetivo de carregar, processar e visualizar dados de alunos utilizando Python e as bibliotecas Pandas e Matplotlib.

🚀 Funcionalidades
📂 Carregamento de Dados
Permite ao usuário importar um arquivo CSV ou JSON contendo informações de desempenho estudantil.

📈 Resumo Estatístico
Exibe dados gerais sobre o conjunto, como:

Quantidade total de registros;

Número de alunos por sexo;

Quantidade de registros com dados ausentes sobre o nível de educação dos pais.

🧹 Limpeza de Dados
Remove registros com valores ausentes na coluna Parent_Education_Level;

Preenche valores nulos na coluna Attendance (%) com a mediana;

Exibe o somatório total da coluna Attendance (%) após a limpeza.

🔍 Consultas Estatísticas
Permite ao usuário consultar estatísticas específicas de qualquer coluna numérica:

Média

Mediana

Moda

Desvio padrão

📊 Visualizações Gráficas
Geração de gráficos para facilitar a análise visual dos dados:

Gráfico de Dispersão: Correlação entre horas de sono por noite e nota final;

Gráfico de Barras: Média da nota intermediária (Midterm Score) por faixa etária;

Gráfico de Pizza: Distribuição de alunos por faixa etária.