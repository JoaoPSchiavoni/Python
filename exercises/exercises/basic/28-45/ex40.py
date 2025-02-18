first_grade_math = float(input('what is your first grade in math:  '))
second_grade_math = float(input('what is your second grade in math:  '))

average_between_grade = (first_grade_math + second_grade_math) / 2

if average_between_grade < 5.0:
    print(f'Sua media foi de {average_between_grade:.1f} Reprovado!')
elif 5.0 <= average_between_grade <= 6.9:
    print(f'Sua media foi de {average_between_grade:.1f} Recuperacao!')
else:
    print(f'Sua media foi de {average_between_grade:.1f} Passou')
