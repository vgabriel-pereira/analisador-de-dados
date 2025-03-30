import pandas as pd

class DataLoader:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.df = None
    
    def carregar_dados(self):
        """Carrega o arquivo CSV e armazena em um DataFrame."""
        try:
            self.df = pd.read_csv(self.arquivo)
            print(f"Arquivo '{self.arquivo}' carregado! Total de registros: {len(self.df)}")
        except (FileNotFoundError, pd.errors.ParserError) as e:
            print(f"Erro ao carregar o arquivo: {e}")
    
    def verificar_dados(self):
        """Verifica se as colunas essenciais estão presentes nos dados."""
        if self.df is None or self.df.empty:
            print("Erro: Dados inválidos ou arquivo vazio.")
            return False
        print(f"Linhas: {self.df.shape[0]}, Colunas: {self.df.shape[1]}")
        
        # Verificação de colunas automáticas - exemplo de verificação sem colunas pré-definidas
        colunas_essenciais = ['coluna1', 'coluna2', 'coluna3']  # Colunas que queremos verificar diretamente
        colunas_faltantes = [col for col in colunas_essenciais if col not in self.df.columns]
        
        if colunas_faltantes:
            print(f"Erro: As seguintes colunas estão ausentes: {colunas_faltantes}")
            return False
        
        print("Validação concluída: Todas as colunas essenciais estão presentes.")
        return True

    def exibir_dados(self):
        """Exibe as primeiras linhas dos dados carregados."""
        if self.df is not None:
            print(self.df.head())

# Exemplo de uso
if __name__ == "__main__":
    arquivo = "dados.csv"
    
    loader = DataLoader(arquivo)
    loader.carregar_dados()
    if loader.verificar_dados():
        loader.exibir_dados()
