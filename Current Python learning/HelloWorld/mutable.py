lists = ["pen", "eraser", "marker", "cutter", "sketches"]
shopping_lists = lists
print(id(lists))
print(id(shopping_lists))

lists += ["foam"]
print(id(lists))
print(shopping_lists)
shopping_lists.append("okok")
print(shopping_lists)
# Using chain sequence
a= b = c = d = e = shopping_lists
print(a)
print(c)
b.append("beans")
print(c)
