# ROS docs

Luis Belloch

## Robot real

[Probando el robot real](https://colab.research.google.com/drive/1dc1PBZNsL8rUADrzLir6FyPiXx4DY4pO?usp=sharing)

Desde la red TP_LINK-6CAE (pass: 41422915)
```
# variables de entorno
export ROS_DOMAIN_ID=30
export TURTLEBOT3_MODEL=burger

# conexión por la ip
ssh ubuntu@192.168.0.62

#[Terminal SSH]
ros2 launch turtlebot3_bringup robot.launch.py
```

## Escanear el entorno físico a mano

[SLAM en simulación](https://colab.research.google.com/drive/1fiTmWS5oSXNJQX8pPo5fWbYyJGpt4l7Z?usp=sharinghttps%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1fiTmWS5oSXNJQX8pPo5fWbYyJGpt4l7Z%3Fusp%3Dsharing)

```
#[Terminal2]
ros2 run turtlebot3_teleop teleop_keyboard

#[Terminal3]
ros2 launch turtlebot3_cartographer cartographer.launch.py
```

### Guardar el mapa

Queda guardado en el directorio HOME el .pgm y el .yaml. Después pueden editarse para
arreglar errores.

```
#[Terminal5]
ros2 run nav2_map_server map_saver_cli -f ~/my_map
```

### Mostrar nodos activos

Hay que tener en cuenta que de base no se muestran todos. Normalmente hay que activar
Plugins -> Introspection -> Node Graph 

```
ros2 run rqt_gui rqt_gui
```

## Simulació enn Gazebo

### Abrir un mapa vacío en Gazebo

```
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

### Colcon build

Al hacer un build hay que tener en cuenta que los archivos Setup.py y Package.xml estén
bien escritos. Los errores no se muestran y pueden ser fatales.

```
colcon build --packages-select [nombre]
```

## Mensajes ROS - Firebase

### Mensaje del robot 

- id: identificador para los mensajes, será el mismo a pares seguido de -app/-web (define el origen).
- time: usado para sincronizar los mensajes y comprobar mensajes nuevos.
```
"dsiaghew98u43oifhe-app" = {
    time: 1235125153,
    connection_data: {
        connected: true,
        ros: {[datos de conexión del robot]},
        rosbridge_access: [ip del robot]"
    },
    msg: {
        odom: [mensage odom],
        goalpose: [mensage goalpose],
        etc...
    }
}
```

```
"dsiaghew98u43oifhe-web" = {
    time: 14362373264,
    msg: {
        goalpose: [msg goalpose],
        etc...
    }
}
```