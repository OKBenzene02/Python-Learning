import time

# k = 1
# initial = time.time()
# while k <= 10:
#     print(k)
#     k += 1
#     time.sleep(1)
#
# final = time.time()
# print(round(final - initial), "seconds")

# =========================================================================
localtime = time.asctime(time.localtime(time.time()))
print(localtime)