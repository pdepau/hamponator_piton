from setuptools import setup
import os #incluir
from glob import glob #incluir

package_name = 'lidar_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')) #incluir
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lbelmar', 
    maintainer_email='lbelmar@alumno.upv.es', 
    description='TODO: Creando un nodo que se subscribe al topic /scan',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_subscriber = lidar_subscriber.lidar_subscriber:main' #incluir
        ],
    },
)
