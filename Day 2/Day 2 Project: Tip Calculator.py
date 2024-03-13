#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
tot_bill = float(input("What was the total bill? $"))
tip_perc = float(input("How much tip would you like to give? "))
num_people = int(input("How many people to split the bill?"))
tot_bill = ((tot_bill / 100) * tip_perc +tot_bill)
print("Each person should pay: $" + str(format(tot_bill / num_people, ".2f")))
# the round function is used to round the number to 2 decimal places but it dosen't somtimes format the number to 2 decimal places
