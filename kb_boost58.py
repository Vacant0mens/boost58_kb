import board
import os
from time import sleep
# from storage import getmount
# from supervisor import runtime
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from custom_rgb import CustomRgb as cRGB
from custom_rgb import AnimationModes
from custom_rgb import RED, ORANGE, GREEN, BLUE, WHITE
from kmk.utils import Debug
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split
from kmk.modules.encoder import EncoderHandler


LED_POSITION_LEFT = [
     5,  4,  3,  2,  1,  0,
    11, 10,  9,  8,  7,  6,
    17, 16, 15, 14, 13, 12,
    23, 22, 21, 20, 19, 18,
            28, 27, 26, 25, 24,

    30, 31, 34,
    29, 32, 33
]
LED_POSITION_RIGHT = [
         0,  1,  2,  3,  4,  5,
         6,  7,  8,  9, 10, 11,
        12, 13, 14, 15, 16, 17,
        18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28,

    34, 31, 30,
    33, 32, 29
]
LED_COUNT = len(LED_POSITION_LEFT)


class Boost58Keyboard(KMKKeyboard):
    def __init__(self) -> None:
        super().__init__()
        self.debug_enabled = False
        # self.debug_enabled = True
        self.debug = Debug(__name__)
        self.board_light = neopixel.NeoPixel(board.NEOPIXEL, 1)
        self.board_light.fill(WHITE)
        sleep(0.5)

        self.diode_orientation = DiodeOrientation.ROW2COL

        split_args = {
            'split_side': None,
            'data_pin': board.D1, # UART RX (always RX for 'data_pin')
            'data_pin2': board.D0,  # UART TX (always TX for 'data_pin2')
            'split_flip': True,
            'use_pio': True,
            'uart_flip': True,
        }
        self.row_pins = (board.D2, board.D3, board.D4, board.D5, board.D6)
        self.col_pins = (board.D29, board.D28, board.D27,  board.D26,  board.D22, board.D20)
        self.split = Split(**split_args)
        self.modules.append(self.split)

        self.board_light.fill(RED)
        self.debug("Split setup done.")

        self.rotary_encoder = EncoderHandler()
        self.modules.append(self.rotary_encoder)
        self.rotary_encoder.pins = ((board.D7, board.D8, None, False,),)

        self.board_light.fill(ORANGE)
        self.debug("Encoder setup done.")

        # sleep(0.5)
        self.rgb_pixel_pin = board.D9
        self.rgb = cRGB(pixel_pin=self.rgb_pixel_pin, num_pixels=LED_COUNT, animation_mode=AnimationModes.RGB_TWINKLE)
        self.debug("RGB initialized.")
        self.extensions.append(self.rgb)
        self.debug("RGB added to extensions.")

        self.board_light.fill(BLUE)
        self.debug("RGB setup done.")
        # sleep(0.5)

        self.board_light.fill(GREEN)
        self.debug("Boost58 setup done.")
        # sleep(0.5)

if __name__ == '__main__':
    keyboard = Boost58Keyboard()
    keyboard.debug("Done initializing keyboard.")
    keyboard.go()
