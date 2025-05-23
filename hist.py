import pyautogui
import pygetwindow as gw
import time
from datetime import datetime  # Para obter o ano e o mês atuais

# Configurações do PyAutoGUI
pyautogui.FAILSAFE = True

def main():
    # ALira
    titulo_janela = "Angel.Lira - Módulo Logística"
    
    # Obtém todas as janelas com o título especificado
    janelas = gw.getWindowsWithTitle(titulo_janela)
    
    if janelas:
        # Ativa a primeira janela que corresponde ao título
        janela = janelas[0]
        janela.activate()  # Ativa a janela
        time.sleep(2)  # Aguarda um tempo para garantir que a janela foi ativada corretamente
    else:
        print("Janela não encontrada!")
        return

    # Define a data atual no início da função
    data_atual = datetime.now()

    # Auto cliques
    # Relatórios viagens

    # Clique 1 – (260, 35)
    pyautogui.click(x=260, y=35)  # RELATÓRIOS VIAGENS
    time.sleep(2)

    # Clique 1.2 – (285, 220)
    pyautogui.click(x=285, y=220)  # DIA 1 MÊS ANTERIOR
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(2)

    # Insere a data "01/MM/AAAA 00:00:00" do mês anterior
    if data_atual.month == 1:
        mes_anterior = 12
        ano_anterior = data_atual.year - 1
    else:
        mes_anterior = data_atual.month - 1
        ano_anterior = data_atual.year

    data_1_2 = data_atual.replace(year=ano_anterior, month=mes_anterior, day=1, hour=0, minute=0, second=0, microsecond=0)
    data_1_2_formatada = data_1_2.strftime("01/%m/%Y 00:00:00")
    pyautogui.write(data_1_2_formatada)
    time.sleep(2)

    # Clique 1.1 – (440, 220)
    pyautogui.click(x=440, y=220)  # DIA 1 MÊS ATUAL
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(2)

    # Insere a data no formato "01/MM/AAAA 00:00:00"
    data_1_1 = data_atual.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    data_1_1_formatada = data_1_1.strftime("01/%m/%Y 00:00:00")
    pyautogui.write(data_1_1_formatada)
    pyautogui.press('enter')
    time.sleep(2)

    # Atualiza - F5
    pyautogui.press('f5')
    time.sleep(70)

    # Clique 2 – (1655, 999)
    pyautogui.click(x=1655, y=999)  # EXPORTAR
    time.sleep(2)

    # Clique 3 – (1150, 335)
    pyautogui.click(x=1150, y=335)  # BARRA DE SELEÇÃO DE CAMINHO
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(1)

    pyautogui.write(r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\alira\hist")
    pyautogui.press('enter')
    time.sleep(2)

    # Clique 4 – (780, 720)
    pyautogui.click(x=780, y=720)  # DEFINIÇÃO DO NOME DO ARQUIVO
    time.sleep(2)

    # Define ano e mês anterior
    if data_atual.month == 1:
        mes_anterior = 12
        ano_anterior = data_atual.year - 1
    else:
        mes_anterior = data_atual.month - 1
        ano_anterior = data_atual.year

    ano_mes = f"{ano_anterior}.{mes_anterior:02d}_HV"
    pyautogui.write(ano_mes)
    pyautogui.press('enter')
    time.sleep(2)

    # Clique 5 – (1090, 600)
    pyautogui.click(x=1090, y=600)  # NÃO ABRE O ARQUIVO

    time.sleep(10)

    print("Execução de hist concluída.")

# Garante que o script só executa se for chamado diretamente
if __name__ == "__main__":
    main()