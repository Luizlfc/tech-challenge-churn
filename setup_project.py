"""
Setup script for tech-challenge-churn project.
Run this inside the project root folder to create all necessary files and folders.
"""
import os

# ============================================================
# 1. Create directories
# ============================================================
directories = [
    "data/raw",
    "data/processed",
    "docs",
    "models",
    "notebooks",
    "src/api",
    "src/data",
    "src/features",
    "src/models",
    "src/utils",
    "tests",
]

for d in directories:
    os.makedirs(d, exist_ok=True)
    print(f"[OK] Pasta criada: {d}")

# ============================================================
# 2. Create __init__.py files
# ============================================================
init_files = [
    "src/__init__.py",
    "src/api/__init__.py",
    "src/data/__init__.py",
    "src/features/__init__.py",
    "src/models/__init__.py",
    "src/utils/__init__.py",
    "tests/__init__.py",
]

for f in init_files:
    with open(f, "w") as fp:
        fp.write("")
    print(f"[OK] Arquivo criado: {f}")

# ============================================================
# 3. Create pyproject.toml
# ============================================================
pyproject = """[project]
name = "tech-challenge-churn"
version = "0.1.0"
description = "Tech Challenge Fase 1 - Previsao de Churn com MLP PyTorch"
requires-python = ">=3.10"
dependencies = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "torch",
    "mlflow",
    "fastapi",
    "uvicorn",
    "pydantic",
    "joblib",
    "pandera",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "ruff",
]

[tool.ruff]
line-length = 120
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I"]

[tool.pytest.ini_options]
testpaths = ["tests"]
"""

with open("pyproject.toml", "w") as f:
    f.write(pyproject)
print("[OK] Arquivo criado: pyproject.toml")

# ============================================================
# 4. Create Makefile
# ============================================================
makefile = """.PHONY: lint test run train

lint:
	ruff check src/ tests/

test:
	pytest tests/ -v

run:
	uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

train:
	python -m src.models.train_baseline
	python -m src.models.train_mlp
"""

with open("Makefile", "w") as f:
    f.write(makefile)
print("[OK] Arquivo criado: Makefile")

# ============================================================
# 5. Create .gitignore
# ============================================================
gitignore = """# Ambiente virtual
venv/
.venv/

# Python
__pycache__/
*.pyc
*.pyo

# Dados grandes
data/raw/*.csv
data/processed/*.csv

# Modelos salvos
models/*.pkl
models/*.pt
models/*.joblib

# MLflow
mlruns/
mlartifacts/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Jupyter
.ipynb_checkpoints/
"""

with open(".gitignore", "w") as f:
    f.write(gitignore)
print("[OK] Arquivo criado: .gitignore")

# ============================================================
# 6. Create placeholder source files
# ============================================================
source_files = {
    "src/api/main.py": '"""FastAPI application for churn prediction."""\n',
    "src/data/preprocessing.py": '"""Data preprocessing module."""\n',
    "src/features/feature_engineering.py": '"""Feature engineering module."""\n',
    "src/models/train_baseline.py": '"""Baseline model training."""\n',
    "src/models/train_mlp.py": '"""MLP PyTorch model training."""\n',
    "src/models/predict.py": '"""Model prediction module."""\n',
    "src/utils/logger.py": '"""Structured logging configuration."""\n',
    "tests/test_smoke.py": '"""Smoke tests."""\n',
    "tests/test_schema.py": '"""Schema validation tests."""\n',
    "tests/test_api.py": '"""API endpoint tests."""\n',
}

for filepath, content in source_files.items():
    with open(filepath, "w") as f:
        f.write(content)
    print(f"[OK] Arquivo criado: {filepath}")

# ============================================================
# 7. Create documentation files
# ============================================================
docs_files = {
    "docs/ml_canvas.md": """# ML Canvas - Churn Prediction

## Problema de Negocio
Uma operadora de telecomunicacoes enfrenta alta taxa de churn.

## Objetivo
Prever clientes com maior risco de cancelamento para acoes preventivas de retencao.

## Stakeholders
- Diretoria comercial
- Time de retencao
- Equipe de analytics

## Usuario Final
Equipe de retencao / CRM

## Target
Churn (Yes/No)

## Metrica de Negocio
- Reducao da taxa de cancelamento
- Aumento da retencao de clientes

## Metricas Tecnicas
- ROC-AUC
- PR-AUC
- F1-score
- Recall

## Riscos
- Desbalanceamento da base
- Falta de variaveis comportamentais
- Dados insuficientes

## Premissas
- Dataset Telco Customer Churn (IBM)
- Classificacao binaria
- Dados tabulares
""",
    "docs/model_card.md": """# Model Card - Churn Prediction

## Finalidade do Modelo
Prever se um cliente de telecomunicacoes ira cancelar o servico.

## Dataset
Telco Customer Churn (IBM) - Kaggle

## Features Principais
(a ser preenchido apos EDA)

## Metricas de Performance
(a ser preenchido apos treinamento)

## Limitacoes
(a ser preenchido)

## Riscos e Vieses
(a ser preenchido)

## Uso Recomendado
Apoio a decisao para times de retencao de clientes.

## Uso Nao Recomendado
Decisao automatica sem supervisao humana.
""",
    "docs/monitoring.md": """# Plano de Monitoramento

## Metricas Monitoradas
- Latencia da API
- Taxa de erro
- Distribuicao de entrada (feature drift)
- Performance do modelo (metric drift)
- Volume de requisicoes

## Alertas
- Latencia > threshold
- Queda de performance
- Drift de features
- Erros frequentes

## Playbook
- Se latencia aumentar: revisar infraestrutura
- Se metricas cairem: reavaliar dados e retreinar
- Se houver drift: reexecutar pipeline e retreinar
""",
}

for filepath, content in docs_files.items():
    with open(filepath, "w") as f:
        f.write(content)
    print(f"[OK] Arquivo criado: {filepath}")

# ============================================================
# Done!
# ============================================================
print("")
print("=" * 50)
print("SETUP COMPLETO! Estrutura do projeto criada.")
print("=" * 50)
print("")
print("Proximos passos:")
print("1. Baixe o dataset e coloque em data/raw/")
print("2. Crie o notebook notebooks/01_eda.ipynb")
print("3. Faca o primeiro commit:")
print("   git add .")
print('   git commit -m "feat: estrutura inicial do projeto"')
print("   git push origin main")
