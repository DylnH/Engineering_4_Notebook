import time
import RPi.GPIO as GPIO # from https://pypi.org/project/RPi.GPIO/

reset_shutdown_pin = 26 # pin setup
GPIO.setwarnings(False) # Suppress warnings
GPIO.setmode(GPIO.BCM) # GPIO numbering for pins

GPIO.setup(reset_shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Use Qwiic pHAT's pullup resistor so that the pin is not floating
#GPIO.setup(reset_shutdown_pin, GPIO.IN)

# modular function to restart Pi
def restart():
    print("restarting Pi")
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

# modular function to shutdown Pi
def shut_down():
    print("shutting down")
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)




while True:
    time.sleep(0.5) # delay
    
    channel = GPIO.wait_for_edge(reset_shutdown_pin, GPIO.FALLING, bouncetime=200) # for safe shutdown/reboot

    if channel is None:
        print('Timeout occurred')
    else:
        print('Edge detected on channel', channel)

        # For troubleshooting
        counter = 0

        while GPIO.input(reset_shutdown_pin) == False:
            # For troubleshooting
            counter += 1 # if button pressed for a moment, reboot
            time.sleep(0.5)

            if counter > 3: # if button press greater than 3 sec, shutdown
                shut_down()

        restart() # restart (short button press only)
