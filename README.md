# Sistema de Automação de Relatórios - Transportes Gral

Automação de coleta e lançamento de dados na rede interna da **Transportes Gral**, acelerando processos manuais de geração de relatórios e extração de informações da web usando Python, Playwright e PyAutoGUI.

## Sobre o Projeto

Este projeto foi idealizado e desenvolvido por Lucas Hochmann Rosa, durante seu período como jovem aprendiz na empresa Transportes Gral. Seu principal objetivo foi automatizar e otimizar processos relacionados à inserção de dados e à geração de relatórios internos, com foco na redução de tarefas manuais repetitivas, no aumento da eficiência operacional e na melhoria da confiabilidade das informações processadas.

A necessidade surgiu no contexto do setor de logística e transporte, no qual a Transportes Gral atua, e onde diversos relatórios diários e consultas a sistemas web são realizados manualmente, consumindo tempo e sendo suscetíveis a falhas humanas.

##
- **Ordem para iniciar Lira Logistica** -
    Somente iniciar os scripts com o AngelLira aberto no múdulo logistica nessa ordem **Monitor de rastreamento - Relatórios de Viagens - Relatórios diversos**.

## Tecnologias Utilizadas

- **Python** (versão 3.x)
- **Playwright** – Automação de interações web.
- **PyAutoGUI** – Automação de ações na interface gráfica.
- **Threading / Agendador de Tarefas** – Execução e agendamento dos módulos.
- Outras bibliotecas auxiliares: `pandas`, `datetime`, etc.

## Requisitos do Sistema

- **Python 3.x** (recomendado Python 3.8 ou superior)
- **Windows 10 ou superior** (64-bit recomendado)
- **Microsoft Edge** instalado
- **Resolução de tela:** 1920x1080 (Full HD)
- **Acesso à internet**
- **Permissões de execução** (pode ser necessário rodar como administrador)

## Instalação das Dependências

1. Clone ou copie este projeto para sua máquina local.
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Instale os navegadores do Playwright:
   ```sh
   playwright install
   ```

## Como Executar

Com o ambiente virtual ativo, execute o script principal:

```sh
python automation.py
```

O script ficará em execução contínua, aguardando os horários programados para cada tarefa. **Não feche o terminal** enquanto o sistema estiver rodando.

## Estrutura de Agendamento

O sistema executa módulos específicos em horários diferentes, conforme configurado em [`automation.py`](automation.py):

- **facilities**: 9 minutos antes do horário base
- **hist**: 6 minutos antes do horário base
- **hist_1**: 3 minutos antes do horário base
- **tracking**: no horário base
- **equipamentos** e **licencas**: horários definidos em `HORARIOS_MULTI`

Os horários podem ser ajustados alterando as listas `HORARIOS_AUTOMATION` e `HORARIOS_MULTI`.

## Descrição dos Módulos

- **tracking**: Extrai dados de rastreamento de veículos.
- **facilities**: Coleta informações de instalações.
- **hist**: Extrai relatórios históricos.
- **hist_1**: Complementa os dados históricos.
- **equipamentos**: Gera relatórios sobre equipamentos e veículos.
- **licencas_multi**: Extrai informações de licenças necessárias para operação.

Cada módulo gera arquivos de saída (planilhas, CSVs) em pastas específicas.

## Verificação e Logs

Após cada execução, o sistema verifica se o arquivo esperado foi gerado e registra o resultado em [`log_execucoes.txt`](log_execucoes.txt). Todas as operações são registradas para auditoria e acompanhamento.

## Limitações e Avisos

- **Resolução de tela:** Mudanças podem afetar a automação.
- **Edge:** O navegador deve estar instalado.
- **Janelas em foco:** Não use o computador durante a execução dos scripts.
- **Estabilidade dos sites:** Mudanças nos portais podem exigir ajustes nos scripts.
- **Permissões:** O script precisa de permissão para controlar mouse/teclado e acessar as pastas de destino.

## Créditos

Desenvolvido por **Lucas Hochmann Rosa**, Aprendiz na Transportes Gral.
