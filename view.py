# plot dog photos from the dogs vs cats dataset
from matplotlib import pyplot
from matplotlib.image import imread


# plot images from dataset
def plot_images(folder, prefix):
    # plot first few images
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # define filename
        filename = folder + '/' + prefix + '.' + str(i) + '.jpg'
        # load image pixels
        image = imread(filename)
        # plot raw pixel data
        pyplot.imshow(image)
    # show the figure
    pyplot.show()
    pass


# define location of dataset
folder = 'train'
prefix_cat = 'cat'
prefix_dog = 'dog'

plot_images(folder, prefix_cat)
plot_images(folder, prefix_dog)
