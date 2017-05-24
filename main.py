#! /usr/bin/python3

import RPi.GPIO as GPIO
import time
import sys, traceback, os

def main():
    # Use board layout of GPIO
    GPIO.setmode(GPIO.BCM)

    ### Constant pins ###
    ## Switches ##
    SWITCH_ONE = 26

    switches = [SWITCH_ONE]

    ## Control Inputs ##
    KEY_SWITCH = 21
    DEPLOY_BUTTON = 20

    ### Setup Channels ###
    # Setup switches, defaulting to low
    GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Setup control inputs, defaulting to high
    GPIO.setup(KEY_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DEPLOY_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    while True:
	if GPIO.input(KEY_SWITCH)  == False and GPIO.input(DEPLOY_BUTTON) == False:
	    print('deploy')
	    time.sleep(0.2)
            # Check which (if any) switches are enabled
            enabled_switches = list(filter(gpio_filter, switches))
            print(len(enabled_switches))
            if len(enabled_switches) > 0:
                for switch in enabled_switches:
                    ## Deploy
                    print('Deploying {}').format(switch)

        ## naptime
        time.sleep(0.01)


def gpio_filter(switch):
	return GPIO.input(switch) == False

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('Interrupted')
        try:
            GPIO.cleanup()
            print('cleaned up GPIO')
            sys.exit(0)
        except SystemExit:
            os._exit(0)
