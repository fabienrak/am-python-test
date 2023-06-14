#	Flask Task API
WebService REST developper en Flask pour :
-   Créer une nouvelle tâche
-   Récupérer une tâche par ID
-   Mettre à jour une tâche existante
-   Supprimer une tâche
-   Récupérer une liste de tâches avec des paramètres optionnels de filtrage par nom et de tri (nom, Id)


### Prise en main
Structure de Dossier :

-	![dossier](https://i.ibb.co/qnb58xH/folder.png,"dossier")
	-	`.github/`: workflows github actions
	-	`env`: environement virtuel python
	-	`migrations`: Dossier contenant le fichier de configuration, alembic et des migrations
	-	`src`: Dossier source de l'application
	-	`src/docs`: Configuration `.yaml` de documentation `swagger`
	-	`src/models`: Les fichier Models
	-	`src/services`: Dossier des fichier `services` de l'app
	-	`src/utils`: Utilitaire et Configuration partager
	-	`src/__init__.py`: Application factory
	-	`src/gunicorn.py`: Configuration de gunicorn au déploiement
	-	`app.py`: Point d'entree de l'app
	-	`.env, .env.prod`: variable d’environnement utiliser
	-	`docker-compose.yml - Dockerfile`: Fichier de configuration sous Docker
	-	`entrypoint.sh`: script de lancement
	-	`wsgi.py`: Configuration du wsgi avec gunicorn
	-	`requirements.txt`: liste des. dependances

Lancement en local :
	-	Activer l'environement virtuel de python `source env/bin/activate`
	![env](https://i.ibb.co/6ZgyF8y/env.png"ENV")
	-	Installer les dépendance lister dans le fichier requirements.txt
	 `pip install -r requirements.txt`
	![dependance](https://i.ibb.co/DrCD4zs/dependance.png,"dependance")
	-	Lancer avec `flask run` ou `python app.py`
	![launch](https://i.ibb.co/VxS98LM/launch.png,"launch")
	- Tester 
	![teste](https://i.ibb.co/5h5jpvv/teste.png,"teste")
	![postman](https://i.ibb.co/RzLkbp2/postman.png,"postman")

---
Si vous utiliser l’environnement de dev. tourné sous docker
	-	Creer l'image de base de l'application en utilisant le fichier de configuration
	`Dockerfile` dans le dossier de l'application.
	- Lancer `docker build --tag [NOM_DE_L_IMAGE] .`
	![DOCKER_BUILD](https://i.ibb.co/cx6vgZ0/docker-build.png,"docker_build")
	- Si le build se passe bien, Vous pouvez tester de lancer l'image directement 
	`docker run -p 5050:5090 [NOM_DE_VOTRE_IMAGE]`
	![DOCKER_RUN](https://i.ibb.co/hcLSXsF/docker-run.png,"docker_run") 
	En cas d'erreur sur le build veuillez vérifier le `Dockerfile` et l'adapter a votre environnement.
	- Vous pouvez utiliser l'image dans le fichier `docker-compose.yaml` pour l'orchestration de vos container.
	![DOCKER_COMPOSE](https://i.ibb.co/XX001tS/docker-compose.png,"DOCKER_COMPOSE")
	
- Lancer `docker-compose up -d` pour le démarrage des service
	- Ouvrir l'app sur votre. navigateur ou tester sur un `HTTPClient`.
	![app](https://i.ibb.co/YjsRfNX/app.png, "app")

-------
- Code, Build, Run !
		Enjoy !!
	
	![enjoy-code](https://media.tenor.com/GfSX-u7VGM4AAAAC/coding.gif,"coding")
