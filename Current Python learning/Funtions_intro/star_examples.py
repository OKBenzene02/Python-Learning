# tuple_star = ("the", "tuple", "is", "unpacked")
# print(tuple_star)
# print(*tuple_star)

def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(0, 1, 2, 3, 4, 5)