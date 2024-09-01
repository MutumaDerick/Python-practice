# A normal python function to determine a palindrome of a given string
def isPalindrome(string):
    if (string == string[::-1]):
        return "A Palindrome"
    else:
        return "Not a Palindrome"
    
# Enter input string
string = input("Enter a string: ")

# call the function
print(isPalindrome(string))


# rewriting the above function using lambda
isPalindrome = lambda string: "Palindrome" if (string == string[::-1]) else "Not a Palindrome"
string = input("Enter a string: ")

# calling the lambda function
print(isPalindrome(string))