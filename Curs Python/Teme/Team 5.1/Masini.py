
my_dict = {'ID': '', 'Brand': '','Model': '','HP': '', 'Price': '' }
my_dict['ID'] = input('Id-ul masinii : ')
my_dict['Brand'] = input('Brand : ')
my_dict['Model'] = input('Modulul : ')
my_dict['HP'] = input('Caii putere : ')
new_value = int(my_dict['HP'])
if new_value < 120:
    print('slow_car')
elif 120 <= new_value < 180:
    print('fast_car')
elif new_value >= 180:
    print('sport_car')

my_dict['Price'] = input('Pretul este : ')
new_value_2 = int(my_dict['Price'])
if new_value_2 < 1000:
    print('cheap')
elif 1000 <= new_value_2 < 5000:
    print('medium')
elif new_value_2 >= 500:
    print('expensive')

import csv

with open('Masini.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file)
    for new_car in my_dict.values():
        csv_writer.writerow(new_car)








