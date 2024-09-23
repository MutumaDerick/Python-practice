# for loop

for item in [1, 2, 3, 4, 5]:
    print(item)

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

for name in names:
    print(name)


   
   # while loop 

count = 0 
while count < 5:
    print(count)
    count += 1  # count = count + 1   

# using loop
colors = ["red", "green", "blue", "purple", "white"]
color_i_want = "white"

for color in colors:
    if color == color_i_want:
        print("I found the color I want")
        break
    print(color)


 # continue statement
ages = [13, 24, 17, 38]

for age in ages:
    if age > 21:
        continue
    print(age)

# Nested loops
groups =[["John", "Sarah", "Bob"], ["Tom", "Jerry", "Mike"], ["Mary", "Liz", "Jane"]]


# This is outer loop will iterate over each list in the groups list

for group in groups:

# This inner loop will go through each name in each list
    for name in group:
        print(name) 

