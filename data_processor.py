import pandas as pd

class DataProcessor:
    """
    Classe responsável por processar e realizar análises estatísticas nos dados.

    Atributos:
        df (pandas.DataFrame): Conjunto de dados a ser processado.
    """

    def __init__(self, df):
        """
        Inicializa o processador de dados com uma cópia do DataFrame.

        Args:
            df (pandas.DataFrame): DataFrame original com os dados carregados.
        """
        self.df = df.copy()

    def resumo_estatistico(self):
        """
        Exibe um resumo estatístico dos dados:
        - Total de registros
        - Contagem por gênero (caso exista a coluna 'Gender')
        - Registros com valores ausentes em 'Parent_Education_Level'
        """
        try:
            total_registros = len(self.df)
            print(f"Total de registros: {total_registros}")

            if 'Gender' in self.df.columns:
                genero_contagem = self.df['Gender'].value_counts()
                print("\nQuantidade por gênero:")
                print(genero_contagem.to_string())
            else:
                print("A coluna 'Gender' não foi encontrada no dataset.")

            if 'Parent_Education_Level' in self.df.columns:
                faltando_educacao_pais = self.df['Parent_Education_Level'].isna().sum()
                print(f"\nRegistros sem dados sobre a educação dos pais: {faltando_educacao_pais}")
            else:
                print("A coluna 'Parent_Education_Level' não foi encontrada no dataset.")

        except Exception as e:
            print(f"Erro ao gerar resumo estatístico: {e}")

    def limpar_dados(self):
        """
        Realiza a limpeza dos dados:

        - Remove registros com valores nulos na coluna 'Parent_Education_Level'
        - Preenche valores nulos de 'Attendance (%)' com a mediana
        - Exibe a soma total da coluna 'Attendance (%)' após a limpeza
        """
        try:
            if 'Parent_Education_Level' in self.df.columns:
                antes = len(self.df)
                self.df = self.df.dropna(subset=['Parent_Education_Level'])
                depois = len(self.df)
                print(f"Registros removidos (Parent_Education_Level nulo): {antes - depois}")
            else:
                print("Coluna 'Parent_Education_Level' não encontrada.")

            if 'Attendance (%)' in self.df.columns:
                mediana = self.df['Attendance (%)'].median()
                self.df.loc[:, 'Attendance (%)'] = self.df['Attendance (%)'].fillna(mediana)
                print(f"Mediana usada para preencher valores nulos em 'Attendance (%)': {mediana}")
                soma = self.df['Attendance (%)'].sum()
                print(f"Soma total de 'Attendance (%)' após limpeza: {soma}")
            else:
                print("Coluna 'Attendance (%)' não encontrada.")

        except Exception as e:
            print(f"Erro ao limpar os dados: {e}")

    def consultar_coluna(self, coluna):
        """
        Exibe estatísticas básicas para uma coluna numérica especificada.

        Args:
            coluna (str): Nome da coluna a ser analisada.

        Exibe:
            - Média
            - Mediana
            - Moda
            - Desvio padrão

        Valida se a coluna existe e se é numérica.
        """
        try:
            if coluna not in self.df.columns:
                print(f"Erro: A coluna '{coluna}' não existe no conjunto de dados.")
                return

            if not pd.api.types.is_numeric_dtype(self.df[coluna]):
                print(f"Erro: A coluna '{coluna}' não é numérica.")
                return

            media = self.df[coluna].mean()
            mediana = self.df[coluna].median()
            moda = self.df[coluna].mode()
            desvio = self.df[coluna].std()

            print(f"\nEstatísticas para a coluna '{coluna}':")
            print(f"  Média: {media:.2f}")
            print(f"  Mediana: {mediana:.2f}")
            print(f"  Moda: {moda.tolist()}")
            print(f"  Desvio padrão: {desvio:.2f}")

        except Exception as e:
            print(f"Erro ao consultar a coluna '{coluna}': {e}")
