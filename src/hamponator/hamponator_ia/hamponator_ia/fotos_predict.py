from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.utils import to_categorical,get_file,load_img,img_to_array
from tensorflow.keras.models import load_model
from tensorflow.image import rgb_to_grayscale
from tensorflow import expand_dims
import numpy
import os
import cv2
import sys

class PublisherFoto():

    def predict(imagen_url):
        os.system('python --version')
        os.system('pwd')

        image = cv2.imread(imagen_url)

        img = load_img(
            imagen_url, target_size=(250, 250)
        )
        gray = rgb_to_grayscale(img)


        img_array = img_to_array(gray)
        img_array = expand_dims(img_array, 0) # Create a batch

        #importante: especificar la ruta absoluta del modelo (o la relativa según salga por
        #pantalla)
        # TODO: hay que poner bien la ruta
        model = load_model('/home/adrian/Documentos/hamponator_piton/src/hamponator/hamponator_ia/resource/modelo.h5')

        predictions = model.predict(img_array)

        return predictions

    