import time
from visualizer import DataVisualizer
from logger import UserLogger


def exibir_menu():
    """Exibe o menu principal com as opções disponíveis ao usuário."""
    print("\n--- MENU PRINCIPAL ---")
    print("1. Exibir resumo estatístico")
    print("2. Limpar dados")
    print("3. Consultar estatísticas de uma coluna")
    print("4. Gráfico de dispersão (Sono x Nota Final)")
    print("5. Gráfico de barras (Idade x Nota Intermediária)")
    print("6. Gráfico de pizza (Faixas Etárias)")
    print("7. Visualizar logs")
    print("0. Sair")
    print("------------------------")


def iniciar_menu(processor, visualizer, log_manager, usuario):
    """
    Inicia o menu interativo do sistema.

    Args:
        processor (DataProcessor): Instância da classe que manipula os dados.
        visualizer (DataVisualizer): Instância da classe de visualização.
        log_manager (UserLogger): Instância do logger de ações.
        usuario (str): Nome do usuário atual.

    Returns:
        None
    """
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
        log_manager.registrar_acao(f"Escolheu opção {escolha}")
        time.sleep(0.5)

        if escolha == "1":
            processor.resumo_estatistico()
        elif escolha == "2":
            processor.limpar_dados()
        elif escolha == "3":
            coluna = input("Digite o nome da coluna: ").strip()
            log_manager.registrar_acao(f"Consultou coluna {coluna}")
            processor.consultar_coluna(coluna)
        elif escolha == "4":
            visualizer.grafico_dispersao()
        elif escolha == "5":
            visualizer.grafico_barras_idade_midterm()
        elif escolha == "6":
            visualizer.grafico_pizza_faixa_etaria()
        elif escolha == "7":
            log_manager.visualizar_logs()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
