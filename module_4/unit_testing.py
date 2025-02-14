# A palindrome is a word or phrase that is spelled the same forward and backward, like racecar or kayak.
# Here we'll define a Python function that tests if a string is a palindrome and write a unit test in test_file.py
# to check that it returns the expected result

# First version - comment out to test updated version below

def is_palindrome(string):
    # First we process the input to remove upper case letters and spaces from phrases
    string = string.strip().lower().replace(" ", "")
    # Then we use list slicing to check the string is the same forward and backward
    return string == string[::-1]
