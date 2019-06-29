import datetime
from datetime import date
today = date.today()
year = 2220
month = 2220
day = 2220
print('\nToday\'s date is: ', today)
def print_statment(year, month, day):
	print('\nYou are %d years, %d months, and %d days old!\n' % (year, month, day))

def check_birthdate(year, month, day):
	if year > today.year:
		return False
	elif year == today.year and month > today.month:
		return False
	elif year == today.year and month == today.month and day > today.day:
		return False
	else:
		return True

def calculate_age(year, month, day):
	year = int(input('\nEnter year of birth: '))
	month = int(input('Enter month of birth: '))
	day = int(input('Enter day of birth: '))

	if check_birthdate(year, month, day) == False:
		print('\nThe birthdate you entered is invalid\n')

	else:
		year = today.year - year
		if (month == today.month and day > today.day) or (month > today.month):
			year = year - 1
			if month > today.month:
				month = today.month + 12 - month
				if day > today.day:
					month = month - 1
					day = 30 - (day - today.day)
				else:
					day = today.day - day
					

			elif month == today.month and day > today.day:
				month = 11
				day = 30 - (day - today.day)
		
		elif month == today.month and day <= today.day:
			day = today.day - day
			month = today.month - month

		elif month < today.month and day > today.day:
			month = today.month - month - 1
			day = 30 - (day - today.day)
		
		elif month < today.month and day <= today.day:
			month = today.month - month 
			day = today.day - day

	if check_birthdate(year, month, day) == True:
		print_statment(year, month, day)

		if month == 0 and day == 0:
			print('Happy Birthday!\n')

calculate_age(year, month, day)