user_input = input("Please enter three numbers: ")
# string_tokens = user_input.split(" , ")
print(tuple(user_input))
int_tokens = []
for st in user_input:
    int_tokens.append(int(st))

result = int_tokens[2] + int_tokens[0] - int_tokens[1]
print(result)

