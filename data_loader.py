import pandas as pd

class DataLoader:
    """
    Classe responsável por carregar e verificar dados a partir de um arquivo CSV.
    
    Atributos:
        arquivo (str): Caminho do arquivo CSV a ser carregado.
        df (pandas.DataFrame): DataFrame contendo os dados carregados.
    """

    def __init__(self, arquivo):
        """
        Inicializa o DataLoader com o caminho do arquivo.

        Args:
            arquivo (str): Caminho do arquivo CSV.
        """
        self.arquivo = arquivo
        self.df = None

    def carregar_dados(self):
        """
        Carrega os dados do arquivo CSV para um DataFrame.

        Exibe uma mensagem com o número total de registros carregados ou erro em caso de falha.
        """
        try:
            self.df = pd.read_csv(self.arquivo)
            print(f"Arquivo '{self.arquivo}' carregado! Total de registros: {len(self.df)}")
        except (FileNotFoundError, pd.errors.ParserError) as e:
            print(f"Erro ao carregar o arquivo: {e}")

    def verificar_dados(self):
        """
        Verifica se os dados foram carregados corretamente e se as colunas essenciais estão presentes.

        Returns:
            bool: True se todas as colunas essenciais estiverem presentes e os dados forem válidos, False caso contrário.
        """
        if self.df is None or self.df.empty:
            print("Erro: Dados inválidos ou arquivo vazio.")
            return False

        print(f"Linhas: {self.df.shape[0]}, Colunas: {self.df.shape[1]}")

        # Verificação de colunas essenciais
        colunas_essenciais = ['coluna1', 'coluna2', 'coluna3']
        colunas_faltantes = [col for col in colunas_essenciais if col not in self.df.columns]

        if colunas_faltantes:
            print(f"Erro: As seguintes colunas estão ausentes: {colunas_faltantes}")
            return False

        print("Validação concluída: Todas as colunas essenciais estão presentes.")
        return True

    def exibir_dados(self):
        """
        Exibe as primeiras linhas do DataFrame carregado.
        """
        if self.df is not None:
            print(self.df.head())

# Exemplo de uso
if __name__ == "__main__":
    arquivo = "dados.csv"

    loader = DataLoader(arquivo)
    loader.carregar_dados()
    if loader.verificar_dados():
        loader.exibir_dados()
