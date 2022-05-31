from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
import numpy
import os


class PublisherFoto():

    def predict(imagen):
        os.system('python --version')
        os.system('pwd')

        #importante: especificar la ruta absoluta del modelo (o la relativa según salga por
        #pantalla)
        # TODO: hay que poner bien la ruta
        model = load_model('/home/alumno/catkin_ws/src/hamponator/src/hamponator/hamponator_ia/resource/modelo.h5')

        predictions = model.predict(imagen)

        return predictions

    