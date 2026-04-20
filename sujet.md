# Exercices Docker — Formation pratique

**Niveau :** Débutant → Challenge | **Langue :** Français
**Prérequis :** Docker Engine installé (docker --version), Docker Compose V2 (docker
compose version)

```
Les commandes sont à taper dans un terminal. Créez un dossier de travail par
exercice.
Répondez dans un fichier séparé fourni par votre formateur.
```
## 🟢 Partie 1 — Les bases (Exercices 1 à 5)

### Exercice 1 — Premier contact avec Docker

**Objectif :** Comprendre le cycle de vie d'un conteneur et les commandes fondamentales.

**Contexte :** Docker suit le modèle **pull → run → stop → remove**. Un conteneur est une
instance isolée d'une image. Quand il s'arrête, il n'est pas supprimé automatiquement (sauf
avec --rm).

**Travail à faire :**

**1.1** Téléchargez l'image nginx:alpine depuis Docker Hub sans lancer de conteneur.

**1.2** Lancez un conteneur nginx:alpine nommé mon-nginx en arrière-plan, en exposant
le port 8080 de votre machine sur le port 80 du conteneur.

**1.3** Vérifiez que le conteneur tourne. Quelle commande permet de lister uniquement les
conteneurs en cours d'exécution?

**1.4** Ouvrez [http://localhost:8080](http://localhost:8080) dans votre navigateur (ou avec curl). Que voyez-
vous?

**1.5** Affichez les logs du conteneur mon-nginx.

**1.6** Arrêtez le conteneur mon-nginx sans le supprimer. Puis listez **tous** les conteneurs (y
compris arrêtés). Quelle est la différence avec la commande de la question 1.3?

**1.7** Supprimez le conteneur mon-nginx. Vérifiez qu'il n'existe plus.


**1.8** Quelle commande aurait permis de lancer le conteneur de façon à ce qu'il soit
**automatiquement supprimé** à l'arrêt?

### Exercice 2 — Construire sa première image avec un Dockerfile

**Objectif :** Écrire un Dockerfile, construire une image, comprendre les layers.

**Contexte :** Un Dockerfile est un fichier texte décrivant les étapes pour construire une
image. Chaque instruction (FROM, RUN, COPY...) crée un **layer** (couche) mis en cache par
Docker.

**Travail à faire :**

Créez le dossier exercice-2/ avec la structure suivante :

```
exercice-2/
├── Dockerfile
└── index.html
```
**2.1** Écrivez index.html avec le contenu HTML minimal suivant (titre : "Ma première
image Docker", un <h1> avec votre prénom).

**2.2** Écrivez un Dockerfile qui :

- Part de l'image nginx:alpine
- Copie index.html dans /usr/share/nginx/html/index.html
- Expose le port 80

**2.3** Construisez l'image avec le tag mon-site:v1.

**2.4** Lancez un conteneur basé sur cette image, en exposant le port 9090 → 80 , avec --
rm. Vérifiez dans le navigateur.

**2.5** Listez les images locales. Quelle est la taille de mon-site:v1? Comparez avec
nginx:alpine.

**2.6** Inspectez les layers de l'image avec docker history mon-site:v1. Combien de
layers ont été ajoutés par rapport à l'image de base?

**2.7** Modifiez index.html (changez le <h1>). Reconstruisez l'image avec le tag mon-
site:v2. Quelle étape a été rechargée depuis le cache? Quelle étape a été réexécutée?

**2.8** Supprimez l'image mon-site:v1 (sans supprimer v2).


### Exercice 3 — Volumes et persistance des données

**Objectif :** Comprendre la différence entre bind mount et volume nommé, et pourquoi la
persistance est cruciale.

**Contexte :** Le système de fichiers d'un conteneur est **éphémère** : toute donnée écrite
dedans disparaît à la suppression du conteneur. Les **volumes** et **bind mounts** permettent
de persister des données.

```
Type Description
Bind mount Monte un dossier de l'hôte dans le conteneur
```
```
Volume nommé Géré par Docker, stocké dans /var/lib/docker/volumes/
```
**Travail à faire :**

**3.1** Lancez un conteneur alpine en mode interactif (-it) avec --rm. À l'intérieur, créez
le fichier /data/test.txt avec le contenu "bonjour". Quittez (exit). Relancez un
nouveau conteneur alpine. Le fichier existe-t-il? Expliquez pourquoi.

**3.2 — Bind mount :** Créez un dossier exercice-3/html/ sur votre machine. Placez-y un
fichier index.html. Lancez un conteneur nginx:alpine en montant ce dossier dans /
usr/share/nginx/html avec -v. Modifiez index.html sur votre machine (sans
redémarrer le conteneur) et rafraîchissez le navigateur. Que constatez-vous?

**3.3 — Volume nommé :** Créez un volume Docker nommé mes-donnees.

**3.4** Lancez un conteneur alpine avec --rm en montant mes-donnees sur /data. Dans
le conteneur, créez /data/persistant.txt avec le contenu "je survis". Quittez.

**3.5** Lancez un **nouveau** conteneur alpine (différent du précédent) avec le même volume
monté. Le fichier /data/persistant.txt existe-t-il? Qu'est-ce que cela démontre?

**3.6** Listez les volumes Docker existants. Où Docker stocke-t-il physiquement ce volume sur
votre machine?

**3.7** Supprimez le volume mes-donnees. Quelle précaution faut-il prendre avant de le
supprimer?

### Exercice 4 — Réseaux Docker

**Objectif :** Comprendre les réseaux Docker, faire communiquer deux conteneurs par leur
nom.


**Contexte :** Par défaut, les conteneurs sont connectés au réseau bridge. Sur un réseau
**bridge personnalisé** , les conteneurs peuvent se joindre par leur **nom** (DNS automatique).
Ce n'est pas le cas sur le réseau bridge par défaut.

**Travail à faire :**

**4.1** Listez les réseaux Docker existants sur votre machine. Quels sont les trois réseaux
créés par défaut?

**4.2** Créez un réseau bridge personnalisé nommé mon-reseau.

**4.3** Lancez un conteneur nginx:alpine nommé serveur-web connecté à mon-reseau,
en arrière-plan.

**4.4** Lancez un conteneur alpine nommé client connecté à mon-reseau en mode
interactif. Depuis client, effectuez un wget -qO- [http://serveur-web.](http://serveur-web.) Que récupérez-
vous? Pourquoi peut-on utiliser le nom serveur-web plutôt qu'une adresse IP?

**4.5** Quittez client. Lancez un **nouveau** conteneur alpine nommé client-externe
**sans** le connecter à mon-reseau (réseau par défaut). Essayez de joindre serveur-web
par son nom. Que se passe-t-il? Pourquoi?

**4.6** Quelle commande permet de connecter client-externe à mon-reseau **après** son
démarrage?

**4.7** Nettoyez : arrêtez et supprimez tous les conteneurs créés dans cet exercice, puis
supprimez mon-reseau.

### Exercice 5 — Containeriser un serveur Flask

**Objectif :** Containeriser une application Python Flask, gérer les dépendances, configurer
via des variables d'environnement.

**Contexte :** Flask est un micro-framework web Python. On utilise python:3.12-slim
comme image de base (plus légère que python:3.12). Les dépendances sont listées dans
requirements.txt.

**Structure à créer :**

```
exercice-5/
├── Dockerfile
├── requirements.txt
└── app.py
```
**5.1** Créez app.py :


```
fromflaskimport Flask
import os
```
```
app= Flask(__name__)
```
```
@app.route("/" )
defhome():
env = os .environ.get ("APP_ENV", "développement")
return f"<h1>Flask fonctionne !</h1><p>Environnement : {env }</p>"
```
```
@app.route("/health")
defhealth():
return {"status": "ok"}, 200
```
```
if __name__== "__main__":
app .run (host="0.0.0.0", port=5000)
```
**5.2** Créez requirements.txt avec Flask 3.0.3 comme unique dépendance.

**5.3** Écrivez un Dockerfile qui :

- Part de python:3.12-slim
- Définit /app comme répertoire de travail
- Copie **d'abord** requirements.txt seul, installe les dépendances (sans cache pip), puis
copie le reste des sources. Pourquoi cet ordre est-il important pour le cache Docker?
- Expose le port 5000
- Définit la commande de démarrage avec flask run --host=0.0.0.

**5.4** Construisez l'image flask-app:v1.

**5.5** Lancez un conteneur en passant la variable d'environnement APP_ENV=production et
en exposant le port 5000. Vérifiez / et /health dans le navigateur ou avec curl.

**5.6** Relancez le conteneur **sans** passer APP_ENV. Quelle valeur s'affiche? D'où vient-elle?

**5.7** Quelle est la taille de l'image flask-app:v1? Que pourrait-on faire pour la réduire
davantage (donnez deux pistes)?

## 🟡 Partie 2 — Approfondissement (Exercices 6 à 8)


### Exercice 6 — Docker Compose : stack multi-services

**Objectif :** Orchestrer plusieurs services avec Docker Compose V2, comprendre
depends_on, les réseaux et volumes déclaratifs.

**Contexte :** Docker Compose V2 (docker compose sans tiret) gère un ensemble de
services définis dans un fichier compose.yaml. Chaque service est un conteneur. Les
services d'un même Compose partagent automatiquement un réseau.

**Structure à créer :**

```
exercice-6/
├── compose.yaml
├── app/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app.py
```
**6.1** Créez app/app.py :

```
fromflaskimport Flask
import redis
import os
```
```
app= Flask(__name__)
r = redis.Redis(host=os .environ.get ("REDIS_HOST", "redis"), port=6379)
```
```
@app.route("/" )
defhome():
count = r.incr("visites")
return f"<h1>Visiteur n°{count}</h1>"
```
```
@app.route("/reset")
defreset():
r.set ("visites", 0)
return "Compteur remis à zéro", 200
```
**6.2** Créez app/requirements.txt avec flask==3.0.3 et redis==5.0.8.

**6.3** Créez app/Dockerfile : image python:3.12-slim, workdir /app, copie et
installation des dépendances, commande flask run --host=0.0.0.0.

**6.4** Écrivez compose.yaml avec :

- Un service web buildé depuis ./app, exposant le port 5000 , avec la variable
    REDIS_HOST=redis
- Un service redis basé sur l'image redis:7-alpine


- Un volume nommé redis-data monté dans le service redis sur /data
- Assurance que web démarre **après** redis (depends_on)

**6.5** Démarrez la stack en arrière-plan avec une seule commande. Quelle est-elle?

**6.6** Visitez [http://localhost:5000](http://localhost:5000) plusieurs fois. Le compteur s'incrémente-t-il? Visitez
/reset. Que se passe-t-il?

**6.7** Arrêtez et relancez la stack (down puis up). Le compteur repart-il de zéro? Expliquez
pourquoi (rôle du volume redis-data).

**6.8** Quelle commande affiche les logs **en temps réel** de tous les services de la stack?

**6.9** Quelle commande permet d'entrer dans le conteneur web pour y ouvrir un shell
interactif via Compose (sans connaître l'ID du conteneur)?

**6.10** Quelle commande arrête **et supprime** les conteneurs, réseaux **et volumes** de la
stack?

### Exercice 7 — Variables d'environnement, fichiers .env et surcharge

### de configuration

**Objectif :** Gérer la configuration d'une stack Compose proprement via .env, comprendre
la surcharge et les bonnes pratiques de sécurité.

**Contexte :** Docker Compose charge automatiquement un fichier .env situé dans le même
dossier que compose.yaml. Les variables peuvent être référencées dans le fichier
Compose avec la syntaxe ${VARIABLE}. Ne jamais committer .env avec des secrets
réels dans Git.

**Structure à créer :**

```
exercice-7/
├── compose.yaml
├── .env
├── .env.example ← version sans secrets, à committer
└── .gitignore
```
**7.1** Créez .env :

```
APP_PORT=
APP_ENV=development
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
POSTGRES_DB=myapp
```

**7.2** Créez .gitignore pour exclure .env du contrôle de version. Pourquoi est-ce
important?

**7.3** Créez .env.example en remplaçant les valeurs sensibles par des placeholders (ex :
POSTGRES_PASSWORD=changeme). Quel est le rôle de ce fichier dans un projet d'équipe?

**7.4** Écrivez compose.yaml avec deux services :

- app : image nginx:alpine, ports ${APP_PORT}:80, variable d'environnement
    APP_ENV
- db : image postgres:16-alpine, variables POSTGRES_USER, POSTGRES_PASSWORD,
    POSTGRES_DB

**7.5** Lancez la stack. Vérifiez que nginx est accessible sur le port défini dans .env.

**7.6** Quelle commande permet d'afficher le fichier Compose **après interpolation** des
variables (pour déboguer)?

**7.7** Surchargez APP_PORT **sans modifier .env** en passant la variable directement dans la
commande shell. Sur quel port nginx sera-t-il accessible? (Indice : la syntaxe est
VAR=valeur docker compose up)

**7.8** Modifiez APP_PORT=9090 dans .env. Relancez. Quelle est la **priorité** entre une
variable dans .env, dans le shell, et dans compose.yaml directement?

**7.9** Pour une base de données PostgreSQL en production, citez **deux** méthodes plus
sécurisées que d'injecter le mot de passe via une variable d'environnement en clair.

### Exercice 8 — Optimisation d'image : multi-stage build, .dockerignore

### et non-root

**Objectif :** Réduire drastiquement la taille d'une image, améliorer sa sécurité, et exclure les
fichiers inutiles du contexte de build.

**Contexte :**

- **Multi-stage build** : plusieurs blocs FROM dans un Dockerfile ; seul le dernier stage
compose l'image finale.
- **.dockerignore** : liste de fichiers/dossiers à exclure du contexte envoyé au daemon Docker
(similaire à .gitignore).
- **Utilisateur non-root** : par défaut, les processus dans un conteneur tournent en root.
C'est un risque de sécurité important.

**Structure à créer :**


```
exercice-8/
├── Dockerfile.naive ← version naïve (fournie)
├── Dockerfile ← version optimisée (à écrire)
├── .dockerignore
├── requirements.txt
├── app.py
└── tests/
└── test_app.py
```
**8.1 — Version naïve :** Créez Dockerfile.naive :

```
FROMpython:3.
WORKDIR/app
COPY..
RUNpip install-r requirements.txt
CMD["python", "app.py"]
```
Créez app.py (Flask minimal avec route /), requirements.txt (flask==3.0.3), et
tests/test_app.py (fichier vide). Construisez app-naive:v1 avec docker build -f
Dockerfile.naive. Notez sa taille.

**8.2 — .dockerignore :** Créez .dockerignore pour exclure : tests/, *.md,
__pycache__/, *.pyc, .git, .env. Pourquoi exclure tests/ du contexte de build de
l'image de production?

**8.3 — Multi-stage build :** Écrivez un Dockerfile en deux stages :

```
Stage builder : python:3.12-slim, installe les dépendances dans /install (avec
pip install --prefix=/install)
Stage final : python:3.12-slim, copie uniquement /install depuis builder et le
code source app.py, définit PYTHONPATH=/install/lib/python3.12/site-packages,
expose 5000 , démarre Flask
```
**8.4** Construisez app-optimisee:v1. Comparez la taille avec app-naive:v1. Quel est le
gain en Mo?

**8.5 — Utilisateur non-root :** Ajoutez dans le stage final de Dockerfile :

- Création d'un groupe et utilisateur système appuser (sans shell de login)
- Changement de propriétaire du dossier /app
- Instruction USER appuser juste avant CMD

Reconstruisez. Vérifiez avec docker run --rm app-optimisee:v1 whoami que le
processus ne tourne plus en root.

**8.6** Expliquez en une phrase pourquoi faire tourner un conteneur en root est un risque,
même si le conteneur est isolé.

#### •

#### •


**8.7** Quelle commande permet de lister la taille de toutes vos images locales, triées du plus
lourd au plus léger?

## 🔴 Partie 3 — Challenges (Exercices 9 et 10)

### Exercice 9 — Stack complète : Flask + PostgreSQL + Nginx (reverse

### proxy)

**Objectif :** Construire une stack de production réaliste avec trois services interconnectés,
healthchecks, dépendances de démarrage et reverse proxy.

**Contexte :** Dans une architecture web typique :

- **Nginx** expose le port 80 et redirige vers l'application (reverse proxy)
- **Flask** est le serveur applicatif (non exposé directement)
- **PostgreSQL** est la base de données (non exposée publiquement)

Les healthcheck permettent à Compose de savoir qu'un service est vraiment **prêt** (et pas
juste démarré).

**Structure cible :**

```
exercice-9/
├── compose.yaml
├── .env
├── nginx/
│ └── nginx.conf
└── app/
├── Dockerfile
├── requirements.txt
└── app.py
```
**9.1 — Application Flask :** Créez app/app.py avec :

- Une connexion PostgreSQL via psycopg2 (utilisez les variables d'environnement
    DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
- Route GET / : retourne le nombre de lignes dans une table visites (créer la table si
elle n'existe pas)
- Route POST /visites : insère une nouvelle visite et retourne le total
- Route GET /health : retourne {"status": "ok"} (200)

**9.2** Créez app/requirements.txt avec flask==3.0.3 et psycopg2-binary==2.9.9.


**9.3** Créez app/Dockerfile en multi-stage (builder + runtime), avec utilisateur non-root, et
un HEALTHCHECK qui appelle /health toutes les 30 secondes.

**9.4 — Nginx :** Créez nginx/nginx.conf configuré pour :

- Écouter sur le port 80
- Proxyfier toutes les requêtes vers [http://app:5000](http://app:5000) (le service Flask)
- Ajouter le header X-Forwarded-For

**9.5 — Compose :** Écrivez compose.yaml avec :

```
Service Image / Build Ports exposés Dépend de
```
```
db postgres:16-alpine aucun —
```
```
app build ./app aucun db (condition: healthy)
```
```
nginx nginx:alpine 80:80 app (condition: healthy)
```
```
db doit avoir un healthcheck : pg_isready -U ${POSTGRES_USER}
app doit avoir un healthcheck : curl -f http://localhost:5000/health
Le service db ne doit pas exposer de port sur l'hôte
Définir un réseau backend pour db et app, un réseau frontend pour app et
nginx
Volume nommé pg-data pour la persistance PostgreSQL
```
**9.6** Lancez la stack. Vérifiez avec docker compose ps que tous les services passent à
l'état healthy. Combien de temps cela prend-il?

**9.7** Testez avec curl -X POST [http://localhost/visites](http://localhost/visites) plusieurs fois. Arrêtez et
relancez la stack. Les données sont-elles persistées?

**9.8** Que se passe-t-il si vous supprimez la condition healthy du depends_on de app?
Quel problème cela peut-il créer au démarrage?

**9.9** Quel est l'avantage de ne **pas** exposer le port de PostgreSQL sur l'hôte?

**9.10** Rédigez le .env correspondant à cette stack avec toutes les variables nécessaires.

#### •

#### •

#### •

#### •

#### •


### Exercice 10 — Sécurité, optimisation avancée et debugging en

### production

**Objectif :** Appliquer les bonnes pratiques de sécurité et de robustesse sur une image et
une stack existantes. Utiliser les outils d'introspection Docker pour diagnostiquer des
problèmes.

**Contexte :** Cet exercice utilise la stack de l'exercice 9 comme point de départ. Vous allez
l'auditer, la renforcer et la déboguer.

**Partie A — Audit et réduction de surface d'attaque**

**10.1** Analysez l'image app avec docker scout cves ou docker scan (si disponible).
Alternativement, utilisez docker image inspect app-image pour lister les layers. Citez
deux informations visibles dans l'inspection qui peuvent indiquer un risque de sécurité.

**10.2** Ajoutez dans le service app du compose.yaml les contraintes de sécurité suivantes.
Expliquez le rôle de chacune :

```
security_opt:
```
- no-new-privileges:true
read_only: true
tmpfs:
- /tmp

**10.3** Ajoutez des **limites de ressources** au service app :

- CPU : max 0.5 core
- Mémoire : max 256M, réservation 128M

Quelle est la différence entre limits et reservations dans Docker Compose?

**Partie B — Debugging de conteneurs**

**10.4** Lancez la stack. Simulez une panne : stoppez le service db manuellement avec
docker compose stop db. Que se passe-t-il sur le service app? Vérifiez avec docker
compose ps.

**10.5** Comment consulter les **20 dernières lignes** de logs du service app uniquement,
sans les logs des autres services?


**10.6** Lancez la commande docker stats sur tous les conteneurs de la stack. Quelle
information vous donne-t-elle? Quelle est l'utilisation mémoire du service nginx au
repos?

**10.7** Sans ouvrir de shell dans le conteneur, examinez les **variables d'environnement**
injectées dans le conteneur app avec docker inspect. Quelle commande utilisez-vous?
Quel risque cela représente-t-il pour des secrets injectés en variable d'environnement?

**Partie C — Bonnes pratiques de build avancées**

**10.8** Ajoutez un HEALTHCHECK à votre Dockerfile Flask. Quelle est la différence entre un
HEALTHCHECK défini dans le Dockerfile et un healthcheck défini dans
compose.yaml? Lequel a la priorité?

**10.9** Dans votre Dockerfile Flask, les instructions sont dans cet ordre :

```
COPY..
RUNpip install-r requirements.txt
```
Proposez l'ordre **optimal** pour maximiser l'utilisation du cache Docker. Expliquez le
raisonnement.

**10.10 — Challenge final :** Rédigez un script shell deploy.sh qui :

1. Construit les images avec --no-cache
2. Lance la stack en arrière-plan
3. Attend que le service nginx soit accessible (boucle curl avec timeout de 60
secondes)
4. Affiche "✅ Stack déployée avec succès" ou "❌ Timeout — vérifiez les logs"
selon le résultat

## 📋 Récapitulatif des commandes clés

```
Commande Description
```
```
docker pull <image> Télécharger une image
```
```
docker build -t <tag>. Construire une image
```
```
docker run -d -p 8080:80 --name <nom>
<image>
Lancer un conteneur
```

```
Commande Description
```
```
docker exec -it <id> sh Ouvrir un shell dans un conteneur
```
```
docker logs -f <nom> Suivre les logs
```
```
docker inspect <nom> Inspecter un conteneur ou une image
```
```
docker system prune -a Nettoyer toutes les ressources
inutilisées
```
```
docker compose up -d Démarrer la stack en arrière-plan
```
```
docker compose down -v Arrêter et supprimer (y compris
volumes)
docker compose logs -f Suivre les logs de tous les services
```
```
docker compose exec <service> sh Shell dans un service Compose
```
```
docker stats Monitorer les ressources en tempsréel
```
_Sources : docs.docker.com · docs.docker.com/compose · github.com/docker/compose_


