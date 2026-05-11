# Sécurité des Runners Auto-Hébergés

## Risques d'un Runner Auto-Hébergé sur Dépôt Public

Lorsqu'un runner auto-hébergé est utilisé pour un dépôt public, plusieurs risques de sécurité critiques émergent. Tout d'abord, **n'importe qui peut créer une pull request** contenant du code malveillant qui s'exécutera avec les permissions du runner — y compris l'accès aux secrets stockés dans GitHub Actions. Deuxièmement, un attaquant peut **compromettre le serveur qui héberge le runner** si du code malveillant obtient l'accès à la machine. Troisièmement, les données sensibles stockées localement (clés SSH, tokens, certificats) pourraient être exposées. Enfin, une PR malveillante pourrait installer des backdoors ou modifier l'environnement d'exécution.

## Trois Mesures de Mitigation Essentielles

### 1. Isolation et Conteneurisation
Exécutez les runners dans des conteneurs Docker ou des VM isolées qui sont **réinitialisées après chaque exécution**. Cela limite l'impact des compromissions à un seul job et empêche la persistance de malwares entre les exécutions.

### 2. Contrôle des Secrets et Permissions
- N'utilisez **jamais** les secrets du dépôt sur un runner auto-hébergé public
- Limitez les actions approuvées via la liste blanche
- Utilisez des tokens à durée limitée plutôt que des credentials permanents
- Implémentez une approbation manuelle obligatoire pour les PRs avant exécution

### 3. Monitoring et Audit
Activez des logs exhaustifs de tous les jobs exécutés, montrez clairement les permissions utilisées, auditez les modifications système, et alertez sur les comportements suspects (changements de fichiers sensibles, communications réseau anormales).

## Recommandation Finale
Pour les dépôts publics, préférez les runners GitHub-hosted qui sont réinitialisés à chaque job. Les runners auto-hébergés doivent être **réservés aux dépôts privés** ou aux workflows spécifiques avec approbation manuelle.
