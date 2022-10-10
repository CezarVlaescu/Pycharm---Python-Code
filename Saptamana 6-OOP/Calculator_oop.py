class Calculator:

    def __init__(self):
        self.operator_1 = float(input('Alege primul nr.: '))
        self.operator_2 = float(input('Alege al doilea nr.: '))
        self.semn = input('Alege semn.: ')

    def adunare(self):
        return self.operator_1 + self.operator_2

    def scadere(self):
        return self.operator_1 - self.operator_2

    def inmultire(self):
        return self.operator_1 * self.operator_2

    def imparitre(self):
        while self.operator_2 == 0.0:
            self.operator_2 = float(input('Alege al doilea numar : '))
            if self.operator_2 != 0.0:
                break
        return self.operator_1 / self.operator_2

    def __str__(self):
        if self.semn == '+':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.adunare()}"
        elif self.semn == '-':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.scadere()}"
        elif self.semn == '*':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.inmultire()}"
        elif self.semn == '/':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.imparitre()}"
        else:
            return ' Operatia nu exista'


obiect_calculator = Calculator()
print(obiect_calculator)