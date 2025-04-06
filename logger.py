import csv
from datetime import datetime
import pandas as pd


class UserLogger:
    """Classe responsável por registrar as ações do usuário em um arquivo CSV de log."""

    def __init__(self, nome_usuario, caminho_arquivo="logs.csv"):
        """
        Inicializa o logger com o nome do usuário e o caminho para o arquivo de log.

        Args:
            nome_usuario (str): Nome do usuário.
            caminho_arquivo (str): Caminho para o arquivo CSV onde os logs serão salvos.
        """
        self.nome_usuario = nome_usuario
        self.caminho_arquivo = caminho_arquivo

        # Criar o cabeçalho do arquivo se ele não existir
        try:
            with open(self.caminho_arquivo, mode='x', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Data/Hora", "Usuário", "Ação"])
        except FileExistsError:
            pass  # Arquivo já existe

    def registrar_acao(self, acao):
        """
        Registra uma ação do usuário no arquivo de log com timestamp.

        Args:
            acao (str): Descrição da ação realizada.
        """
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.caminho_arquivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([data_hora, self.nome_usuario, acao])

    def visualizar_logs(self):
        """
        Exibe o conteúdo do arquivo de log em formato tabular.
        """
        try:
            df = pd.read_csv(self.caminho_arquivo)
            print("\n=== LOG DE AÇÕES ===")
            print(df.to_string(index=False))
        except FileNotFoundError:
            print("Arquivo de log não encontrado.")
