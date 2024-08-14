#Let's store a favorite number
favourite_number = 7
print(f"My favourite number is {favourite_number}.")

#String variable
greeting = "Hello, World!"
print(greeting)

#Boolean
is_raining = True
print(f"It is raining in Nairobi: {is_raining}")

#control flow: if, elif, else
if is_raining:
    print("You need an umbrella.")

temperature = 30
if temperature > 28:
    print("It's a hot day.")    
elif temperature < 18:
        print("It's a cold day.")
else:
        print("It's neither hot nor cold.")


#loops: repeates a block of code multiple times - for(when you know the no. of iterations), while
for i in range(5):
    print(f"This is a for loop iteration {i}")

# for i in range(0, 10, 2):
#     print(f"This is a for loop iteration {i}")    

while temperature > 25:
    print(f"The temperature is {temperature}. It's too hot.")
    temperature -= 18

countdown = 5 
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1   
print("Blast off!")

#functions: reusable block of code that performs operations
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))    
