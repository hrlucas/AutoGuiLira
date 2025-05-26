import os
import time
import datetime
import facilities_al
import tracking_al
import hist
import hist_1
import licencas_multi
import equipamentos
import ctes

# Caminho do log
LOG_PATH = r"C:\Users\Gral\Projetos\AutoGuiLira\log_execucoes.txt"

# Extra
ano_mes = datetime.datetime.now().strftime("%Y.%m")

# Horários principais
HORARIOS_LIRA = ["08:30", "10:00", "13:30", "15:00"]
HORARIOS_MULTI = ["08:00"]
HORARIOS_CTES = ["09:00", "10:30", "11:30", "14:30", "15:30", "17:00"]

def str_to_time(hora_str):
    return datetime.datetime.strptime(hora_str, "%H:%M").time()

def agendar_execucoes():
    execucoes = []

    # Automation
    for hora_str in HORARIOS_LIRA:
        base_time = str_to_time(hora_str)
        data = datetime.datetime.combine(datetime.date.today(), base_time)
        execucoes.extend([
            (data - datetime.timedelta(minutes=9), "facilities"),
            (data - datetime.timedelta(minutes=6), "hist"),
            (data - datetime.timedelta(minutes=3), "hist_1"),
            (data, "tracking"),
        ])

    # Multi
    for hora_str in HORARIOS_MULTI:
        base_time = str_to_time(hora_str)
        data = datetime.datetime.combine(datetime.date.today(), base_time)
        execucoes.extend([
            (data, "equipamentos"),
            (data + datetime.timedelta(minutes=3), "licencas"),
        ])

    # CTEs
    for hora_str in HORARIOS_CTES:
        base_time = str_to_time(hora_str)
        data = datetime.datetime.combine(datetime.date.today(), base_time)
        execucoes.append((data, "ctes"))  

    return execucoes

def verificar_arquivo(tarefa):
    time.sleep(240)  # Aguarda 4 minutos
    data_atual = datetime.datetime.now()

    if tarefa == "facilities":
        caminho = r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\alira"
        esperado = "facilities_al"
    elif tarefa == "tracking":
        caminho = r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\alira"
        esperado = "tracking_al"
    elif tarefa == "hist":
        mes_anterior = data_atual.month - 1 or 12
        ano = data_atual.year if data_atual.month > 1 else data_atual.year - 1
        esperado = f"{ano}.{mes_anterior:02d}"
        caminho = r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\alira\hist"
    elif tarefa == "hist_1":
        esperado = data_atual.strftime("%Y.%m_HV")
        caminho = r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\alira\hist"
    elif tarefa == "equipamentos":
        caminho = r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\multi"
        esperado = "Relatório_de_Equipamentos.csv"
    elif tarefa == "licencas":
        caminho = r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\multi"
        esperado = "Relatório_de_Licenças.csv"
    elif tarefa == "ctes":
        caminho = r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\multi"
        esperado = f"CTEs_{ano_mes}.csv"
    else:
        return

    arquivos = os.listdir(caminho)
    # Pega o horário programado da tarefa
    execucoes = {t: dt for dt, t in agendar_execucoes()}
    horario_tarefa = execucoes.get(tarefa)
    if not horario_tarefa:
        horario_tarefa = data_atual

    sucesso = False
    for nome in arquivos:
        if esperado in nome:
            caminho_arquivo = os.path.join(caminho, nome)
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(caminho_arquivo))
            # Verifica se está dentro de 10 minutos do horário programado
            if abs((mtime - horario_tarefa).total_seconds()) <= 600:
                sucesso = True
                break

    if tarefa in ["facilities", "tracking", "hist", "hist_1"]:
        tipo = "AUTOMATION"
    elif tarefa == "ctes":
        tipo = "CTES"
    else:
        tipo = "MULTI"
    resultado = "✔ ARQUIVO GERADO COM SUCESSO" if sucesso else "✖ ERRO: ARQUIVO NÃO GERADO"

    mensagem = f"""
#########################################################
### [{tipo}] RESULTADO DA EXECUÇÃO - {tarefa.upper()}
### VERIFICAÇÃO APÓS 4 MINUTOS
### DIRETÓRIO: {caminho}
### ESPERADO: {esperado}
### RESULTADO: {resultado}
#########################################################
"""
    registrar_log(mensagem)

def executar_tarefa(tarefa):
    agora_str = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    if tarefa in ["facilities", "tracking", "hist", "hist_1"]:
        tipo = "AUTOMATION"
    elif tarefa == "ctes":
        tipo = "CTES"
    else:
        tipo = "MULTI"
    cabecalho = f"""
=========================================================
### [{tipo}] INICIANDO EXECUÇÃO: {tarefa.upper()} - {agora_str}
========================================================="""
    print(cabecalho)
    registrar_log(cabecalho)

    try:
        import threading
        if tarefa == "tracking":
            threading.Thread(target=tracking_al.main).start()
        elif tarefa == "facilities":
            threading.Thread(target=facilities_al.main).start()
        elif tarefa == "hist":
            threading.Thread(target=hist.main).start()
        elif tarefa == "hist_1":
            threading.Thread(target=hist_1.main).start()
        elif tarefa == "equipamentos":
            threading.Thread(target=equipamentos.main).start()
        elif tarefa == "licencas":
            threading.Thread(target=licencas_multi.main).start()
        elif tarefa == "ctes":
            threading.Thread(target=ctes.main).start()
        threading.Thread(target=verificar_arquivo, args=(tarefa,)).start()
    except Exception as e:
        erro_log = f"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!! ERRO AO EXECUTAR {tarefa.upper()}: {str(e)}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
        print(erro_log)
        registrar_log(erro_log)

def registrar_log(mensagem):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{mensagem}\n")

def loop_agendador():
    execucoes_realizadas = set()
    while True:
        agora = datetime.datetime.now().replace(second=0, microsecond=0)
        for dt, tarefa in agendar_execucoes():
            if agora == dt and (dt, tarefa) not in execucoes_realizadas:
                execucoes_realizadas.add((dt, tarefa))
                executar_tarefa(tarefa)
        if datetime.datetime.now().time() == datetime.time(0, 0):
            execucoes_realizadas.clear()
        time.sleep(1)

if __name__ == "__main__":
    loop_agendador()