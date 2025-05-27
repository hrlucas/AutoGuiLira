import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import datetime
import threading
import facilities_al
import tracking_al
import hist
import hist_1

### Sempre iniciar na ordem - Monitor de rastreamento - Relatórios de Viagens - Relatórios diversos ###

# Caminho do log
LOG_PATH = r"C:\Users\Gral\Projetos\AutoGuiLira\log_lira.txt"

# Define os horários principais (com hora exata)
HORARIOS_BASE = ["10:00"]

def str_to_time(hora_str):
    # Converte string para objeto de tempo 
    return datetime.datetime.strptime(hora_str, "%H:%M").time()

def agendar_execucoes():
    # Calcula os horários de execução para cada script 
    execucoes = []

    for hora_str in HORARIOS_BASE:
        base_time = str_to_time(hora_str)

        # Calcula os horários de execução para cada script
        hora_tracking = datetime.datetime.combine(datetime.date.today(), base_time)
        hora_facilities = hora_tracking - datetime.timedelta(minutes=9)
        hora_hist = hora_tracking - datetime.timedelta(minutes=6)
        hora_hist_1 = hora_tracking - datetime.timedelta(minutes=3)

        execucoes.append((hora_facilities.time(), "facilities"))
        execucoes.append((hora_hist.time(), "hist"))
        execucoes.append((hora_hist_1.time(), "hist_1"))  
        execucoes.append((hora_tracking.time(), "tracking"))

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
    except Exception as e:
        erro_log = f"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!! ERRO AO EXECUTAR {tarefa.upper()}: {str(e)}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
        print(erro_log)
        registrar_log(erro_log)


def loop_agendador():
   # Loop principal para agendar e executar os scripts nos horários definidos 
    execucoes_realizadas = set()

    while True:
        agora = datetime.datetime.now().time().replace(second=0, microsecond=0)

        for hora, tarefa in agendar_execucoes():
            if agora == hora and (hora, tarefa) not in execucoes_realizadas:
                execucoes_realizadas.add((hora, tarefa))
                executar_tarefa(tarefa)

        # Limpa o set à meia-noite
        if datetime.datetime.now().time() == datetime.time(0, 0):
            execucoes_realizadas.clear()

        time.sleep(1)

def registrar_log(mensagem):
    # Registra a execução no log 
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{mensagem}\n")

if __name__ == "__main__":
    loop_agendador()
