# coding=utf-8
########################################################################################
# Author: Ujash Joshi, University of Toronto, 2017                                     #
# Based on Octave implementation by: Benjamin Eltzner, 2014 <b.eltzner@gmx.de>         #
# Octave/Matlab normxcorr2 implementation in python 3.5                                #
# Details:                                                                             #
# Normalized cross-correlation. Similiar results upto 3 significant digits.            #
# https://github.com/Sabrewarrior/normxcorr2-python/master/norxcorr2.py                #
# http://lordsabre.blogspot.ca/2017/09/matlab-normxcorr2-implemented-in-python.html    #
########################################################################################


import numpy as np
from scipy.signal import fftconvolve
from PIL import Image
from cv2 import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    template = np.asarray(Image.open("NEW_Phenocam_Processing_PY_codes\pictures\\trunk_matching_part.jpg"))
    image = np.asarray(Image.open("NEW_Phenocam_Processing_PY_codes\pictures\\2012-07-10-1100.jpg"))
    print ("temp:",np.ndim(template), template.shape,"image:",np.ndim(image), image.shape)
    temp_shape = [s for s in template.shape]
    temp_shape.pop(2)
    c = normxcorr2(template,image)
    absC = np.absolute(c)
    imax = np.argmax(absC)
    c_max = np.amax(absC)
    shape = [c for c in c.shape]
    shape.pop(2)
    peak = ind2sub(shape, imax)
    corr_offset = [peak[1] - temp_shape[0], peak[0] - temp_shape[1]]
    x1 = corr_offset[0]
    y1 = corr_offset[1]
    print ("shape c:",shape,"xy:", (x1,y1), "shape matching:",temp_shape, "peak:",peak, "imax:",imax, "c_max:", c_max)
    display(image, (x1,y1), temp_shape)


def normxcorr2(template, image, mode="valid"):
    """
    Input arrays should be floating point numbers.
    :param template: N-D array, of template or filter you are using for cross-correlation.
    Must be less or equal dimensions to image.
    Length of each dimension must be less than length of image.
    :param image: N-D array
    :param mode: Options, "full", "valid", "same"
    full (Default): The output of fftconvolve is the full discrete linear convolution of the inputs. 
    Output size will be image size + 1/2 template size in each dimension.
    valid: The output consists only of those elements that do not rely on the zero-padding.
    same: The output is the same size as image, centered with respect to the ‘full’ output.
    :return: N-D array of same dimensions as image. Size depends on mode parameter.
    """

    # If this happens, it is probably a mistake
    if np.ndim(template) > np.ndim(image) or \
            len([i for i in range(np.ndim(template)) if template.shape[i] > image.shape[i]]) > 0:
        print("normxcorr2: TEMPLATE larger than IMG. Arguments may be swapped.")

    template = template - np.mean(template)
    image = image - np.mean(image)

    a1 = np.ones(template.shape)
    # Faster to flip up down and left right then use fftconvolve instead of scipy's correlate
    ar = np.flipud(np.fliplr(template))
    out = fftconvolve(image, ar.conj(), mode=mode)
    
    image = fftconvolve(np.square(image), a1, mode=mode) - \
            np.square(fftconvolve(image, a1, mode=mode)) / (np.prod(template.shape))

    # Remove small machine precision errors after subtraction
    image[np.where(image < 0)] = 0

    template = np.sum(np.square(template))
    out = out / np.sqrt(image * template)

    # Remove any divisions by 0 or very close to 0
    out[np.where(np.logical_not(np.isfinite(out)))] = 0
    
    return out

def ind2sub(array_shape, ind):
    # Gives repeated indices, replicates matlabs ind2sub
    rows = (ind.astype("int32") // array_shape[1])
    cols = (ind.astype("int32") % array_shape[1])
    return (rows, cols)
def display(image, position, size):
    im = np.array(image, dtype=np.uint8)

    # Create figure and axes
    fig,ax = plt.subplots(1)

    # Display the image
    ax.imshow(im)

    # Create a Rectangle patch
    rect = patches.Rectangle(position,size[0],size[1],linewidth=1,edgecolor='r',facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

    plt.show()


if __name__ == '__main__':
    main()