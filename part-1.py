# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n < 0:
        raise ValueError('Invalid input')
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

# reverse

def reverse(text):
    
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:]) + text[0]

# bunny

def bunny(count):
    if not count:
        return count
    else:
        return 2 + bunny(count-1)

# is_nested_parens

def is_nested_parens(parens):
    
    if len(parens) == 0:
        return True
        
    if parens[0] == "(" and parens[-1] == ")":
        index = int(len(parens)//2)
        return is_nested_parens(parens[1:index] + parens[index:-1])
        
    else:
        return False

