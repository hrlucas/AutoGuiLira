import pyautogui
import pygetwindow as gw
import time
import sys
from datetime import datetime  # Para obter o ano e o mês atuais

# Configurações do PyAutoGUI
pyautogui.FAILSAFE = True

# ALira

titulo_janela = "Angel.Lira - Módulo Logística"

janelas = gw.getWindowsWithTitle(titulo_janela)

if not janelas:
    print(f"❌ Janela com o título '{titulo_janela}' não foi encontrada.")
    sys.exit(1)

janela = janelas[0]
janela.activate()
time.sleep(2)

# Auto cliques

####################################################################################

# M. de Rastreamento

# Clique 1 – (100, 35)
pyautogui.click(x=100, y=35) #ABRE M. DE RASTREAMENTO
time.sleep(2)

# Pressiona F5
pyautogui.press('f5') #ATUALIZA A TELA
time.sleep(20)

# Clique 2 – (1655, 999)
pyautogui.click(x=1655, y=999) #EXPORTAR
time.sleep(2)

# Clique 2.1 – (1150, 335)
pyautogui.click(x=1150, y=335) #BARRA DE SELEÇÃO DE CAMINHO
time.sleep(2)

# Apaga o conteúdo do campo
pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
pyautogui.press('backspace')  # Apaga o texto selecionado
time.sleep(1)

# Cola outro caminho especificado
pyautogui.write(r"C:\Users\Gral\Projetos\Save Lira")  # Usando string bruta
pyautogui.press('enter')
time.sleep(2)

# Clique 3 – (780, 471)
pyautogui.click(x=780, y=471) #VAI PARA O ARQUIVO
time.sleep(2)

# Clique 4 – (1270, 785)
pyautogui.click(x=1270, y=785) #Salvar
time.sleep(15)

# Clique 5 – (1090, 600)
pyautogui.click(x=1090, y=600) #NÃO ABRE O ARQUIVO

time.sleep(10) #CALMA

####################################################################################

# Relatórios viagens

# Clique 1 – (260, 35)
pyautogui.click(x=260, y=35)  # RELATÓRIOS VIAGENS
time.sleep(2)

# Clique 1.1 – (440, 220)
pyautogui.click(x=440, y=220)  # DIA 1 MÊS ATUAL
pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
pyautogui.press('backspace')  # Apaga o texto selecionado
time.sleep(2)

# Insere a data no formato "01/MM/AAAA 00:00:00" (mês atual e ano atual)
data_atual = datetime.now()
data_1_1 = data_atual.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
data_1_1_formatada = data_1_1.strftime("01/%m/%Y 00:00:00")
pyautogui.write(data_1_1_formatada)
time.sleep(2)

# Clique 1.2 – (285, 220)
pyautogui.click(x=285, y=220)  # DIA 1 MÊS ANTERIOR
pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
pyautogui.press('backspace')  # Apaga o texto selecionado
time.sleep(2)

# Insere a data no formato "01/MM/AAAA 00:00:00" (mês anterior e ano ajustado)
if data_atual.month == 1:  # Se for janeiro, ajusta para dezembro do ano anterior
    mes_anterior = 12
    ano_anterior = data_atual.year - 1
else:
    mes_anterior = data_atual.month - 1
    ano_anterior = data_atual.year

data_1_2 = data_atual.replace(year=ano_anterior, month=mes_anterior, day=1, hour=0, minute=0, second=0, microsecond=0)
data_1_2_formatada = data_1_2.strftime("01/%m/%Y 00:00:00")
pyautogui.write(data_1_2_formatada)
time.sleep(2)

# Pressiona F5
pyautogui.press('f5')  # ATUALIZA A TELA
time.sleep(30)

# Clique 2 – (1655, 999)
pyautogui.click(x=1655, y=999)  # EXPORTAR
time.sleep(2)

# Clique 3 – (1150, 335)
pyautogui.click(x=1150, y=335) #BARRA DE SELEÇÃO DE CAMINHO
time.sleep(2)

# Apaga o conteúdo do campo
pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
pyautogui.press('backspace')  # Apaga o texto selecionado
time.sleep(1)

# Cola o caminho especificado e pressiona Enter
pyautogui.write(r"C:\Users\Gral\Projetos\Save Lira\hist")  # Usando string bruta
pyautogui.press('enter')
time.sleep(2)

# Clique 4 – (780, 720)
pyautogui.click(x=780, y=720) #DEFINIÇÃO DO NOME DO ARQUIVO
time.sleep(2)

# Insere o formato do nome do arquivo com ano e mês atuais
ano_mes = datetime.now().strftime("%Y.%m_HV")  # Exemplo: "2025.05_HV"
pyautogui.write(ano_mes)
pyautogui.press('enter')
time.sleep(2)

# Clique 5 – (1090, 600)
pyautogui.click(x=1090, y=600) #NÃO ABRE O ARQUIVO

time.sleep(10)

###################################################################################

# Relatórios diversos

# Clique 1 – (385, 35)
pyautogui.click(x=385, y=35) #RELATÓRIOS DIVERSOS
time.sleep(2)

# Clique 1.1 – (1850, 90)
pyautogui.click(x=1850, y=90) #CONSULTAR
time.sleep(2)

# Clique 1.2 – (1045, 505)
pyautogui.click(x=1045, y=505)
pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
pyautogui.press('backspace')  # Apaga o texto selecionado
time.sleep(1)
pyautogui.write("3264") #CODIGO PARAMETRO
time.sleep(1) 

# Clique 1.3 – (1050, 550)
pyautogui.click(x=1050, y=550) #APLICANDO CODIGO PARAMETRO
time.sleep(30)

# Clique 2 – (1655, 999)
pyautogui.click(x=1800, y=990) #EXPORTAR
time.sleep(2)

# Clique 2 – (1655, 999)
pyautogui.click(x=1800, y=930) #XLSX
time.sleep(2)

# Clique 3 – (1150, 335)
pyautogui.click(x=1150, y=335) #BARRA DE SELEÇÃO DE CAMINHO
time.sleep(2)

# Apaga o conteúdo do campo
pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
pyautogui.press('backspace')  # Apaga o texto selecionado
time.sleep(1)

# Cola outro caminho especificado
pyautogui.write(r"C:\Users\Gral\Projetos\Save Lira")  # Usando string bruta
pyautogui.press('enter')
time.sleep(2)

# Clique 4 – (780, 471)
pyautogui.click(x=780, y=450) #VAI PARA O ARQUIVO
time.sleep(2)

# Clique 5 – (1270, 785)
pyautogui.click(x=1270, y=785) #Salvar
time.sleep(30)

# Clique 6 – (1090, 600)
pyautogui.click(x=1090, y=600)  #NÃO ABRE O ARQUIVO
time.sleep(2)

#enceramento

# Retorna para a aba do VS Code
titulo_vs_code = "Visual Studio Code"
vs_code_janelas = gw.getWindowsWithTitle(titulo_vs_code)

if vs_code_janelas:
    vs_code_janela = vs_code_janelas[0]
    vs_code_janela.activate()
    print("✅ Retornando para a aba do Visual Studio Code.")
else:
    print(f"⚠️ Janela do '{titulo_vs_code}' não encontrada.")