# 🧪 GUIDE DE TESTS — Tous les workflows

**Comment tester et déclencher chaque workflow GitHub Actions**

---

## ✅ État des workflows

Tous les 18 workflows sont **opérationnels et testables** :

### ✅ Peut s'exécuter **immédiatement** (workflow_dispatch)

Ces workflows ont une action "Run workflow" dans GitHub UI :

1. **scheduled.yml** (Exo 3)
   - Peut tester manuellement cron + dispatch
   - Choisir `dev`, `staging`, ou `prod`

2. **shell-lab.yml** (Exo 4)
   - Scripts multi-lignes
   - Variables et codes de sortie

3. **env-demo.yml** (Exo 7)
   - Variables et secrets
   - Affiche GITHUB_TOKEN usage

4. **deploy.yml** (Exo 12A)
   - Choisir environment
   - Voir approbations (production)

5. **pages.yml** (Exo 12B)
   - Crée un site HTML
   - Accessible via GitHub Pages

6. **self-hosted.yml** (Exo 12C)
   - Teste runner auto-hébergé
   - (Nécessite un runner enregistré)

7. **cache-artifacts.yml** (Exo 10)
   - Démontre cache et artefacts

8. **caller.yml** (Exo 11A)
   - Appelle workflow réutilisable

9. **composite-action-usage.yml** (Exo 11B)
   - Utilise action composite

### 🔄 S'exécute **sur push** (automatique)

Ces workflows se déclenchent automatiquement quand vous poussez :

1. **bonjour.yml** (Exo 1-2)
   - Workflow simple
   - S'exécute sur push

2. **pipeline.yml** (Exo 5)
   - 4 jobs avec dépendances
   - S'exécute sur push

3. **ci.yml** (Exo 6)
   - Tests pytest
   - S'exécute sur push ET pull_request

4. **matrix-ci.yml** (Exo 9)
   - 9 combinaisons OS/versions
   - S'exécute sur push ET pull_request

### 📡 S'exécute sur **événements spécifiques**

1. **pr-check.yml** (Exo 3)
   - Déclenché sur **pull request**
   - Affiche info PR

2. **docs-only.yml** (Exo 3)
   - Déclenché sur **push dans docs/**
   - Modifier `docs/README-docs.md` pour tester

3. **smart.yml** (Exo 8)
   - Déclenché sur **tags** (`git tag v1.x.x`)
   - Aussi sur PR

4. **reusable-test.yml** (Exo 11A)
   - Déclenché via `workflow_call`
   - Appelé par `caller.yml`

---

## 🚀 Comment tester : 5 méthodes

### **Méthode 1 : Cliquer "Run workflow" dans GitHub UI** ⭐ LA PLUS FACILE

Pour les workflows avec `workflow_dispatch` :

1. Aller à → **Actions** tab
2. Sélectionner un workflow (ex: `scheduled.yml`)
3. Cliquer **"Run workflow"**
4. Voir le job s'exécuter en temps réel

**Workflows testables** :
- scheduled.yml
- shell-lab.yml
- env-demo.yml
- deploy.yml
- pages.yml
- self-hosted.yml
- cache-artifacts.yml
- caller.yml
- composite-action-usage.yml

**Temps d'exécution** : 30 secondes à 2 minutes

---

### **Méthode 2 : Pousser sur la branche github-actions-lab**

Tous les workflows avec `push` se déclenchent automatiquement :

```bash
cd /tmp/exo-docker
git checkout github-actions-lab

# Faire une modification quelconque
echo "# Modification de test" >> README_RAPPORT_FINAL.md

# Committer et pousser
git add .
git commit -m "test: Déclencher les workflows"
git push origin github-actions-lab
```

**Résultat** : Les 8 workflows de push se déclenchent automatiquement

**Workflows déclenchés** :
- bonjour.yml
- pipeline.yml
- ci.yml
- matrix-ci.yml
- cache-artifacts.yml
- caller.yml
- composite-action-usage.yml
- pages.yml

**Temps d'exécution** : 1-5 minutes total

---

### **Méthode 3 : Créer une pull request**

Les workflows `on: pull_request` se déclenchent :

```bash
# Créer une branche de feature
git checkout -b feature/test

# Faire une modification
echo "test" > test.txt

# Committer et pousser
git add .
git commit -m "test: Feature PR"
git push -u origin feature/test

# Créer une PR via GitHub UI ou gh CLI
gh pr create --title "Test workflows" --body "Teste les workflows"
```

**Résultat** : Les workflows PR se déclenchent

**Workflows déclenchés** :
- pr-check.yml (affiche numéro PR et auteur)
- ci.yml (tests pytest)
- matrix-ci.yml (9 combinaisons)
- smart.yml (selon labels/conditions)

**Temps d'exécution** : 2-10 minutes

---

### **Méthode 4 : Créer un tag de version**

Pour tester les workflows `on: push tags`:

```bash
# Créer un tag
git tag v1.0.0

# Pousser le tag
git push origin v1.0.0
```

**Résultat** : Les workflows taggés se déclenchent

**Workflows déclenchés** :
- smart.yml (condition : `startsWith(github.ref, 'refs/tags/v')`)

**Temps d'exécution** : 30 secondes à 2 minutes

---

### **Méthode 5 : Modifier les fichiers docs/**

Pour tester le filtrage par chemin :

```bash
# Modifier un fichier dans docs/
echo "# Modification" >> docs/README-docs.md

# Committer et pousser
git add docs/
git commit -m "docs: Update documentation"
git push origin github-actions-lab
```

**Résultat** : `docs-only.yml` se déclenche

**Temps d'exécution** : 30 secondes

---

## 📋 Tableau récapitulatif : Comment déclencher chaque workflow

| # | Workflow | Méthode | Commande / Action |
|---|----------|--------|-------------------|
| 1 | bonjour.yml | Push | `git push` |
| 2 | pr-check.yml | PR | `gh pr create` |
| 3 | scheduled.yml | Manuel | Run workflow UI |
| 4 | docs-only.yml | Push docs | `git push docs/` |
| 5 | shell-lab.yml | Manuel | Run workflow UI |
| 6 | pipeline.yml | Push | `git push` |
| 7 | ci.yml | Push ou PR | `git push` ou `gh pr create` |
| 8 | env-demo.yml | Manuel | Run workflow UI |
| 9 | smart.yml | Tag ou PR | `git tag v1.0.0` |
| 10 | matrix-ci.yml | Push ou PR | `git push` ou `gh pr create` |
| 11 | cache-artifacts.yml | Push ou Manuel | `git push` ou Run workflow UI |
| 12 | reusable-test.yml | Via caller | Exécuté par caller.yml |
| 13 | caller.yml | Push ou Manuel | `git push` ou Run workflow UI |
| 14 | composite-action-usage.yml | Push ou Manuel | `git push` ou Run workflow UI |
| 15 | deploy.yml | Push ou Manuel | `git push` ou Run workflow UI |
| 16 | pages.yml | Push ou Manuel | `git push` ou Run workflow UI |
| 17 | self-hosted.yml | Manuel | Run workflow UI |
| 18 | smart.yml | Tag ou PR | `git tag v1.0.0` ou `gh pr create` |

---

## 🎯 Plan de test complet (30 minutes)

### **Phase 1 : Tests manuels (10 min)**
Déclencher via UI (workflow_dispatch) :

```
Aller à Actions → Choisir un workflow → Run workflow
```

Tester :
- [ ] scheduled.yml
- [ ] shell-lab.yml
- [ ] env-demo.yml
- [ ] pages.yml

### **Phase 2 : Tests push (5 min)**
```bash
git push origin github-actions-lab
```

Observe :
- [ ] bonjour.yml ✓
- [ ] pipeline.yml ✓
- [ ] ci.yml ✓
- [ ] matrix-ci.yml ✓

### **Phase 3 : Tests PR (10 min)**
```bash
gh pr create --title "Test" --body "Test workflows"
```

Observe :
- [ ] pr-check.yml ✓
- [ ] ci.yml ✓
- [ ] matrix-ci.yml ✓

### **Phase 4 : Tests tag (5 min)**
```bash
git tag v1.0.0 && git push origin v1.0.0
```

Observe :
- [ ] smart.yml ✓

---

## 🔍 Vérifier les résultats

### Via GitHub UI
1. Aller à **Actions** tab
2. Voir l'historique des runs
3. Cliquer sur un run pour voir les logs détaillés
4. Voir les étapes individuelles (vert = succès)

### Via CLI
```bash
# Voir les workflows disponibles
gh workflow list

# Voir les runs récents
gh run list

# Voir les logs d'un run
gh run view <RUN_ID> --log
```

---

## ✅ Vérifications de succès

### Workflow "Bonjour" (bonjour.yml)
```
✓ Exécution réussie
✓ 3 étapes affichées
✓ Logs affichent : "Bonjour depuis GitHub Actions !"
```

### Workflow "CI Tests" (ci.yml)
```
✓ Setup Python
✓ Installer dépendances
✓ Exécuter pytest
✓ Tous les tests passent
```

### Workflow "Matrix" (matrix-ci.yml)
```
✓ 9 jobs en parallèle
✓ Mix OS/versions affichés
✓ Certains en succes, experimental peut être warning
```

### Workflow "Pages" (pages.yml)
```
✓ Build HTML
✓ Upload artifact
✓ Deploy successful
✓ URL GitHub Pages accessible
```

---

## 🐛 Dépannage

### Le workflow ne s'exécute pas

**Problème :** "Run workflow" est grisé  
**Solution :** Le workflow doit avoir `workflow_dispatch` dans `on:`
- Vérifier la syntaxe YAML
- Vérifier l'indentation

**Problème :** Le push ne déclenche rien  
**Solution :** Vérifier que la branche est dans `branches: [...]`
- Ajouter `github-actions-lab` à la liste
- Ou ajouter `workflow_dispatch`

### Le test pytest échoue

**Problème :** `ModuleNotFoundError: No module named 'pytest'`  
**Solution :** Les dépendances ne sont pas installées
- Vérifier `requirements.txt` existe
- Vérifier pip install dans le workflow

**Problème :** `AssertionError: assert 5 == 6`  
**Solution :** Le code ou le test a changé
- Vérifier `app.py` et `test_app.py`
- Corriger le code ou le test

### La matrice ne crée pas 9 jobs

**Problème :** Nombre de jobs < 9  
**Solution :** Include/exclude a trop de combinaisons
- Vérifier la configuration include/exclude
- Compter les combinaisons : 3 OS × 3 versions = 9, sauf exclude

### GitHub Pages ne se déploie pas

**Problème :** "404 - Not Found"  
**Solution :** GitHub Pages n'est pas activé
- Settings → Pages
- Source: "GitHub Actions"
- Attendre 1-2 minutes après le premier déploiement

---

## 📊 Résumé des tests

```
Total workflows       : 18
Testables manuellement: 9 (workflow_dispatch)
Déclenchés auto (push): 8
Déclenchés sur PR    : 4
Déclenchés sur tag   : 1
Déclenchés doc modif : 1
Déclenchés via call  : 1

Durée totale de test : ~30-45 minutes
Taux de succès       : 100% (si syntaxe correcte)
```

---

## 🎓 Ordre recommandé de test

**Pour apprendre progressivement :**

1. **Jour 1 :** Workflows simples
   - bonjour.yml (push)
   - scheduled.yml (manuel)
   - shell-lab.yml (manuel)

2. **Jour 2 :** Workflows CI/CD
   - ci.yml (push + PR)
   - pipeline.yml (push)
   - cache-artifacts.yml (push)

3. **Jour 3 :** Workflows avancés
   - matrix-ci.yml (9 combinaisons)
   - deploy.yml (manuel + approbations)
   - pages.yml (déploiement)

4. **Jour 4 :** Réutilisabilité
   - reusable-test.yml + caller.yml
   - composite-action-usage.yml

---

## 🔐 Notes de sécurité

- ✅ Tous les workflows sont sûrs (pas de secrets en texte clair)
- ✅ Actions pinnées à SHA complet
- ✅ Pas de `--no-verify` ou contournement de sécurité
- ✅ GITHUB_TOKEN uniquement pour accès APIs
- ⚠️ Ne pas ajouter de runners auto-hébergés à un dépôt public

---

## 📞 Questions fréquentes

**Q : Pourquoi mes workflows ne s'exécutent pas sur github-actions-lab ?**  
R : Les workflows sont maintenant configurés pour s'exécuter sur `github-actions-lab`. Utiliser "Run workflow" ou faire un push.

**Q : Combien de temps ça prend ?**  
R : 30 secondes à 5 minutes selon la complexité du workflow.

**Q : Puis-je modifier les workflows pour apprendre ?**  
R : Oui ! C'est encouragé. Faire des modifications et voir les résultats.

**Q : Mes secrets sont-ils visibles ?**  
R : Non, ils sont auto-masqués avec `***` si référencés correctement.

---

**Branche :** `github-actions-lab`  
**Tous les workflows sont prêts à être testés ! 🚀**
