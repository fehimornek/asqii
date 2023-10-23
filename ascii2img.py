from PIL import Image, ImageDraw, ImageFont
from img2ascii import *
import math

def char_get_max_size(ascii_string, original_img):
    img_width, img_height = original_img.size       # For example 1920x1080 => img_width=1920, img_height = 1080

    ascii_string = ascii_string.replace('\n', 'e')  # Change '\n' with e because \n is a pain to deal with in general
    # split the part before getting an 'e' this is the characters that we have to fit horizontally
    ascii_char_count_horizontal = len(ascii_string.split('e')[0])
    # count number of 'e' this is the amount of vertical spaces we need
    # also we add +1 because the last line doesnt contain '\n' or 'e'
    ascii_char_count_vertical = ascii_string.count('e') + 1
    print(ascii_char_count_horizontal, ascii_char_count_vertical)
    len_char_x = img_width / ascii_char_count_horizontal
    len_char_y = img_height / ascii_char_count_vertical

    return len_char_x, len_char_y

def calc_font_size(x_max_size, y_max_size):
    font_size = x_max_size / 2
    space_size = (font_size + math.modf(font_size)[0]) / 2
    return int(font_size), space_size

"""
def get_text_resolution(ascii_string, font_size = 10):
    # Create a new temp image to get the texts required resolution
    temp_image = Image.new("L", (1, 1))
    draw = ImageDraw.Draw(temp_image)
    # get resolution
    font = ImageFont.truetype("cour.ttf", font_size)
    text_width, text_height = draw.textsize(ascii_string, font)
    return text_width, text_height
"""

def image_creator(ascii_string, ascii_width, ascii_height):
    # replace values of \n with e because checking for double character is problematic and \ is a pain to check
    ascii_string_mapped = ascii_string.replace('\n','e')
    # create image
    image = Image.new('L', (ascii_width, ascii_height),'white')
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    font_size = 10
    font = ImageFont.truetype("cour.ttf", font_size)
    # start drawing from the origin using x=0 y=0
    x,y = 0,0
    for char in ascii_string_mapped:
        # if e exists we need to increase y value of the image because it corresponds to \n. Afterwards delete it because 
        # it served its function as an enter key. Also we need to x = 0 because we want to start drawing from origin again.
        if char == 'e':
            char = ''
            y += 5
            x = 0
        # Draw the text on the image
        draw.text((x,y), char, fill="black", font=font)
        x += 5
        
    image.show()
