# Documentation

Cette documentation démontre le déclenchement du workflow `docs-only.yml` lorsque des fichiers du dossier `docs/` sont modifiés.

## Exercice 3 - Déclencheurs filtrés par chemin

Le workflow `docs-only.yml` se déclenche **uniquement** quand les fichiers dans ce dossier changent :

```yaml
on:
  push:
    paths:
      - 'docs/**'
```

Cela permet de ne déclencher la vérification que pour les vrais changements de documentation, sans surcharger avec des runs inutiles.
