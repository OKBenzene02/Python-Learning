try:
    print("enter a number: ")
    num1 = int(input())
    print("enter a number: ")
    num2 = int(input())
    print(num1 + num2)
except Exception as e:
    print(e)

for i in range(1, 5):
    print(i)