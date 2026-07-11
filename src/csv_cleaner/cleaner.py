"""Fonctions de nettoyage de données CSV.

MOIS 1 — Semaine 1 : ce fichier contient UNE fonction d'exemple qui marche déjà
(pour que le test passe). Ton travail des semaines 2 à 4 : remplacer/enrichir ces
fonctions avec de vraies opérations de nettoyage que TU trouves utiles.

Idées de fonctions à coder toi-même au fil du mois :
- supprimer les lignes entièrement vides
- retirer les espaces en trop autour des valeurs
- normaliser les noms de colonnes (minuscules, sans accents, underscores)
- supprimer les doublons
- détecter les colonnes numériques mal typées
"""

from __future__ import annotations


def strip_whitespace(value: str) -> str:
    """Retire les espaces en début et fin d'une chaîne.

    Exemple :
        >>> strip_whitespace("  Nantes  ")
        'Nantes'
    """
    return value.strip()


def normalize_column_name(name: str) -> str:
    """Normalise un nom de colonne : minuscules, espaces -> underscores.

    Exemple :
        >>> normalize_column_name("  Nom Client ")
        'nom_client'
    """
    return name.strip().lower().replace(" ", "_")
