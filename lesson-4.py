# loops

while True:
    print("Hello, loops")
    break # stop loop


scores = [89, 67, 76, 91, 69, 84, 50, 78, 81]

# for each loop
for score in scores:
    if 60 <= score <= 70 and score % 2 == 0:
        print(score)