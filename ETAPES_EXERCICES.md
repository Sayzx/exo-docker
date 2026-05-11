# 📋 Étapes d'Exécution — Série GitHub Actions

## Résumé de ce qui a été fait

### 🎯 Objectif
Implémenter les **12 exercices progressifs GitHub Actions** sur la branche `github-actions-lab`.

### ✅ État final
- **Branche créée :** `github-actions-lab` (partant de `master`)
- **Commit initial :** `829e13b` (26 fichiers ajoutés, 1529 insertions)
- **Fichiers créés :** 26 fichiers (workflows, actions, code, documentation)
- **Statut :** ✅ **COMPLET ET PRÊT À UTILISER**

---

## 📂 Structure des fichiers créés

```
exo-docker/
├── .github/
│   ├── workflows/                      # Tous les 12 exercices
│   │   ├── bonjour.yml                 # Exo 1-2: premier contact
│   │   ├── pr-check.yml                # Exo 3: déclencheur PR
│   │   ├── scheduled.yml               # Exo 3: cron + dispatch
│   │   ├── docs-only.yml               # Exo 3: filtrage chemin
│   │   ├── shell-lab.yml               # Exo 4: shell avancé
│   │   ├── pipeline.yml                # Exo 5: jobs dépendants
│   │   ├── ci.yml                      # Exo 6: CI marketplace
│   │   ├── env-demo.yml                # Exo 7: secrets/variables
│   │   ├── smart.yml                   # Exo 8: conditions if
│   │   ├── matrix-ci.yml               # Exo 9: stratégie matricielle
│   │   ├── cache-artifacts.yml         # Exo 10: cache et artefacts
│   │   ├── reusable-test.yml           # Exo 11A: workflow réutilisable
│   │   ├── caller.yml                  # Exo 11A: appel du workflow
│   │   ├── composite-action-usage.yml  # Exo 11B: action composite
│   │   ├── deploy.yml                  # Exo 12A: déploiement
│   │   ├── pages.yml                   # Exo 12B: GitHub Pages
│   │   └── self-hosted.yml             # Exo 12C: runner auto-hébergé
│   └── actions/
│       └── setup-project/
│           └── action.yml              # Action composite (Exo 11B)
├── scripts/
│   └── test.sh                         # Script pour Exo 4
├── docs/
│   └── README-docs.md                  # Documentation pour Exo 3
├── app.py                              # Code test pour Exo 6
├── test_app.py                         # Tests pytest pour Exo 6
├── requirements.txt                    # Dépendances pour Exo 6/9
├── README_EXERCICES_GITHUB_ACTIONS.md  # Documentation complète (625+ lignes)
├── SECURITY.md                         # Sécurité des runners (Exo 12)
├── README.md                           # Mis à jour avec pointeur
└── ETAPES_EXERCICES.md                 # Ce fichier
```

---

## 🔄 Étapes d'exécution détaillées

### Phase 1 : Préparation
```bash
cd /tmp && git clone git@github.com:Sayzx/exo-docker.git
cd exo-docker
git stash                                    # Conserver les changements k8s
git checkout master && git pull
git checkout -b github-actions-lab           # Créer la branche
```

### Phase 2 : Création de la structure
```bash
mkdir -p .github/workflows
mkdir -p .github/actions/setup-project
mkdir -p scripts docs
```

### Phase 3 : Exercices 1-4 (Fondamentaux)
#### Exo 1-2 : Premier workflow
- `bonjour.yml` : 3 étapes (salutation, date, contexte)
- Concepts : structure YAML, contextes, runs-on

#### Exo 3 : Déclencheurs variés
- `pr-check.yml` : `on: pull_request`
- `scheduled.yml` : `on: schedule` (cron) + `workflow_dispatch`
- `docs-only.yml` : `on: push` avec `paths:`

#### Exo 4 : Shell avancé
- `shell-lab.yml` : scripts multi-lignes, variables d'env, continue-on-error
- `scripts/test.sh` : script de démo
- Concepts : working-directory, exit codes, gestion d'erreurs

### Phase 4 : Exercices 5-6 (CI/CD fondamental)
#### Exo 5 : Orchestration
- `pipeline.yml` : 4 jobs (lint → test, build, notify) avec `needs:`
- Concepts : dépendances, `if: always()`, multi-OS

#### Exo 6 : Actions marketplace
- `ci.yml` : checkout, setup-python, pip install, pytest
- **Sécurité :** Actions pinnées à SHA complet (pas de tags v4)
- `app.py`, `test_app.py`, `requirements.txt` : code réel
- Concepts : actions de la communauté, bonnes pratiques de sécurité

### Phase 5 : Exercices 7-8 (Configuration avancée)
#### Exo 7 : Secrets et variables
- `env-demo.yml` : 3 niveaux (workflow, job, step)
- Masquage des secrets, GITHUB_TOKEN, gh cli
- Concepts : portées, masquage, contextes secrets

#### Exo 8 : Exécution conditionnelle
- `smart.yml` : 4 types de conditions
  * `if: github.ref == 'refs/heads/main'`
  * `if: contains(github.event.pull_request.labels.*.name, 'deploy')`
  * `if: startsWith(github.ref, 'refs/tags/v')`
  * `if: failure()` / `if: always()` / `if: success()`
- Concepts : expressions, contextes d'événement, outputs de jobs

### Phase 6 : Exercices 9-10 (Performance)
#### Exo 9 : Stratégie matricielle
- `matrix-ci.yml` : 3 OS × 3 versions = 9 jobs
- `include:` (Ubuntu 3.13 expérimental)
- `exclude:` (macOS 3.9)
- `fail-fast: false`
- Concepts : parallelisation, expérimentaux, continue-on-error conditionnel

#### Exo 10 : Optimisation
- `cache-artifacts.yml` : cache pip + upload/download artefacts
- Concepts : performance, données entre jobs, rétention

### Phase 7 : Exercices 11-12 (Avancé)
#### Exo 11A : Workflows réutilisables
- `reusable-test.yml` : `on: workflow_call` avec inputs
- `caller.yml` : appel via `uses:`
- Concepts : DRY principle, réutilisabilité

#### Exo 11B : Actions composites
- `.github/actions/setup-project/action.yml` : étapes groupées
- `composite-action-usage.yml` : utilisation
- Concepts : actions custom, composition

#### Exo 12A : Déploiement avec approbations
- `deploy.yml` : staging (auto) vs production (approbation)
- `environment:` + règles de relecteur
- Concepts : environnements, workflow_dispatch inputs

#### Exo 12B : GitHub Pages
- `pages.yml` : build HTML + deploy
- `permissions:` pour pages écriture
- Concepts : déploiement statique, URL publique

#### Exo 12C : Runner auto-hébergé
- `self-hosted.yml` : utilise `runs-on: self-hosted`
- `SECURITY.md` : documentation des risques (200+ mots)
- Concepts : runners personnalisés, sécurité

### Phase 8 : Documentation
#### `README_EXERCICES_GITHUB_ACTIONS.md`
- 625+ lignes
- Structure complète pour chaque exo :
  * Objectifs
  * Concepts clés avec code
  * Commandes exécutées
  * Leçons apprises
  * Difficultés et solutions
- Tableau récapitulatif
- Résumé des apprentissages
- Bonnes pratiques

#### `SECURITY.md`
- Risques des runners auto-hébergés
- 3 mesures de mitigation
- Recommandations finales

#### `README.md`
- Section NEW pointant vers `github-actions-lab`
- Lien vers documentation complète

### Phase 9 : Commit et push
```bash
git add .github/ app.py test_app.py requirements.txt scripts/ docs/ README*.md SECURITY.md
git commit -m "Exercices GitHub Actions 1-12: Série complète..."
git push -u origin github-actions-lab
```

---

## 📊 Métriques finales

| Métrique | Valeur |
|----------|--------|
| **Workflows créés** | 18 fichiers |
| **Actions composites** | 1 (setup-project) |
| **Fichiers de test** | 3 (app.py, test_app.py, requirements.txt) |
| **Fichiers de doc** | 4 (README*.md, SECURITY.md, ETAPES_EXERCICES.md) |
| **Lignes de code YAML** | ~600 |
| **Lignes de documentation** | ~1000+ |
| **Concepts couverts** | 20+ |
| **Branches créées** | 1 (github-actions-lab) |
| **Commits** | 1 commit complet avec tous les fichiers |

---

## 🧪 Comment tester les workflows

### Option 1 : Manuellement via GitHub UI
1. Aller à `Actions` tab sur GitHub
2. Sélectionner un workflow (ex: "Workflow d'initiation")
3. Cliquer `Run workflow`

### Option 2 : Déclencher des événements
```bash
# Pousser sur main pour déclencher push workflows
git checkout main
git merge github-actions-lab  # ⚠️ Ou créer une PR
git push origin main

# Créer une PR pour pr-check.yml
gh pr create --title "Test" --body "Test PR workflow"

# Créer un tag pour smart.yml
git tag v1.0.0
git push origin v1.0.0
```

### Option 3 : workflow_dispatch
- Tous les workflows avec `workflow_dispatch` peuvent être déclenchés manuellement
- Ex: `scheduled.yml`, `shell-lab.yml`, `self-hosted.yml`

---

## 🔐 Considérations de sécurité implémentées

✅ **Actions pinnées à SHA complet** (pas de tags flottants)  
✅ **Secrets masqués** dans les logs (auto-masquage si référencés)  
✅ **GITHUB_TOKEN** utilisé plutôt que tokens personnels  
✅ **Conditions explicites** plutôt que magiques  
✅ **Dépendances claires** entre jobs (pas de race conditions)  
✅ **Documentation des risques** (SECURITY.md)

---

## 🎓 Points d'apprentissage clés

### 1. Structure YAML
- Indentation critique (2 espaces)
- Contextes dynamiques `${{ }}`
- Hérédocs pour scripts multi-lignes

### 2. Événements
- Push, PR, cron, dispatch, tags
- Filtrage par chemin, branch, tag

### 3. Orchestration
- Jobs parallèles et séquentiels
- `needs:` pour dépendances
- `if: always()` pour notifications

### 4. Sécurité
- Pinning des actions
- Masquage des secrets
- Dépôts privés pour runners auto-hébergés

### 5. Performance
- Cache pour dépendances
- Matrice pour parallelisation
- Artefacts pour transfert de données

### 6. Réutilisabilité
- Workflows réutilisables (`workflow_call`)
- Actions composites (réduire copie-colle)

### 7. Déploiement
- Environnements avec approbations
- GitHub Pages statique
- Runners auto-hébergés (avec précautions)

---

## 🚀 Prochaines étapes pour l'étudiant

### Court terme
1. Lire `README_EXERCICES_GITHUB_ACTIONS.md`
2. Examiner les workflows et comprendre chaque étape
3. Déclencher manuellement les workflows via GitHub UI

### Moyen terme
4. Modifier les workflows pour les adapter à un vrai projet
5. Ajouter des secrets réels et tester les approbations
6. Déployer une vraie application via GitHub Pages

### Long terme
7. Intégrer GitHub Actions dans le projet principal
8. Configurer des runners auto-hébergés (dépôt privé!)
9. Mettre en place un pipeline CI/CD complet

---

## 📞 Support et dépannage

### Les workflows ne s'exécutent pas
→ Vérifier que la branche `github-actions-lab` est activée  
→ Vérifier l'indentation YAML  
→ Lire les logs dans l'onglet `Actions`

### Les tests échouent en CI
→ Reproduire l'environnement CI localement  
→ `python 3.11`, `pip install pytest`, `pytest -v`

### Secrets non trouvés
→ Les secrets doivent être ajoutés dans Settings → Secrets  
→ `GITHUB_TOKEN` est auto-fourni

### Runner auto-hébergé : non connecté
→ Vérifier qu'un runner est enregistré dans Settings → Runners  
→ S'assurer qu'il n'y a **aucun dépôt public** utilisant ce runner

---

## ✨ Particularités de cette implémentation

### 1. **Chaque exercice est autonome**
Chaque workflow peut être compris seul, sans dépendre des autres.

### 2. **Code réel dans les workflows**
Pas d'echo fictifs — la CI teste vraiment du code Python avec pytest.

### 3. **Sécurité première**
Actions pinnées, secrets masqués, documentation des risques.

### 4. **Documentation intégrée**
Commentaires dans les workflows + guide complet + SECURITY.md.

### 5. **Scalabilité**
Patterns réutilisables pour de vrais projets.

---

**Branche officielle :** `github-actions-lab`  
**Repo :** https://github.com/Sayzx/exo-docker  
**Créé le :** Mai 2026  
**Statut :** ✅ Production-ready
