import rclpy
# importar ROS2 python lib
from rclpy.node import Node
# importamos LaserScan desde senros_msgs
from sensor_msgs.msg import LaserScan
# importar la librería de calidad del servicio para fijar las políticas de calidad
from rclpy.qos import ReliabilityPolicy, QoSProfile
# Necesario para el scanner https://github.com/ROBOTIS-GIT/turtlebot3_simulations/issues/85#issuecomment-749194092
from rclpy.qos import qos_profile_sensor_data

class LidarSubscriber(Node):

    def __init__(self):
        # constructor
        #  super() ininicializa el Nodo
        super().__init__('lidar_subscriber')
        # crear el objeto subscriptor
        # al topic /odom topic wcon una cola de 10 messages.
        # create_subscription(msg_type, topic, callback, qos_profile, callback_group, event_callbacks, raw)
        self.subscriber = self.create_subscription(
                LaserScan,
                'scan',
                self.scan_callback,  # function to run upon message arrival
                qos_profile_sensor_data)  # allows packet loss
        # prevent unused variable warning
        self.subscriber       

    def scan_callback(self, msg):
        # imprime los datos leídos       
        self.get_logger().info('Se está recibiendo "%s"' % str(msg))

def main(args=None):
    # inicializa la comunicacion ROS2
    rclpy.init(args=args)
    # declara el nodo
    lidar_subscriber = LidarSubscriber()
    # dejamos abierto el nodo hasta ctr+c
    rclpy.spin(lidar_subscriber)
    # Destruimos el nodo
    lidar_subscriber.destroy_node()
    # se cierra la comunicacion ROS2
    rclpy.shutdown()

if __name__ == '__main__':
    main()