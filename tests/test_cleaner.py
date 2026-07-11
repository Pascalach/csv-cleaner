"""Tests du module cleaner.

Lance-les avec :  pytest
Chaque fonction de test vérifie UN comportement. Quand tu ajoutes une fonction
dans cleaner.py, ajoute son test ici (objectif du mois : au moins 3 tests qui passent).
"""

from csv_cleaner.cleaner import normalize_column_name, strip_whitespace


def test_strip_whitespace_retire_espaces():
    assert strip_whitespace("  Nantes  ") == "Nantes"


def test_normalize_column_name_minuscules_underscores():
    assert normalize_column_name("  Nom Client ") == "nom_client"


def test_normalize_column_name_deja_propre():
    assert normalize_column_name("age") == "age"
