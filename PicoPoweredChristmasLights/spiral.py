import board
import neopixel
from adafruit_led_animation.animation.comet import Comet

tree_lights = neopixel.NeoPixel(board.GP28, 100)
tree_lights.brightness = 0.75

spiral = Comet(tree_lights, speed=0.1, color=(255,255,255), tail_length=100, bounce=False )

while True:
    spiral.animate()