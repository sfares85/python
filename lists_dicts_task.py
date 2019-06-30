# creating a list and dict
skills = ['python', 'c++', 'javascript', 'holding breath for 10 minutes', 'juggling', 'family tech support']
cv = {}

#taking applicant information in the below code and inserting them in the dict
print('\nWelcome to the special recruitment program, please answer the following questions:')

name = input('\n\tName: ')

cv["name"] = name

age = int(input('\tAge: '))

cv["age"] = age

exp = int(input('\tHow many years of experience do you have: '))

cv["exp"] = exp

print('\n\tSkills:')
print('\t\t1- ' + skills[0])
print('\t\t2- ' + skills[1])
print('\t\t3- ' + skills[2])
print('\t\t4- ' + skills[3])
print('\t\t5- ' + skills[4])
print('\t\t6- ' + skills[5])
uskill_1 = int(input('\n\tChoose one skill from above: '))

cv["skill_1"] = skills[uskill_1-1]

uskill_2 = int(input('\tChoose another skill from above: '))

cv["skill_2"] = skills[uskill_2-1]

#now checking user input to the following criteria
"""
age is 25-32
exp is >= 5
python skill
"""

if uskill_1 == 4 and uskill_2 == 5 or name.upper() == 'GUYBRUSH THREEPWOOD':
	print('\n\t LOOK! A THREE HEADED MONKEY!')

elif (uskill_1 == 1 or uskill_2 == 1) and age >= 25 and age <= 32 and exp >= 5 :
	print('\nYou have been accepted, ' + name.capitalize() + '. Welcome to our family.')

else:
	print('\nDear ' + name.capitalize() + ',\n\tWe regretfully have to decline your application. We wish you the best in your future endeavours.')