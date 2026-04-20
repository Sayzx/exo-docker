# Réponses aux exercices Docker

## Exercice 1

1.1 `docker pull nginx:alpine`

1.2 `docker run -d --name mon-nginx -p 8080:80 nginx:alpine`

1.3 `docker ps`

1.4 On voit la page d'accueil par défaut de Nginx.

1.5 `docker logs mon-nginx`

1.6 `docker stop mon-nginx` puis `docker ps -a`. La différence avec `docker ps` est que `docker ps -a` affiche aussi les conteneurs arrêtés.

1.7 `docker rm mon-nginx`

1.8 `docker run --rm ...`

## Exercice 2

Les fichiers de l'exercice sont dans [exercice-2](exercice-2).

2.5 `mon-site:v1` est une image proche de `nginx:alpine`, avec une petite couche supplémentaire pour `index.html`.

2.6 Une seule couche utile a été ajoutée par rapport à l'image de base, celle du `COPY` du fichier HTML.

2.7 Au rebuild, la couche `FROM nginx:alpine` est reprise du cache, et la couche `COPY index.html ...` est réexécutée si le fichier a changé.

2.8 `docker rmi mon-site:v1`

## Exercice 3

3.1 Le fichier n'existe pas dans le nouveau conteneur. Le système de fichiers du conteneur a été supprimé avec `--rm`.

3.2 Le contenu change immédiatement dans le navigateur, car le bind mount relie le dossier de l'hôte au conteneur.

3.3 `docker volume create mes-donnees`

3.5 Oui. Cela montre qu'un volume nommé survit à la suppression du conteneur.

3.6 `docker volume ls`. Physiquement, Docker le stocke dans `/var/lib/docker/volumes/` sur Linux.

3.7 `docker volume rm mes-donnees`. Il faut d'abord s'assurer qu'aucun conteneur n'utilise encore ce volume et qu'aucune donnée importante n'est à conserver.

## Exercice 4

4.1 Les trois réseaux par défaut sont `bridge`, `host` et `none`.

4.2 `docker network create mon-reseau`

4.3 `docker run -d --name serveur-web --network mon-reseau nginx:alpine`

4.4 Depuis `client`, `wget -qO- http://serveur-web` renvoie la page Nginx. Le nom fonctionne grâce au DNS automatique du réseau bridge personnalisé.

4.5 La résolution du nom échoue sur le réseau par défaut, car ce réseau ne fournit pas le même DNS par nom de conteneur.

4.6 `docker network connect mon-reseau client-externe`

4.7 `docker rm -f serveur-web client client-externe` puis `docker network rm mon-reseau`

## Exercice 5

Les fichiers de l'exercice sont dans [exercice-5](exercice-5).

5.3 L'ordre `COPY requirements.txt` puis installation est important pour maximiser le cache Docker : les dépendances ne sont réinstallées que si le fichier des dépendances change.

5.6 La valeur affichée est `développement`, car elle vient de la valeur par défaut définie dans le code Python.

5.7 L'image est basée sur `python:3.12-slim`. Deux pistes pour réduire la taille : utiliser un multi-stage build avec seulement les dépendances utiles, et supprimer les outils et fichiers inutiles du runtime.

## Exercice 6

Les fichiers de l'exercice sont dans [exercice-6](exercice-6).

6.5 `docker compose up -d`

6.6 Oui, le compteur s'incrémente à chaque visite. `/reset` remet la clé Redis à zéro.

6.7 Non, le compteur ne repart pas de zéro si le volume `redis-data` est conservé, car la persistance de Redis est stockée dans le volume.

6.8 `docker compose logs -f`

6.9 `docker compose exec web sh`

6.10 `docker compose down -v`

## Exercice 7

Les fichiers de l'exercice sont dans [exercice-7](exercice-7).

7.2 `.gitignore` sert à éviter de committer `.env`, qui peut contenir des secrets.

7.3 `.env.example` sert de modèle partagé pour l'équipe, sans secrets réels.

7.6 `docker compose config`

7.7 Le port dépend de la variable d'environnement passée au shell. Avec `APP_PORT=9090 docker compose up`, nginx sera accessible sur 9090.

7.8 Priorité générale : variable passée dans le shell, puis `.env`, puis valeur directe dans `compose.yaml` si aucune substitution n'est faite.

7.9 Deux solutions plus sûres : secrets Docker / secrets Compose, ou un gestionnaire de secrets externe comme Vault ou AWS Secrets Manager.

## Exercice 8

Les fichiers de l'exercice sont dans [exercice-8](exercice-8).

8.2 Exclure `tests/` du contexte de build évite d'envoyer des fichiers inutiles à Docker et réduit le risque d'inclure des artefacts ou des dépendances de test dans l'image de production.

8.4 Le gain dépend de l'environnement, mais le multi-stage réduit fortement l'image finale en évitant d'emporter les outils de build et les caches pip.

8.5 `docker run --rm app-optimisee:v1 whoami` doit afficher `appuser`.

8.6 Exécuter un conteneur en root augmente l'impact d'une compromission, car l'attaquant obtient des privilèges élevés dans le conteneur et peut exploiter plus facilement des failles de montée de privilèges.

8.7 `docker images --format "{{.Repository}}:{{.Tag}} {{.Size}}" | sort -k2 -h`

## Exercice 9

Les fichiers de l'exercice sont dans [exercice-9](exercice-9).

9.6 Le passage en `healthy` dépend du temps de démarrage de PostgreSQL puis de l'application, généralement quelques dizaines de secondes.

9.7 Oui, les données sont persistées si le volume `pg-data` est conservé.

9.8 Sans `condition: service_healthy`, Flask peut démarrer avant PostgreSQL et échouer au premier accès à la base.

9.9 Ne pas exposer PostgreSQL sur l'hôte réduit la surface d'attaque et évite des accès directs à la base depuis l'extérieur de la stack.

9.10 Le fichier `.env` correspondant contient au minimum `POSTGRES_USER`, `POSTGRES_PASSWORD` et `POSTGRES_DB`.

## Exercice 10

10.1 Deux signaux utiles dans l'inspection : une image avec beaucoup de couches ou une base système plus lourde que nécessaire, et la présence d'outils inutiles ou d'une image de base trop large.

10.2 `no-new-privileges:true` empêche l'acquisition de nouveaux privilèges, `read_only: true` rend le système de fichiers non modifiable, et `tmpfs: /tmp` fournit un espace temporaire en mémoire pour les écritures nécessaires.

10.3 Les `limits` imposent une borne maximale, tandis que les `reservations` décrivent la ressource minimale à garantir au service.

10.4 Si `db` s'arrête, `app` perd sa dépendance et les requêtes vers la base échouent.

10.5 `docker compose logs --tail 20 app`

10.6 `docker stats` affiche l'utilisation CPU, mémoire, réseau et I/O des conteneurs en temps réel. Au repos, nginx utilise généralement très peu de mémoire.

10.7 `docker inspect <conteneur>` puis consulter `.Config.Env`. Les variables d'environnement ne sont pas adaptées pour stocker des secrets sensibles car elles sont faciles à exposer via l'inspection.

10.8 Un `HEALTHCHECK` dans le Dockerfile est porté par l'image elle-même, alors que celui dans `compose.yaml` est spécifique au déploiement Compose. Si les deux existent, la définition Compose prend le dessus.

10.9 L'ordre optimal est : copier d'abord `requirements.txt`, installer les dépendances, puis copier le reste du code. Cela maximise le cache des couches de dépendances.

10.10 Le script de déploiement est dans [exercice-9/deploy.sh](exercice-9/deploy.sh).
