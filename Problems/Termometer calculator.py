class Termometer:
    def __init__(self, celsius, fahrenheit, kelvin):
        self.Celsius = celsius
        self.Fahrenheit = fahrenheit
        self.Kelvin = kelvin
    def celsius_calculator(self):
        if self.Celsius > 0:
            calc_fer = self.Celsius * 9/5 + 32
            calc_kel = self.Celsius + 273.15
            return "Fahrenheit : {} and Kelvin : {}".format(calc_fer, calc_kel)
    def fahrenheit_calculator(self):
        if self.Fahrenheit > 0:
            calc_cel = (self.Fahrenheit - 32) * 5/9
            calc_kel = (self.Fahrenheit + 459.67) * 5/9
            return "Celsius : {} and Kelvin : {}".format(calc_cel, calc_kel)
    def kelvin_calculator(self):
        if self.Kelvin > 0:
            calc_cel = self.Kelvin - 273.15
            calc_fer = self.Kelvin * 9/5 - 459.67
            return "Celsius : {} and Fahrenheit : {}".format(calc_cel, calc_fer)


obj = Termometer(0, 0, 10)
var = obj.kelvin_calculator()
var1 = obj.fahrenheit_calculator()
var2 = obj.celsius_calculator()
print(var)
