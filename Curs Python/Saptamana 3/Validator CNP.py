import datetime
def validare(var):
    """

    :param var: CNP=ul introdus de utilizator de la tastatura
    :return: CNP-ul valid
    """
    while len(var) != 13 and var.isdigit() is False:
        var = input("Reintroidu CNP : ")
    return var

def validare_sex(a):
    if int(a[0]) in range(1,10):
        return True
    else:
        return False


def valiadare_data_nastere(cnp):
    data_nastere = cnp[1:7]
    try:
        datetime.datetime.strptime(data_nastere, '%y%m%d')
        return True
    except Exception:
        return False


def validator_cnp(cnp):
    """

    :param cnp: CNP-ul introdus de utilizator de la tastatura
    :return: mesaj "valid" in cazul in care CNP este valid, "Invalid" in cazul in care CNP-ul nu este valid
    """
    if cnp and validare_sex(cnp) and valiadare_data_nastere(cnp):
        return "valid"
    return "Invalid"

var_cnp = validare(input("Introdu CNP-ul : "))
validator = validator_cnp(var_cnp)
print(validator)