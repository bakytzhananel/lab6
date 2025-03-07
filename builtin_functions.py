from functools import reduce
import time
import math

# Task 1: Write a Python program with a built-in function to multiply all the numbers in a list.
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Task 2: Write a Python program with a built-in function that accepts a string and calculates the number of uppercase and lowercase letters.
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Task 3: Write a Python program with a built-in function that checks whether a passed string is a palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

# Task 4: Write a Python program that invokes the square root function after a specific number of milliseconds.
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

# Task 5: Write a Python program with a built-in function that returns True if all elements of the tuple are true.
def all_true(tup):
    return all(tup)

print(multiply_list([1, 2, 3, 4]))  
text = "Hello World!"
upper, lower = count_case(text)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
print(is_palindrome("radar"))  
print(is_palindrome("hello"))  
num = 25100
delay = 2123
print(f"Square root of {num} after {delay} milliseconds is {delayed_sqrt(num, delay)}")
print(all_true((True, True, True)))  
print(all_true((True, False, True)))  

