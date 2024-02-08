import pygame

import numpy as np


def sigmoid(x: float) -> float:
    return 1 / (1 + np.exp(-x))

def floor(nb):
    if nb > 255:
        return 255
    elif nb < 0:
        return 0
    else:
        return nb

def change_color(path, r, g, b):
    """
    Multiply each pixel (r,g,b) by these three values
    """

    img = pygame.image.load(path).convert_alpha()
    pixels = pygame.PixelArray(img)

    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            (r_, g_, b_, a_)= img.unmap_rgb(pixels[i][j])
            pixels[i][j] = (floor(r_ * r),floor(g_ * g) , floor(b_ * b), a_)


    img = pixels.make_surface()
    return img
