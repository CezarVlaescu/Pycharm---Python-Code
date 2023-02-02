def password_check(passwrd, max_Repet):
    last_character = None
    repeat = 0
    for i in range(1, len(passwrd)):
        last_character = passwrd[i-1]
        if passwrd[i] == last_character:
            repeat += 1
        else:
            repeat = 0

        if repeat == max_Repet and len(passwrd) > 10 or len(passwrd) <= 1:
            return "Rejected"
        return "Accepted"

var = input("Read your password here : ")
print(password_check(var, 1))
print(var.upper())