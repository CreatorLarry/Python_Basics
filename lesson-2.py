# if statements
# store data list, tuple, dictionary, set
# loops

# score = 77
enteredValue = input("Enter your score: ")

if not enteredValue.isnumeric():
    print("Please ENTER a valid number")
    exit(0) #stop

score = int(enteredValue) #convert enteredValue which is a string into an integer for code to run
# remember we have strings, floats and integers as data types

if score >= 78:
    print("A")
elif 71 <= score <= 77:
    print("A-")

elif 64 <= score <= 70:
    print("B+")

elif 57 <= score <= 63:
    print("B")

elif 50 <= score <= 56:
    print("B-")

elif 43 <= score <= 49:
    print("C+")

elif 36 <= score <= 42:
    print("C")

else:
    print("C")
