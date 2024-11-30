import random
from kmk.keys import make_key
from kmk.handlers.stock import passthrough
from kmk.extensions.rgb import RGB

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

LED_COUNT = 29
CHANCE_OF_NEW_LIGHT = 0.5
SKIP_LEDS = 1
LED_RANGE = range(0, LED_COUNT, SKIP_LEDS)


class CustomRgb(RGB):
    def __init__(self, pixel_pin, pixel_count: int, *args, **kwargs) -> None:
        self.colors = [WHITE, RED, ORANGE, YELLOW, GREEN, CYAN, AZURE, BLUE, MAGENTA, PURPLE, TEAL, PINK]
        make_key(
            names=('RGB_TWINKLE', 'RGB_TWK'),
            on_press=self._twinkle_animation,
            on_release=passthrough,
        )
        super.__init__(pixel_pin=pixel_pin, pixel_count=pixel_count, *args, **kwargs)


    def _twinkle_animation(self):
        self._twinkle
        self._do_update()

    def _twinkle(self):
        new_light = round(1 / CHANCE_OF_NEW_LIGHT)
        # pick random LED
        led = random.getrandbits(len(int(LED_COUNT*new_light).to_bytes(8, 'big')))
        # turn on new LED (50/50 chance to turn on?)
        # if random LED is not in LED range, move on
        if led in LED_RANGE:
            color_number = random.getrandbits(len(len(self.colors).to_bytes(8, 'big')))
            self.set_rgb(self.colors[color_number], led)
        # decrease value of all lights by 1
        self.decrease_val(1)
