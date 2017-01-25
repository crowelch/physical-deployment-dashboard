#! /usr/bin/python3

import RPi.GPIO as GPIO

# Use board layout of GPIO
GPIO.setmode(GPIO.BOARD)

### Constant pins ###
## Switches ##
SWITCH_ONE = 26

switches = [SWITCH_ONE]

## Control Inputs ##
KEY_SWITCH = 21
DEPLOY_BUTTON = 20

### Setup Channels ###
# Setup switches, defaulting to low #
GPIO.setup(SWITCH_ONE, GPIO.IN, initial=GPIO.LOW)

# Setup control inputs, defaulting to low
GPIO.setup(KEY_SWITCH, GPIO.IN, initial=GPIO.LOW)
GPIO.setup(DEPLOY_BUTTON, GPIO.IN, initial=GPIO.LOW)

# Setup interrupt callbacks
def test_callback(channel):
    print("Rising edge detected on " + channel)

def button_callback:
    # Ensure controller is armed
    if GPIO.input(KEY_SWITCH):
        # Check which (if any) switches are enabled
        enabled_switches = filter(GPIO.input, switches)
        if len(enabled_switches) > 0:
            for switch in enabled_switches:
                ## Deploy

## Attach events to callbacks
GPIO.add_event_detect(DEPLOY_BUTTON, GPIO.RISING, button_callbacks)
