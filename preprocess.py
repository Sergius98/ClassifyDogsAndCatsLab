from os import listdir
from os import makedirs
from numpy import asarray
from numpy import save
from shutil import copyfile
from random import seed
from random import random
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# save final pre-processed images into standard directories (slower, but can run on most PC)
def to_final_folder(src_directory='train/', dataset_home='finalize_dogs_vs_cats/',
              cat_tag='cat', dog_tag='dog',
              subdirs=['train/', 'test/'], labeldirs=['dogs/', 'cats/']):
    for labldir in labeldirs:
        newdir = dataset_home + labldir
        makedirs(newdir, exist_ok=True)
    for file in listdir(src_directory):
        src = src_directory + '/' + file
        if file.startswith(cat_tag):
            dst = dataset_home + 'cats/' + file
            copyfile(src, dst)
        elif file.startswith(dog_tag):
            dst = dataset_home + 'dogs/' + file
            copyfile(src, dst)


to_final_folder()
