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

# save pre-processed images into standard directories (slower, but can run on most PC)
def to_folder(src_directory='train/', dataset_home='dataset_dogs_vs_cats/',
              cat_tag='cat', dog_tag='dog',
              subdirs=['train/', 'test/'], labeldirs=['dogs/', 'cats/']):
    # create directories
    for subdir in subdirs:
        # create label subdirectories
        for labldir in labeldirs:
            newdir = dataset_home + subdir + labldir
            makedirs(newdir, exist_ok=True)
    # seed random number generator
    seed(1)
    # define ratio of pictures to use for validation
    val_ratio = 0.25
    # copy training dataset images into subdirectories
    for file in listdir(src_directory):
        src = src_directory + '/' + file
        dst_dir = 'train/'
        if random() < val_ratio:
            dst_dir = 'test/'
        if file.startswith(cat_tag):
            dst = dataset_home + dst_dir + cat_tag + 's/' + file
            copyfile(src, dst)
        elif file.startswith(dog_tag):
            dst = dataset_home + dst_dir + dog_tag + 's/' + file
            copyfile(src, dst)


# save pre-processed images into a single NumPy array (faster, but require a lot of RAM)
def to_array(folder='train', cat_tag='cat', dog_tag='dog'):
    # load dogs vs cats dataset, reshape and save to a new file
    # define location of dataset
    folder += '/'
    photos, labels = list(), list()
    # enumerate files in the directory
    for file in listdir(folder):
        # determine class
        if file.startswith(dog_tag):
            output = 0.0
        elif file.startswith('cat'):
            output = 1.0
        else:
            raise Exception("found a file that belongs to neither classes : " + file)
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


to_folder()
