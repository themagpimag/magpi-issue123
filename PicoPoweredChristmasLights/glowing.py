import board
import neopixel
from adafruit_led_animation.animation.pulse import Pulse

tree_lights = neopixel.NeoPixel(board.GP28, 100)
tree_lights.brightness = 0.75

glowing = Pulse(tree_lights, speed=0.1, color=(255,255,255))

while True:
    glowing.animate()