#!/usr/bin/env python3
n = int(input("Enter the number of students:"))
data = {}
subjects = ("physics", "Maths", "Historys")
for i in range(0,n):
    name = input("Enter the name of student {}".format(i+1))
    marks = []
    for x in subjects:
        marks.append(int(input("Enter mark of {}".format(x))))
    data[name] = marks
for x, y in data.items():
    total = sum()
    print("{}'s total marks is: {}".format(x,total))
    if total < 120:
        print(x,"failed :(")
    else:
        print(x,"passed :)")
