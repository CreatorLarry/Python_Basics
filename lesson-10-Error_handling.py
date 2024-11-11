# Error handling
x = input("Enter first number: ")

y = input("Enter second number: ")

z = input("Enter third number: ")


# try and catch
try:
    first_num = int(x)
    second_num = int(y)
    third_num = int(z)

    print(first_num * second_num * third_num)
except:
    print("Enter valid numbers")