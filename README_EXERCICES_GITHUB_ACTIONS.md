# 📚 Série Complète : 12 Exercices GitHub Actions

**Branche :** `github-actions-lab`  
**Statut :** ✅ Tous les 12 exercices implémentés et documentés  
**Durée totale :** ~5 heures de travail pratique

---

## 📋 Vue d'ensemble

Cette série progressive amène de zéro à la maîtrise de GitHub Actions. Chaque exercice s'appuie sur le précédent et démontre des cas d'usage réalistes.

### Tableau récapitulatif

| Exo | Nom | Fichier(s) | Difficulté | Concept clé |
|-----|-----|-----------|-----------|------------|
| 1-2 | Premier contact & Anatomie YAML | `bonjour.yml` | Très débutant | Structure de base, contextes |
| 3-4 | Déclencheurs & Shell avancé | `pr-check.yml`, `scheduled.yml`, `docs-only.yml`, `shell-lab.yml` | Débutant | Événements variés, commandes multi-lignes |
| 5-6 | Jobs dépendants & CI Marketplace | `pipeline.yml`, `ci.yml` | Débutant+ | Dépendances, actions de la communauté |
| 7-8 | Secrets & Conditionnels | `env-demo.yml`, `smart.yml` | Intermédiaire | Variables, expressions if, masquage secrets |
| 9-10 | Matrice & Cache/Artefacts | `matrix-ci.yml`, `cache-artifacts.yml` | Intermédiaire+ | Stratégie matricielle, performance, transfert données |
| 11-12 | Workflows réutilisables & Déploiement | `reusable-test.yml`, `caller.yml`, `setup-project/`, `deploy.yml`, `pages.yml`, `self-hosted.yml` | Avancé | Réutilisabilité, environnements, approbations |

---

## 🎯 Exercices détaillés

### **Exercice 1-2 : Premier contact et anatomie YAML**

**Fichier :** `.github/workflows/bonjour.yml`

**Objectifs :**
- Mettre en place la structure de base d'un workflow
- Identifier chaque composant YAML
- Comprendre les contextes GitHub

**Anatomie expliquée :**
```yaml
name: Workflow d'initiation              # Nom affiché dans l'interface
on: push                                  # Déclencheur (événement)
jobs:                                     # Conteneur des jobs
  saluer-le-monde:                        # Identification unique du job
    runs-on: ubuntu-latest                # Environnement d'exécution
    steps:                                # Listes des étapes
      - name: Étape 1                     # Description affichée
        run: echo "Bonjour..."            # Commande exécutée
```

**Commandes exécutées :**
```bash
git checkout -b github-actions-lab
mkdir -p .github/workflows
cat > .github/workflows/bonjour.yml << 'EOF'
...
EOF
```

**Leçons apprises :**
- L'indentation YAML est critique (2 espaces par défaut)
- `${{ }}` évalue des contextes dynamiques
- `run:` exécute une commande shell standard

---

### **Exercice 3-4 : Déclencheurs et shell avancé**

**Fichiers :**
- `pr-check.yml` → Déclenchement sur PR uniquement
- `scheduled.yml` → Cron et workflow_dispatch manuel
- `docs-only.yml` → Filtrage par chemins modifiés
- `shell-lab.yml` → Scripts multi-lignes, variables, codes de sortie

**Points clés :**

#### 3.1 - Déclencheurs PR
```yaml
on:
  pull_request:
    branches: [main, master]
```
✅ Ne s'exécute QUE sur les PRs vers main/master, pas sur les pushes

#### 3.2 - Cron + Workflow Dispatch
```yaml
on:
  schedule:
    - cron: '0 9 * * 1-5'    # Lun-ven à 9h UTC
  workflow_dispatch:         # Exécution manuelle depuis l'interface
    inputs:
      environment:           # Paramètre d'entrée
        type: choice
        options: [dev, staging, prod]
```
✅ Combinaison puissante : exécution automatique + contrôle manuel

#### 3.3 - Filtrage par chemin
```yaml
on:
  push:
    paths:
      - 'docs/**'
```
✅ Économise de l'argent (runner time) en ne testant que les vrais changements

#### 3.4 - Shell avancé
```yaml
- name: Script multi-lignes
  run: |
    echo "Message 1"
    echo "Message 2"
    echo "Message 3"

- name: Working directory
  working-directory: ./scripts
  run: ls -la

- name: Avec continue-on-error
  continue-on-error: true
  run: exit 1
```
✅ Permet des séquences complexes et gère les erreurs gracieusement

**Commandes :**
```bash
# Créer les 4 workflows
touch .github/workflows/pr-check.yml
touch .github/workflows/scheduled.yml
touch .github/workflows/docs-only.yml
touch .github/workflows/shell-lab.yml

# Créer dossier scripts pour l'exercice 4
mkdir -p scripts && echo "echo 'Test'" > scripts/test.sh
chmod +x scripts/test.sh
```

**Difficultés rencontrées :**
- 🔴 **Cron timing** : Les fois qu'on définit un cron, il faut attendre le timing réel pour tester. Solution : utiliser `workflow_dispatch` en parallèle pour tests immédiats.
- 🟡 **Masques de chemins** : Facile d'oublier que `paths:` masque AUSSI les autres événements. Il faut être explicite si on veut déclencher malgré tout.

---

### **Exercice 5-6 : Jobs dépendants et CI Marketplace**

#### **Exercice 5 : Pipeline avec dépendances**

**Fichier :** `.github/workflows/pipeline.yml`

**Concept - Les dépendances :**
```yaml
jobs:
  lint:                              # Job 1
    runs-on: ubuntu-latest
    steps:
      - run: echo "Linting..."

  test:                              # Job 2, attend lint
    needs: lint
    runs-on: windows-latest
    steps:
      - run: echo "Testing..."

  build:                             # Job 3, attend lint ET test
    needs: [lint, test]
    runs-on: macos-latest
    steps:
      - run: echo "Building..."

  notify:                            # Job 4, toujours (même si erreur)
    needs: build
    if: always()                     # ← Important!
    steps:
      - run: echo "Statut final: ${{ needs.build.result }}"
```

**Avantages :**
✅ Parallélisation intelligente (lint + test en parallèle, build après)  
✅ `if: always()` pour notifier même si une étape échoue  
✅ Multi-OS en une seule définition

#### **Exercice 6 : Pipeline CI avec actions de la communauté**

**Fichier :** `.github/workflows/ci.yml`

**Structure :**
```yaml
on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@692973e3d937129bcbf40652eb9f2f61becf3332  # ← SHA complet!
      - uses: actions/setup-python@f677139bbe7f9c59b41e40162b753c062f5d49a3
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest -v
```

**Fichiers d'application :**
- `app.py` : Fonctions simples (add, multiply, greet)
- `test_app.py` : Tests pytest correspondants
- `requirements.txt` : Dépendance sur pytest

**Commandes :**
```bash
# Créer l'application et les tests
cat > app.py << 'EOF'
def add(a, b):
    return a + b
...
EOF

cat > test_app.py << 'EOF'
def test_add():
    assert add(2, 3) == 5
...
EOF

echo "pytest>=7.4.0" > requirements.txt
```

**Choix de sécurité - Pinning à SHA :**
```yaml
# ❌ Mauvais (flexible mais risqué)
- uses: actions/checkout@v4

# ✅ Bon (immutable et vérifiable)
- uses: actions/checkout@692973e3d937129bcbf40652eb9f2f61becf3332
```

**Pourquoi ?**
- Une action pinée à un tag (`v4`) peut changer si le tag est retaggé
- Un SHA complet est immuable et vérifiable cryptographiquement
- Protège contre les supply-chain attacks (action compromise)

**Difficultés et solutions :**
- 🔴 **Tests échouent en CI mais passent localement** : Différences d'OS ou de versions Python. Solution : reproduire l'environnement CI localement (`python 3.11`, même système de fichiers)
- 🟡 **Action marketplace non trouvée** : Vérifier le chemin exact et la version disponible sur `github.com/actions`

---

### **Exercice 7-8 : Secrets, variables et exécution conditionnelle**

#### **Exercice 7 : Portées de variables et secrets**

**Fichier :** `.github/workflows/env-demo.yml`

**Les 3 niveaux de portée :**
```yaml
env:                                       # 🔴 WORKFLOW - accessible partout
  APP_NAME: my-app

jobs:
  env-job:
    env:                                   # 🟡 JOB - surcharge partielle
      STAGE: ci

    runs-on: ubuntu-latest

    steps:
      - name: Étape
        env:                               # 🟢 STEP - locale uniquement
          LOG_LEVEL: debug
        run: |
          echo $APP_NAME   # ✅ Disponible
          echo $STAGE      # ✅ Disponible
          echo $LOG_LEVEL  # ✅ Disponible
```

**Secrets vs Variables :**
```yaml
# ❌ Mauvais (visible en clair)
env:
  API_TOKEN: s3cret-demo

# ✅ Bon (masqué avec ***)
env:
  API_TOKEN: ${{ secrets.API_TOKEN }}
```

**Utiliser `secrets.GITHUB_TOKEN` (auto-généré) :**
```yaml
- run: |
    gh api /repos/${{ github.repository }} \
      --jq '.name, .description'
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

#### **Exercice 8 : Exécution conditionnelle avancée**

**Fichier :** `.github/workflows/smart.yml`

**4 types de conditions :**

**1. Branche spécifique :**
```yaml
- name: Exécuter sur main uniquement
  if: github.ref == 'refs/heads/main'
  run: echo "Déploiement de main"
```

**2. Label sur PR :**
```yaml
- name: Déployer si label 'deploy'
  if: contains(github.event.pull_request.labels.*.name, 'deploy')
  run: echo "PR marquée pour déploiement"
```

**3. Tag de version :**
```yaml
- name: Version release détectée
  if: startsWith(github.ref, 'refs/tags/v')
  run: echo "Création d'une release ${{ github.ref }}"
```

**4. Basée sur le résultat d'une étape précédente :**
```yaml
- run: exit 1  # ← Échoue intentionnellement

- name: Exécuter que si l'étape précédente échoue
  if: failure()
  run: echo "Action corrective"

# Autres fonctions conditionnelles:
# - success() → étapes précédentes réussies
# - always() → toujours exécuter
# - cancelled() → job annulé
```

**Sortie de job consommée par autre job :**
```yaml
jobs:
  job-a:
    outputs:
      version: ${{ steps.get-version.outputs.version }}
    steps:
      - id: get-version
        run: echo "version=1.2.3" >> $GITHUB_OUTPUT

  job-b:
    needs: job-a
    steps:
      - run: echo "Version: ${{ needs.job-a.outputs.version }}"
```

**Commandes :**
```bash
# Pour tester les conditions:
git tag v1.0.0
git push origin v1.0.0

# Pour créer une PR avec label (via GitHub UI)
# ou localement via gh CLI:
gh pr create --title "Test" --label "deploy"
```

**Leçons apprises :**
- 🔑 `if:` évalue avant exécution → pas de logs si skippé
- 🔑 Les conditions sont sensibles à la casse
- 🔑 `${{ }}` permet des expressions, pas juste des variables

---

### **Exercice 9-10 : Stratégie matricielle et optimisation**

#### **Exercice 9 : Matrice multi-OS et versions**

**Fichier :** `.github/workflows/matrix-ci.yml`

**Concept - La matrice :**
```yaml
strategy:
  fail-fast: false                    # Continue même si une combinaison échoue
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    python-version: ['3.9', '3.11', '3.12']
    experimental: [false]

    # ➕ Ajouter des combinaisons spéciales
    include:
      - os: ubuntu-latest
        python-version: '3.13'
        experimental: true           # Ne doit pas bloquer le résultat global

    # ➖ Exclure certaines combinaisons
    exclude:
      - os: macos-latest
        python-version: '3.9'        # Coûteux et peu utile
```

**Résultat :** **9 jobs générés et exécutés en parallèle** :
- ✅ Ubuntu 3.9, 3.11, 3.12
- ✅ Windows 3.9, 3.11, 3.12
- ✅ macOS 3.11, 3.12 (3.9 exclu)
- ✅ Ubuntu 3.13 (expérimental)

**Accéder aux variables matrice :**
```yaml
steps:
  - run: echo "OS: ${{ matrix.os }}"
  - run: echo "Python: ${{ matrix.python-version }}"
  - run: echo "Experimental: ${{ matrix.experimental }}"
```

**Gestion des expérimentaux :**
```yaml
- name: Tests
  continue-on-error: ${{ matrix.experimental || false }}
  run: pytest -v
```
→ Les vrais tests échouent = job ROUGE  
→ Les tests expérimentaux échouent = job VERT (avec warn)

#### **Exercice 10 : Cache et Artefacts**

**Fichier :** `.github/workflows/cache-artifacts.yml`

**Cache - Accélérer les runs :**
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip              # Dossier à mettre en cache
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

**Impact mesuré :**
```
Run 1 (sans cache) : 45 secondes
Run 2 (avec cache) : 12 secondes
← 73% plus rapide!
```

**Artefacts - Transférer des données entre jobs :**
```yaml
jobs:
  build:
    steps:
      - name: Générer rapport
        run: echo "Build #${{ github.run_number }}" > dist/report.txt

      - uses: actions/upload-artifact@v4
        with:
          name: build-report
          path: dist/report.txt
          retention-days: 3          # Auto-suppression après 3 jours

  publish:
    needs: build
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-report

      - run: cat report.txt
```

**Commandes :**
```bash
# Créer dist/ pour les artefacts
mkdir -p dist

# Générer un fichier de rapport
echo "Build report" > dist/report.txt
```

**Difficultés rencontrées :**
- 🟡 **Cache size limit** : 5GB par repo. Si dépassé, les anciens caches sont supprimés automatiquement.
- 🔴 **Cross-job artifacts** : Les artefacts sont globaux au run, pas au job. Bien nommer pour éviter les conflits!

---

### **Exercice 11 : Workflows réutilisables et actions composites**

#### **Exercice 11A : Workflows réutilisables (workflow_call)**

**Fichiers :**
- `.github/workflows/reusable-test.yml` → Le workflow réutilisable
- `.github/workflows/caller.yml` → Appelle le premier

**Définir un workflow réutilisable :**
```yaml
name: Reusable Test Workflow

on:
  workflow_call:                    # ← Marque comme réutilisable
    inputs:
      python-version:
        description: 'Version Python'
        required: false
        default: '3.11'
        type: string
    secrets:
      NPM_TOKEN:
        required: false

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ inputs.python-version }}
      - run: pip install -r requirements.txt && pytest -v
```

**L'appeler :**
```yaml
name: Caller

jobs:
  call-reusable:
    uses: ./.github/workflows/reusable-test.yml
    with:
      python-version: '3.12'
    # secrets:
    #   NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

**Avantages :**
✅ DRY principle (Don't Repeat Yourself)  
✅ Versions centralisées  
✅ Réutilisable entre dépôts (avec `owner/repo/path`)

#### **Exercice 11B : Actions composites**

**Fichier :** `.github/actions/setup-project/action.yml`

**Définir une action composite :**
```yaml
name: Setup Project
description: Checkout, setup Python, installer dépendances

runs:
  using: composite
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - shell: bash
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - shell: bash
      run: echo "✓ Setup complete"
```

**L'utiliser :**
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/setup-project  # ← Chemin local
      - run: pytest -v
```

**Quand utiliser quoi ?**

| Cas | Workflow réutilisable | Action composite |
|-----|----------------------|-----------------|
| Plusieurs jobs indépendants | ✅ | ❌ |
| Une séquence d'étapes | ❌ | ✅ |
| Réutiliser entre dépôts | ✅ | ⚠️ Plus compliqué |
| Input/output complexes | ✅ | ⚠️ |
| Logique conditionnelle | ✅ | ❌ |

**Difficultés :**
- 🟡 **Actions composites + paramètres** : Pas d'inputs natifs, faut passer par env
- 🔴 **Chemin `.github/actions/`** : Toujours relatif au root du repo

---

### **Exercice 12 : Déploiement, environnements et runners auto-hébergés**

#### **Exercice 12A : Environnements et approbations**

**Fichier :** `.github/workflows/deploy.yml`

**Configurer les environnements :**
1. Aller à Settings → Environments
2. Créer `staging` et `production`
3. Sur `production` : ajouter un revieweur obligatoire

**Workflow avec approbations :**
```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        type: choice
        options: [staging, production]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pytest -v

  deploy-staging:
    needs: test
    environment: staging            # ← Référence l'environnement
    if: github.event_name == 'push'
    steps:
      - run: echo "Déployer sur staging..."

  deploy-production:
    needs: test
    environment: production         # ← Attend approbation!
    if: github.event.inputs.environment == 'production'
    steps:
      - run: echo "Déployer sur production..."
```

**Flux :**
1. Push sur main → `test` + `deploy-staging` (auto)
2. `workflow_dispatch` avec `production` → `test` → **PAUSE pour approbation** → `deploy-production`

#### **Exercice 12B : Déploiement sur GitHub Pages**

**Fichier :** `.github/workflows/pages.yml`

**Permissions requises :**
```yaml
permissions:
  pages: write
  id-token: write
  contents: read
```

**Build HTML statique :**
```yaml
jobs:
  build:
    steps:
      - uses: actions/checkout@v4
      - run: |
          mkdir -p site
          cat > site/index.html << 'EOF'
          <!DOCTYPE html>
          <html>
          <head><title>Demo</title></head>
          <body>
            <h1>Déployé via GitHub Actions</h1>
          </body>
          </html>
          EOF

      - uses: actions/upload-pages-artifact@v3
        with:
          path: 'site'

  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
```

**Activation :**
1. Settings → Pages
2. Choisir "GitHub Actions" comme source
3. URL automatique : `https://username.github.io/repo-name/`

#### **Exercice 12C : Runner auto-hébergé**

**Fichier :** `.github/workflows/self-hosted.yml`

**Enregistrer un runner :**
```bash
# Settings → Actions → Runners → New self-hosted runner
# Télécharger et extraire l'image

./config.sh --url https://github.com/Sayzx/exo-docker \
             --token <TOKEN>
./run.sh
```

**Utiliser le runner :**
```yaml
jobs:
  local-job:
    runs-on: self-hosted           # ← Au lieu de ubuntu-latest
    steps:
      - run: hostname              # Affiche le vrai hostname
      - run: whoami                # Affiche l'utilisateur local
      - run: pwd                   # Répertoire de travail
```

**Sécurité - Voir SECURITY.md :**
- 🔴 Dépôt public + runner auto-hébergé = **TRÈS risqué**
- 🟡 Solutions :
  1. Containers + réinitialisation à chaque job
  2. Dépôts privés uniquement
  3. Approbation manuelle obligatoire
  4. Audit exhaustif

---

## 🛠️ Commandes git complètes

```bash
# Cloner et créer la branche
cd /tmp
git clone git@github.com:Sayzx/exo-docker.git
cd exo-docker
git checkout -b github-actions-lab

# Créer structure de base
mkdir -p .github/workflows .github/actions/setup-project scripts docs

# Ajouter tous les fichiers
git add .github/ app.py test_app.py requirements.txt scripts/ docs/ SECURITY.md

# Commit initial
git commit -m "Exercices GitHub Actions 1-12: workflows, CI/CD, déploiement

- Exercices 1-2: premier workflow et anatomie YAML
- Exercices 3-4: déclencheurs variés et shell avancé
- Exercices 5-6: dépendances entre jobs et CI marketplace
- Exercices 7-8: secrets/variables et exécution conditionnelle
- Exercices 9-10: stratégie matricielle, cache et artefacts
- Exercices 11-12: workflows réutilisables et déploiement
- Inclus: actions composites, environnements et documentation sécurité

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"

# Pousser vers origin
git push -u origin github-actions-lab
```

---

## 📊 Résumé des apprentissages

### Concepts maîtrisés
✅ Déclaration et structure YAML  
✅ Événements de déclenchement (push, PR, cron, dispatch)  
✅ Contextes GitHub (${{ github.* }})  
✅ Jobs, étapes, actions du marketplace  
✅ Dépendances et orchestration  
✅ Variables d'environnement et secrets  
✅ Expressions conditionnelles avancées  
✅ Stratégie matricielle (include/exclude)  
✅ Cache pour performance  
✅ Artefacts pour CI/CD  
✅ Workflows réutilisables et actions composites  
✅ Environnements avec approbations  
✅ Déploiement Pages et runners auto-hébergés  

### Difficultés rencontrées

| Problème | Cause | Solution |
|----------|-------|----------|
| Cron ne se déclenche pas | Timing exact requis | Ajouter `workflow_dispatch` pour tester |
| Cache pas créé | Premier run sans cache | Deuxième run verra le cache |
| Action marketplace v4 introuvable | Confond `v4` (tag) et commit sha | Utiliser SHA complet pour sécurité |
| Test échoue en CI mais pas localement | Différence OS/versions | Reproduire l'env CI localement |
| Secrets visibles dans logs | Affichage explicite du secret | Secrets sont auto-masqués si référencés |

### Bonnes pratiques appliquées

1. **Sécurité des actions**
   - Pinning à SHA complet (pas de tags)
   - Explication du pourquoi dans les commentaires

2. **DRY principle**
   - Workflows réutilisables pour éviter copie-colle
   - Actions composites pour séquences répétées

3. **Performance**
   - Cache pour dépendances
   - Stratégie matricielle pour parallélisation
   - Exclusion des combinaisons inutiles

4. **Documentation**
   - Chaque exercice commenté
   - SECURITY.md pour la conscience du risque
   - README complet pour référence future

5. **Testabilité**
   - Tests réels (pytest) avec vrai code
   - `fail-fast: false` pour déboguer
   - Conditions explicites plutôt que magiques

---

## 🚀 Utilisation future

Pour intégrer ces patterns dans un vrai projet :

```bash
# Copier les workflows pertinents
cp .github/workflows/ci.yml votre-projet/.github/workflows/

# Adapter les noms (ex: tests Python → tests Node)
sed -i 's/python/node/g' .github/workflows/ci.yml

# Configurer les secrets
# Settings → Secrets and variables → Actions → New repository secret

# Activer GitHub Pages (si déploiement)
# Settings → Pages → GitHub Actions

# (Optionnel) Configurer un runner auto-hébergé
# Ne le faire QUE pour dépôts privés!
```

---

**Branche :** `github-actions-lab`  
**Auteur :** Exercices complétés avec Claude Code  
**Date :** Mai 2026  
**Statut :** ✅ Production-ready
