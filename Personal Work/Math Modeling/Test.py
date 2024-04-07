# og = 3.7911
# a = og
# digit = 4
# Limit = 0.791288
# satisfyed = False
#
# # while not satisfyed:
# for i in range(30):
#     try:
#         a = (a ** 2) * (-1 / 3) + 1
#         # print("----", a, (previousA - a))
#
#         if round(a, 6) == Limit:
#             og = og + 10 ** (-digit)
#             a = og
#             print(og)
#
#         # previousA = a
#     except OverflowError:
#         og = round(og, digit) - 0.1 * 10 ** (-digit)
#         a = og
#         digit += 1
#         print("og changed to: ", og)
#         print("digit changed to: ", digit)
#
# #
# #
# # for t in range(100):
# #     previousA = a
# #     a = (a ** 2) * (-1 / 3) + 1
# #     print(a, (previousA - a))

