# LLM Classification Finetuning

Base reutilizável para competições Kaggle, preparada para crescer de uma primeira experiência até pipelines com validação, treino, inferência e submissões reproduzíveis.

## Estrutura

```text
.
├── configs/                 # Uma configuração por experiência/competição
├── data/
│   ├── raw/                 # Dados originais (imutáveis)
│   ├── interim/             # Dados transformados temporários
│   └── processed/           # Dados prontos para treino
├── models/                  # Checkpoints e modelos treinados
├── notebooks/               # Exploração; lógica final deve ir para src/
├── outputs/                 # Métricas, gráficos e previsões de validação
├── scripts/                 # Pontos de entrada executáveis
├── src/llm_classification/  # Código reutilizável
├── submissions/             # CSVs submetidos ao Kaggle
├── tests/                   # Testes automáticos
└── pyproject.toml           # Dependências e ferramentas
```

Os conteúdos de `data/`, `models/`, `outputs/` e `submissions/` não entram no Git. Os ficheiros `.gitkeep` conservam apenas as pastas.

## Preparação local

Requer Python 3.10 ou superior.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
Copy-Item .env.example .env
```

Para autenticar o cliente Kaggle apenas na sessão atual do PowerShell, gera um novo
token no Kaggle e define-o sem o guardar no repositório:

```powershell
$env:KAGGLE_API_TOKEN = "COLOCA_AQUI_O_NOVO_TOKEN"
kaggle competitions list
```

Não coloques o token diretamente em código, notebooks ou commits. Para transferir
dados de uma competição, aceita primeiro as regras no Kaggle e executa:

```powershell
kaggle competitions download -c NOME-DA-COMPETICAO -p data/raw/NOME-DA-COMPETICAO
Expand-Archive data/raw/NOME-DA-COMPETICAO/NOME-DA-COMPETICAO.zip `
  -DestinationPath data/raw/NOME-DA-COMPETICAO
```

## Fluxo recomendado

1. Guarda os dados sem alterações em `data/raw/<competicao>/`.
2. Explora-os em `notebooks/`.
3. Move transformações reutilizáveis para `src/llm_classification/features/`.
4. Define a experiência em `configs/` e treina através de `scripts/train.py`.
5. Grava métricas em `outputs/`, modelos em `models/` e o CSV final em `submissions/`.

Os scripts incluídos são pontos de entrada intencionais: validam a estrutura e indicam onde ligar o pipeline específico da competição.
