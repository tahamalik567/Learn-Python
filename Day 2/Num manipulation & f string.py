print(8/3)
# prints float 
print(int(8/3))
# prints int
print(round(8/3))
# prints int
print(round(8/3, 2))
# prints float
print(8//3)
# prints int and floors the value

score = 4
score /= 2  # score = score / 2
print("score = "+str(score))


# f string
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
# with f string no need to convert int to string