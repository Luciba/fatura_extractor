import pandas as pd
import pdfplumber
import re
import os
import getpass

# --- CONFIGURAÇÕES ---
# 1. Coloque o caminho para o seu arquivo PDF da fatura.
ARQUIVO_PDF = r"Fatura_052025.PDF" # <-- MUDE AQUI

# 2. Defina o ano da fatura. Com base no seu PDF.
ANO_DA_FATURA = "2025" # <-- CONFIRME SE ESTE É O ANO CORRETO DAS COMPRAS

# 3. Defina o nome do arquivo CSV que será gerado.
ARQUIVO_SAIDA_CSV = "fatura_processada.csv"
# --- FIM DAS CONFIGURAÇÕES ---

def extrair_transacoes(caminho_pdf, ano, senha):
    """
    Versão 6: Processa o PDF coluna por coluna para evitar a mistura de dados.
    """
    print("📄 Iniciando leitura do arquivo PDF...")
    
    transacoes = []
    portador_atual = "Não Identificado"

    try:
        with pdfplumber.open(caminho_pdf, password=senha) as pdf:
            for pagina in pdf.pages:
                # Ignora a primeira página que é apenas um resumo
                if pagina.page_number == 1:
                    print(f"-> Ignorando página 1 (resumo da fatura).")
                    continue
                
                print(f"-> Processando página {pagina.page_number} de {len(pdf.pages)}...")

                # AJUSTE CRÍTICO: Define as duas colunas da página
                metade_da_pagina = pagina.width / 2
                colunas = [
                    # Bounding Box da coluna da esquerda: (x0, top, x1, bottom)
                    (0, 0, metade_da_pagina, pagina.height),
                    # Bounding Box da coluna da direita:
                    (metade_da_pagina, 0, pagina.width, pagina.height)
                ]

                # Processa cada coluna como se fosse uma página separada
                for i, bbox_coluna in enumerate(colunas):
                    print(f"   -> Lendo coluna {i + 1}...")
                    
                    pagina_cortada = pagina.crop(bbox=bbox_coluna)
                    texto_coluna = pagina_cortada.extract_text(layout=True, x_tolerance=2)
                    
                    if not texto_coluna:
                        continue  # Pula colunas vazias

                    linhas = texto_coluna.split('\n')

                    for linha in linhas:
                        linha_limpa = linha.strip()

                        # Padrão 1: Identifica o meliante que usou o cartão
                        match_portador = re.search(r'^([A-Z\s@.*]+?)\s+-\s+\d{4}', linha_limpa)
                        if match_portador:
                            nome_completo = match_portador.group(1).replace('@', '').strip()
                            portador_atual = nome_completo.split()[0].capitalize()
                            print(f"      👤 Portador na coluna {i + 1}: {portador_atual}")
                            continue

                        # Padrão 2: Identifica transação
                        match_transacao = re.search(r'(\d{2}/\d{2})\s+(.+?)\s+((?:-)?[\d.,]+)$', linha_limpa)
                        if match_transacao:
                            if "VALOR TOTAL" in linha_limpa.upper():
                                continue

                            data_pdf = match_transacao.group(1)
                            descricao = match_transacao.group(2).strip()
                            valor_str = match_transacao.group(3)
                            
                            data_formatada = f"{data_pdf}/{ano}"
                            descricao_final = f"({portador_atual}) - {descricao}"
                            valor_float = float(valor_str.replace('.', '').replace(',', '.'))
                            
                            transacoes.append({
                                "Data": data_formatada,
                                "Descrição": descricao_final,
                                "Valor": valor_float
                            })
    
    except pdfplumber.exceptions.PDFPasswordIncorrect:
        print("\n❌ ERRO: Senha do PDF incorreta.")
        return None
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")
        return None

    return transacoes


# --- EXECUÇÃO DO SCRIPT ---
if __name__ == "__main__":
    if os.path.exists(ARQUIVO_PDF):
        senha_pdf = getpass.getpass("🔑 Digite a senha do PDF e pressione Enter: ")
        if senha_pdf:
            lista_de_transacoes = extrair_transacoes(ARQUIVO_PDF, ANO_DA_FATURA, senha_pdf)

            if lista_de_transacoes:
                compritchas = pd.DataFrame(lista_de_transacoes)
                compras = compritchas[compritchas['Valor'] >= 0]
                pagamentos = compritchas[compritchas['Valor'] < 0]
                
                compritchas.to_csv(ARQUIVO_SAIDA_CSV, index=False, sep=';', decimal=',')
                
                print(f"\n✅ Sucesso! As transações foram salvas em '{ARQUIVO_SAIDA_CSV}'")
                print(f"📊 Total de {len(compras)} compras e {len(pagamentos)} pagamentos/créditos processados.")
            else:
                print("\n⚠️ Nenhuma transação foi extraída. Verifique o conteúdo do PDF.")
    else:
        print(f"❌ Erro: O arquivo PDF não foi encontrado em '{ARQUIVO_PDF}'.")