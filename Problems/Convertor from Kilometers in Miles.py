def select_conversion():
    print('\nMeniu')
    print('1. From Miles to Kilo')
    print('2. From Kilo in Miles')
    print('0. Exit')

def miles_to_kilo():
    km = float(input("Input your distance in kilo: "))
    miles = km / 1.609
    return "The distance in miles is {}".format(miles)


def kilo_to_mile():
    miles = float(input("Input your distance in miles: "))
    km = miles / 1.609
    return "The distance in kilos is {}".format(km)


option = '1'
while option != '0':
    select_conversion()
    option = input("What you want to convert : ")
    if option == '1':
        print(miles_to_kilo())
    elif option == '2':
        print(kilo_to_mile())






