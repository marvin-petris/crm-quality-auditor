# CRM Quality Auditor

Outil d'audit qualité pour bases de données CRM : détecte automatiquement les anomalies dans un export CSV (âges, emails, téléphones invalides) et génère un rapport clair, accompagné d'une synthèse en langage naturel.

Projet personnel réalisé pour apprendre Python à travers la construction d'un outil réel, dans une logique d'audit qualité de données CRM.

Le raisonnement derrière les principaux choix techniques est documenté dans [DECISIONS.md](./DECISIONS.md).

## Ce que fait l'outil

1. Lit un fichier CSV de clients (`nom`, `email`, `age`, `telephone`)
2. Applique des règles de validation déterministes sur chaque champ :
   - **Email** : doit contenir un `@`
   - **Âge** : doit être un nombre entre 1 et 120
   - **Téléphone** : doit faire exactement 10 caractères et commencer par `0`
3. Génère un rapport détaillé (`rapport.md`) listant les clients concernés et le détail de leurs anomalies
4. Envoie ce rapport à l'API Claude (Anthropic) pour produire une synthèse en langage naturel, destinée à un lecteur non technique

## Prérequis

- Python 3.10+
- Une clé API Anthropic ([console.anthropic.com](https://console.anthropic.com))

## Installation

```bash
git clone https://github.com/marvin-petris/crm-quality-auditor
cd crm-quality-auditor
pip install python-dotenv anthropic
```

## Configuration

Crée un fichier `.env` à la racine du projet, contenant :

```
ANTHROPIC_API_KEY=ta_cle_api_ici
```

Ce fichier ne doit **jamais** être partagé ni committé — il est déjà exclu via `.gitignore`.

## Utilisation

Place ton fichier de clients au format CSV (colonnes `nom,email,age,telephone`) à la racine du projet, sous le nom `clients.csv`. Un exemple de fichier de test est fourni : `clients.csv`.

Lance l'audit :

```bash
python audit.py
```

Le script affiche le détail des anomalies dans le terminal, génère `rapport.md`, puis affiche une synthèse générée par l'API Claude.

## Exemple de sortie

```
Durand -> anomalies : age
Martin -> anomalies : email
...
un total de 20 clients ayant au moins une anomalie, voir fichier rapport.md pour plus de détails

# Synthèse de l'audit qualité CRM
L'audit qualité de notre base CRM a identifié 20 clients présentant des données
invalides, ce qui représente un risque pour la fiabilité de nos communications...
```

## Structure du projet

```
crm-quality-auditor/
├── audit.py          # Script principal
├── clients.csv        # Données de test (synthétiques)
├── rapport.md          # Rapport généré (recréé à chaque exécution)
├── DECISIONS.md        # Journal des décisions techniques
├── .env                # Clé API (non versionné)
├── .venv/              # Environnement virtuel Python (non versionné)
├── .gitignore
└── README.md
```

## Limites connues (v1)

- Règles de validation simplifiées (pas de vérification de format d'email par expression régulière, pas de validation de plage de téléphone selon l'indicatif pays)
- Le rapport est écrasé à chaque exécution (pas d'historique)
- Aucun test automatisé pour l'instant

## Feuille de route

- Renforcement des règles de validation (regex email, format téléphone international)
- Historisation des rapports
- Anonymisation systématique des données personnelles envoyées au LLM
- Interface ou export enrichi (CSV des anomalies, rapport PDF)
