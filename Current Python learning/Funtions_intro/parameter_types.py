# def func(p1, p2, *args, k, **kargs):
#     print("positional-or-keyword:...{}, {}".format(p1, p2))
#     print("var-positional (*args):..{}".format(args))
#     print("keyword:.................{}".format(k))
#     print("var-keyword:.............{}".format(kargs))
#
#
# func(1, 2, 3, 4, 5, k = 6, key1=7, key2=8)

def sum_number(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    result = 0
    for number in values:
        result += number
    return result


print(sum_number(1, 2, 3))
print(sum_number(8, 20, 2))
print(sum_number(12.5, 3.147, 98.1))
print(sum_number(1.1, 2.2, 5.5))
