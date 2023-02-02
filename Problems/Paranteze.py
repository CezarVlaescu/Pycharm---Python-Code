open_list = ['(', '[', '{']
closed_list = [')', ']', '}']

def function(str):
    stat = []
    for i in str:
        if i in open_list:
            stat.append(i)
        elif i in closed_list:
            var = closed_list.index(i)
            if len(stat) > 0 and open_list[var] == stat[len(stat)-1]:
                stat.pop()
            else:
                return "Invalid"
    if len(stat) == 0:
        return "Valid"
    else:
        return "Invalid"


string = "{[]{()}}"
print(string, "-", function(string))

string = "[{}{})(]"
print(string, "-", function(string))

string = "((()"
print(string, "-", function(string))