# hamponator_piton

## Escanear el entorno físico a mano
SLAM en simulación
```
#[Terminal2]
ros2 run turtlebot3_teleop teleop_keyboard
```
```
#[Terminal3]
ros2 launch turtlebot3_cartographer cartographer.launch.py
```
Guardar el mapa
Queda guardado en el directorio HOME el .pgm y el .yaml. Después pueden editarse para arreglar errores.
```
#[Terminal5]
ros2 run nav2_map_server map_saver_cli -f ~/my_map
```
Mostrar nodos activos
Hay que tener en cuenta que de base no se muestran todos. Normalmente hay que activar Plugins -> Introspection -> Node Graph
```
ros2 run rqt_gui rqt_gui
Simulación en Gazebo
Abrir un mapa vacío en Gazebo
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo empty_world.launch.py
```
## Colcon build
Al hacer un build hay que tener en cuenta que los archivos Setup.py y Package.xml estén bien escritos. Los errores no se muestran y pueden ser fatales.
```
colcon build --packages-select [nombre]
```