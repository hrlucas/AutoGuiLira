import time
import datetime
import threading
import os
import facilities_al
import tracking_al
import hist
import hist_1

### Sempre iniciar na ordem - Monitor de rastreamento - Relatórios de Viagens - Relatórios diversos ###

# Caminho do log
LOG_PATH = r"C:\Users\Gral\Projetos\AutoGuiLira\log_execucoes.txt"

# Define os horários principais (com hora exata)
HORARIOS_BASE = ["08:30", "10:00", "13:30", "15:00"]

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

def executar_tarefa(tarefa):
   # Executa o script conforme o tipo de tarefa "
    agora_str = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    mensagem_log = f"{agora_str} - Executando: {tarefa}"
    print(mensagem_log)
    registrar_log(mensagem_log)

    try:
        if tarefa == "tracking":
            threading.Thread(target=tracking_al.main).start()
        elif tarefa == "facilities":
            threading.Thread(target=facilities_al.main).start()
        elif tarefa == "hist":
            threading.Thread(target=hist.main).start()
        elif tarefa == "hist_1":  
            threading.Thread(target=hist_1.main).start()
    except Exception as e:
        erro_log = f"{agora_str} - ERRO ao executar {tarefa}: {str(e)}"
        print(erro_log)
        registrar_log(erro_log)

if __name__ == "__main__":
    loop_agendador()
