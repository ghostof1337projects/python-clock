import colorama
from colorama import Fore, Back, Style
import pyfiglet
import datetime
import os
import threading
import time 
import sys
import winsound

os.system(f'cls & mode 85,20 & title Clock App By Ghost of 1337')

colorama.init()

def set_alarm():
    """Set an alarm to go off at a specified time"""
    print("\n" + Back.YELLOW + Fore.BLACK + " SET ALARM " + Style.RESET_ALL + "\n")
    while True:
        alarm_time = input("Enter alarm time in HH:MM format (24-hour clock): ")
        try:
            alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
            if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
                break
            else:
                print(Fore.RED + "Invalid time. Please try again." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid time. Please try again." + Style.RESET_ALL)

    alarm_time_str = f"{alarm_hour:02d}:{alarm_minute:02d}"
    print(Fore.GREEN + f"\nAlarm set for {alarm_time_str}." + Style.RESET_ALL)
    
    now = datetime.datetime.now()
    alarm_datetime = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
    if alarm_datetime < now:
        alarm_datetime += datetime.timedelta(days=1)

    while True:
        now = datetime.datetime.now()
        if now >= alarm_datetime:
            print("\n" + Back.YELLOW + Fore.BLACK + " ALARM " + Style.RESET_ALL + "\n")
            frequency = 2000
            duration = 5000
            winsound.Beep(frequency, duration)
            break
        time.sleep(1)

    os._exit(0)

def main():
    app_title = pyfiglet.figlet_format("Clock App", font="banner3")
    print(Fore.BLUE + app_title)
    print("\n" + Back.CYAN + Fore.WHITE + " MENU " + Style.RESET_ALL)

    print("1. Set alarm")
    print("2. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            set_alarm()
        elif choice == "2":
            print(Fore.RESET + "\nGoodbye!" + Style.RESET_ALL)
            os._exit(0)
        else:
            print(Fore.RED + "\nInvalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()