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
            if not stack:        # To account for an empty stack but more values
                return False
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
#print(is_valid_post_format("())"))

# Problem 2: Reverse User Comments Queue
def reverse_comments_queue(comments):
  stack = []
  for i in range(len(comments)):
      stack.append(comments[i])
  reverse = []
  while stack:
      reverse.append(stack.pop())
  return reverse
    
# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# Problem 3: Check Symmetry in Post Titles
def is_symmetrical_title(title):
    left = 0
    right = len(title)-1
    regex = "(){}!@#$%^&*<>,.?;:' "
    
    while left < right:
        if title[left] or title[right] in regex:
            left += 1
            right -= 1
        if title[left].lower() == title[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))