import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# LED module
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()

# Enable macro module
macros = Macros()
keyboard.modules.append(macros)

# ========= LED SETUP =========
LED_PIN = board.GP3

# LEDS
rgb = RGB(
    pixel_pin=LED_PIN,
    num_pixels=2,
    hue_default=0,
    sat_default=255,
    val_default=150,
    animation_mode=RGB.ANIM_BREATHING,
)

keyboard.modules.append(rgb)

# ========= SWITCH SETUP =========

PINS = [
    board.GP26,  # SW1
    board.GP27,  # SW2
    board.GP28,  # SW3
    board.GP29,  # SW4
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ========= KEYMAP =========

keyboard.keymap = [
    [
        KC.A,  # SW1
        KC.B,  # SW2
        KC.C,  # SW3
        KC.D,  # SW4
    ]
]

# ========= START FIRMWARE =========
if __name__ == '__main__':
    keyboard.go()