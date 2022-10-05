intrebare_1 = input('Vrei sa joci? :  ')
if intrebare_1 == 'DA':
    print('Sa inceapa jocul')
else:
    print('O zi buna')

intrebare_2 = input('Care este cel mai inalt munte din lume ?  : ' )
scor = 0
if intrebare_2 == 'Hymalaya':
    print('Felicitari! Raspuns corect')
    print('Ai 1 punct')
    scor += 1
else:
    eroare = input('Raspuns gresit, mai incearca odata : ')
    if eroare != 'Hymalaya':
        print('Ai gresit, treci mai departe!')
        scor = 0

intrebare_3 = input('Care este cel mai rapid animal terestru : ')
if intrebare_3 == 'Jaguar':
    print('Felicitari! Raspuns corect')
    print('Ai 1 punct')
    scor += 1
else:
    eroare = input('Raspuns gresit, mai incearca odata : ')
    if eroare != 'Jaguar':
        print('Ai gresit, treci mai departe!')
        scor = 0

print(f'Ai acumulat {str(scor)} puncte')








