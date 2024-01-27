# prog for printing table 
num = int(input('Enter the num for the table - '))
for i in range(1,11):
    print(num, 'X', i, '=', num*i)
else:
    print('Here"s the Table of', num)