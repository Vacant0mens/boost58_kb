import random
from kmk.utils import Debug
from kmk.keys import make_key
from kmk.handlers.stock import passthrough
from kmk.extensions.rgb import RGB, AnimationModes

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

LED_COUNT = 35
CHANCE_OF_NEW_LIGHT = 0.05
SKIP_LEDS = 1
LED_RANGE = range(0, LED_COUNT, SKIP_LEDS)
DIM_STEP = 1
NEW_LIGHT_CHANCE_MULTIPLIER = round(1 / CHANCE_OF_NEW_LIGHT)
POSSIBLE_LIGHTS = int(LED_COUNT*NEW_LIGHT_CHANCE_MULTIPLIER)


class AnimationModes(AnimationModes):
    RGB_TWINKLE = 9

class CustomRgb(RGB):
    def __init__(self, pixel_pin, pixel_count: int, *args, **kwargs) -> None:
        self.debug = Debug(__name__)
        self.colors = [WHITE, RED, ORANGE, YELLOW, GREEN, CYAN, AZURE, BLUE, MAGENTA, PURPLE, TEAL, PINK]
        make_key(
            names=('RGB_TWINKLE', 'RGB_TWK'),
            on_press=self._twinkle_animation,
            on_release=passthrough,
        )
        super.__init__(pixel_pin=pixel_pin, pixel_count=pixel_count, *args, **kwargs)
        if not self.enable:
            return

        self._animation_step()

        if self.animation_mode == AnimationModes.STATIC_STANDBY:
            return
        elif self.animation_mode == AnimationModes.RGB_TWINKLE:
            self._twinkle_animation()
        elif self.animation_mode == AnimationModes.BREATHING:
            self.effect_breathing()
        elif self.animation_mode == AnimationModes.BREATHING_RAINBOW:
            self.effect_breathing_rainbow()
        elif self.animation_mode == AnimationModes.KNIGHT:
            self.effect_knight()
        elif self.animation_mode == AnimationModes.RAINBOW:


    def _twinkle_animation(self):
        self._twinkle
        self._do_update()

    def _twinkle(self):
        # pick random LED
        led = random.randint(0, POSSIBLE_LIGHTS)
        # if random LED is not in LED range, move on
        if led in LED_RANGE:
            color_number = random.getrandbits(len(len(self.colors).to_bytes(8, 'big')))
            self.set_rgb(self.colors[color_number], led)
        # decrease value of all lights by 1
        self.decrease_val(1)
