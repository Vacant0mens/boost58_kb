from kb_boost58 import Boost58Keyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.oneshot import OneShot
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


# keyboard = HandwireKeyboard()
keyboard = Boost58Keyboard()

# keyboard.debug_enabled = False
keyboard.debug_enabled = True
keyboard.debug("Keyboard starting...")
keyboard.modules.append(Layers())
keyboard.modules.append(StickyMod())
keyboard.modules.append(OneShot())
keyboard.extensions.append(MediaKeys())

keyboard.debug("Setting custom keys...")

SPC = KC.SPC
setattr(KC, 'NOT_SET', KC.NO) # key not set
setattr(KC, 'COPY', KC.LCTL(KC.C)) # Copy
setattr(KC, 'PSTE', KC.LCTL(KC.V)) # Paste
setattr(KC, 'CUT', KC.LCTL(KC.X)) # Cut
setattr(KC, 'UNDO', KC.LCTL(KC.Z)) # Undo
setattr(KC, 'REDO', KC.LCTL(KC.Y)) # Undo
setattr(KC, 'SAVE', KC.LCTL(KC.S)) # Save
setattr(KC, 'SEL_ALL', KC.LCTL(KC.A)) # Select All
setattr(KC, 'LT', KC.LCTL(KC.LABK)) # <
setattr(KC, 'GT', KC.LCTL(KC.RABK)) # >
setattr(KC, 'CTL_SHFT_N', KC.LCTL(KC.LSFT(KC.N)))
setattr(KC, 'PLAYPAUSE', KC.MEDIA_PLAY_PAUSE)
setattr(KC, 'CTL_F5', KC.LCTL(KC.F5))
setattr(KC, 'AUTOFMT', KC.LALT(KC.LSFT(KC.F))) # VSCode AutoFormat
setattr(KC, 'COMMENT', KC.LCTRL(KC.SLSH)) # VSCode Comment Line Toggle
setattr(KC, 'xxxxxxxxxx', KC.NO) # Not a key

keyboard.debug("Custom keys set. Setting keymap...")


keyboard.keymap = [
    [  # 0 - Qwerty
        KC.GRV,        KC.N1,         KC.N2,         KC.N3,         KC.N4,         KC.N5,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.N6,         KC.N7,         KC.N8,         KC.N9,         KC.N0,         KC.BSPC,
        KC.TAB,        KC.Q,          KC.W,          KC.E,          KC.R,          KC.T,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.Y,          KC.U,          KC.I,          KC.O,          KC.P,          KC.BSLASH,
        KC.LSFT,       KC.A,          KC.S,          KC.D,          KC.F,          KC.G,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.H,          KC.J,          KC.K,          KC.L,          KC.SCLN,       KC.QUOT,
        KC.LCTL,       KC.Z,          KC.X,          KC.C,          KC.V,          KC.B,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.N,          KC.M,          KC.COMM,       KC.DOT,        KC.SLSH,       KC.ENT,
        KC.xxxxxxxxxx,
        KC.xxxxxxxxxx,
                       KC.LALT,       KC.LCTL,       KC.SPC,        KC.MO(2),      KC.MO(1),      KC.MO(1),      KC.SPC,        KC.LALT,       KC.LGUI,       KC.TG(2),
        KC.xxxxxxxxxx,
        KC.xxxxxxxxxx,
    ],
    [  # 1 - Nav, Symbols
        KC.ESC,        KC.LCTL(KC.U), KC.F9,         KC.F10,        KC.F11,        KC.F12,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.LCBR,       KC.RCBR,       KC.DEL,
        KC.F8,         KC.LCTL(SPC),  KC.CTL_F5,     KC.F5,         KC.F2,         KC.F1,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.TAB,        KC.HOME,       KC.UP,         KC.END,        KC.LBRC,       KC.RBRC,
        KC.PSCR,       KC.COPY,       KC.SAVE,       KC.LCTL(KC.N), KC.LCTL(KC.F), KC.UNDO,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.BSLS,       KC.LEFT,       KC.DOWN,       KC.RGHT,       KC.SCLN,       KC.QUOT,
        KC.CUT,        KC.PSTE,       KC.SEL_ALL,    KC.CTL_SHFT_N, KC.LCTL(KC.H), KC.REDO,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.LABK,       KC.RABK,       KC.MINUS,
        KC.xxxxxxxxxx,
        KC.xxxxxxxxxx,
                       KC.PLAYPAUSE,  KC.LGUI(KC.I), KC.LGUI(KC.L), KC.LSFT,       KC.TRNS,       KC.TRNS,       KC.SPC,        KC.COMMENT,    KC.AUTOFMT,    KC.MUTE,
        KC.xxxxxxxxxx,
        KC.xxxxxxxxxx,
    ],
    [  # 2 - Media, HotKeys (Pwsh, VSCode), NumPad/10-key
        KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.LPRN,       KC.RPRN,       KC.DEL,
        KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.NOT_SET,    KC.N7,         KC.N8,         KC.N9,         KC.MINUS,      KC.PLUS,
        KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.NOT_SET,    KC.N4,         KC.N5,         KC.N6,         KC.UNDS,       KC.EQUAL,
        KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,
                                                                    KC.xxxxxxxxxx, KC.xxxxxxxxxx, KC.NOT_SET,    KC.N1,         KC.N2,         KC.N3,         KC.NOT_SET,    KC.ENT,
        KC.xxxxxxxxxx,
        KC.xxxxxxxxxx,
                       KC.NOT_SET,    KC.NOT_SET,    KC.NOT_SET,    KC.TRNS,       KC.NOT_SET,    KC.NOT_SET,    KC.SPC,        KC.N0,         KC.DOT,        KC.TG(2),
        KC.xxxxxxxxxx,
        KC.xxxxxxxxxx,
    ]
]
keyboard.debug("Keymap set.")

if getattr(keyboard, 'rotary_encoder'):
    # sticky LALT
    # rotate right == hold LALT, tap TAB
    STICKY_ALT = KC.SM(KC.TAB, mod=KC.LALT)
    # rotate left == hold LALT(LSFT), tap TAB
    STICKY_SHFTALT = KC.SM(KC.LSHIFT(KC.TAB), mod=KC.LALT)

    keyboard.rotary_encoder.map = [
        [ # 0 - Qwerty
            (STICKY_ALT, STICKY_SHFTALT,), (KC.LEFT, KC.RGHT,)
        ],
        [ # 1 - Nav, Symbols
            (KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK,), (KC.VOLD, KC.VOLU,)
        ],
        [ # 2 - Media, etc
            (KC.LSHIFT(KC.DOWN), KC.LSHIFT(KC.UP),), (KC.LSHIFT(KC.LEFT), KC.LSHIFT(KC.RGHT),)
        ]
    ]
    keyboard.debug("Encoder rotations set.")

if __name__ == '__main__':
    keyboard.go()