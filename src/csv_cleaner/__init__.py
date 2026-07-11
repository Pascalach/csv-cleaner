"""csv_cleaner — petit outil de nettoyage de fichiers CSV.

Projet du Mois 1 (feuille de route AI Engineer). But pédagogique : structurer un
projet Python proprement (modules, tests, packaging), pas la complexité.
"""

from csv_cleaner.cleaner import normalize_column_name, strip_whitespace

__all__ = ["strip_whitespace", "normalize_column_name"]
__version__ = "0.1.0"
