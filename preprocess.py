from os import listdir
from os import makedirs
from numpy import asarray
from numpy import save
from shutil import copyfile
from random import seed
from random import random
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# save pre-processed images into standard directories (slower, but can run on most PC)
def to_folder():
# create directories
    dataset_home = 'dataset_dogs_vs_cats/'
    subdirs = ['train/', 'test/']
    for subdir in subdirs:
        # create label subdirectories
        labeldirs = ['dogs/', 'cats/']
        for labldir in labeldirs:
            newdir = dataset_home + subdir + labldir
            makedirs(newdir, exist_ok=True)
    # seed random number generator
    seed(1)
    # define ratio of pictures to use for validation
    val_ratio = 0.25
    # copy training dataset images into subdirectories
    src_directory = 'train/'
    for file in listdir(src_directory):
        src = src_directory + '/' + file
        dst_dir = 'train/'
        if random() < val_ratio:
            dst_dir = 'test/'
        if file.startswith('cat'):
            dst = dataset_home + dst_dir + 'cats/'  + file
            copyfile(src, dst)
        elif file.startswith('dog'):
            dst = dataset_home + dst_dir + 'dogs/'  + file
            copyfile(src, dst)

# save pre-processed images into a single NumPy array (faster, but require a lot of RAM)
def to_array():
    # load dogs vs cats dataset, reshape and save to a new file
    # define location of dataset
    folder = 'train/'
    photos, labels = list(), list()
    # enumerate files in the directory
    for file in listdir(folder):
        # determine class
        output = 0.0
        if file.startswith('cat'):
            output = 1.0
        # load image
        photo = load_img(folder + file, target_size=(200, 200))
        # convert to numpy array
        photo = img_to_array(photo)
        # store
        photos.append(photo)
        labels.append(output)
    # convert to a numpy arrays
    photos = asarray(photos)
    labels = asarray(labels)
    print(photos.shape, labels.shape)
    # save the reshaped photos
    save('dogs_vs_cats_photos.npy', photos)
    save('dogs_vs_cats_labels.npy', labels)

