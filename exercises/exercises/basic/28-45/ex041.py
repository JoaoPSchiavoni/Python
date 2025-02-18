from datetime import date

# get today's date
date_today = date.today()

# get the year of birth
year_of_birth = int(input('Digite o ano de nascimento do atleta '))

# get this year
current_year = date_today.year
# get the age
age =  current_year - year_of_birth

if age <= 9:
    print(f'O atleta com {age} corresponde a categoria MIRIN')
elif 10 <= age <= 14:
    print(f'O atleta com {age} corresponde a categoria INFANTIL')
elif 15 <= age <= 19:
    print(f'O atleta com {age} corresponde a categoria JUNIOR')
elif age == 20:
    print(f'O atleta com {age} corresponde a categoria SENIOR')
else:
    print(f'O atleta com {age} corresponde a categoria MASTER')



