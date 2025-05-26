from playwright.sync_api import sync_playwright
import time
import os
from datetime import datetime
import calendar

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=edge_path,
        channel="msedge",
        headless=False,
        args=["--start-maximized"]
    )
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        accept_downloads=True
    )
    page = context.new_page()

    # Abre login
    page.goto("https://gral.multitms.com.br/Login")
    time.sleep(2)
    page.keyboard.press('Meta+ArrowUp')  # maximiza janela
    page.wait_for_load_state('load')

    # Faz login
    page.fill('input[placeholder="Usuário"]', 'roberto')
    page.fill('input[placeholder="Senha"]', '@NewMulti#123')
    page.click('button:has-text("Acessar")')
    page.wait_for_load_state('load')

    # Vai para Relatórios
    page.goto("https://gral.multitms.com.br/#Relatorios/CTe/CTes")
    page.wait_for_load_state('load')
    time.sleep(2)

    # Clica no botão "Buscar" do campo "Tipo do Relatório"
    botao_tipo_relatorio = page.locator('button[data-bind*="TipoRelatorio.idBtnSearch"]')
    botao_tipo_relatorio.wait_for(state="visible", timeout=5000)
    botao_tipo_relatorio.click()

    # Aguarda o modal "Buscar Modelos de Relatórios"
    modal = page.locator('div[role="dialog"]', has_text="Buscar Modelos de Relatórios")
    modal.wait_for(state="visible", timeout=15000)

    # Preenche o campo "Descrição"
    modal.get_by_label("Descrição").fill("SIG_CTEs_PROJECOES_NOVO")

    # Clica em "Pesquisar"
    modal.get_by_role("button", name="Pesquisar").click()
    time.sleep(2)

    # Aguarda a linha com o modelo correto
    linha = modal.locator('table tbody tr', has_text='SIG_CTEs_PROJECOES_NOVO')
    linha.wait_for(state="visible", timeout=5000)

    # Clica na última célula da linha (botão "Selecionar")
    selecionar_celula = linha.locator('td').nth(-1)
    selecionar_celula.click()
    time.sleep(2)

    # Preenche as datas de emissão usando evaluate para disparar eventos

    hoje = datetime.now()
    primeiro_dia = hoje.replace(day=1).strftime("%d/%m/%Y")
    ultimo_dia = hoje.replace(day=calendar.monthrange(hoje.year, hoje.month)[1]).strftime("%d/%m/%Y")

    # Data Emissão Inicial
    seletor_data_inicial = 'input[data-bind*="DataInicialEmissao.val"]'
    page.evaluate("""
    ({ selector, valor }) => {
        const el = document.querySelector(selector);
        if(el){
            el.value = valor;
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
        }
    }
    """, {"selector": seletor_data_inicial, "valor": primeiro_dia})

    # Data Emissão Final
    seletor_data_final = 'input[data-bind*="DataFinalEmissao.val"]'
    page.evaluate("""
    ({ selector, valor }) => {
        const el = document.querySelector(selector);
        if(el){
            el.value = valor;
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
        }
    }
    """, {"selector": seletor_data_final, "valor": ultimo_dia})


    # Clica em "Preview"
    page.wait_for_selector('button:has-text("Preview")', timeout=5000)
    page.click('button:has-text("Preview")')
    time.sleep(3)

    # Rola até o final da página
    page.keyboard.press("End")
    time.sleep(5)

    # Diretório e nome do arquivo para salvar
    diretorio_salvar = r"C:\Users\Gral\TRANSPORTES GRAL LTDA\RTO - PB\sig\multi\teste"
    ano_mes = datetime.now().strftime("%Y.%m")
    nome_arquivo = f"CTEs_{ano_mes}.csv"
    caminho_arquivo = os.path.join(diretorio_salvar, nome_arquivo)
    os.makedirs(diretorio_salvar, exist_ok=True)
    time.sleep(2)

    # Captura o download e salva no local desejado
    with page.expect_download() as download_info:
        page.click('button:has-text("Gerar Planilha Excel")')
    download = download_info.value
    download.save_as(caminho_arquivo)

    print(f"Arquivo salvo em: {caminho_arquivo}")
    print("Processo concluído. Navegador será fechado em 5 segundos.")
    time.sleep(5)
    browser.close()
