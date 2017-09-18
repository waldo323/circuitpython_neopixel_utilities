import board
import neopixel
from time import sleep
import random

strand_length = 10
pixels = neopixel.NeoPixel(board.D6, strand_length, auto_write=False)


def lightsoff():
    for x in list(range(0, strand_length)):
        pixels[x] = (0, 0, 0)
        pixels.show()


def allwhite():
    for x in list(range(0, strand_length)):
        pixels[x] = (255, 255, 255)
        pixels.show()


def lowwhite():
    for x in list(range(0, strand_length)):
        pixels[x] = (5, 5, 5)
        pixels.show()


def lightup(pixel, red, green, blue):
    pixels[pixel] = (red, green, blue)
    pixels.show()


def randlights():
    # while 1:
    lightnum = random.randint(0, strand_length-1)

    red = random.randint(0, 5)
    green = random.randint(0, 5)
    blue = random.randint(0, 5)
    lightup(lightnum, red, green, blue)
    sleep(.1)


def left_to_right(red=0, green=0, blue=0):
    for x in list(range(0, strand_length)):
        lightup(x, red, green, blue)
        sleep(0.05)
    sleep(.1)


def right_to_left(red=0, green=0, blue=0):
    for x in sorted(list(range(0, strand_length)), reverse=True):
        lightup(x, red, green, blue)
        sleep(.05)
    sleep(.1)


def middle_to_edges(red=0, green=0, blue=0):
    for x in sorted(list(range(0, strand_length//2))):
        lightup(x+5, red, green, blue)
        lightup(4-x, red, green, blue)
        sleep(.1)


def edges_to_middle(red=0, green=0, blue=0):
    for x in sorted(list(range(0, strand_length//2)), reverse=True):
        lightup(x+5, red, green, blue)
        lightup(4-x, red, green, blue)
        sleep(.1)


def ribbon(pixel_count=1, red=10, green=10, blue=10, start_position=0):
    lightsoff()
    for x in list(range(0, pixel_count)):
        # print(x+start_position)
        if (x+start_position) < strand_length:
            lightup(x + start_position, red, green, blue)


def ribbon_left_to_right(pixel_count, red=10, green=10, blue=10, speed=0.5):
    lightsoff()

    for pos in list(range(0, strand_length)):
        lightsoff()
        ribbon(pixel_count, red, green, blue, pos)
        sleep(speed)

    lightsoff()


def ribbon_right_to_left(pixel_count, red=10, green=10, blue=10, speed=0.5):
    lightsoff()
    for pos in sorted(list(range(0, strand_length)), reverse=True):
        lightsoff()
        ribbon(pixel_count, red, green, blue, pos)
        sleep(speed)
    lightsoff()


def demo():
    x = 1
    while 0:
        lightsoff()

    while x:
        ribbon(2, 20, 20, 10, 5)
        sleep(2)
        ribbon_left_to_right(pixel_count=3, red=0, green=0, blue=20)
        sleep(1)
        ribbon_right_to_left(pixel_count=4, red=0, green=20, blue=0)
        sleep(1)
        left_to_right(red=10)
        sleep(1)
        left_to_right(green=10)
        sleep(1)
        left_to_right(blue=10)
        sleep(1)
        left_to_right(red=10, green=10, blue=10)
        sleep(1)
        right_to_left(red=10)
        sleep(1)
        right_to_left(green=10)
        sleep(1)
        right_to_left(blue=10)
        sleep(1)
        right_to_left(red=10, green=10, blue=10)
        sleep(1)
        lowwhite()
        sleep(1)
        middle_to_edges()
        sleep(1)
        middle_to_edges(red=10)
        sleep(1)
        middle_to_edges(green=10)
        sleep(1)
        middle_to_edges(blue=10)
        sleep(1)
        middle_to_edges(10, 10, 10)
        sleep(1)
        edges_to_middle(red=10)
        sleep(1)
        edges_to_middle(green=10)
        sleep(1)
        edges_to_middle(blue=10)
        sleep(1)
        edges_to_middle(10, 10, 10)
        sleep(1)
        lowwhite()
        sleep(1)
        lightsoff()
        sleep(1)
        for x in list(range(0, strand_length*10)):
            randlights()
        sleep(1)
        lightsoff()
        sleep(2)
        # allwhite()
        # sleep(.1)
        x = 0
