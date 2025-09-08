x_list = ['hadi', 'rhys']
x_set = ('hadi', 'rhys')


x_list[0] = 'payam' #OK
# x_set[0] = 'payam' #ERROR

print(x_list)
print([x_list[i] for i in range(len(x_list))])

print(x_set)

for x in x_set:
    print(f"{x}", end=', ')
print()
