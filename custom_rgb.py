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
    def __init__(self, pixel_pin, num_pixels: int, **kwargs) -> None:
        self.debug = Debug(__name__)
        self.colors = [WHITE, RED, ORANGE, YELLOW, GREEN, CYAN, AZURE, BLUE, MAGENTA, PURPLE, TEAL, PINK]
        self.leds = []
        [self.leds.append([0,0,0]) for i in range(num_pixels)]
        make_key(
            names=('RGB_TWINKLE', 'RGB_TWK'),
            on_press=self._twinkle_animation,
            on_release=passthrough,
        )
        self.debug("Twinkle key created. Initializing base RGB...")
        super().__init__(pixel_pin=pixel_pin, num_pixels=num_pixels, animation_speed=1, **kwargs)
        self.debug("RGB Init done.")

    def animate(self):
        if self.effect_init:
            self._init_effect()

        if self.animation_mode is AnimationModes.STATIC_STANDBY:
            return

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
            self.effect_rainbow()
        elif self.animation_mode == AnimationModes.STATIC:
            self.effect_static()
        elif self.animation_mode == AnimationModes.SWIRL:
            self.effect_swirl()
        elif self.animation_mode == AnimationModes.USER:
            self.user_animation()
        else:
            self.off()

        self.show()

    def _rgb_mode_twinkle(self):
        self.effect_init = True
        self.animation_mode = AnimationModes.RGB_TWINKLE


    def _twinkle_animation(self):
        self._twinkle()
        # self.debug("Picked new color.")
        self._do_update()

    def _twinkle(self):
        # dim all LED's by DIM_STEP
        for i in range(len(self.leds)):
            if self.leds[i] == [0, 0, 0]:
                pass
            else:
                new_led = [0, 0, 0]
                for l in range(len(new_led)):
                    if self.leds[i][l] > 1:
                        new_led[l] = self.leds[i][l] - DIM_STEP
                    else:
                        new_led[l] = 0

                self.leds[i] = new_led
                self.set_rgb(self.leds[i], i)

        # pick random LED
        led = random.randint(0, POSSIBLE_LIGHTS)
        # if random LED is not in LED range, move on
        # otherwise, make LED a random new color
        if led in LED_RANGE:
            color = random.choice(self.colors)
            self.debug(f"Color picked for led {led}: {color}")
            self.leds[led] = color
            self.set_rgb(color, led)
            # time.sleep(0.5)
