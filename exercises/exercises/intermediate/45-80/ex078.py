num_list = []
for n in range(5):
    num_list.append(int(input(f'Digite o {n+1} valor: ')))
        
max_num = max(num_list)
min_num = min(num_list)

pos_max_num = num_list.index(max_num)
pos_min_num = num_list.index(min_num)

print(f'O maior valor digitado foi {max_num} na posição {pos_max_num+1}.')
print(f'O menor valor digitado foi {min_num} na posição {pos_min_num+1}.')