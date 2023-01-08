import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.models import load_model

# Path for train, validation and test datasets
train_path = 'Dataset/training_set'
valid_path = 'Dataset/test_set'
test_path = 'Dataset/val'

IMAGE_SIZE = [224, 224]

folders = glob('Dataset/training_set/*')



train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)


training_set = train_datagen.flow_from_directory('Dataset/training_set',
                                                 target_size = (224, 224),
                                                 batch_size = 16,
                                                 class_mode = 'categorical')


test_set = test_datagen.flow_from_directory('Dataset/test_set',
                                            target_size = (224, 224),
                                            batch_size = 16,
                                            class_mode = 'categorical')


vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights=None, include_top=False)


for layer in vgg.layers:
  layer.trainable = False

x = Flatten()(vgg.output)
prediction = Dense(len(folders), activation='softmax')(x)


model = Model(inputs=vgg.input, outputs=prediction)

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(training_set, validation_data=test_set, epochs=20, batch_size=32)

model.save('FlowerClassification_VGG16.h5')
