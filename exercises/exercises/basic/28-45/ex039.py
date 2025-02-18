from datetime import date
# get today's date
date_today = date.today()

# Asks for the user's year of birth
birth = int(input('what is your year of birth: '))

# get the user's age
current_year = date_today.year
age =  current_year - birth

# Checks age and prints corresponding messages
if age == 18:
    print('This year you need to go to the nearest military junta to enlist')
elif age < 18:
    years_left = 18 - age
    print(f'{years_left} years left until your enlistment')
elif age > 18:
    years_ago = age - 18
    print(f'your time to enlist has passed {years_ago} years')
