from tensorflow.keras.layers import Input, Lambda, Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.models import Sequential
import numpy as np
from glob import glob

IMAGE_SIZE = [224, 224]

train_path = '/Users/vamshibukya/Desktop/pythonProject/Datasets/Train'
valid_path = '/Users/vamshibukya/Desktop/pythonProject/Datasets/Test'

resnet = ResNet50(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)


for layer in resnet.layers:
    layer.trainable = False

folders = glob('/Users/vamshibukya/Desktop/pythonProject/Datasets/Train/*')

x = Flatten()(resnet.output)

prediction = Dense(len(folders), activation='softmax')(x)

# create a model object
model = Model(inputs=resnet.input, outputs=prediction)

# tell the model what cost and optimization method to use
model.compile(
  loss='categorical_crossentropy',
  optimizer='adam',
  metrics=['accuracy']
)


from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)


# Make sure you provide the same target size as initialied for the image size
training_set = train_datagen.flow_from_directory('/Users/vamshibukya/Desktop/pythonProject/Datasets/Train',
                                                 target_size = (224, 224),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')



test_set = test_datagen.flow_from_directory('/Users/vamshibukya/Desktop/pythonProject/Datasets/Test',
                                            target_size = (224, 224),
                                            batch_size = 32,
                                            class_mode = 'categorical')


# fit the model
# Run the cell. It will take some time to execute
r = model.fit_generator(
  training_set,
  validation_data=test_set,
  epochs=50,
  steps_per_epoch=len(training_set),
  validation_steps=len(test_set)
)

# save it as a h5 file

from tensorflow.keras.models import load_model

model.save('model_resnet50.h5')

y_pred = model.predict(test_set)

y_pred = model.predict(test_set)

import numpy as np
y_pred = np.argmax(y_pred, axis=1)

print(y_pred)

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


model=load_model('model_resnet50.h5')

img=image.load_img('/Users/vamshibukya/Desktop/pythonProject/frame_807.jpg',target_size=(224,224))

x=image.img_to_array(img)

x.shape
x=x/255
import numpy as np
x=np.expand_dims(x,axis=0)
img_data=preprocess_input(x)
img_data.shape
print(model.predict(img_data))


a=np.argmax(model.predict(img_data), axis=1)




