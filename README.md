# csv-cleaner

Petit outil Python en ligne de commande pour nettoyer des fichiers CSV.
Projet du **Mois 1** de ma reconversion Data Analyst → AI Engineer (objectif : un projet
Python **propre** — structure, tests, packaging).

## Structure

```
csv-cleaner/
├── src/csv_cleaner/      # le code du package
│   ├── __init__.py
│   └── cleaner.py        # fonctions de nettoyage
├── tests/                # tests pytest
│   └── test_cleaner.py
├── requirements.txt      # dépendances
├── .gitignore
└── README.md
```

## Installation

```bash
# 1. Créer un environnement virtuel
python3 -m venv .venv

# 2. L'activer (macOS / Linux)
source .venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

## Lancer les tests

```bash
# Depuis la racine du projet, l'environnement activé :
PYTHONPATH=src pytest
```

## Utilisation

_(À compléter au fil du mois, quand tu ajoutes des fonctions et une interface
en ligne de commande.)_

## Ce que j'ai appris

 Semaine 1 : j'ai appris à structurer un projet Python et à publier sur GitHub.


