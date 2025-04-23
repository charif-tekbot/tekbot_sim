from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch_ros.actions import LifecycleNode



def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    maze_and_robot_path = PathJoinSubstitution(
        [FindPackageShare("maze_solving"),
        "launch",
        "tekbot_maze.launch.py"])
    maze_and_robot_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource([maze_and_robot_path]))

    slam_params_file = PathJoinSubstitution(
        [FindPackageShare('maze_solving'), 'config', ('mapper_params_online_async.yaml')]
    )
    
    slam_toolbox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('slam_toolbox'),
                'launch',
                'online_async_launch.py'
            ])
        ]),
        launch_arguments={
            'slam_params_file': slam_params_file,
            'use_sim_time': use_sim_time,
        }.items()
    )
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['-d', '/opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz']
    )
    
    nav2_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('nav2_bringup'),
                'launch',
                'navigation_launch.py'
            ])
        ]),
        launch_arguments={
            'use_sim_time': use_sim_time,
        }.items()
    )

    ld = LaunchDescription()
    ld.add_action(rviz_node)
    ld.add_action(maze_and_robot_launch)
    ld.add_action(nav2_bringup_launch)
    ld.add_action(slam_toolbox_launch)

    return ld
