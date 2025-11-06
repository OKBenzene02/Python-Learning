# import time
# print(time.gmtime(0))
# time_here = time.localtime()
# print("Year: ", time_here[0], time_here.tm_year)
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[2], time_here.tm_mday)

# import time
# from time import process_time as my_timer #Time, perf_count, perf_count_ns, monotonic, process_time.....
# import random
#
# input("press enter to start: ")
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("press enter to stop: ")
#
# end_timer = my_timer()
# print("started at: " + time.strftime("%X", time.localtime(start_time)))
# print("ended at: " + time.strftime("%X", time.localtime(end_timer)))
#
# print("reaction timer {} seconds".format(end_timer - start_time))

# ===========================================================================

# import time
#
# print("monotonic(): \t\t", time.get_clock_info('monotonic'))
# print("perf_counter(): \t", time.get_clock_info('perf_counter'))
# print("process_time(): \t", time.get_clock_info('process_time'))
# print("time(): \t\t\t", time.get_clock_info('time'))