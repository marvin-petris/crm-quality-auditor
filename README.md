# CRM Quality Auditor

Outil d'audit qualité pour bases de données CRM : détecte automatiquement les anomalies dans un export CSV (âges, emails, téléphones invalides) et génère un rapport clair, accompagné d'une synthèse en langage naturel.

Projet personnel réalisé pour apprendre Python à travers la construction d'un outil réel, dans une logique d'audit qualité de données CRM.

Le raisonnement derrière les principaux choix techniques est documenté dans [DECISIONS.md](./DECISIONS.md).

## Ce que fait l'outil

1. Lit un fichier CSV de clients (`ID`, `nom`, `email`, `age`, `telephone`)
2. Applique des règles de validation déterministes sur chaque champ :
   - **Email** : doit contenir un `@`, qui ne doit pas être en première position, suivi d'une partie contenant un `.`
   - **Âge** : doit être un nombre entre 1 et 120
   - **Téléphone** : doit faire exactement 10 caractères et commencer par `0`
3. Génère un rapport détaillé (`rapport.md`) listant les clients concernés par leur ID, avec le détail de leurs anomalies
4. Envoie uniquement les totaux (nombre de clients, nombre d'anomalies par champ) à l'API Claude (Anthropic) pour produire une synthèse en langage naturel, destinée à un lecteur non technique. Aucune donnée client (nom, email, téléphone, ID) n'est transmise au LLM.

## Prérequis

- Python 3.10+
- Une clé API Anthropic ([console.anthropic.com](https://console.anthropic.com))

## Installation

```bash
git clone https://github.com/marvin-petris/crm-quality-auditor
cd crm-quality-auditor
pip install -r requirements.txt
```

## Configuration

Crée un fichier `.env` à la racine du projet, contenant :

```
ANTHROPIC_API_KEY=ta_cle_api_ici
```

Ce fichier ne doit **jamais** être partagé ni committé. Il est déjà exclu via `.gitignore`.

## Utilisation

Place ton fichier de clients au format CSV (colonnes `ID,nom,email,age,telephone`) à la racine du projet, sous le nom `clients.csv`. Un fichier de test avec des données fictives est fourni.

Lance l'audit :

```bash
python audit.py
```

Le script affiche le détail des anomalies dans le terminal, génère `rapport.md`, puis affiche une synthèse générée par l'API Claude.

## Lancer les tests

Les règles de validation sont couvertes par des tests automatisés (`test_audit.py`). Depuis la racine du projet :

```bash
pytest
```

Les tests n'appellent pas l'API et ne lisent pas `clients.csv` : ils vérifient chaque règle isolément, sur des valeurs choisies pour couvrir les cas limites.

## Exemple de sortie

```
C001 -> anomalies : age
C002 -> anomalies : email
...
un total de 20 clients ayant au moins une anomalie, voir fichier rapport.md pour plus de détails

## Synthèse de l'audit qualité CRM
Sur les 31 clients analysés, 20 présentent au moins une anomalie, ce qui représente
près de 65% de la base...
```

## Structure du projet

```
crm-quality-auditor/
├── audit.py            # Script principal
├── test_audit.py       # Tests automatisés (pytest)
├── clients.csv         # Données de test (fictives)
├── rapport.md          # Rapport généré (recréé à chaque exécution, non versionné)
├── requirements.txt    # Dépendances Python
├── DECISIONS.md        # Journal des décisions techniques
├── .env                # Clé API (non versionné)
├── .venv/              # Environnement virtuel Python (non versionné)
├── .gitignore
└── README.md
```

## Limites connues (v1)

- **Téléphone** : seul le format français à 10 chiffres sans séparateur est accepté. Les numéros internationaux (`+33`, `+352`...) et les saisies avec espaces ou points sont signalés comme anomalies.
- **Email** : validation volontairement simple, sans expression régulière.
- Le fichier d'entrée doit contenir une colonne `ID` : l'outil ne génère pas d'identifiants, il lit ceux de l'export.
- Le rapport est écrasé à chaque exécution (pas d'historique).

## Feuille de route

- Validation téléphone internationale (indicatifs pays, normalisation des séparateurs)
- Validation email par expression régulière
- Nouvelle règle de qualité : ID manquant ou en double dans l'export
- Calcul des pourcentages par le code plutôt que par le LLM
- Historisation des rapports
- Export enrichi (CSV des anomalies, rapport PDF)
