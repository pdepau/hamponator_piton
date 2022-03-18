import os
from glob import glob
from setuptools import setup


package_name = 'my_nav2_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*.pgm')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),  
        (os.path.join('share', package_name, 'config'), glob('config/*.lua')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')), 
        (os.path.join('share', package_name, 'config'), glob('config/*.xml')) 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lbelmar',
    maintainer_email='lbelmar@alumno.upv.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Ejecuta el sistema de posicion inicial 
           'initial_pose_pub = my_nav2_system.initial_pose_pub:main'
        ],
    },
)
