# Problem 1: Post Format Validator
def is_valid_post_format(posts):
    # Should be using a stack for pushing and popping values -> 
    # 1) Check for an opening tag, else return false
    # 2) Check for closing tag, else return false
    pass

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))