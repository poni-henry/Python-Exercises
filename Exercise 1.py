'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them 
the year that they will turn 100 years old. '''
name = input("What is your name?: ")
age = int(input("What is your age?: "))

#year you will turn 100
year_born = 2024 - age
age_100= year_born + 100
age_100_str = str(age_100)

print(name + " you will turn 100 in " + age_100_str ) 

'''asking the user for another number
printing out that many copies of the previous message'''

new_num = int(input("Enter new number: "))
#failed to print on next line multiple statements
print(name + " you will turn 100 in " + age_100_str, end="\n" *new_num)