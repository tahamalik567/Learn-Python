import random
random.seed(5)
# sets the starting point for the sequence of random numbers generated
# it can be any integer, and it's usually a value you want to be able to reproduce later on

print(random.randint(0,10))
# prints a number between 0 and 10 
print(random.random())
# prints a number between 0 and 1 (not including 1)
print(random.uniform(0,1))
# prints a number between 0 and 1 (including 1)


# how to create a random decimal number between 0 and 5
print(random.uniform(0.0,5.0))
#  or 
print(random.random()*5)

love_score = random.uniform(0,100)
print(f"your love score is {love_score}")