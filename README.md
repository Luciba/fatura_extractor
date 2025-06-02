# 📄 Conversor de Faturas PDF para CSV

Este script Python foi projetado para extrair transações financeiras de faturas de cartão de crédito em formato PDF e convertê-las para um arquivo CSV estruturado. Ele é particularmente útil para organizar suas despesas e importá-las para softwares de planilhas ou de finanças pessoais.

O script processa o PDF, identifica o portador do cartão para cada transação, extrai a data, descrição e valor, e lida com PDFs protegidos por senha.

## ✨ Funcionalidades

* Extração de transações de arquivos PDF.
* Suporte a PDFs protegidos por senha.
* Identificação do portador do cartão associado a cada transação (baseado no primeiro nome).
* Processamento de layouts de PDF com múltiplas colunas (divide a página ao meio).
* Formatação da data para inclusão do ano da fatura.
* Separação de compras e pagamentos/créditos no sumário final.
* Saída dos dados em formato CSV, configurável para separador e decimal.

## ⚙️ Pré-requisitos

* Python 3.7 ou superior.
* PIP (gerenciador de pacotes Python).
* O arquivo PDF da sua fatura.

## 🛠️ Configuração Inicial

1.  **Clone ou baixe este repositório/script:**
    Se estiver no GitHub:
    ```bash
    git clone https://github.com/Luciba/fatura_extractor.git
    cd NOME_DO_REPOSITORIO
    ```
    Ou simplesmente baixe o arquivo `card_santa.py`.

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    Crie um arquivo chamado `requirements.txt` na mesma pasta do script com o seguinte conteúdo:
    ```txt
    pandas
    pdfplumber
    ```
    Em seguida, instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Script:**
    Abra o arquivo `card_santa.py` em um editor de texto e modifique as seguintes variáveis na seção `# --- CONFIGURAÇÕES ---`:

    * `ARQUIVO_PDF`: Coloque o caminho completo ou apenas o nome do arquivo PDF da sua fatura se ele estiver na mesma pasta do script.
        * Exemplo: `ARQUIVO_PDF = r"C:\Users\SeuUsuario\Documentos\Fatura_052025.PDF"`
        * Ou: `ARQUIVO_PDF = "Fatura_052025.PDF"` (se na mesma pasta)

    * `ANO_DA_FATURA`: Defina o ano correspondente às transações da fatura. Este ano será usado para complementar as datas extraídas (que geralmente vêm como DD/MM).
        * Exemplo: `ANO_DA_FATURA = "2025"`

    * `ARQUIVO_SAIDA_CSV` (Opcional): Nome do arquivo CSV que será gerado. O padrão é `fatura_processada.csv`.

## ▶️ Como Executar

1.  Certifique-se de que seu ambiente virtual (se criado) está ativado.
2.  Navegue pelo terminal até a pasta onde o script `card_santa.py` e sua fatura PDF estão localizados.
3.  Execute o script:
    ```bash
    python card_santa.py
    ```
4.  Quando solicitado, digite a senha do seu arquivo PDF e pressione Enter.
    ```
    🔑 Digite a senha do PDF e pressione Enter:
    ```
5.  Aguarde o processamento. O script exibirá o progresso da leitura das páginas e colunas.

## 📊 Saída

Após a execução bem-sucedida, um arquivo CSV (nomeado conforme `ARQUIVO_SAIDA_CSV`) será criado na mesma pasta. Este arquivo conterá as seguintes colunas:

* `Data`: Data da transação no formato DD/MM/AAAA.
* `Descrição`: Descrição da transação, prefixada com o nome do portador do cartão (ex: "(Luciano) - NOME DO ESTABELECIMENTO").
* `Valor`: Valor da transação. Valores positivos são compras, valores negativos podem ser pagamentos ou estornos.

O script também imprimirá um resumo no console:
```
✅ Sucesso! As transações foram salvas em 'fatura_processada.csv'
📊 Total de X compras e Y pagamentos/créditos processados.
```

## ⚠️ Solução de Problemas Comuns

* **`Erro: O arquivo PDF não foi encontrado em 'CAMINHO'.`**: Verifique se o valor da variável `ARQUIVO_PDF` está correto e se o arquivo PDF realmente existe no local especificado.
* **`ERRO: Senha do PDF incorreta.`**: A senha digitada está errada. Tente executar o script novamente com a senha correta.
* **`Nenhuma transação foi extraída.`**:
    * Verifique se o `ANO_DA_FATURA` está correto.
    * O layout do seu PDF pode ser diferente do esperado pelo script. O script foi ajustado para um layout específico com duas colunas e padrões de texto para identificar portadores e transações. Pode ser necessário ajustar as expressões regulares (`re.search`) ou a lógica de extração de colunas em `extrair_transacoes` para diferentes formatos de fatura.
    * A fatura pode não conter transações nas páginas processadas (lembre-se que a página 1 é ignorada).
* **Erro de dependências**: Certifique-se de ter instalado `pandas` e `pdfplumber` corretamente no ambiente ativo.

## 📝 Observações

* Este script foi desenvolvido com base em um formato específico de fatura que utiliza um layout de duas colunas para listar transações. Se a sua fatura tiver um layout diferente (uma única coluna, por exemplo), a lógica de divisão de página e processamento de colunas pode precisar de ajustes.
* A identificação do portador e das transações depende de expressões regulares. Se os padrões de texto na sua fatura forem muito diferentes, essas expressões também precisarão ser adaptadas.

---
```

## Instruções para uso no VS Code:

Aqui estão os passos para configurar e rodar seu script `card_santa.py` usando o Visual Studio Code:

1.  **Instalar o VS Code e a Extensão Python:**
    * Se ainda não o fez, baixe e instale o [Visual Studio Code](https://code.visualstudio.com/).
    * Abra o VS Code, vá para a aba de Extensões (ícone de quadrados no menu lateral ou `Ctrl+Shift+X`).
    * Procure por "Python" (da Microsoft) e instale-a.

2.  **Abrir a Pasta do Projeto:**
    * No VS Code, vá em `File > Open Folder...` (Arquivo > Abrir Pasta...).
    * Navegue até a pasta onde você salvou o arquivo `card_santa.py` e, idealmente, onde você colocará suas faturas PDF. Selecione a pasta.

3.  **Criar o arquivo `requirements.txt` (se ainda não existir):**
    * Na visualização do Explorer do VS Code (menu lateral esquerdo), clique com o botão direito na área da sua pasta e escolha `New File...` (Novo Arquivo...).
    * Nomeie o arquivo como `requirements.txt`.
    * Cole o seguinte conteúdo nele:
        ```txt
        pandas
        pdfplumber
        ```
    * Salve o arquivo (`Ctrl+S`).

4.  **Criar e Ativar um Ambiente Virtual (Recomendado):**
    * Abra o Terminal integrado no VS Code: `Terminal > New Terminal` (Terminal > Novo Terminal) ou `Ctrl+'`.
    * No terminal, digite:
        ```bash
        python -m venv venv
        ```
    * O VS Code pode perguntar se você deseja usar este novo ambiente para o workspace. Clique em "Sim".
    * Para ativar o ambiente no terminal do VS Code (se não ativou automaticamente):
        * **Windows (PowerShell/CMD):**
            ```powershell
            .\venv\Scripts\Activate.ps1
            ```
            ou
            ```cmd
            .\venv\Scripts\activate.bat
            ```
        * **macOS/Linux (bash/zsh):**
            ```bash
            source venv/bin/activate
            ```
    * Você deverá ver `(venv)` no início do prompt do seu terminal.

5.  **Instalar as Dependências:**
    * Com o ambiente virtual ativo no terminal do VS Code, digite:
        ```bash
        pip install -r requirements.txt
        ```
    * Aguarde a instalação dos pacotes `pandas` e `pdfplumber`.

6.  **Configurar o Script `card_santa.py`:**
    * No Explorer do VS Code, clique duas vezes em `card_santa.py` para abri-lo no editor.
    * Modifique as variáveis na seção `# --- CONFIGURAÇÕES ---` conforme necessário:
        * `ARQUIVO_PDF`: Certifique-se de que este caminho aponte para o seu arquivo PDF. Se o PDF estiver na mesma pasta do script, apenas o nome do arquivo é suficiente (ex: `"minha_fatura.PDF"`).
        * `ANO_DA_FATURA`: Confirme o ano correto das transações.
        * `ARQUIVO_SAIDA_CSV` (opcional).

7.  **Executar o Script:**
    * Com o arquivo `card_santa.py` aberto e ativo no editor do VS Code:
        * **Opção 1 (Botão Play):** Clique no botão "Run Python File" (um ícone de play ▶️) no canto superior direito da janela do editor.
        * **Opção 2 (Terminal):** Certifique-se de que o terminal integrado está aberto, com o ambiente virtual ativo, e na pasta correta. Digite:
            ```bash
            python card_santa.py
            ```
    * O script será executado no painel "TERMINAL" do VS Code. Você será solicitado a digitar a senha do PDF ali mesmo.
        ```
        🔑 Digite a senha do PDF e pressione Enter:
        ```
    * Digite a senha e pressione Enter.

8.  **Verificar a Saída:**
    * Após a execução, o arquivo CSV (ex: `fatura_processada.csv`) aparecerá no Explorer do VS Code, na mesma pasta do seu projeto.
    * Você pode clicar duas vezes no arquivo CSV dentro do VS Code para visualizá-lo (o VS Code tem extensões que podem formatar CSVs para melhor visualização, ou você pode abri-lo no Excel, Google Sheets, LibreOffice Calc, etc.).
    * Verifique também as mensagens de log no painel "TERMINAL" para confirmar o sucesso ou identificar erros.

