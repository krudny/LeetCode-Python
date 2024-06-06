# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.

s = "a1b2"

def letterCasePermutation(): 
    n = len(s)
    result = []
    curr_string = []

    def backtrack(i): 
        if i == n: 
            result.append(''.join(curr_string))
            return
        
        if s[i].isdigit():  
            curr_string.append(s[i])
            backtrack(i + 1)
            curr_string.pop()

        elif s[i].isalpha():  
            curr_string.append(s[i].upper())
            backtrack(i + 1)
            curr_string.pop()
            
            curr_string.append(s[i].lower())
            backtrack(i + 1)
            curr_string.pop()
    

    backtrack(0)
    return result



print(letterCasePermutation())
