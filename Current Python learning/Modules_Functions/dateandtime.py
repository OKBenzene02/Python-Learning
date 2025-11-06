import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC time {}".format(utc_time))

now_local_time = pytz.utc.localize(local_time).astimezone()
now_utc_time = pytz.utc.localize(utc_time)

print("Now local time {}, timezone {}".format(now_local_time, now_local_time.tzinfo))
print("Now UTC time {}, timezone {}".format(now_utc_time, now_utc_time.tzinfo))

gap_time = datetime.datetime(2021, 5, 13, 18, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1620910800
t = s / (60 * 60)

ind = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(ind)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(ind)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))