'''Question 1- Write a RegEx pattern in python program to check that a string contains only
a certain set of characters (in this case a-z, A-Z and 0-9).'''
import regex as re
#print(help(re))
import re

pattern = r'^[a-zA-Z0-9]+$'

def check_string(input_string):
    if re.match(pattern, input_string):
        print("String contains only a-z, A-Z, and 0-9.")
    else:
        print("String contains characters other than a-z, A-Z, and 0-9.")


input_string = input("Enter a string: ")
check_string(input_string)

'''
Question 2- Write a RegEx pattern that matches a string that has an a followed by zero or more b's
'''
import re

def check_string(input_string):
    pattern = r'^ab*$'
    if re.match(pattern, input_string):
        print("String matches the pattern: 'a' followed by zero or more 'b's.")
    else:
        print("String does not match the pattern.")

# Example usage:
input_examples = ["a", "ab", "abb", "abbb", "aab", "ac", "b", "bb"]
for example in input_examples:
    check_string(example)

'''
Question 3-  Write a RegEx pattern that matches a string that has an a followed by one or more b's
'''
import re

# Sample input strings
input_strings = ["ab", "abb", "aabb", "b", "ac"]

# Regular expression pattern
pattern = r'ab+'

# Check if the input strings match the pattern
for input_string in input_strings:
    if re.search(pattern, input_string):
        print(f"Match found in '{input_string}'")
    else:
        print(f"No match found in '{input_string}'")

''' 
Question 4- Write a RegEx pattern that matches a string that has an a followed by zero or one 'b'.
'''
import re

# Sample input strings
input_strings = ["a", "ab", "b", "aab", "ac"]

# Regular expression pattern
pattern = r'ab?'

# Check if the input strings match the pattern
for input_string in input_strings:
    if re.search(pattern, input_string):
        print(f"Match found in '{input_string}'")
    else:
        print(f"No match found in '{input_string}'")
'''
Question 5- Write a RegEx pattern in python program that matches a string that has an a followed by three 'b'.
'''
import re

# Sample input strings
input_strings = ["abbb", "aabb", "ab", "aaabbb", "abb", "abbbb"]

# Regular expression pattern
pattern = r'abbb'

# Check if the input strings match the pattern
for input_string in input_strings:
    if re.search(pattern, input_string):
        print(f"Match found in '{input_string}'")
    else:
        print(f"No match found in '{input_string}'")

'''
Question 6- Write a RegEx pattern in python program that matches a string 
that has an a followed by two to three 'b'.'''
input_strings = ["ab", "abb", "abbb", "aabb", "abbbb", "ac"]

# Regular expression pattern
pattern = r'ab{2,3}'

# Check if the input strings match the pattern
for input_string in input_strings:
    if re.search(pattern, input_string):
        print(f"Match found in '{input_string}'")
    else:
        print(f"No match found in '{input_string}'")

'''
Question 7- Write a Python program that matches a string that has an
 'a' followed by anything, ending in 'b'.'''
import re

# Sample input strings
input_strings = ["acb", "ab", "axby", "a123b", "abbbb", "abxyz", "aB"]

# Regular expression pattern
pattern = r'a.*b$'

# Check if the input strings match the pattern
for input_string in input_strings:
    if re.match(pattern, input_string, re.IGNORECASE):  # Case-insensitive match
        print(f"Match found in '{input_string}'")
    else:
        print(f"No match found in '{input_string}'")

'''
Question 8- Write a RegEx pattern in python program that 
matches a word at the beginning of a string.'''
import re

# Sample input strings
input_strings = ["apple pie", "banana bread", "cherry jam", "orange juice", "grapefruit"]

# Regular expression pattern for matching a word at the beginning of a string
pattern = r'^\w+'

# Check if the input strings match the pattern
for input_string in input_strings:
    match = re.match(pattern, input_string)
    if match:
        matched_word = match.group()
        print(f"Match found: '{matched_word}' in '{input_string}'")
    else:
        print(f"No match found in '{input_string}'")

'''
Question 9- Write a RegEx pattern in python program that matches a word at the end of a string.'''

import re

# Sample input strings
input_strings = ["pie apple", "bread banana", "jam cherry", "juice orange", "grapefruit"]

# Regular expression pattern for matching a word at the end of a string
pattern = r'\w+$'

# Check if the input strings match the pattern
for input_string in input_strings:
    match = re.search(pattern, input_string)
    if match:
        matched_word = match.group()
        print(f"Match found: '{matched_word}' in '{input_string}'")
    else:
        print(f"No match found in '{input_string}'")

'''
Question 10- Write a RegEx pattern in python program to find all words that are 
4 digits long in a string.

'''
import re

# Sample input string
input_string = "1234 hello 5678 world 98765 test 4321"

# Regular expression pattern for matching 4-digit words
pattern = r'\b\d{4}\b'

# Find all words that are 4 digits long using re.findall()
matches = re.findall(pattern, input_string)

# Output the matched words
print("Words with 4 digits long:", matches)