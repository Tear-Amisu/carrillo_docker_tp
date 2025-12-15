# CARRILLO DOCKER TP - Compteur réalisé avec Flask & Redis

Ce README fournit les étapes pour démarrer ce projet


INFOS SUR L'IMAGE PUBLIEE ET LA SECURITE

Si vous souhaitez récupérer l'image docker:
```
docker pull tearamisu/carrillo_docker_tp:latest
```

Si vous souhaitez avoir un rapport de scan des vulnérabilités:
voir le fichier vulnerability_scan.txt
> Comment a été produit le rapport ?
 
RECUPERER LE PROJET:

Pour récupérer le projet depuis GitHub, exécutez la commande:
git clone https://github.com/Tear-Amisu/carrillo_docker_tp


CONSTRUCTION ET LANCEMENT DU PROJET:

1. Rendez-vous à la racine du projet:
```
cd carrillo_docker_tp
```

2. Lancez la construction et le déploiement des conteneurs:
```
docker compose up --build -d
```

ACCES A L'APPLICATION:

Vérifiez si le docker tourne bien avec la commande:
```
docker compose ps
```

Accédez à l'application dans votre navigateur:
http://localhost:5000


ARRET DU PROJET:

Pour arrêter le projet, exécutez la commande:
```
docker compose down
```