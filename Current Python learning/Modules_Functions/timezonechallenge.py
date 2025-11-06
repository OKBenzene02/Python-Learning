import datetime
import pytz

availabletime = {"1": "Africa/Tunis",
                 "2": "Asia/Kolkata",
                 "3": "Australia/Adelaide",
                 "4": "Europe/Brussels",
                 "5": "Europe/london",
                 "6": "Japan",
                 "7": "Pacific/Tahiti",
                 "8": "US/Hawaii",
                 "9": "Zulu"}

print("Please choose a timezone (0 to quit).")
for place in sorted(availabletime):
    print("\t{}. {}".format(place, availabletime[place]))

while True:
    choice = input()

    if choice == "0":
        break

    if choice in availabletime.keys():
        tz_to_display = pytz.timezone(availabletime[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}.".format(availabletime[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))