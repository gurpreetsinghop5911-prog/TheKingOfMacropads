import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# 1. Enable Media Keys and HoldTap
holdtap = HoldTap()
holdtap.tap_time = 2000 # Set hold threshold to 2 seconds
keyboard.modules.append(holdtap)
keyboard.extensions.append(MediaKeys())

# 2. Define the 3 pins from your PCB
PINS = [board.D8, board.D9, board.D10]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False, # Matches your circuit's ground-trigger logic
)

# 3. Define the Keymap
# SW3 (Left): Hold 2s for SHUTDOWN. Quick tap does nothing.
# SW2 (Middle): Instant SLEEP.
# SW1 (Right): Hold 2s for RESTART. Quick tap does nothing.
keyboard.keymap = [
    [
        KC.HT(KC.NO, KC.PWR),  
        KC.SLEP,               
        KC.HT(KC.NO, KC.RST)   
    ],
]

if __name__ == '__main__':
    keyboard.go() # Starts the keyboard