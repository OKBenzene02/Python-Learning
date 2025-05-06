# Infix to postfix conversion

# def priority(operator):
#     if operator == '+' or operator == '-':
#         return 1
#     if operator == '*' or operator == '/':
#         return 2
#     if operator == '^':
#         return 3
#     return 0
#
# def infix_to_postfix(s):
#     i = 0; stack = []; ans = ""
#     while i < len(s):
#         if s[i].isalnum():
#             ans += s[i]
#         elif s[i] == '(':
#             stack.append(s[i])
#         elif s[i] == ')':
#             while stack and stack[-1] != '(':
#                 ans += stack.pop()
#             if stack and stack[-1] == '(':
#                 stack.pop()
#         else:
#             while stack and priority(s[i]) <= priority(stack[-1]):
#                 if s[i] == '^' and stack[-1] == '^': break
#                 ans += stack.pop()
#             stack.append(s[i])
#
#         i += 1
#
#     while stack:
#         ans += stack.pop()
#     return ans
#
# print(infix_to_postfix("a+b*(c^d-e)"))

# ================================================================================================================================
# Next greater element - 1

def next_greater_element(arr):
    stack = []
    res = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        res[i] = stack[-1] if stack else -1
        stack.append(arr[i])

    return res

print(next_greater_element([4,12,5,3,1,2,5,3,1,2,4,6]))