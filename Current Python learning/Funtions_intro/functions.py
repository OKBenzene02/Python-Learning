# def multiply(p: float, q: float) -> float:
#     result = p * q
#     return result
#
#
# # print(multiply(10.5, 4))
# for number in range(1, 11):
#     for val in range(1, 11):
#         times_table = multiply(number, val)
#         print("{} * {} = {}".format(number, val, times_table))
#
#     print("=" * 16)
# # =================================================
# def is_palindrome(string):
#     return string[::-1] == string
#
#
# def palindrome_sentence(sentence):
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     return string[::-1] == string
#
#
# word = input("Please enter a word to check: ").casefold()
#
#
# if palindrome_sentence(word):
#     print("{} is a palindrome".format(word))
#
# else:
#     print("{} is not a palindrome".format(word))
# # ========================================================

#
# def is_palindrome(string: str) -> bool:
#     """
#     The actual example to do set the code was to ensure that
#     we write a palindrome.
#     :param string: Just to make the code read the word in backwards
#         so here we use slices
#     :return: The output of the word will be in backwards
#     """
#     return string[::-1].casefold() == string.casefold()
#
# def palindrome_sentence(sentence: str) -> bool:
#     """
#     here we are making the word which we just entered
#         was to check any of them contains any numbers or
#         escape characters(ignores them)
#     :param sentence:checks for numbers and alphabets in word
#     :return:ignoring the case fold characters and returns the output
#     """
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     return is_palindrome(string)
#
#
# word = input("please enter a word: ")
#
# if palindrome_sentence(word):
#     print("{} is a palindrome".format(word))
#
# else:
#     print("{} is not a palindrome".format(word))
# # ========================================================



# def fibonacci(n: int) -> int:
#     """Return the `nth` fibonacci number, or the positive `nth`."""
#     if 0 <= n <= 1:
#         return n
#
#     n_minus1, n_minus2 = 1, 0
#
#     result = None
#     for f in range(n - 1):
#         result = n_minus2 + n_minus1
#         n_minus2 = n_minus1
#         n_minus1 = result
#
#     return result
#
#
# for i in range(37):
#     print(i, fibonacci(i))

#
# def fibonacci(n: int)->int:
#     if 0 <= n <= 1:
#         return n
#     n_minus1, n_minus2 = 1, 0
#
#     result = None
#     for f in range(n - 1):
#         result = n_minus2 + n_minus1
#         n_minus2 = n_minus1
#         n_minus1 = result
#
#     return result
# for i in range(21):
#     print(i, fibonacci(i))

# def fibbiseries(n: int):
#     if 0 <= n <= 1:
#         return n
#     one, zero = 1, 0
#     for i in range(n - 1):
#         result = one + zero
#         zero = one
#         one = result
#     return result
#
# for i in range(21):
#     print(i, fibbiseries(i))
# # ========================================================
# def palindrome(word: str) -> bool:
#     n = ""
#     for char in word:
#         if char.isalnum():
#             n += word
#     return n[::-1] == n
#
#
# sentence = str(input("please enter string: "))
# if palindrome(sentence):
#     print("{} word is palindrome.".format(sentence))
#
# else:
#     print("{} word is not palindrome.".format(sentence))

# # ========================================================

# def hcf(x, y):
#     if x > y:
#         smaller = x
#     else:
#         smaller = y
#     for i in range(1, smaller + 1):
#         if x % i == 0 and y % i == 0:
#             res = i
#     return res
#
# num1 = int(input("enter number 1: "))
# num2 = int(input("enter number 2: "))
# print(hcf(num1, num2))

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            res = greater
            break
        greater += 1
    return res


num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
print(lcm(num1, num2))