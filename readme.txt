CARRILLO DOCKER TP - Compteur réalisé avec Flask & Redis

Ce README fournit les étapes pour démarrer ce projet


INFOS SUR L'IMAGE PUBLIEE ET LA SECURITE

Si vous souhaitez récupérer l'image docker:
docker pull tearamisu/carrillo_docker_tp:latest

Si vous souhaitez avoir un rapport de scan des vulnérabilités:
voir vulnerability_scan.txt

 
RECUPERER LE PROJET:

Pour récupérer le projet depuis GitHub, exécutez la commande:
git clone https://github.com/Tear-Amisu/carrillo_docker_tp


CONSTRUCTION ET LANCEMENT DU PROJET:

1. Rendez-vous à la racine du projet:
cd carrillo_docker_tp

2. Lancez la construction et le déploiement des conteneurs (Flask et Redis) en mode détaché.
   Cette commande build l'image à partir du Dockerfile et utilise docker-compose:

docker compose up --build -d


ACCES A L'APPLICATION:

Vérifiez avec 'docker compose ps' si les conteneurs ont démarrés, puis accédez à l'application dans votre navigateur:
http://localhost:5000


ARRET DU PROJET:

Pour arrêter le projet, exécutez la commande:
docker compose down