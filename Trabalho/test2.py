import pandas as pd
import os

class DataLoader:
    """Classe para carregar e verificar dados de um arquivo CSV."""

    def __init__(self, file_path, required_columns=None):
        self.file_path = file_path
        self.required_columns = required_columns
        self.data = None

    def load_data(self):
        """Carrega o arquivo CSV e trata erros."""
        if not os.path.exists(self.file_path):
            return print("Erro: Arquivo não encontrado!")

        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Dados carregados com sucesso! Total de registros: {len(self.data)}")
        except (pd.errors.EmptyDataError, pd.errors.ParserError):
            print("Erro: Arquivo vazio ou corrompido!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def check_missing_values(self):
        """Verifica e exibe os valores ausentes no dataset."""
        if self.data is None:
            return print("Nenhum dado carregado!")

        missing_values = self.data.isnull().sum()
        missing_columns = missing_values[missing_values > 0]  # Filtra apenas as colunas com valores ausentes

        if not missing_columns.empty:
            print("Existem valores ausentes nos dados!")
            print(missing_columns.to_string())  # Exibe a quantidade de valores nulos por coluna
        else:
            print("Não há valores ausentes!")

    def validate_columns(self):
        """Verifica se as colunas obrigatórias estão presentes."""
        if self.data is None:
            return print("Nenhum dado carregado!")

        if self.required_columns:
            missing = [col for col in self.required_columns if col not in self.data.columns]
            if missing:
                return print(f"Erro: Colunas ausentes: {missing}")

        print("Todas as colunas obrigatórias estão presentes!")

    def preview(self, rows=5):
        """Exibe uma prévia dos dados."""
        if self.data is not None:
            print(self.data.head(rows))

# Testando o módulo
if __name__ == "__main__":
    loader = DataLoader("dados.csv", ["Nome", "Idade", "Email"])
    loader.load_data()
    loader.validate_columns()
    loader.check_missing_values()
   
    
