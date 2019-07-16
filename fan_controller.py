#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

check_temp_interval = 15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO18 = 18

def get_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        tmp = f.read()
        return int(tmp) / 1000

def run():
    print("run pwm fan")
    p = GPIO.PWM(GPIO18, 50)
    try:
        # fan_power 0% ~ 100%
        fan_power = 10
        while True:
            p.start(fan_power)
            temp = get_temp()
            if temp < 20.0:
                fan_power = 20
            elif temp < 50:
                fan_power = 50
            else:
                fan_power = 100
            p.ChangeDutyCycle(fan_power)

            time.sleep(check_temp_interval)
    except Exception as e:
        print(e)
    finally:
        p.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    run()
