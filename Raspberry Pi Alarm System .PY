import RPi.GPIO as GPIO
import time
from datetime import datetime

# Buzzer GPIO pin
BUZZER = 18

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

# Get alarm time
alarm_time = input("Enter alarm time (HH:MM): ")

print("Alarm set for:", alarm_time)

try:
    while True:
        current_time = datetime.now().strftime("%H:%M")

        print("Current Time:", current_time, end="\r")

        # Check alarm time
        if current_time == alarm_time:
            print("\nAlarm ringing!")

            # Ring buzzer
            for i in range(10):
                GPIO.output(BUZZER, GPIO.HIGH)
                time.sleep(0.5)

                GPIO.output(BUZZER, GPIO.LOW)
                time.sleep(0.5)

            print("Alarm stopped.")
            break

        time.sleep(1)

except KeyboardInterrupt:
    print("\nAlarm program stopped.")

finally:
    GPIO.output(BUZZER, GPIO.LOW)
    GPIO.cleanup()
