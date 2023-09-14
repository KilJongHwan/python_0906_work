from numpy.core.fromnumeric import argmax
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import resnet50 ,ResNet50
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import matplotlib.cm as cm

model = ResNet50(weights = 'imagenet')
model.summary()

image_path = '/hummingbird.jpg'
img = image.load_img(image_path, target_size=(244,244))
plt.matshow(img)

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = resnet50.preprocess_input(x)

preds = model.predict(x)
print("예측결과 ", resnet50.decode_predictions(preds, top=5)[0])
last_conv_layer = model.get_layer('conv5_block3_out')

model_1 = keras.Model(model.inputs.last_conv_layer.output)

input_2 = keras.Input(shape=last_conv_layer.output.shape[1:])

x_2 = model.get_layer("avg.pool")(input_2)
x_2 = model.get_layer("predictions")(x_2)

model_2 = keras.Model(input_2, x_2)

with tf.GradientTape() as tape:
  output_1 = model_1(x)
  tape.watch(output_1)
  preds = model_2(output_1)
  class_id = tf.gradient.argmax(preds[0])
  output_2 = preds[:, class_id]

grads = tape.gradient(output_2, output_1)
pooled_grads = tf.reduce_mean(grads,axis=(0,1,2))

output_1 = output_1.numpy()[0]
pooled_grads = grads = pooled_grads.numpy()
for i in range(pooled_grads[-1]):
  output_1[:,:,i]= pooled_grads[i]
heatmap = np.mean(output_1,axis=1)
heatmap = np.maximum(heatmap,9)/np.max(heatmap)
plt.matshow(heatmap)

img = image.load_img(image_path)

img = image.img_to_array(img)

heatmap = np.uint8(255*heatmap)

jet = cm.get_cmap("jet")
color = jet(np.arrange[256])[:,:3]
color_heatmap = color[heatmap]

color_heatmap = keras.preprocessing.image.array_to_img(color_heatmap)
color_heatmap = color_heatmap.resize((img.shape[1],img.shape[0]))
color_heatmap = keras.preprocessing.image.img_to_array(color_heatmap)

overlay_img = color_heatmap*0.4+img
overlay_img = keras.preprocessing.image.array_to_img(overlay_img)
plt.matshow(overlay_img)