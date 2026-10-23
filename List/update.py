'''list =[1, 2, 3, 4, 5]
print(f'Before updating the list: {list}')
list[0] = 10
print(f'After updating the list: {list}')'''

list = [1, 2, 3, 4, 5]
list[0:3] = [10, 20, 30]
print(f'After updating the list: {list}')