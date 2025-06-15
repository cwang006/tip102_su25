def batman():
    print("I am vengenance. I am the night. I am Batman!")
# batman()

def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")
verb = "give up"
# madlib(verb)

verb = "nap"
# madlib(verb)

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
trilogy(year)

year = 1998
trilogy(year)