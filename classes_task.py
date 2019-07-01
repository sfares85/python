from datetime import date
today = date.today()
year = 0
class employee:
	
	def __init__(self, name, age, salary, employment_date):

		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
			
class manager(employee):
	def __init__(self, name, age, salary, employment_date, bonus_percentage):

		employee.__init__(self, name, age, salary, employment_date)
		self.bonus_percentage = bonus_percentage

def get_working_years(year):

			year = int(year)
			year = today.year - year
			return year

def get_bonus_percentage(bonus, years, salary):
		bonus = bonus * years * salary
		return bonus


employees = []
managers =[]

print('\n\tWelcome to CODED HR managment system')
while True:
	print('\n\t Choose an action to do:\n\n\t\t1. show employees\n\t\t2. show managers\n\t\t3. add an employee\n\t\t4. add a manager\n\t\t5. exit\n\n')
	
	choice = input('What would you like to do? ')
	print('-----------------')

	if choice.isnumeric():
		choice = int(choice)

		if choice == 1:
			for x in employees:
				print('\nName: %s, Age %d, Salary: %d, Working years: %d' % (x.name.capitalize(), int(x.age), int(x.salary), x.employment_date))

		elif choice == 2:
			for x in managers:
				print('\nName: %s, Age %d, Salary: %d, Working years: %d, Bonus: %.3f' % (x.name.capitalize(), int(x.age), int(x.salary), x.employment_date, x.bonus_percentage))

		elif choice == 3:
			
			peon = employee('name', 'age', 'salary', 'employment_date')
			peon.name = input('\nName: ')
			peon.age = input('Age: ')
			peon.salary = input('Salary: ')
			peon.employment_date = input('Employment year: ')

			if peon.employment_date.isnumeric() and (int(peon.employment_date) <= today.year) and peon.age.isnumeric() and peon.salary.isnumeric():

				peon.employment_date = get_working_years(int(peon.employment_date))
				employees.append(peon)
				print('\nEmployee %s added succesfully' % peon.name.capitalize())
				
			else:
				print('\nPlease enter valid data\n')

		elif choice == 4:

			mudeer_kabeer = manager('name', 'age', 'salary', 'employment_date', 'bonus_percentage')
			mudeer_kabeer.name = input('\nName: ')
			mudeer_kabeer.age = input('Age: ')
			mudeer_kabeer.salary = input('Salary: ')
			mudeer_kabeer.employment_date = input('Employment year: ')
			mudeer_kabeer.bonus_percentage = input('Bonus percentage: ')

			if mudeer_kabeer.employment_date.isnumeric() and (int(mudeer_kabeer.employment_date) <= today.year) and mudeer_kabeer.age.isnumeric() and mudeer_kabeer.salary.isnumeric():

				mudeer_kabeer.employment_date = get_working_years(int(mudeer_kabeer.employment_date))
				mudeer_kabeer.bonus_percentage = get_bonus_percentage(float(mudeer_kabeer.bonus_percentage), mudeer_kabeer.employment_date, int(mudeer_kabeer.salary))
				managers.append(mudeer_kabeer)


				print('\nBig boss %s added succesfully' % mudeer_kabeer.name.capitalize())
				
			else:
				print('\nPlease enter valid data\n')

		elif choice == 5:
			break

	else:
		print('\nPlease enter a valid choice\n')
