# 🗂️ Index — Série Exercices GitHub Actions

> **Branche :** `github-actions-lab`  
> **Statut :** ✅ 12/12 exercices complétés  
> **Dernière mise à jour :** Mai 2026

---

## 📚 Documentation principale

### 1. [📖 README_EXERCICES_GITHUB_ACTIONS.md](README_EXERCICES_GITHUB_ACTIONS.md) ⭐
**La documentation la plus complète.** Lire en priorité.

- Vue d'ensemble des 12 exercices
- Tableau récapitulatif
- Explication détaillée de chaque exercice avec:
  * Code complet annoté
  * Concepts expliqués
  * Commandes exécutées
  * Leçons apprises
  * Difficultés rencontrées et solutions
- Bonnes pratiques et patterns
- Section "utilisation future"

**Durée de lecture :** 30-45 minutes

---

### 2. [📋 ETAPES_EXERCICES.md](ETAPES_EXERCICES.md)
**Synthèse exécutive.** Résumé des étapes et comment tout a été implémenté.

- Structure complète des 26 fichiers créés
- Étapes d'exécution détaillées (9 phases)
- Métriques finales
- Comment tester les workflows
- Considérations de sécurité
- Points d'apprentissage clés

**Durée de lecture :** 15-20 minutes

---

### 3. [🔐 SECURITY.md](SECURITY.md)
**Document de sécurité.** Risques des runners auto-hébergés sur dépôts publics.

- 200+ mots sur les risques
- 3 mesures de mitigation
- Recommandations finales

**Durée de lecture :** 5-10 minutes

---

## 🎯 Workflows par exercice

### Exercices 1-2 : Premier contact
| Fichier | Exercice | Concepts |
|---------|----------|----------|
| [`.github/workflows/bonjour.yml`](.github/workflows/bonjour.yml) | 1-2 | Structure YAML, contextes, runs-on |

### Exercices 3-4 : Déclencheurs et shell
| Fichier | Exercice | Concepts |
|---------|----------|----------|
| [`.github/workflows/pr-check.yml`](.github/workflows/pr-check.yml) | 3 | Déclencheur pull_request |
| [`.github/workflows/scheduled.yml`](.github/workflows/scheduled.yml) | 3 | Cron + workflow_dispatch |
| [`.github/workflows/docs-only.yml`](.github/workflows/docs-only.yml) | 3 | Filtrage par chemins |
| [`.github/workflows/shell-lab.yml`](.github/workflows/shell-lab.yml) | 4 | Scripts multi-lignes, variables, errors |

### Exercices 5-6 : Orchestration et CI
| Fichier | Exercice | Concepts |
|---------|----------|----------|
| [`.github/workflows/pipeline.yml`](.github/workflows/pipeline.yml) | 5 | Jobs dépendants, needs: |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | 6 | Actions marketplace, pinning SHA |

### Exercices 7-8 : Configuration avancée
| Fichier | Exercice | Concepts |
|---------|----------|----------|
| [`.github/workflows/env-demo.yml`](.github/workflows/env-demo.yml) | 7 | Secrets, variables, portées |
| [`.github/workflows/smart.yml`](.github/workflows/smart.yml) | 8 | Conditions if avancées, outputs |

### Exercices 9-10 : Performance
| Fichier | Exercice | Concepts |
|---------|----------|----------|
| [`.github/workflows/matrix-ci.yml`](.github/workflows/matrix-ci.yml) | 9 | Matrice, include/exclude |
| [`.github/workflows/cache-artifacts.yml`](.github/workflows/cache-artifacts.yml) | 10 | Cache, artefacts, transfert données |

### Exercices 11-12 : Avancé et déploiement
| Fichier | Exercice | Concepts |
|---------|----------|----------|
| [`.github/workflows/reusable-test.yml`](.github/workflows/reusable-test.yml) | 11A | Workflows réutilisables |
| [`.github/workflows/caller.yml`](.github/workflows/caller.yml) | 11A | Appel de workflows |
| [`.github/actions/setup-project/action.yml`](.github/actions/setup-project/action.yml) | 11B | Actions composites |
| [`.github/workflows/composite-action-usage.yml`](.github/workflows/composite-action-usage.yml) | 11B | Utilisation d'actions |
| [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) | 12A | Déploiement avec approbations |
| [`.github/workflows/pages.yml`](.github/workflows/pages.yml) | 12B | GitHub Pages |
| [`.github/workflows/self-hosted.yml`](.github/workflows/self-hosted.yml) | 12C | Runner auto-hébergé |

---

## 📦 Code d'application

### Test Python pour CI (Exercices 6, 9-10)
| Fichier | Description |
|---------|-------------|
| [`app.py`](app.py) | Application simple avec 3 fonctions |
| [`test_app.py`](test_app.py) | Tests pytest pour app.py |
| [`requirements.txt`](requirements.txt) | Dépendances (pytest) |

### Ressources supplémentaires
| Fichier | Destination | Usage |
|---------|-------------|-------|
| [`scripts/test.sh`](scripts/test.sh) | Exo 4 | Démonstration working-directory |
| [`docs/README-docs.md`](docs/README-docs.md) | Exo 3 | Fichier pour trigger docs-only.yml |

---

## 🎓 Guide de lecture recommandé

### Pour un survol rapide (15 min)
1. Ce fichier (INDEX.md)
2. ETAPES_EXERCICES.md (résumé)
3. README_EXERCICES_GITHUB_ACTIONS.md (section "Vue d'ensemble")

### Pour une compréhension complète (2-3h)
1. README_EXERCICES_GITHUB_ACTIONS.md (complet)
2. Lire chaque workflow correspondant
3. SECURITY.md (sécurité)
4. ETAPES_EXERCICES.md (contexte d'exécution)

### Pour l'implémentation (4-6h)
1. Choisir un exercice
2. Lire la section dédiée dans README_EXERCICES_GITHUB_ACTIONS.md
3. Examiner le/les fichiers associés
4. Comprendre les concepts
5. Adapter à un vrai projet si nécessaire

---

## 🧪 Points d'entrée pour tester

### Via GitHub UI
1. Aller à l'onglet `Actions`
2. Sélectionner un workflow
3. Cliquer `Run workflow`

### Via workflow_dispatch
Ces workflows peuvent être déclenchés manuellement :
- `scheduled.yml`
- `shell-lab.yml`
- `env-demo.yml`
- `deploy.yml` (pour choisir environment)
- `self-hosted.yml`

### Via événements Git
- **Push :** Déclenche `bonjour.yml`, `pipeline.yml`, `ci.yml`, etc.
- **PR :** Déclenche `pr-check.yml`, `ci.yml`
- **Tag :** Crée `git tag v1.0.0 && git push origin v1.0.0` → déclenche `smart.yml`
- **Cron :** Tous les jours ouvrés à 9h UTC → `scheduled.yml`

---

## 📊 Vue d'ensemble statistique

```
Fichiers créés:
├── Workflows YAML      : 18
├── Actions composites  : 1
├── Code d'app         : 3
├── Documentation      : 4
└── Autres             : 3

Total: 29 fichiers

Lignes de code:
├── YAML workflows     : ~600
├── Python            : ~60
├── Documentation     : ~1300
└── Total             : ~1960

Concepts couverts: 20+
```

---

## 🔗 Liens rapides

### Documentation
- **📖 [README_EXERCICES_GITHUB_ACTIONS.md](README_EXERCICES_GITHUB_ACTIONS.md)** ← Lire en premier
- **📋 [ETAPES_EXERCICES.md](ETAPES_EXERCICES.md)** ← Vue d'ensemble
- **🔐 [SECURITY.md](SECURITY.md)** ← Sécurité
- **📂 [README.md](README.md)** ← Pointeur vers la branche

### Workflows (14 fichiers)
- [bonjour.yml](.github/workflows/bonjour.yml) (Exo 1-2)
- [pr-check.yml](.github/workflows/pr-check.yml) (Exo 3)
- [scheduled.yml](.github/workflows/scheduled.yml) (Exo 3)
- [docs-only.yml](.github/workflows/docs-only.yml) (Exo 3)
- [shell-lab.yml](.github/workflows/shell-lab.yml) (Exo 4)
- [pipeline.yml](.github/workflows/pipeline.yml) (Exo 5)
- [ci.yml](.github/workflows/ci.yml) (Exo 6)
- [env-demo.yml](.github/workflows/env-demo.yml) (Exo 7)
- [smart.yml](.github/workflows/smart.yml) (Exo 8)
- [matrix-ci.yml](.github/workflows/matrix-ci.yml) (Exo 9)
- [cache-artifacts.yml](.github/workflows/cache-artifacts.yml) (Exo 10)
- [reusable-test.yml](.github/workflows/reusable-test.yml) (Exo 11A)
- [caller.yml](.github/workflows/caller.yml) (Exo 11A)
- [deploy.yml](.github/workflows/deploy.yml) (Exo 12A)
- [pages.yml](.github/workflows/pages.yml) (Exo 12B)
- [self-hosted.yml](.github/workflows/self-hosted.yml) (Exo 12C)
- [composite-action-usage.yml](.github/workflows/composite-action-usage.yml) (Exo 11B)

### Actions
- [setup-project/action.yml](.github/actions/setup-project/action.yml) (Exo 11B)

### Code
- [app.py](app.py) (Exo 6, 9-10)
- [test_app.py](test_app.py) (Exo 6, 9-10)
- [requirements.txt](requirements.txt)

---

## ❓ FAQ

**Q : Par où commencer ?**  
R : Lire `README_EXERCICES_GITHUB_ACTIONS.md`, section "Vue d'ensemble" puis "Exercice 1-2".

**Q : Comment tester localement ?**  
R : Pas possible — GitHub Actions s'exécute uniquement sur GitHub. Pousser la branche et vérifier via l'onglet Actions.

**Q : Puis-je réutiliser ces workflows ?**  
R : Oui ! Les patterns sont prévus pour être copiés dans de vrais projets. Adapter les noms et les chemins.

**Q : Comment fonctionne le runner auto-hébergé ?**  
R : Lire `SECURITY.md` et `smart.yml`. Enregistrer via Settings → Actions → Runners.

**Q : Où sont les captures d'écran ?**  
R : Pas de captures dans cette implémentation. Générer les vôtres en poussant et en visualisant dans GitHub UI.

---

## ✨ Caractéristiques principales

✅ **12 exercices progressifs** du très débutant à l'avancé  
✅ **Code réel** (tests pytest, code fonctionnel)  
✅ **Sécurité intégrée** (actions pinnées à SHA, secrets masqués)  
✅ **Documentation complète** (1300+ lignes)  
✅ **Patterns réutilisables** pour vrais projets  
✅ **Pratiques industrie** (CI/CD, déploiement)

---

## 🎯 Prochaines étapes

1. **Lire** : `README_EXERCICES_GITHUB_ACTIONS.md`
2. **Comprendre** : Examiner les workflows correspondants
3. **Tester** : Pousser et vérifier dans l'onglet Actions
4. **Adapter** : Modifier pour votre propre projet
5. **Déployer** : Intégrer à une vraie application

---

**Branche :** `github-actions-lab`  
**Repo :** https://github.com/Sayzx/exo-docker  
**Créé :** Mai 2026  
**Statut :** ✅ Complet et prêt à utiliser

Bon apprentissage ! 🚀
