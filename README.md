# TRC ROS2 Training
## How to use this simulator ?

Clone the repository :

```bash
git clone https://github.com/charif-tekbot/tekbot_sim.git
```
Compile the contained packages using the configure script.
This will create and build a workspace `tekbot_ws` and move to it root (it also manages sourcing).

```bash
cd tekbot_sim
chmod +x configure.sh (optional)
source configure.sh
```


Launch `tekbot` in an empty word:

```bash
ros2 launch tekbot_description gazebo.launch.py
```

Visualize the maze environment:

```bash
ros2 launch maze_solving maze.launch.py
```
Launch the Robot in the maze environment:

```bash
ros2 launch maze_solving tekbot_maze.launch.py
```

*Exercise 1*(already done): Spawn the robot in the maze environnement at a desired position

*Exercie 2* (already done): Create a package named `tekbot_control` and perfom teleoperation and localization task using the native packages `teleop_joy` and `robot_localization`.
To install them :
```bash
sudo apt install ros-humble-robot-localization
sudo apt install ros-humble-teleop-twist-joy
```

*Exercie 3*: Escape from the maze environment using `slam_toolbox` and `nav2` packages.


## Tips pour Déboguer avec RQt dans ROS

RQt est un outil puissant et polyvalent pour superviser et déboguer vos systèmes basés sur ROS. Il permet de regrouper plusieurs outils GUI dans une seule fenêtre, offrant une vue d'ensemble de l'architecture ROS en temps réel. Voici quelques conseils pour l'utiliser efficacement.

Pour installer RQt et tous ses plugins, exécutez la commande suivante dans un terminal :
```bash
sudo apt install ros-humble-rqt*
```

### Utilisation de Base
Une fois que vous avez lancé un fichier launch, ouvrez RQt dans un autre terminal avec la commande :
```bash
rqt
```

**Remarque :** Lors de la première utilisation, la fenêtre RQt apparaîtra vide. Vous devrez ajouter manuellement les plugins nécessaires selon vos besoins (la config est conservée lors des prochains lancement).

### Plugins Recommandés
Pour une configuration de base efficace, nous recommandons les plugins suivants :

#### 1. Node Graph
- **Localisation :** `Plugins → Introspection → Node Graph`
- **Description :** Permet de visualiser la structure des nodes et leurs connexions. (fac. Choisir Nodes/Topics(all) et coché Debug ; mettez Group à 4 pour regrouper les parties du graphe)

#### 2. Topic Monitor
- **Localisation :** `Plugins → Topics → Topic Monitor`
- **Description :** Affiche la liste des topics actifs avec leurs fréquences de publication et la structure des messages. Utile pour comprendre comment les données sont formatées et pour diagnostiquer des problèmes de fréquence.

#### 3. TF Tree
- **Localisation :** `Plugins → Visualization → TF Tree`
- **Description :** Affiche en temps réel l'arbre des transformations (TF). Ce plugin est crucial pour diagnostiquer les erreurs liées aux repères manquants ou aux problèmes d'asynchronisme entre les frames.


Au premier lancement, les fenêtres de ces outils se logeront partout sur la fenêtre principale mais vous pouvez les superposés et obtenir un menu horizontal en bas permettant de naviguer entre les outils.

