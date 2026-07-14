# LLM Classification Finetuning

Base reutilizável para competições Kaggle, preparada para crescer de uma primeira experiência até pipelines com validação, treino, inferência e submissões reproduzíveis.

## Estrutura

```text
.
|-- configs/                 # Uma configuração por experiência/competição
|-- data/
|   |-- raw/                 # Dados originais (imutáveis)
|   |-- interim/             # Dados transformados temporários
|   `-- processed/           # Dados prontos para treino
|-- models/                  # Checkpoints e modelos treinados
|-- notebooks/               # Exploração; lógica final deve ir para src/
|-- outputs/                 # Métricas, gráficos e previsões de validação
|-- scripts/                 # Pontos de entrada executáveis
|-- src/llm_classification/  # Código reutilizável
|-- submissions/             # CSVs submetidos ao Kaggle
|-- tests/                   # Testes automáticos
`-- pyproject.toml           # Dependências e ferramentas
```

Os conteúdos de `data/`, `models/`, `outputs/` e `submissions/` não entram no Git. Os ficheiros `.gitkeep` conservam apenas as pastas.

## Preparação local

Este projeto requer **Python 3.11 ou superior**. As versões recentes do Kaggle CLI também requerem Python 3.11+. Em Python 3.10, o `pip` pode instalar automaticamente uma versão antiga do cliente que não reconhece `KAGGLE_API_TOKEN` e procura apenas o ficheiro legado `kaggle.json`.

Consulta as versões de Python instaladas:

```powershell
py -0p
```

Se Python 3.11 ainda não estiver instalado:

```powershell
winget install Python.Python.3.11
```

Depois de instalar, fecha e volta a abrir o PowerShell. Dentro da pasta do projeto, cria e ativa o ambiente virtual:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
pip install --upgrade kaggle
```

Confirma as versões utilizadas:

```powershell
python --version
kaggle --version
```

Se já existir um ambiente `.venv` criado com uma versão antiga de Python, recria-o:

```powershell
deactivate
Remove-Item -Recurse -Force .venv
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
pip install --upgrade kaggle
```

Eliminar `.venv` não elimina código nem dados do projeto; remove apenas as dependências instaladas nesse ambiente.

## Autenticação no Kaggle

1. Abre as definições de API da conta Kaggle.
2. Gera um token novo.
3. Nunca coloques o token em código, notebooks, imagens, commits ou ficheiros versionados.
4. Se um token ficar exposto, revoga-o e gera outro imediatamente.

Define o token apenas na sessão atual do PowerShell:

```powershell
$env:KAGGLE_API_TOKEN = "COLOCA_AQUI_O_TOKEN_NOVO"
```

Confirma que a variável existe sem mostrar o seu conteúdo:

```powershell
if ($env:KAGGLE_API_TOKEN) {
    Write-Host "Token configurado"
} else {
    Write-Host "Token não configurado"
}
```

Testa a ligação:

```powershell
kaggle competitions list
```

O token deixa de estar definido quando fechas essa janela do PowerShell. Como alternativa, as versões atuais do cliente permitem autenticação através do browser:

```powershell
kaggle auth login
```

## Transferir dados de uma competição

Aceita primeiro as regras na página da competição. Depois usa o identificador presente no final do URL:

```powershell
$competition = "NOME-DA-COMPETICAO"
New-Item -ItemType Directory -Force "data/raw/$competition"
kaggle competitions download -c $competition -p "data/raw/$competition"
Expand-Archive "data/raw/$competition/$competition.zip" `
  -DestinationPath "data/raw/$competition"
```

Mantém os ficheiros originais em `data/raw/` sem alterações.

Para esta competição:

```powershell
$competition = "llm-classification-finetuning"
New-Item -ItemType Directory -Force "data/raw/$competition"
kaggle competitions download -c $competition -p "data/raw/$competition"
Expand-Archive "data/raw/$competition/$competition.zip" `
  -DestinationPath "data/raw/$competition"
```

Depois confirma a estrutura e faz a primeira análise automática:

```powershell
python scripts/inspect_data.py --config configs/llm_classification.yaml
```

Os detalhes do problema estão resumidos em `docs/competition.md`.

## Fluxo recomendado

1. Guarda os dados sem alterações em `data/raw/<competicao>/`.
2. Explora-os em `notebooks/`.
3. Move transformações reutilizáveis para `src/llm_classification/features/`.
4. Define a experiência em `configs/` e treina através de `scripts/train.py`.
5. Grava métricas em `outputs/`, modelos em `models/` e o CSV final em `submissions/`.

Os scripts incluídos são pontos de entrada intencionais: validam a estrutura e indicam onde ligar o pipeline específico da competição.
