# list [], tuple (), dictionary {}
# list
scores = [90, 50, 63, 57, 78, 67, 59]

# access a value
print(scores[0]) #first
print(scores[2]) #third

# to add a value
scores.append(86)
print(scores)

# to remove a value
scores.pop(3)
print(scores)

# sorting values
scores.sort() # sorts in natural order
print(scores)
scores.sort(reverse=True)
print(scores)

# len function counts number of value in list
print(len(scores))


# Tuples
# immutables -- ORDER CANNOT BE CHANGED

days_of_the_week = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")

print(days_of_the_week[0])
print(days_of_the_week)

people = ("Mary", )
print(people[0])



# Dictionary
student = {"name": "Josh Peter", "id": 65547, "age": 22, "gender": "Male"}

print(student["name"]) #key
print(student["gender"]) #key

print(student)
#Add
student["Weight"] = 65

print(student)


# set -- removes duplicates, it is unordered therefore doesn't guarantee the order it was put in
people = {"Mary", "Ben", "Frank", "Kitty", "Ben"}
print(people)

people.add("William")
print(people)

print(len(people)) #counting

people.remove("Ben")
print(people)

