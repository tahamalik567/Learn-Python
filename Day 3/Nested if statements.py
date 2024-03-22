height = 120
if(height > 120):
    print("You can ride the rollercoaster")
    age = int(input("your age is"))
    if(age < 12):
        print("Please pay $5")
    elif(age <= 18):
        print("Please pay $7")
    elif(age >= 45 and age <= 55):
        print("Please pay $0, have a free ride")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")
    
#  can add as many elif condition as you want beteen if and else condition