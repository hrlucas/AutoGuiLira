import pyautogui
import pygetwindow as gw
import time
from datetime import datetime

# Configurações do PyAutoGUI
pyautogui.FAILSAFE = True

def main():
    # Alira
    titulo_janela = "Angel.Lira - Módulo Logística"

    # Obtém todas as janelas com o título especificado
    janelas = gw.getWindowsWithTitle(titulo_janela)

    if janelas:
        janela = janelas[0]
        janela.activate()
        time.sleep(2)
    else:
        print("Janela não encontrada!")
        return

    # Auto cliques – Relatórios viagens

    # Clique 1 – Acessa menu RELATÓRIOS VIAGENS
    pyautogui.click(x=260, y=35)
    time.sleep(2)

    data_atual = datetime.now()


     # Clique 1.2 – Define o primeiro dia do MÊS ATUAL
    pyautogui.click(x=285, y=220)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(2)

    data_1_2 = data_atual.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    data_1_2_formatada = data_1_2.strftime("01/%m/%Y 00:00:00")
    pyautogui.write(data_1_2_formatada)
    time.sleep(2)

    # Clique 1.1 – Define o primeiro dia do PRÓXIMO MÊS
    pyautogui.click(x=440, y=220)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(2)

    if data_atual.month == 12:
        mes_seguinte = 1
        ano_seguinte = data_atual.year + 1
    else:
        mes_seguinte = data_atual.month + 1
        ano_seguinte = data_atual.year

    data_1_1 = datetime(year=ano_seguinte, month=mes_seguinte, day=1, hour=0, minute=0, second=0)
    data_1_1_formatada = data_1_1.strftime("01/%m/%Y 00:00:00")
    pyautogui.write(data_1_1_formatada)
    pyautogui.press('enter')
    time.sleep(2)

   

    # Atualiza com F5
    pyautogui.press('f5')
    time.sleep(70)

    # Clique 2 – EXPORTAR
    pyautogui.click(x=1655, y=999)
    time.sleep(2)

    # Clique 3 – BARRA DE CAMINHO
    pyautogui.click(x=1150, y=335)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(1)

    pyautogui.write(r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\alira\hist")
    pyautogui.press('enter')
    time.sleep(2)

    # Clique 4 – NOME DO ARQUIVO
    pyautogui.click(x=780, y=720)
    time.sleep(2)

    ano_mes = datetime.now().strftime("%Y.%m_HV")
    pyautogui.write(ano_mes)
    pyautogui.press('enter')
    time.sleep(2)

    # Clique 5 – NÃO ABRE O ARQUIVO
    pyautogui.click(x=1090, y=600)
    time.sleep(10)

    print("Execução de hist concluída.")

# Executa o script apenas se for chamado diretamente
if __name__ == "__main__":
    main()
