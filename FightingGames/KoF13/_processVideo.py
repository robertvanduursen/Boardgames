"""

video processing attempts

extracting frame data - hit boxes / pixel distances

prep for machine learning

"""

''' WHAT I WANT '''
'''

to be able to measure the pixel dimensions of KoF sprites programmatically to extract stats like Range
and movement patterns

'''

import cv2, os
import numpy as np

# vidcap = cv2.VideoCapture(r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\data\benimaru_basics.mp4")
# success,image = vidcap.read()
# count = 0
# # 60 fps
#
# while success:
#   # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
#   success,image = vidcap.read()
#   # print('Read a new frame: ', success)
#   count += 1
#
#   # if count > 300:
#   #   success = False
#
# print('total nr of frames', count)
# # total nr of frames 4335

def capture(_from,_to):
  vidcap = cv2.VideoCapture(r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\data\benimaru_basics.mp4")
  success, image = vidcap.read()
  count = 0
  # 60 fps

  while success and count < _to:
    if count > _from:
      cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    success, image = vidcap.read()
    count += 1


# capture(2340,2460)
# right = capture(2580,2590)
# left = capture(3240,3250)

def extractBackground(image, background):
  """
  find matching pixels of the background in the image
  calculate the offset from that
  subtract non-matching pixels

  :returns remaining pixels

  """

  import numpy as np
  im = image
  if isinstance(image,str):
    im = cv2.imread(image)
  bg = cv2.imread(background)
  height, width, depth = im.shape
  circle_img = np.zeros((height, width), np.uint8)
  cv2.circle(circle_img, (int(width / 2.0), int(height / 2)), 280, 1, thickness=-1)

  # masked_data = cv2.bitwise_and(im, bg, mask=circle_img)
  masked_data = cv2.bitwise_and(im, bg)

  # cv2.imshow("masked", masked_data)
  # cv2.waitKey(0)

  return masked_data

  # image = cv2.imread(image)
  # cv2.imshow("image", image)
  # cv2.waitKey(0)

# test = extractBackground(
#   r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\frame2357.jpg",
#                   r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\frame2366.jpg")
# cv2.imshow("masked", test)
# cv2.waitKey(0)

def commandLine():
  import argparse

  # ap = argparse.ArgumentParser()
  # ap.add_argument("-i", "--image", required=True, help="Path to the image")
  # args = vars(ap.parse_args())
  pass


def extractCharacter(image_A, path):
  """
  find matching pixels of the background in the image
  calculate the offset from that
  subtract non-matching pixels

  :returns remaining pixels

  """

  import os

  A = cv2.imread(image_A)
  masked_data = A
  for im in os.listdir(path):
    if im.endswith('.jpg'):
      image = os.path.join(path,im)
      if image != image_A:
        B = cv2.imread(image)

        # masked_data = cv2.max(masked_data, B) # todo: produces full bounding shape over time of move
        masked_data = cv2.min(masked_data, B)


        # masked_data = cv2.bitwise_xor(masked_data, B)

  # find a few random (matching) pixels

  # height, width, depth = im.shape

  cv2.imshow("masked", masked_data)
  cv2.waitKey(0)

  return False

#
# test = extractCharacter(
#   r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\frame2357.jpg",
#   r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13")


def compBG():

  left = cv2.imread(r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\frame_left.jpg")
  mid  = cv2.imread(r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\frame2354.jpg")
  right = cv2.imread(r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\frame_right.jpg")

  height, width, depth = left.shape
  newImg = np.zeros((height, width*3, 3), np.uint8)

  x = 0
  y = 0
  newImg[y:y + left.shape[0], x:x + left.shape[1]] = left

  x = left.shape[1]
  y = 0
  newImg[y:y + right.shape[0], x:x + right.shape[1]] = right


  # left = np.re(left, newImg.shape)
  # newImg = cv2.add(newImg, left)
  #newImg = cv2.add(newImg, right)


  cv2.imwrite("final_comp.jpg", newImg)


def matchNumberSequence(image_A, path):
  """
  find matching pixels of the background in the image
  calculate the offset from that

  this is to be able to Track a static object from a starting Frame !!

  :returns remaining pixels

  """

def motionVector_test():
  A = cv2.imread(r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\frame2357.jpg")
  BG = cv2.imread(r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\data\frame_right.jpg")

  height, width, depth = A.shape


  x = 150
  block = 500

  for w in [283,284]:
    new_x = w # 283 , 284
    newImg = np.zeros((height, width, 3), np.uint8)
    newImg[0:height, 0 + new_x+ x:x + new_x + block] = BG[0:height, 0 + x:x + block]

    # newImg[0:height, 0 + new_x:new_x + block] = newImg[0:height, 0 + x:x + block]


    # masked_data = cv2.max(masked_data, B) # todo: produces full bounding shape over time of move
    # masked_data = cv2.absdiff(newImg, A)

    # print(np.linalg.norm(A[550][550] - newImg[550][550]))

    finalImg = np.zeros((height, width, 3), np.uint8)
    for (x, y, _), value in np.ndenumerate(newImg):
      # val = np.linalg.norm(A[x][y] - newImg[x][y])
      # finalImg[x][y] = [val, val, val]

      if np.linalg.norm(A[x][y]-newImg[x][y]) < 55:
        finalImg[x][y] = [255, 255, 255]

    # finalImg = cv2.add(A, newImg)
    cv2.imshow("mask_%s" % w, finalImg)
    cv2.waitKey(0)

motionVector_test()
