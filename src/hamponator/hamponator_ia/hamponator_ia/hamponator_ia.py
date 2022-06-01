from fotos_predict import *
import cv2
from cv_bridge import CvBridge, CvBridgeError

import rclpy
# importar ROS2 python lib
from rclpy.node import Node
# importar Odometry desde la interface nav_msgs
from nav_msgs.msg import Odometry,Path
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped
from lifecycle_msgs.msg import TransitionEvent
from visualization_msgs.msg import MarkerArray
from std_msgs.msg import String
# importar la librería de calidad del servicio para fijar las políticas de calidad
from rclpy.qos import ReliabilityPolicy, QoSProfile

class SimpleSubscriber(Node):

    def __init__(self):
        # constructor
        #  super() ininicializa el Nodo
        super().__init__('simple_subscriber')

        self.bridge_object = CvBridge()
        self.image_sub = self.create_subscription(Image,'/camera/image_raw',self.camera_callback,QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
        self.publisher_ = self.create_publisher(String, 'resultado', 10)
        # crear el objeto subscriptor
        # al topic /odom topic wcon una cola de 10 messages.
        # create_subscription(msg_type, topic, callback, qos_profile, callback_group, event_callbacks, raw)
        self.subscriber= self.create_subscription(
            String,
            '/analizar',
            self.listener_callback,
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)) 
        # prevent unused variable warning
        self.subscriber    
        self.subscriber2= self.create_subscription(
            String,
            '/resultado',
            self.listener_callback2,
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)) 
        # prevent unused variable warning
        self.subscriber2     

    def listener_callback(self, msg):
        #cv2.waitKey(0)
        print(msg)
        resultado = PublisherFoto.predict('src/hamponator/hamponator_ia/hamponator_ia/foto.jpg')
        mensaje = String()
        mensaje.data=str(resultado)
        print(mensaje)
        self.publisher_.publish(mensaje)

    def listener_callback2(self, msg):
        print(msg)
        
    def camera_callback(self,data):

        try:
            # Seleccionamos bgr8 porque es la codificacion de OpenCV por defecto
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
            #cv2.imwrite('src/hamponator/hamponator_ia/hamponator_ia/foto.jpg', cv_image)
        except CvBridgeError as e:
            print(e)
        

def main(args=None):
    # inicializa la comunicacion ROS2
    rclpy.init(args=args)
    # declara el nodo
    simple_subscriber = SimpleSubscriber()
    # dejamos abierto el nodo hasta ctr+c
    rclpy.spin(simple_subscriber)
    # Destruimos el nodo
    simple_subscriber.destroy_node()
    # se cierra la comunicacion ROS2
    rclpy.shutdown()

if __name__ == '__main__':
    main()