import matplotlib.pyplot as plt
import pandas as pd


def faixa_etaria(idade):
    """
    Classifica a idade em uma faixa etária específica.

    Args:
        idade (int): Idade da pessoa.

    Returns:
        str: Faixa etária correspondente.
    """
    if idade <= 17:
        return "Até 17"
    elif 18 <= idade <= 21:
        return "18 a 21"
    elif 22 <= idade <= 24:
        return "22 a 24"
    else:
        return "25 ou mais"


class DataVisualizer:
    """
    Classe responsável pela geração de gráficos com base nos dados fornecidos.
    """

    def __init__(self, df):
        """
        Inicializa o visualizador com um DataFrame.

        Args:
            df (pd.DataFrame): DataFrame contendo os dados a serem visualizados.
        """
        self.df = df

    def grafico_dispersao(self):
        """
        Exibe um gráfico de dispersão entre 'Sleep_Hours_per_Night' e 'Final_Score'.
        """
        try:
            x = self.df['Sleep_Hours_per_Night']
            y = self.df['Final_Score']

            plt.figure(figsize=(8, 6))
            plt.scatter(x, y, alpha=0.7, color='teal')
            plt.title("Horas de Sono x Nota Final")
            plt.xlabel("Horas de Sono por Noite")
            plt.ylabel("Nota Final")
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"Erro ao gerar gráfico de dispersão: {e}")

    def grafico_barras_idade_midterm(self):
        """
        Exibe um gráfico de barras com a média da nota intermediária (Midterm_Score) por idade.
        """
        try:
            agrupado = self.df.groupby('Age')['Midterm_Score'].mean()

            plt.figure(figsize=(10, 6))
            agrupado.plot(kind='bar', color='skyblue', edgecolor='black')
            plt.title("Idade x Média da Nota Intermediária")
            plt.xlabel("Idade")
            plt.ylabel("Média Midterm Score")
            plt.xticks(rotation=0)
            plt.grid(axis='y')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Erro ao gerar gráfico de barras: {e}")

    def grafico_pizza_faixa_etaria(self):
        """
        Exibe um gráfico de pizza com a distribuição dos estudantes por faixa etária.
        """
        try:
            self.df['Faixa_Etaria'] = self.df['Age'].apply(faixa_etaria)
            contagem = self.df['Faixa_Etaria'].value_counts()

            plt.figure(figsize=(7, 7))
            plt.pie(
                contagem,
                labels=contagem.index,
                autopct='%1.1f%%',
                startangle=140,
                colors=plt.cm.Pastel1.colors
            )
            plt.title("Distribuição de Faixas Etárias")
            plt.axis('equal')  # Deixa o gráfico circular
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Erro ao gerar gráfico de pizza: {e}")
