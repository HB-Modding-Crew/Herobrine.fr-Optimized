# Herobrine.fr - Optimized changelog
Ceci est le changelog pour le modpack Fabric [Herobrine.fr - Optimized](https://www.curseforge.com/minecraft/modpacks/herobrine-fr-optimized).

# 1.19.2

## 2.0.0-alpha.6 (2023-03-05)

<br>

### Fonctionnalités générales du modpack:

- Un bouton est maintenant disponible dans le menu principal de Minecraft pour **mettre a jour le pack de ressrouces HBCubemonde** ! (En cours d'intégration)
- Avec la **suppression de SkinSwapper**, **tous les mods** du modpack sont maintenant **compatibles entre eux** ! Vous pouvez activer les mods optionnels **sans crainte de conflits**.
- Toutes les **commandes dont vous ne vous souvenez jamais des keybinds** (Exemple: Recharger les shaders) sont maintenant accessibles via le mod **TooManyBinds**. *Appuyez sur **H** en jeux et testez* !

<br>

### Options:

- Changement des **KeyBinds** par défaut pour éviter les conflits de touches entre les mods. SERA FORCE SUR LA MISE A JOUR ! (vous perdrez donc vos en mettant à jour vers cette alpha).

<br>

- Désactivation de **MinecraftCapes** et des textures de la cape sur les elytras sur le mod **Capes**.
- Désactivation du port de l'épée en fourreau intégré de base avec **NotEnoughAnimations**.

<br>

### Mods:

- Suppresion de **SkinSwapper**. Incompatible avec NotEnoughAnimations et FirstPersonModel. Pourra éventuellement être réintégré dans une future version du modpack.
- Suppression de **NoFade**. Non mis à jour sur Modrinth, et peu d'utilité.
- Suppression de **Farsight**. Non mis à jour sur Modrinth, remplacé par Bobby.
- Suppression de **CustomSkinLoader**. La fonctionnalité de skin transparents est maintenant gérée par le mod **Entity Texture Features**.

<br>

- Update de **Fabric API**.
- Update de **Entity Texture Features**. Gère maintenant les skins transparents !

<br>

- Ajout de **Better Ping Display** !
- Ajout de **TooManyBinds** ! Permet d'avoir une barre de recherches pour les raccourcis clavier dont on ne se souvient pas. Exemple: Recharger les shaders.
- Ajout de **ClickThrough**. Permet de cliquer au travers des pannneaux et item frames pour accéder à vos coffres et autres conteneurs.
- Ajout du mod **Effective**, optionnel, **désactivé par défaut**.
- Ajout de **Perspective Mod Redux**, utile pour les sapères. Optionel, désactivé par défaut.
- Ajout de **Falling Leaves**, optionnel, **désactivé par défaut**.
- Ajout de **Camera Overhaul**, optionnel, **désactivé par défaut**.
- Ajout de **Raised**. Corrige la hauter de la barre d'items.
- Ajout de **Stendhal**, optionnel, **désactivé par défaut**. Sert pour laditions de livres et de panneaux.
- Ajout de **Bobby**, optionnel, **désactivé par défaut**. Garde les chunks chargés en mémoire pour voir plus loin.

<br>

## 2.0.0-alpha.5 (2023-02-17)

<br>

### Options:

- Désactivation de l'accès aux **menu de configuration** de Simple Discord RPC.
- Changement de baucoup de **touches par défaut** (activations de mods / fonctionalités, accès aux menus de mods, rechargements de shaders, etc.)

<br>

### Mods:

- Suppression de **More Chat History**. (Inutile avec le mod Advanced Chat Core).
- Suppression de **AntiGhost**.

<br>

- Ajout de **NotEnoughAnimations** et **FirstPersonModel** ! **Désactivés par défaut**. Attention ! **Incompatibles avec SkinSwapper**. Ne pas avoir SkinSwapper et NotEnoughAnimations/FirstPersonModel activés en même temps.
- Ajout de **BetterF3** !
- Ajout de **Skins Layers 3D** ! **Désactivé par défaut**.
- Ajout de **Amecs** ! Allows to use CTRL, ALT, SHIFT, etc. to create custom keybinds.

<br>

- Retour à une ancienne version de **YetAnotherConfigLib** pour résoudre des problèmes d'incompatibilité.

<br>

- **IBE Editor** est maintenant Optionel, **désactivé par défaut**.


## 2.0.0-alpha.4 (2023-02-12)

<br>

Cette mise à jour passe directement à une version majeure car les changements sont nombreux, que la façon de développer le modpack est en train de changer, avec des outils dédiés, et que la la mise à jour depuis d'anciennes versions du modpack n'est pas garantie de fonctionner comme prévue.

<br>

**!!! POUR UNE INSTALLATION PROPRE !!!** Préférez la création d'une nouvelle instance de minecraft plutôt que de mettre à jour l'ancienne.

Les utilisateurs du laucher minecraft vanilla devront se fier à l'installateur, qui installera l'instance automatiquement.

<br>

Principaux changements:
- Revue complète des options/configurations par défaut du modpack
- Ajout, mise à jour, et suppressions de beaucoup de mods
- Certains mods sont maintenant optionels ! Ils sont désactivés par défaut, et vous pouvez les activer seulement si vous le souhaitez !

- Update de Fabric ! Maintenant en 0.14.13

<br>

### Options:

<br>

- Nettoyage de la **configuration par défaut** (suppression de vieux fichiers inutiles, anciens mods déjà enlevés)

<br>

- Modifications de la configuration de **Advanced Tooltips** pour rendre les affichages moins lourds et plus RP. Restent activés par défaut:
    - Vue de l'**inventaire des shulkers**
    - **Preview du texte d'un panneau** déjà écrit dans l'inventaire
    - **Vue d'une map** dans l'inventaire
    - **Patternes de bannières**
- Désactivation des **élytres customisées** par la cape dans les options du mod **Fabric Capes**
- Changement du **volume sonore du jeu** quand la fenêtre du jeu n'est plus du tout visible: **0% -> 25%**
- Désactivation des **panneaux améliorés** dans **Enhanced Block Entities**. Cela cassait la fonctionalité de panneaux transparents.
- Désactivation de la **gestion de Entity Texture Feature** dans le mod **Puzzle** pour éviter un crash dans les menus.
- Désactivation des **skins transparents** dans Entity Texture Feature au bénéfice de CustomSkinLoader. Temporaire.

### Mods:

<br>

- Suppression de **Midnight Controls**. Personne ne l'utilise sur Herobrine.fr, prend de la place pour rien.
- Suppression de **LambdaBetterGrass**. Tout le monde n'aime pas le visuel, et n'est pas 100% comptaible avec le Resource Pack Hb.fr.
- Suppression de **Cull Clouds** !

<br>

- Update de **Fabric API**
- Update de **Entity Texture Features**
- Update de **Iris**
- Update de **Fabric Language Kotlin**
- Update de **FabricSkyboxes**
- Update de **FabricSkyBoxes Interop**
- Update de **Farsight**
- Update du **Mod Menu**
- Update de **Zoomify**
- Update de **Sodium**
- Update de **Sodium Extra**
- Update de **Reese's Sodium Options**
- Update de **Lithium**
- Update de **Language Reload**
- Update de **LambDynamicLights**
- Update de **YetAnotherConfigLib**

<br>

- Ajout **temporaire** de **CustomSkinLoader** pour enfin voir le moignon de Na'Kaar, en attendant que Entity Texture Features gère les skins transparents sans avoir besoin de marqueur sur le skin (voir https://github.com/Traben-0/Entity_Texture_Features/issues/142 pour plus d'informations). **Désactivé par défaut** car il cause des problèmes de chargement de skin.
- Ajout de **AdaptiveTooltips**
- Ajout du mod **AriKeys**. **Désactivé par défaut** car il n'a pour l'insstant aucun effet.
- Ajout de **SkinSwapper**, **désactivé par défaut** !
- Ajout de **Presence Footstep**, **désactivé par défaut** !
- Ajout de **Advanced Chat Core** et **Advanced Chat HUD**, **désactivés par défaut** !
- Ajout de **Dynamic Surrounding**, **désactivé par défaut** !
- Ajout de **Fancy Menu** ! Merci à Sylakbe pour son trailer épique !
- Ajout de **Simple Discord RPC** !
- Ajout de **IBE Editor** !

<br>

- **Advanced Tooltips** est maintenant **désactivé par défaut** !
- **Farsight** est maintenant **désactivé par défaut** !

---

## 1.0.4 (2022-12-03)

Mods mis à jour:
- Fabric API: 0.66.0 -> 0.67.1
- Fabric Language Kotlin: 1.8.6 -> 1.8.7
- FerriteCore: 5.0.0 -> 5.0.3
- Iris Shaders: 1.4.2 -> 1.4.3

Mods:
- Ajout de Advanced Tooltips

Options:
- Le pack de ressources de MidnightControl n'est plus activé par défaut
- Désactivation de certaines options par défaut de Advanced ToolTips

---

### 1.0.3 (2022-11-21)

Modrinth:
- La configuration est enfin inclue dans le modpack

Mod Menu Helper:
- Logo changé pour celui du HbModdingCrew

Options:
- Jeu passé en français par défaut

---

### 1.0.2 (2022-11-20)

Mods:
- Update de certains mods
- Mod Cull Clouds ajouté
- Mod Builtin Servers ajouté

Contenus:
- Ajout du pack de texture hivers

Configuration:
- CIT: N'autorise plus les broken path
- Enhanced Block Entity: Activation des smooth lighting
- ETF: Activation des skins transparents
- ETF: Désactivation du clignement des yeux des mobs
- ETF: Désactivation des broken path
- Lambda better Grass: Désactivation (vote à effectuer pour savoir si il est à garder ou non)
- LambDynamicLight: Lumières dynamiques détaillées.
- LambDynamicLight: Lumières dynamiques d'entités.
- LambDynamicLight: Désactivation de la sensibilité à l'eau
- Builtin Servers: Herobrine.fr ajouté comme serveur par défaut

Structure de projet:
- Ne copie plus le options.txt de l'instance pour les mises à jour, utilisation de config/yosbr.options.txt à la place

---

### 1.0.1 (2022-11-18)

Remaniement du mod pack pour être plus adapté à Herobrine.fr.

Changements mineurs:
- Changement de certaines configurations
- Changement du nom de modpack dans le menu principal

Changements majeurs:
- Suppression de AdvancementInfo qui ne sert à rien dans le cadre du roleplay
- Traduction complète du ressource pack Mod Menu Helper en Français
- Ajout de Herobrine.fr dans la liste de serveurs par défaut

---

### 1.0.0 (2022-11-17)

- Fork de Fabulously Optimized.
- Modifications du fork pour avoir une compatibilité complète avec Herobrine.fr
- Première release pour entamer le processus de développement