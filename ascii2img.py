from PIL import Image, ImageDraw, ImageFont
from img2ascii import *

def get_text_resolution(ascii_string, font_size = 10):
    # Create a new temp image to get the texts required resolution
    temp_image = Image.new("L", (1, 1))
    draw = ImageDraw.Draw(temp_image)
    # get resolution
    font = ImageFont.truetype("cour.ttf", font_size)
    text_width, text_height = draw.textsize(ascii_string, font)
    return text_width, text_height

def image_creator(ascii_string, ascii_width, ascii_height):
    # create image
    image = Image.new('L', (ascii_width, ascii_height),'white')
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    font_size = 10
    # font is important because cour.tff is a monospaced font. Which means for every character space between is the same.
    font = ImageFont.truetype("cour.ttf", font_size)
    # Draw the text on the image
    draw.text((0, 0), ascii_string, fill="black", font=font)

    image.show()
