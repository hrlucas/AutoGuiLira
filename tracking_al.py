import pyautogui
import pygetwindow as gw
import time
from datetime import datetime  # Para obter o ano e o mês atuais

# Configurações do PyAutoGUI
pyautogui.FAILSAFE = True

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

    # M. de Rastreamento

    # Clique 1 – (100, 35) - ABRE M. DE RASTREAMENTO
    pyautogui.click(x=100, y=35)
    time.sleep(2)

    # Pressiona F5 - ATUALIZA A TELA
    pyautogui.press('f5')
    time.sleep(55)

    # Clique 2 – (1655, 999) - EXPORTAR
    pyautogui.click(x=1655, y=999)
    time.sleep(2)

    # Clique 2.1 – (1150, 335) - BARRA DE SELEÇÃO DE CAMINHO
    pyautogui.click(x=1150, y=335)
    time.sleep(2)

    # Apaga o conteúdo do campo
    pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
    pyautogui.press('backspace')  # Apaga o texto selecionado
    time.sleep(1)

    # Cola o caminho especificado
    pyautogui.write(r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\alira")  # Usando string bruta
    pyautogui.press('enter')
    time.sleep(2)

    # Clique – (780, 720)
    pyautogui.click(x=780, y=720)  # DEFINIÇÃO DO NOME DO ARQUIVO
    time.sleep(2)
    pyautogui.write("tracking_al")  # Nome do arquivo
    pyautogui.press('enter')
    time.sleep(2)

    time.sleep(15)  # Aguarda o processo de salvamento

    # Clique 5 – (1090, 600) - NÃO ABRE O ARQUIVO
    pyautogui.click(x=1090, y=600)
    time.sleep(10)  # Aguarda mais um pouco para garantir que o processo termine

    print("Execução de tracking concluída.")

# Executa o script ao ser chamado
if __name__ == "__main__":
    main()
