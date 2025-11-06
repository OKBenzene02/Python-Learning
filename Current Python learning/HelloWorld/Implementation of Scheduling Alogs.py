"""First come First serve (FCFS)"""
"""Without Arrival time"""
#
# from pandas import DataFrame
#
# n = int(input("Enter number of processes: "))
# bt = []
# wt = [0] * n
# tat = [0] * n
# avg_wt = 0
# avg_tat = 0
#
# # For entering all the values for burst time
# for i in range(n):
#     a = int(input(f"Enter the Burst time for P{i+1}: "))
#     bt.append(a)
#
# # For Waiting time
# wt[0] = 0
# for i in range(1, n):
#     total_wt = 0
#     wt[i] = bt[i - 1] + wt[i - 1]
#     total_wt += wt[i]
#     avg_wt = total_wt / n
#
# # For Turn around time
# for i in range(n):
#     total_tat = 0
#     tat[i] = bt[i] + wt[i]
#     total_tat += tat[i]
#     avg_tat = total_tat / n
#
# p = [f"P{i+1}" for i in range(n)]
# print(p)
#
# df = DataFrame({"Processes": p, "Burst time": bt, "Waiting time": wt, "Turn-around time": tat})
# print(df)
#
# print(f"Average Waiting time = {avg_wt:{1}.{2}}")
# print(f"Average Turn around time = {avg_tat:{1}.{2}}")

""" FCFS With Arrival time"""
#
# n = int(input("Enter number of processes: "))
# l = []
# ct = [0] * n
# tat = [0] * n
# total_tat = 0
# avg_tat = 0
# wt = [0] * n
# total_wt = 0
# avg_wt = 0
#
# for i in range(n):
#     process = f"P{i + 1}"
#     a = int(input(f"Enter arrival time P{i+1}: "))
#     b = int(input(f"Enter burst time P{i+1}: "))
#     l.append([process, [a, b]])
#
# l = sorted(l, key=lambda item: item[1][0])
# # print(l)
#
# # For Completion time and Turn around time
# for i in range(1, n):
#     ct[0] = l[0][1][1]
#     if l[i][1][0] - l[i - 1][1][0] > 1:
#         ct[i] = l[i][1][1] + l[i][1][0]
#     else:
#         ct[i] = ct[i - 1] + l[i][1][1]
#
# for i in range(n):
#     tat[i] = ct[i] - l[i][1][0]
#     total_tat += tat[i]
#
# avg_tat = total_tat / n
#
# # For waiting time
# for i in range(n):
#     wt[i] = tat[i] - l[i][1][1]
#     total_wt += wt[i]
#
# avg_wt = total_wt / n
#
#
# print("Processes\tArrival time\tBurst time\tCompletion time\tTurn around time\tWaiting time")
# for i in range(n):
#     print("{0:>4} {1:>12} {2:>14} {3:>15} {4:>16} {5:>17}".format(l[i][0], l[i][1][0], l[i][1][1], ct[i], tat[i], wt[i]))
#
# print()
# print("Average Turn around time: {:.2f}".format(avg_tat))
# print("Average Waiting time: {:.2f}".format(avg_wt))

# ==================================================================================================================

"""Round Robin Scheduling Algorithm"""
"""Without Arrival time"""

# n = int(input("Enter number of processes: "))
# quantum = int(input("Enter the time quantum: "))
# l = []
# rem_bt = [0] * n
# ct = [0] * n
# tat = [0] * n
# total_tat = 0
# avg_tat = 0
# wt = [0] * n
# total_wt = 0
# avg_wt = 0
#
# for i in range(n):
#     process = f"P{i + 1}"
#     a = int(input(f"enter arrival time P{i+1}: "))
#     b = int(input(f"enter burst time P{i+1}: "))
#     l.append([process, [a, b]])
#
# l = sorted(l, key=lambda item: item[1][0])
#
# for i in range(n):
#     rem_bt[i] = l[i][1][1]
#
# t = 0
# while True:
#     done = True
#     for i in range(n):
#         if rem_bt[i] > 0:
#             done = False
#             if rem_bt[i] > quantum:
#                 t += quantum
#                 rem_bt[i] -= quantum
#             else:
#                 t = t + rem_bt[i]
#                 wt[i] = t - l[i][1][1]
#                 rem_bt[i] = 0
#
#     if done:
#         break
#
# for i in range(n):
#     tat[i] = wt[i] + l[i][1][1]
#     ct[i] = tat[i] + l[i][1][0]
#     total_tat += tat[i]
#     avg_tat = total_tat / n
#
# for i in range(n):
#     total_wt += wt[i]
#     avg_wt = total_wt / n
#
# print("Processes\tArrival time\tBurst time\tCompletion time\tTurn around time\tWaiting time")
#
# for i in range(n):
#     print("{0:>4} {1:>12} {2:>14} {3:>15} {4:>16} {5:>17}".format(l[i][0], l[i][1][0], l[i][1][1], ct[i], tat[i], wt[i]))
#
# print("Average Turn-around time: {:.2f}".format(avg_tat))
# print("Average Waiting time: {:.2f}".format(avg_wt))

# ==================================================================================================================

"""Priority scheduling"""
#
# n = int(input("Enter number of processes: "))
# l = []
# rem_bt = [0] * n
# ct = [0] * n
# tat = [0] * n
# total_tat = 0
# avg_tat = 0
# wt = [0] * n
# total_wt = 0
# avg_wt = 0
#
# for i in range(n):
#     process = f"P{i + 1}"
#     a = int(input(f"enter arrival time P{i+1}: "))
#     b = int(input(f"enter burst time P{i+1}: "))
#     c = int(input(f"enter priority for P{i+1}: "))
#     l.append([process, [a, b, c]])
#
# l = sorted(l, key=lambda item: item[1][0])
#
# # for i in range(n):
# #     rem_bt[i] = l[i][1][1]
#
#
# for i in range(n):
#     if l[i][1][2] > l[i - 1][1][2]:
#         ct[i] = ct[i - 1] + l[i][1][1]
#     else:
#         ct[i] = ct[i] + l[i][1][1]
#
#
# for i in range(n):
#     tat[i] = wt[i] + l[i][1][1]
#     ct[i] = tat[i] + l[i][1][0]
#     total_tat += tat[i]
#     avg_tat = total_tat / n
#
# for i in range(n):
#     total_wt += wt[i]
#     avg_wt = total_wt / n
#
# print("Processes\tArrival time\tBurst time\tCompletion time\tTurn around time\tWaiting time")
#
# for i in range(n):
#     print("{0:>4} {1:>12} {2:>14} {3:>15} {4:>16} {5:>17}".format(l[i][0], l[i][1][0], l[i][1][1], ct[i], tat[i], wt[i]))
#
# print("Average Turn-around time: {:.2f}".format(avg_tat))
# print("Average Waiting time: {:.2f}".format(avg_wt))


# ==================================================================================================================
""" FCFS With Arrival time"""

# n = int(input("Enter number of processes: "))
# l = []
# ct = [0] * n
# tat = [0] * n
# total_tat = 0
# avg_tat = 0
# wt = [0] * n
# total_wt = 0
# avg_wt = 0
#
# for i in range(n):
#     process = f"P{i + 1}"
#     a = int(input(f"Enter arrival time P{i+1}: "))
#     b = int(input(f"Enter burst time P{i+1}: "))
#     l.append([process, [a, b]])
#
# l = sorted(l, key=lambda item: item[1][0])
# # print(l)
#
# # For Completion time and Turn around time
# for i in range(1, n):
#     ct[0] = l[0][1][1]
#     if l[i][1][0] - l[i - 1][1][0] > 1:
#         if l[i][1][0] - l[i - 1][1][0] > 2 and l[i][1][0] < ct[i - 1]:
#             ct[i] = l[i][1][1] + l[i][1][0]
#         else:
#             ct[i] = l[i][1][1] + ct[i - 1]
#     else:
#         ct[i] = ct[i - 1] + l[i][1][1]
#
# for i in range(n):
#     tat[i] = ct[i] - l[i][1][0]
#     total_tat += tat[i]
#
# avg_tat = total_tat / n
#
# # For waiting time
# for i in range(n):
#     wt[i] = tat[i] - l[i][1][1]
#     total_wt += wt[i]
#
# avg_wt = total_wt / n
#
#
# print("Processes\tArrival time\tBurst time\tCompletion time\tTurn around time\tWaiting time")
# for i in range(n):
#     print("{0:>4} {1:>12} {2:>14} {3:>15} {4:>16} {5:>17}".format(l[i][0], l[i][1][0], l[i][1][1], ct[i], tat[i], wt[i]))
#
# print()
# print("Average Turn around time: {:.2f}".format(avg_tat))
# print("Average Waiting time: {:.2f}".format(avg_wt))