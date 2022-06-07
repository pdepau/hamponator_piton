from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hamponator_ia',
            executable='hamponator_ia',
            output='screen'),
    ])