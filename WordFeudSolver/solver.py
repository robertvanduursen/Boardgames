import os
import requests
import numpy as np
from PIL import Image
import cv2
import numpy as np

LOCAL = os.path.dirname(__file__)


def get_data_from_img(imgpath):
    # open and show image
    # imgs = [Image.open(f) for f in os.listdir(os.path.dirname(__file__)) if f.startswith("myimage")]
    img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
    # cv2.imshow('original', img)
    print("Shape of the image", img.shape)

    # [rows, columns]
    playing_field = img[465:1542, :]
    letters = img[1716:1863, :]

    # cv2.imshow('playing_field', playing_field)
    # cv2.imshow('letters', letters)

    # Q = letters[10:, 314:410]
    # cv2.imshow('Q', Q)
    # print("Q shape", Q.shape)

    cv2.waitKey(0)
    return playing_field


def recognize_letters(letters):
    # https://www.geeksforgeeks.org/how-to-recognize-optical-characters-in-images-in-python/
    import pytesseract

    # seting the path of pytesseract exe
    # you have to write the location of
    # on which your tesseract was installed
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    # Now we will read the image in our program
    # you have to put your image path in place of photo.jpg
    img = Q  # cv2.imread('photo.jpg')

    # Our image will read as BGR format,
    # So we will convert in RGB format because
    # tesseract can only read in RGB format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    invert = cv2.bitwise_not(img)
    # cv2.imshow('Q2', invert)
    # For getting the text and number from image
    # https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html
    print(f"letter found {pytesseract.image_to_string(letters)}")


playing_field = get_data_from_img(r"G:\Games\WordFeudSolver\test.jpg")


def slice_and_iterate_through_field(playing_field):
    # Q = letters[10:, 314:410]
    print(playing_field.shape)
    width = 1080
    height = 1077

    horizontal_tiles = 15
    vertical_tiles = 15

    hor_step = int(width / horizontal_tiles)
    vert_step = int(height / vertical_tiles)
    print(hor_step, vert_step)

    colors = {
        'TW': [55, 49, 137],  # RED
        'DW': [56, 42, 37],  # ORANGE
        'DL': [94, 151, 112],  # GREEN
        'TL': [155, 98, 52],  # BLUE
        'EMPTY': [56, 47, 42],  # GREY
        'FILLED IN': [141, 211, 233],  # yellowish
        'LAID': [156, 241, 252],  # WHITE
        # 'LAID DW': [246 251 255],  # WHITE
        'LAID DW': [212, 232, 247],  # WHITE
        'PINK': [255, 0, 168]
        #     31, 25, 22
    }

    cell = 0
    for x in range(0, 15):
        for y in range(0, 15):
            cell += 1
            # print(x,y)
            X = min((x * vert_step) + 15, height - 1)
            Y = min((y * hor_step) + 15, width - 1)
            color = playing_field[X][Y]

            # print(color.tolist())
            match = color.tolist() if color.tolist() in colors.values() else False
            if match:
                for key, value in colors.items():
                    if match == value:
                        match = key
                        break
            print(f"color of cell nr {cell} {x,y}, coord: {X, Y} = {color} {match}")
            playing_field[X][Y] = colors['PINK']

    # image[row][col]
    # playing_field
    cv2.imshow(f'new letter', playing_field)

    cv2.waitKey(0)
    # for x in range(1, 5):
    #     print(74 * x - 1, 74 * x)
    #     letter = playing_field[:74, 74 * (x - 1):74 * x]
    #     print(letter.shape)
    #     cv2.imshow(f'new letter {x}', letter)
    #
    #     cv2.waitKey(0)


slice_and_iterate_through_field(playing_field)
