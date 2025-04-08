  GNU nano 8.1                                                              tekbot_maze.launch.py                                                                       
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():

    # Configure model path for Gazebo
    model_path = PathJoinSubstitution(
        [FindPackageShare("maze_solving"), "models"]
    )
    
    gz_model = SetEnvironmentVariable(
            name='GAZEBO_MODEL_PATH',
            value=model_path
    )
    
    # Path to the maze world
    world_file = PathJoinSubstitution(
        [FindPackageShare("maze_solving"),
        "worlds",
        "maze_4_metal_6x6.world"],
    )

    # Include the gazebo launch file from maze_solving
    gazebo_launch = PathJoinSubstitution(
        [FindPackageShare("maze_solving"),
        "launch",
        "empty_world.launch.py"],
    )


^G Aide         ^O Écrire	^F Chercher     ^K Couper	^T Exécuter     ^C Emplacement  M-U Annuler     M-A Marquer     M-] -> Crochet  M-B Précédent
^X Quitter	^R Lire fich.   ^\ Remplacer    ^U Coller	^J Justifier    ^/ Aller ligne  M-E Refaire     M-6 Copier	^B Retrouver    M-F Suivant
