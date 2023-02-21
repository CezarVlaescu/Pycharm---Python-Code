from chempy import chemistry
from chempy.util import periodic

# number of elements to be fetched
n = 10

# displaying the information
print("Atomic No.\tName\t\tSymbol\t\tMass")

# fetching the information for
# the first 10 elements
for i in range(1, n + 1):

    # displaying the atomic number
    print(i, end="\t\t")

    # displaying the name
    if len(periodic.names[i]) > 7:
        print(periodic.names[i], end="\t")
    else:
        print(periodic.names[i], end="\t\t")

    # displaying the symbol
    print(periodic.symbols[i], end="\t\t")

    # displaying the mass
    print(periodic.relative_atomic_masses[i])

# creating the reaction
reaction = chemistry.Reaction({'H2': 2, 'O2': 1},
                              {'H2O': 2})

# displaying the reaction
print(reaction)

# displaying the reaction order
print(reaction.order())