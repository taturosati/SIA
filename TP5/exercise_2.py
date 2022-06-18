import tensorflow
import numpy
from PIL import Image

encoder = tensorflow.keras.models.load_model("VAE_encoder.h5", compile=False)
decoder = tensorflow.keras.models.load_model("VAE_decoder.h5", compile=False)

# Preparing MNIST Dataset
(x_train, y_train), (x_test, y_test) = tensorflow.keras.datasets.mnist.load_data()
x_test = x_test.astype("float32") / 255.0

x_test = numpy.reshape(x_test, newshape=(x_test.shape[0], x_train.shape[1], x_train.shape[2], 1))

encoded_data = encoder.predict(x_test)

number_indexes = numpy.random.choice(encoded_data.shape[0], 5, replace=False)
number_data = encoded_data[number_indexes]
encoded_data_x = number_data[:, 0]
encoded_data_y = number_data[:, 1]

decoded_data = decoder.predict(numpy.array([[numpy.average(encoded_data_x), numpy.average(encoded_data_y)]]))

decoded_img = decoded_data[0] * 255.0
img = Image.fromarray(decoded_img.reshape(28, 28).round(0).astype("uint8"))
img.save("out.png")
