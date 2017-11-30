import board
import neopixel
import random
import time


class neopixel_strip:

    def __init__(self, strand_length=10, pin_placement=board.NEOPIXEL):
        # alternatively board.D6
        self.strand_length = strand_length
        self.pixels = neopixel.NeoPixel(pin_placement, self.strand_length, auto_write=False)

    def lightsoff(self):
        for x in list(range(0, self.strand_length)):
            self.pixels[x] = (0, 0, 0)
            self.pixels.show()

    def allwhite(self):
        for x in list(range(0, self.strand_length)):
            self.pixels[x] = (255, 255, 255)
            self.pixels.show()

    def lowwhite(self):
        for x in list(range(0, self.strand_length)):
            self.pixels[x] = (5, 5, 5)
            self.pixels.show()

    def lightup(self, pixel, red, green, blue):
        self.pixels[pixel] = (red, green, blue)
        self.pixels.show()

    def randlights(self):
        # while 1:
        lightnum = random.randint(0, self.strand_length-1)

        red = random.randint(0, 5)
        green = random.randint(0, 5)
        blue = random.randint(0, 5)
        self.lightup(lightnum, red, green, blue)
        time.sleep(.1)

    def left_to_right(self, red=0, green=0, blue=0):
        for x in list(range(0, self.strand_length)):
            self.lightup(x, red, green, blue)
            time.sleep(0.05)
        time.sleep(.1)

    def right_to_left(self, red=0, green=0, blue=0):
        for x in sorted(list(range(0, self.strand_length)), reverse=True):
            self.lightup(x, red, green, blue)
            time.sleep(.05)
        time.sleep(.1)

    def middle_to_edges(self, red=0, green=0, blue=0):
        for x in sorted(list(range(0, self.strand_length//2))):
            self.lightup(x+5, red, green, blue)
            self.lightup(4-x, red, green, blue)
            time.sleep(.1)

    def edges_to_middle(self, red=0, green=0, blue=0):
        for x in sorted(list(range(0, self.strand_length//2)), reverse=True):
            self.lightup(x+5, red, green, blue)
            self.lightup(4-x, red, green, blue)
            time.sleep(.1)

    def ribbon(self, pixel_count=1, red=10, green=10, blue=10, start_position=0):
        self.lightsoff()
        for x in list(range(0, pixel_count)):
            # print(x+start_position)
            if (x+start_position) < self.strand_length:
                self.lightup(x + start_position, red, green, blue)

    def ribbon_left_to_right(self, pixel_count, red=10, green=10, blue=10, speed=0.5):
        self.lightsoff()

        for pos in list(range(0, self.strand_length)):
            self.lightsoff()
            self.ribbon(pixel_count, red, green, blue, pos)
            time.sleep(speed)

        self.lightsoff()

    def ribbon_right_to_left(self, pixel_count, red=10, green=10, blue=10, speed=0.5):
        self.lightsoff()
        for pos in sorted(list(range(0, self.strand_length)), reverse=True):
            self.lightsoff()
            self.ribbon(pixel_count, red, green, blue, pos)
            time.sleep(speed)
        self.lightsoff()

    def demo(self, demo_runs=1):
        if demo_runs == 0:
            self.lightsoff()

        while demo_runs:
            self.ribbon(2, 20, 20, 10, 5)
            time.sleep(2)
            self.ribbon_left_to_right(pixel_count=3, red=0, green=0, blue=20)
            time.sleep(1)
            self.ribbon_right_to_left(pixel_count=4, red=0, green=20, blue=0)
            time.sleep(1)
            self.left_to_right(red=10)
            time.sleep(1)
            self.left_to_right(green=10)
            time.sleep(1)
            self.left_to_right(blue=10)
            time.sleep(1)
            self.left_to_right(red=10, green=10, blue=10)
            time.sleep(1)
            self.right_to_left(red=10)
            time.sleep(1)
            self.right_to_left(green=10)
            time.sleep(1)
            self.right_to_left(blue=10)
            time.sleep(1)
            self.right_to_left(red=10, green=10, blue=10)
            time.sleep(1)
            self.lowwhite()
            time.sleep(1)
            self.middle_to_edges()
            time.sleep(1)
            self.middle_to_edges(red=10)
            time.sleep(1)
            self.middle_to_edges(green=10)
            time.sleep(1)
            self.middle_to_edges(blue=10)
            time.sleep(1)
            self.middle_to_edges(10, 10, 10)
            time.sleep(1)
            self.edges_to_middle(red=10)
            time.sleep(1)
            self.edges_to_middle(green=10)
            time.sleep(1)
            self.edges_to_middle(blue=10)
            time.sleep(1)
            self.edges_to_middle(10, 10, 10)
            time.sleep(1)
            self.lowwhite()
            time.sleep(1)
            self.lightsoff()
            time.sleep(1)
            for x in list(range(0, self.strand_length*10)):
                self.randlights()
            time.sleep(1)
            self.lightsoff()
            time.sleep(2)
            # self.allwhite()
            # time.sleep(.1)
            demo_runs = demo_runs - 1


if __name__ == "__main__":
    print('Neopixel Demo Starts Now!')
    ns = neopixel_strip()
    ns.demo()
