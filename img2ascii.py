import PIL.Image as Image
import numpy as np

image = Image.open("doge.jpg")

def img_resize(image, new_width = 48):
    width, height = image.size[0], image.size[1]
    # get the ratio to keep it the same resolution
    img_ratio = height / width
    # get the new height based on width
    new_height = int(new_width * img_ratio)
    # resize the image based on new heigth and width
    img_resized = image.resize((new_width, new_height))
    return img_resized

def rgb2gray(image): return image.convert('L')

resized = img_resize(image)
gray_resized = rgb2gray(resized)
gray_resized.show()