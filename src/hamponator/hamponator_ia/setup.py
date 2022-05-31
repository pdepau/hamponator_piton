from setuptools import setup

package_name = 'hamponator_ia'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lbelmar@alumno.upv.es',
    maintainer_email='lbelmar@alumno.upv.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hemponator_ia=hamponator_ia.fotos_predict:main'
        ],
    },
)
