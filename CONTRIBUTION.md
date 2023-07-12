# Contribution

## Pré-requis:

- Installer python3.11.3
- Installer packwiz (https://packwiz.infra.link/installation/)
- Installer mmc-export==2.8.5
```
pip install mmc-export==2.8.5
```
- Installer le Prism Launcher

## Modifier et mettre à jour le modpack

Vous devez être à peu près familier avec le launcher Prism pour pouvoir éditer le modpack. L'aide du launcher peut vous être très utile: https://prismlauncher.org/wiki/help-pages/

![Fenêtre des mods](images/mods_windows.png)

### Créer l'instance de développement

Créez l'instance de développement à partir de la dernière version du modpack.

![Création de l'instance](images/instance_creation.png)

### Ajouts de mods

Le plus important à savoir pour les mods de l'instance c'est qu'il faut prioriser ceux qui ont pour source Modrinth. Les mods provenant d'autres sources demanderont d'autres précautions avant d'être installés.

#### Comment ajouter le mod dans chacun des deux cas:

>#### Ajout de mods Modrinth
>
>Le modpack est principalement hébergé sur Modrinth, ce qui implique que quasiment tous les mods du modpacks en dépendent aussi. Ainsi, si vous voulez ajouter un mod depuis modrinth, c'est plutôt simple: cliquez sur ajouter **Télécharger un mod** et cherchez le mod que vous voulez ajouter depuis l'interface.


>#### Ajouter un mod depuis une autre source
>
>Ajouter un mod depuis une autre source est plus compliqué. Comme le mod sera en dur dans le pack téléchargeable, cela équivaut à une redistribution du mod, et il faut alors vérifier la license d'utilisation de celui-ci.
<br>
>*TODO: Ajouter la méthode pour vérifier et ajouter la license*

### Mettre à jour les mods

Il est facile de vérifier et appliquer les mises à jour de mods grâce au bouton dédié. Il est cepdendant important de vérifier que tous les mods dans le pack sont activés (la case cochée dans la liste) avant de faire la mise à jour, car les mods désactivés risquent d'être dédoublés.

### Ajout ou modification de configuration par défaut

Dans les fichiers de l'instance, vous pouvez trouver le dossier **config/yosbr**. Ce dossier contient une arborescence de fichier par défaut à appliquer si jamais un de ces fichiers n'existe pas dans l'instance au moment du lancement du jeu. C'est donc là que se trouve la **Configuration par défaut** du modpack.

<br>

Pour l'éditer, il est conseillé de changer la configuration de minecraft depuis le jeu, puis aller chercher les fichiers de configuration modfifiés et les copier dans le répertoire correspondant sous le dossier yosbr.

### Suppression de mod

Un mod peut-être supprimé tant qu'aucun autre mod n'en dépend. Si vous effectuez une telle opération, n'oubliez pas de supprimer les fichiers de configuration par défaut asscoiés dans la dossier config/yosbr (ils peuvent être gardés si la suppression est temporaire).

## Release d'une version du modpack

### Vérifications et actions à effectuer avant l'export

#### Changement de version

La version du modpack est affichée dans le menu principal du jeu. Il faut la changer manuellement avant d'exporter le modpack en dehors du launcher. Voici comment faire:

1. Faire apparaitre la barre d'édition de Fancy Menu

![Afficher barre d'édition](images/display_edit_bar.png)

2. Current Menu -> Layouts -> Manage layouts -> HerobrineMainMenu -> Edit

![Editer HerobrineMainMenu](images/edit_herobrine_main_menu.png)

3. Clic droit sur le texte de version en bas à gauche, puis "Set Text Content"

![Set text](images/set_version_text.png)

4. Layout -> Save puis Layout -> Exit, sans oublier de refaire Ctrl + Alt + C avant de quitter pour désactiver la barre d'édition.

#### Vérification que la barre d'édition de FancyMenu est bien désactivée

Si une barre d'édition apparait au sommet du menu principal, désactivez la avec Ctrl + Alt + C.

#### Vérifier la configuration

- Vérifier qu'il n'y a aucun conflit de touches dans la configuration
- Pour que les modifications de configuration arrive à l'utilisateur finale, elles doivent être dans le dossier par défaut (changements de touches compris)

*TODO: Fichier répertoriant les configurations en dure et celles mises par défaut à vérifier (chaque mod concerné, placement des RP dans la liste, configuration des touches dans options.txt + fichier de config amecs, FancyMenu et autres mods avec config forcée...)*

#### Vérifier les packs de ressource

Avec tous les mods activés:

- Vérifier que les items de base du pack de ressource de Herobrine.fr fonctionnent (Example: Grande Torche, épées... ect)
- Vérifier que les items de pack de ressources ajoutés pour le modpack fonctionnent (Example: Lanterne)
- Vérifier que les packs de ressources ajoutés pour le modpack apparaissent bien à jour

#### Vérification du fonctionnement des mods

Avec tous les mods activés, vérifiez:
- Que le jeu est jouable avec les performances attendues
- Que la première personne est bien celle du mod FirstPersonModel (on doit voir ses pieds en baissant la tête)