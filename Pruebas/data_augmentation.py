# Importing necessary functions
from PIL import Image
from numpy import asarray
import os
from os import listdir
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range = 40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        brightness_range = (0.5, 1.5),
        fill_mode='nearest')
    
folder_dir = './fotos_para_duplicar'

for images in os.listdir(folder_dir):
    if (images.endswith(".jpg")):
        image = Image.open(folder_dir + '/' + images)
        x = asarray(image)
        x = x.reshape((1, ) + x.shape)
        i = 0
        for batch in datagen.flow(x, batch_size = 1,
                                  save_to_dir ='./fotos_nuevas', 
                                  save_prefix ='data', save_format ='jpeg'):
            i += 1
            if i > 5:
                break
