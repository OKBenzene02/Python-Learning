# # import pandas as pd
# from pandas import DataFrame
#
# tabdata = DataFrame({"Range of unit": ["<=99", "100 - 199", "200 - 299", "300 - 399", "400 - 499", ">=500"],
#                      "Amount in Rupees per unit": ["Nil", 2.00, 3.00, 4.00, 5.00, 6.00]})
#
# print(tabdata)
# print()
#
# total_cost = 0
# while True:
#     meter_range = float(input("Enter Range of unit: "))
#     if meter_range != 0:
#         if meter_range <= 99:
#             print("Total amount in Rupees: Nil")
#             break
#
#         elif 100 <= meter_range < 199:
#             total_cost = meter_range * 2.00
#             print(f"Total amount in Rupees: Rs.{total_cost}/-")
#             break
#
#         elif 200 <= meter_range < 299:
#             total_cost = meter_range * 3.00
#             print(f"Total amount in Rupees: Rs.{total_cost}/-")
#             break
#
#         elif 300 <= meter_range < 399:
#             total_cost = meter_range * 4.00
#             print(f"Total amount in Rupees: Rs.{total_cost}/-")
#             break
#
#         elif 400 <= meter_range < 499:
#             total_cost = meter_range * 5.00
#             print(f"Total amount in Rupees: Rs.{total_cost}/-")
#             break
#
#         elif meter_range >= 500:
#             total_cost = meter_range * 6.00
#             print(f"Total amount in Rupees: Rs.{total_cost}/-")
#             break
#
#     else:
#         print("Enter valid Range from the above table.")
#
