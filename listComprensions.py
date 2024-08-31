nums = [4, -11, 69, 53, -65]
doubled = []

for num in nums:
    doubled.append(num * 2)
print(doubled)

# same problem but using list comprehension
nums = [4, -11, 69, 53, -65]
doubled = [num * 2 for num in nums]
print(doubled)  