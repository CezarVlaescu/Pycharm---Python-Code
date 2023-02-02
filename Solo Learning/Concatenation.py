x = 'Hello World'
y = ' It is beautiful outside'

x = x + y
print(x)

z = 'Sam'
q = 'P'
sliced = z[1:3]
conc = q + sliced
print(conc)

mystring = 'Hello World'
mystring = mystring.upper() # mareste caracterele
print(mystring)
mystring = mystring.split() # imi creaza o lista
print(mystring)

# Formating - adding a string to an existing string like concatention : string {what we read in format} . format(what we want)
var = "Afara este frumos si {}"
print(var.format("soare"))
#Other form of formating f"string {}"
age = 20
city = "Romania"
print(f"Cezar este un baiat de {age} ani si locuieste in {city}")


