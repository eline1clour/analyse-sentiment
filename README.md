# Analyse de sentiment sur des avis de fast-food

## Description
Ce  projet consiste à analyser la polarité d'avis clients issus de restaurants de fast-food.

L'objectif est de déterminer si l'opinion exprimée dans un avis est **positive**, **négative** ou **neutre**.

Deux approches sont implémentées : 
- **Approche naïve** : basée sur des règles simples et des dictionnaires.
- **Approche intelligente** : approche plus avancée pour améliorer la détection de la polarité.

Les performances des deux approches sont ensuite évaluées à l'aide de différentes métriques.

## Organisation du projet

```
Analyse-sentiment
    ├── approcheIntelligente
    │   ├── detect_polarite.py
    │   ├── eval_system.py
    │   └── read_corpus.py
    ├── approcheNaïve
    │   ├── detect_polarite.py
    │   ├── eval_system_polarite.py
    │   └── read_corpus.py
    ├── corpus
    │   ├── avis1.txt ... avis100.txt
    │   └── goldStandard.csv
    ├── README.md
    ├── requirements.txt
```
## Données utilisées

Le corpus est composé de **100 avis clients** collectés sur **Google Maps** pour les restaurants :
- **BURGER KING**
- **QUICK**

Chaque avis est annoté avec **une poalrité de référence** dans le fichier :
`corpus/goldStandard.csv`.
Ce fichier constitue le **gold standard**, utilisé pour évaluer les performances des systèmes de classification.

---

## Scripts principaux

### Approche naïve

| Script  | Description |
| --------|-------------|
| `detect_polarite.py` | Prédit la polarité (positif, négatif, neutre) pour chaque avis |
| `eval_system_polarite.py` | Évalue les performances du système |
Cette approche repose sur des **règles simples et des dictionnaires de mots positifs et négatifs**. 
Le dictionnaire a été construit **manuellement**, en prenant les mots qui correspondent le plus généralement à une opinion positive et négative.

### Approche intelligente

| Script  | Description |
| --------|-------------|
| `detect_polarite.py` | Prédit la polarité des avis avec TextBlob |
| `eval_system.py` | Évalue les performances du modèle |
Cette approche utilise la **bibliothèque TextBlob de TAL** pour améliorer la détection de sentiment.

---
## Installation

### Prérequis
- Python **3.10 ou supérieur**.

Installer les dépendances :

```
python -m pip install -r requirements.txt
```
---

## Exécution du projet

### Approche naïve

```bash
cd approcheNaïve
python -m detect_polarite
python - m eval_system_polarite
```

### Approche intelligente

```bash
cd approcheIntelligente
python -m detect_polarite
python -m eval_system
```
---

## Résultats de sortie

### Détection de polarité
Les scripts `detect_polarite.py` retournent la polarité prédite pour chaque avis du corpus.

**Exemple de sortie** : 
- Pour approche naive:

``
avis5: {'service': 'positif'},
avis6: {'service': 'neutre'},
avis7: {'service': 'positif'},
avis8: {'service': 'positif'},
avis9: {'service': 'négatif'}
``
- Pour approche intelligente:

``
avis5: positif,
avis6: positif,
avis7: positif,
avis8: positif,
avis9: négatif
``
- **positif** : opinion positive.
- **négatif** : opinion négative.
- **neutre** : opinion mitigée ou absence d'opinion claire.

---

## Évaluation du système
Les scripts d'évaluation calculent plusieurs métriques :
- **Matrice de confusion**
- **Accuracy**
- **Précision**
- **Rappel**
- **F1-score**
- **Macro-average**

Ces métriques permettent de mesurer la capacité du système à prédire correctement la polarité des avis.
Plus les valeurs sont proches de 1, meilleures sont les performances du modèle.

**Exemple de sortie :**
- Pour approche naive:


| ----     |precision | recall | f1-score | support |
|----------|----------|--------|----------|---------|
| positif  |0.73      | 0.84   |  0.78    |    44   |
|négatif   |    0.97  | 0.62   |  0.76    |    48   |
|neutre    |   0.28   | 0.62   |  0.38    |     8   |
|accuracy  |          |        | 0.72     |  100    |

- Pour approche intelligente :

| ----     | precision | recall | f1-score | support |
|----------|-----------|--------|----------|---------|
| positif  | 0.72      | 0.82   | 0.77     |    44   |
|négatif   | 1.00      | 0.29   | 0.45     |    48   |
|neutre    | 0.11      | 0.50   | 0.18     |     8   |
|accuracy  |           |        | 0.54     |  100    |

---

## Technologies utilisées
Python 3.12.3

## Auteurs
Projet académique réalisé en groupe.
- **Youmna Ahmed**
- **Saida Lounas**
	 
	   
	   



