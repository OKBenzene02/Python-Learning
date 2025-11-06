""""
CONVERTING:
MONTHS TO MILLISECONDS
HOUR TO MILLISECONDS
DAY TO MILLISECONDS
A WEEK TO MILLISECONDS
MONTH TO MILLISECONDS
YEAR TO MILLISECONDS
"""
print("""
CONVERSIONS IN MILLISECONDS: 
one min = 60000
one hour = 3600000
one day = 86400000
one week = 604800000
one month = 2592000000
one year = 31536000000
""")
conversion = input("Enter a time to convert: ")
units = conversion[-1]
number = float(conversion[:-1])

onemin = 60000
onehour = 3600000
oneday = 86400000
oneweek = 604800000
onemonth = 2592000000
oneyear = 31536000000
if units.upper() == "M":
    minu_to_milli = number * 60000
    print("{}Minute = {:.3f}mS".format(number, minu_to_milli))
    if onemin > minu_to_milli:
        print("{} is greater than {}.".format(onemin, minu_to_milli))
    else:
        print("{} is lesser than {}.".format(onemin, minu_to_milli))
elif units.upper() == "H":
    hour_to_milli = float(number * 3600000)
    print("{}Hour = {:.3f}mS".format(number, hour_to_milli))
    if onehour > hour_to_milli:
        print("{} is greater than {}.".format(onehour, hour_to_milli))
    else:
        print("{} is lesser than {}.".format(onehour, hour_to_milli))
elif units.upper() == "D":
    day_to_milli = float(number * 86400000)
    print("{}Day = {:.3f}mS".format(number, day_to_milli))
    if oneday > day_to_milli:
        print("{} is greater than {}.".format(oneday, day_to_milli))
    else:
        print("{} is lesser than {}.".format(oneday, day_to_milli))
elif units.upper() == "W":
    week_to_milli = float(number * 86400000 * 7)
    print("{}Week = {:.3f}mS".format(number, week_to_milli))
    if oneweek > week_to_milli:
        print("{} is greater than {}.".format(oneweek, week_to_milli))
    else:
        print("{} is lesser than {}.".format(oneweek, week_to_milli))
elif units.upper() == "N":
    month_to_milli = float(number * 86400000 * 30)
    print("{}Month = {:.3f}mS".format(number, month_to_milli))
    if onemonth > month_to_milli:
        print("{} is greater than {}.".format(onemonth, month_to_milli))
    else:
        print("{} is lesser than {}.".format(onemonth, month_to_milli))
elif units.upper() == "Y":
    year_to_milli = float(number * 86400000 * 365)
    print("{}Year = {:.3f}mS".format(number, year_to_milli))
    if oneyear > year_to_milli:
        print("{} is greater than {}.".format(oneyear, year_to_milli))
    else:
        print("{} is lesser than {}.".format(oneyear, year_to_milli))