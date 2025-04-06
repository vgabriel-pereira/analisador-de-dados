import os
import pandas as pd
from data_loader import DataLoader
from data_processor import DataProcessor
from visualizer import DataVisualizer
from logger import UserLogger
from menu import iniciar_menu


def solicitar_nome_usuario():
    """
    Solicita o nome do usuário com validação.

    Returns:
        str: Nome do usuário válido.
    """
    while True:
        nome = input("Digite seu nome: ").strip()
        if nome.replace(" ", "").isalpha() and len(nome) >= 3:
            return nome
        print("Nome inválido. Digite novamente (apenas letras, mínimo 3 caracteres).")


def solicitar_arquivo_csv():
    """
    Solicita ao usuário o caminho para o arquivo CSV e valida sua existência.

    Returns:
        str: Caminho válido para o arquivo CSV.
    """
    while True:
        caminho = input("Digite o caminho do arquivo CSV: ").strip()
        if os.path.isfile(caminho):
            return caminho
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")


def main():
    """
    Função principal que inicia o sistema de análise de dados.
    """
    usuario = solicitar_nome_usuario()
    arquivo = solicitar_arquivo_csv()

    # Carregamento dos dados
    loader = DataLoader(arquivo)
    loader.carregar_dados()

    if loader.df is not None:
        processor = DataProcessor(loader.df)
        visualizer = DataVisualizer(processor.df)
        log_manager = UserLogger(usuario)
        log_manager.registrar_acao("Iniciou o sistema")

        iniciar_menu(processor, visualizer, log_manager, usuario)
    else:
        print("Erro: Não foi possível carregar os dados. O sistema será encerrado.")


if __name__ == "__main__":
    main()
