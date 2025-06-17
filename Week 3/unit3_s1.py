# Problem 1: Post Format Validator
def is_valid_post_format(posts):
    # Should be using a stack for pushing and popping values -> 
    # 1) Check for an opening tag, else return false
    # 2) Check for closing tag, else return false
    stack = []
    
    formats = {'(': ')', '{':'}', '[':']'}

    for i in posts:
        if i in formats: 
            stack.append(i)
        elif i in formats.values():
            top = stack.pop()
            if formats[top] != i:
                return False
        else:
            continue
    return True

#is_valid_post_format("([])")
#print(is_valid_post_format("()"))
#print(is_valid_post_format("()[]{}")) 
#print(is_valid_post_format("(]"))

# Problem 2: Reverse User Comments Queue
def reverse_comments_queue(comments):
  comments = []
  
  for i in range(len(comments)-1):
      comments.append(i)
      
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
