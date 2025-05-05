import psutil
import subprocess
import time

def send_notification(message):
    subprocess.run(["zenity", "--info", "--text", message])

def check_battery():
    battery = psutil.sensors_battery()
    percent = round(battery.percent)
    plugged = battery.power_plugged

    print(f"Battery: {percent}% - {'Plugged In' if plugged else 'Not Plugged In'}")
    print(f'{  time.localtime().tm_hour  } : {  time.localtime().tm_min  } ')

    if percent <=20:
        send_notification(f"Battery is at {percent}%. Please plug the charger.")
    if percent >= 80 and plugged:
        send_notification(f"Battery is at {percent}%. Please unplug the charger.")

while True:
    check_battery()
    time.sleep(60)
