# Gurpreet N's Hackpad

A   3-key macropad designed for quick system control, encased in a 3D printed case.

# Contact
@GurpreetN (Slack)

# BOM
| Component | Qty |
|-----------|-----|
| Seeed XIAO SAMD21 | 1x |
| MX-Style switches | 3x |
| Blank DSA keycaps | 3x |
| Custom PCB | 1x |
| Case | 1x |

# Pin Mapping
The switches are wired directly to the microcontroller pins.

| Key Function | Pin |
|--------------|-----|
| Power Off (2s hold) | D8 |
| Sleep | D9 |
| Restart (2s hold) | D10 |



# Usage
Power Off: Hold the left key (D8) for 2 seconds to trigger shutdown.
Sleep: Tap the middle key (D9) to put the system to sleep.
Restart: Hold the right key (D10) for 2 seconds to restart the system.

# Firmware Setup
This project runs on [KMK Firmware](https://github.com/KMKfw/kmk_firmware). To change the functionality of your keys, simply update the `code.py` file on your XIAO's drive.