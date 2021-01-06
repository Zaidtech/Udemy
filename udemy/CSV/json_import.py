import json

file = open("friends_json.txt", 'r')
file_contents = json.load(file)
file.close()
print(file_contents)

friends = [
    {"name":"Zaid", "age": "19"},
    {"name":"Nabz", "age": "17"}
]
file = open("friends_json.txt", 'w')
json.dump(friends, file)
file.close()
# print(to_json)
my_json_string = '[{"name":"Zaid", "age":"19"}]'
incorrect_string = json.loads(my_json_string)
print(incorrect_string)

