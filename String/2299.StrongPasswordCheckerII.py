# A password is said to be strong if it satisfies all the following criteria:
# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
# Given a string password, return true if it is a strong password. Otherwise, return false.

import string

def strongPasswordCheckerII(password):
    lowercase = set(string.ascii_lowercase)
    uppercase = set(string.ascii_uppercase)
    digits = set(string.digits)
    special = set("!@#$%^&*()-+")

    if len(password) < 8: 
        return False

    for i in range(len(password) - 1): 
        if password[i] == password[i+1]: 
            return False

    password = set(password)
    
    return (len(lowercase & password) > 0 
            and len(uppercase & password) > 0 
            and len(digits & password) > 0 
            and len(special & password) > 0)
