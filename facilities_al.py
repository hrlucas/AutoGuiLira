import pyautogui
import pygetwindow as gw
import time

def main():
    # Título da janela que você deseja ativar
    titulo_janela = "Angel.Lira - Módulo Logística"
    
    # Obtém todas as janelas abertas com o título especificado
    janelas = gw.getWindowsWithTitle(titulo_janela)
    
    if janelas:
        # Ativa a primeira janela que corresponde ao título
        janela = janelas[0]
        janela.activate()  # Ativa a janela
        time.sleep(2)  # Aguarda um tempo para garantir que a janela foi ativada corretamente
    else:
        print("Janela não encontrada!")
        return

    pyautogui.click(x=385, y=35)  # Clique no item "RELATÓRIOS DIVERSOS" ou similar
    time.sleep(2)  # Espera 2 segundos antes de continuar

    pyautogui.click(x=1850, y=90)  # Clique no item "CONSULTAR"
    time.sleep(2)

    pyautogui.click(x=1045, y=505)  # Clique para inserir o código de parâmetro
    pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
    pyautogui.press('backspace')  # Apaga o texto selecionado
    time.sleep(1)
    pyautogui.write("3264")  # Insere o código do parâmetro
    time.sleep(1) 

    pyautogui.click(x=1050, y=550)  # Clique para aplicar o código do parâmetro
    time.sleep(70)  # Aguarda um tempo para garantir que a aplicação foi feita

    # Clique para exportar o arquivo
    pyautogui.click(x=1800, y=990)  # Clique no botão "EXPORTAR"
    time.sleep(2)

    # Escolhe o formato do arquivo (XLSX)
    pyautogui.click(x=1800, y=930)  # Clique na opção "XLSX"
    time.sleep(2)

    # Seleciona o caminho para salvar o arquivo
    pyautogui.click(x=1150, y=335)  # Clique na barra de seleção de caminho
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto no campo de caminho
    pyautogui.press('backspace')  # Apaga o texto selecionado
    time.sleep(1)

    # Cola o novo caminho para salvar o arquivo
    pyautogui.write(r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\alira")  # Caminho especificado
    pyautogui.press('enter')
    time.sleep(2)

    # Clique – (780, 720)
    pyautogui.click(x=780, y=720)  # DEFINIÇÃO DO NOME DO ARQUIVO
    time.sleep(2)
    pyautogui.write("facilities_al")
    pyautogui.press('enter')
    time.sleep(2)

    time.sleep(30)  # Aguarda o processo de salvamento

    # Finaliza o processo de exportação sem abrir o arquivo
    pyautogui.click(x=1090, y=600)  # Clique para não abrir o arquivo após o salvamento
    time.sleep(2)

    print("Execução de facilities concluída.")

# Executa o script ao ser chamado
if __name__ == "__main__":
    main()
