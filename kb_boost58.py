import board
import os
from time import sleep
# from storage import getmount
from kmk.kmk_keyboard import KMKKeyboard
import neopixel
from kmk.utils import Debug
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled,OledData,OledReactionType,OledDisplayMode
from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data


LED_POSITION_LEFT = [
     5,  6,  7,  8,  9, 10,
    11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 29,
    23, 24, 25, 26, 27, 28,
                30, 31, 32, 33,

                1,  0,
                3,  2,  4
]
LED_POSITION_RIGHT = [
        10,  9,  8,  7,  6,  5,
        16, 15, 14, 13, 12, 11,
    29, 22, 21, 20, 19, 18, 17,
        28, 27, 26, 25, 24, 23,
    33, 32, 31, 30,

        0,  1,
    4,  2,  3
]

OFF = [0, 0, 0]
BLACK = OFF
WHITE = [255, 255, 255]
RED = [255, 0, 0]
ORANGE = [255, 100, 0]
YELLOW = [200, 255, 0]
GREEN = [0, 255, 0]
CYAN = [0, 255, 255]
AZURE = [153, 245, 255]
BLUE = [0, 0, 255]
MAGENTA = [255, 0, 255]
PURPLE = [242, 0, 255]
TEAL = [0, 128, 128]
PINK = [255, 0, 255]


class Boost58Keyboard(KMKKeyboard):
    def __init__(self) -> None:
        super().__init__()
        self.debug = Debug(__name__)
        self.board_light = neopixel.NeoPixel(board.NEOPIXEL, 1)
        self.board_light.fill(WHITE)
        sleep(0.5)

        self.diode_orientation = DiodeOrientation.ROW2COL
        self.rgb_pixel_pin = board.D21
        self.num_pixels = 35
        self.brightness_limit = 0.35
        split_args = {
            'split_side': None,
            'data_pin': board.D1,  # UART RX
            'data_pin2': board.D0, # UART TX
            'split_flip': True,
            'use_pio': True,
            # 'uart_flip': True
        }
        self.rotary_encoder = EncoderHandler()
        self.modules.append(self.rotary_encoder)
        self.row_pins = (board.D2, board.D3, board.D4, board.D5, board.D6)
        self.col_pins = (board.D29, board.D28, board.D27,  board.D26,  board.D22, board.D20)

        if '_LEFT' in os.listdir():
            # LEFT
            self.is_right = False
            split_args['split_side'] = SplitSide.LEFT
            self.debug("set to Left")
            self.rotary_encoder.pins = ((board.D7, board.D8, None, False,),)
            self.led_key_pos = LED_POSITION_LEFT
        elif '_RIGHT' in os.listdir():
            # RIGHT
            self.is_right = True
            split_args['split_side'] = SplitSide.RIGHT
            split_args['uart_flip'] = True
            self.debug("set to Right")
            self.rotary_encoder.pins = ((board.D7, board.D8, None, False,),)
            self.led_key_pos = LED_POSITION_RIGHT
        else:
            while True:
                self.board_light.fill(RED)
                print("No side set.")
                sleep(1)
                print("Copy _LEFT or _RIGHT file to circuitpython drive.")
                self.board_light.fill(OFF)
                sleep(1)


        self.split = Split(**split_args)
        self.modules.append(self.split)

        self.board_light.fill(ORANGE)
        self.debug("Side set.")
        # sleep(0.5)
        
        self._set_rgb_matrix()
        # self._set_oled()

        self.board_light.fill(BLUE)
        self.debug("Setup done.")
        # sleep(0.5)
        self.board_light.fill(GREEN)
        # sleep(0.5)

    def _set_rgb_matrix(self):
        self.debug("Adding RGB.")
        lights = []
        glow = []
        for c in range(6):
            lights.append(RED) # top row
        for c in range(6):
            lights.append(ORANGE) # top-middle row
        for c in range(6):
            lights.append(YELLOW) # bottom-middle row
        for c in range(7):
            lights.append(GREEN) # bottom row
        for c in range(4):
            lights.append(BLUE) # thumb row
        for c in range(5):
            glow.append(MAGENTA) # underglow

        # self.debug("***** Lights array length:", str(len(lights)))
        # self.debug("***** Underglow array length:", str(len(glow)))
        rgb_ext = Rgb_matrix(
            ledDisplay=Rgb_matrix_data(
                keys=lights,                     
                underglow=glow
            ),
            split=False, rightSide=self.is_right
        )
        self.extensions.append(rgb_ext)

    # def _set_oled(self):
    #     self.debug("Adding OLED extension")
    #     self.SCL = board.D3
    #     self.SDA = board.D2
    #     oled_ext = Oled(
    #         OledData(
    #             corner_one={0:OledReactionType.STATIC,1:["layer"]},
    #             corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
    #             corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust"]},
    #             corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds"]}
    #         )
    #     )
    #     # self.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard = Boost58Keyboard()
    keyboard.go()
