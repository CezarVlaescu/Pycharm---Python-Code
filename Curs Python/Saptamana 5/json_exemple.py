# import json
# x = '{"name": "John", "age": 30, "city": "New Work"}'
# y = json.loads(x)
# # print(type(y))
# # print(y['name'])
# a = {"name": "John", "age": 30, "city": "New Work"}
# b = json.dumps(a)
# print(type(b))

import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)