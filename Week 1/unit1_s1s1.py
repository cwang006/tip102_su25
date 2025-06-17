# Problem 1: Batman
def batman():
    print("I am vengenance. I am the night. I am Batman!")
# batman()

# Problem 2: Mad Libs
def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")
verb = "give up"
# madlib(verb)
verb = "nap"
# madlib(verb)

# Problem 3: Trilogy
def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie ins {year}.")

year = 2008
# trilogy(year)
year = 1998
# trilogy(year)

# Problem 4: Last
def get_last(items):
    if not items:
        return None
    else:
        return items[-1:]
        
items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
# print(get_last(items))
items = []
# print(get_last(items))

# Problem 5: Concatenate
def concatenate(words):
    new_str = ''.join(words)
    return new_str

words = ["vengeance", "darkness", "batman"]
# print(concatenate(words))

words = []
# print(concatenate(words))

# Using an accumulator variable:
def concatenate1(words):
    result = ""
    for word in words:
        result += word
    return result
words = ["vengeance", "darkness", "batman"]
# print(concatenate1(words))

words = []
# print(concatenate1(words))

# Problem 6: Squared
def squared(numbers):
    result = []
    for i in numbers:
        sq_nums = i*i
        result.append(sq_nums)
    return result

numbers = [1, 2, 3]
# print(squared(numbers))

# Another way:
def squared1(numbers):
    for i in numbers:
        return i ** 2
numbers = [1, 2, 3]
# print(squared(numbers))