import board
import neopixel
from adafruit_led_animation.animation.solid import Solid

tree_lights = neopixel.NeoPixel(board.GP28, 100)
tree_lights.brightness = 0.75

lights_on = Solid(tree_lights, color=(255,255,255))

while True:
    lights_on.animate()