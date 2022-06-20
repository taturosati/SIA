import tensorflow
import numpy
from PIL import Image
from sampling import Sampling

encoder = tensorflow.keras.models.load_model("VAE_encoder.h5", compile=False, custom_objects={"Sampling": Sampling})
decoder = tensorflow.keras.models.load_model("VAE_decoder.h5", compile=False, custom_objects={"Sampling": Sampling})
img_size = 32
num_channels = 1
# # Preparing MNIST Dataset
# (x_train, y_train), (x_test, y_test) = tensorflow.keras.datasets.mnist.load_data()
# x_test = x_test.astype("float32") / 255.0

dataset_size = 151
pokemon_dataset = numpy.zeros((dataset_size, img_size, img_size, num_channels))
for i in range(dataset_size):
    img_name = "pokemon_dataset/" + str(i+1) + ".png"
    img = Image.open(img_name).convert("L")
    arr = numpy.array(img)
    arr.resize((img_size, img_size, num_channels))
    pokemon_dataset[i] = arr / 255.0

x_train = pokemon_dataset 
x_test = pokemon_dataset

x_test = numpy.reshape(x_test, newshape=(x_test.shape[0], x_train.shape[1], x_train.shape[2], 1))

encoded_data = encoder.predict(x_test)
encoded_data = encoded_data[0]
number_indexes = numpy.random.choice(encoded_data.shape[0], 3, replace=False)
number_data = encoded_data[number_indexes]
new_pokemon_encoded = [numpy.average(number_data[:, i]) for i in range(encoded_data.shape[1])]


# decoded_data = decoder.predict(numpy.array([[numpy.average(encoded_data_x), numpy.average(encoded_data_y)]]))
decoded_data = decoder.predict(encoded_data)

for i in range(len(decoded_data)):

    decoded_img = decoded_data[i] * 255.0
    img = Image.fromarray(decoded_img.reshape(img_size, img_size))
    img = img.convert("RGB")
    img.save("out/" + str(i) + ".png")

new_pokemon = decoder.predict(numpy.array([new_pokemon_encoded]))[0] * 255.0
img = Image.fromarray(new_pokemon.reshape(img_size, img_size))
img = img.convert("RGB")
img.save("new_pokemon.png")


