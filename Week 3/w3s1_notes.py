# Stacks use append() and pop()
# Queues use append()/appendleft() and popleft()/pop()
# Deque is like a double-ended stack? 

# Instructor Demo:
# Write a function that checks if a given string containing parentheses is balanced.
# The function should return True if everyone opening parenthesis has a corresponding
# parenthesis in the correct order, and False otherwise

# The idea is every opening parenthesis is added to the stack, which allows us to keep
# track of the total opening parenthesis

def is_balanced(s):
    open_parens = []
    for c in s:
        if c == "(":
            open_parens.append(c)
        else:
            if open_parens:
                open_parens.pop()
            else:
                return False
    return not open_parens

print(is_balanced("()"))
print(is_balanced("())"))
print(is_balanced("(()"))