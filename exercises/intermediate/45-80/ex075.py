even_num = 0
num_tuple = (int(input('Digite um numero ')),
                     int(input('Digite um numero ')),
                     int(input('Digite um numero ')),
                     int(input('Digite um numero '))) 

# find the position of number 3 in num_tuple
try:
     index_3 = num_tuple.index(3)
     print(f'the first time the number 3 appeared was in position {index_3+1}.')
except ValueError:
     print('The number 3 is not in tuple')

count_apple = num_tuple.count(9)
print(f'the number 9 appeared {count_apple} time')


# find all the even number
for num in num_tuple:
    if num % 2 == 0:
        even_num += 1



print(f'How many time Even Numbers appeared {even_num}')
