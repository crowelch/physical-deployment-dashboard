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
# Setup switches, defaulting to low
GPIO.setup(SWITCH_ONE, GPIO.IN, initial=GPIO.LOW)

# Setup control inputs, defaulting to low
GPIO.setup(KEY_SWITCH, GPIO.IN, initial=GPIO.LOW)
GPIO.setup(DEPLOY_BUTTON, GPIO.IN, initial=GPIO.LOW)

while True:
    # Only proceed if dashboard is armed
    if (GPIO.input(DEPLOY_BUTTON) and GPIO.input(KEY_SWITCH)):
        # Check which (if any) switches are enabled
        enabled_switches = filter(GPIO.input, switches)
        if len(enabled_switches) > 0:
            for switch in enabled_switches:
                ## Deploy
                print('deploying ' + switch)


    time.sleep(0.01)
