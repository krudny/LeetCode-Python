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
