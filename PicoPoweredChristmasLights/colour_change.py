import board
import neopixel
from adafruit_led_animation.animation.colorcycle import ColorCycle

tree_lights = neopixel.NeoPixel(board.GP28, 100)
tree_lights.brightness = 0.75

red = (255,0,0)
green = (0,255,0)

colour_change = ColorCycle(tree_lights, 1, colors=[red, green])

while True:
    colour_change.animate()