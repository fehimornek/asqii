import PIL.Image as Image
import numpy as np

def img_resize(image, new_width = 100):
    width, height = image.size[0], image.size[1]
    # get the ratio to keep it the same resolution
    img_ratio = height / width
    # get the new height based on width
    new_height = int(new_width * img_ratio)
    # resize the image based on new heigth and width
    img_resized = image.resize((new_width, new_height))
    return img_resized

def rgb2gray(image): return image.convert('L')

def pixel2ascii(image, new_width = 100):
    pixels = list(image.getdata())

    ascii_chars = "@#$S%/?!*+=;:,."      # 15 ascii characters  

    mapping = 255 / len(ascii_chars)
    """
    if ascii characters are 15 then in 0-255 range 
        0-17 is .
        17-34 is ,
        34-51 is :
        51-68 is ;
        ...
        ... so on
    """

    ascii_characters_list = []
    for pixel in pixels:
        mapped_char = int(pixel // mapping) - 1
        ascii_characters_list.append(ascii_chars[mapped_char])

    # turn the list into string
    ascii_str = ''.join(ascii_characters_list)
    ascii_image = "\n".join([ascii_str[index:(index+new_width)] for index in range(0, len(ascii_str), new_width)])
    print(ascii_image)


img = Image.open("meta.png")
resized = img_resize(img)
gray = rgb2gray(resized)
pixel2ascii(gray)