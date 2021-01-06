file = open("csv_data.txt", "r")
lines = file.readlines()
file.close()
new_data = []
lines = [line.strip() for line in lines]
print(lines)
for line in lines:
    new_data = (line.split(","))
    name = new_data[0].title()
    age = new_data[1].capitalize()
    university = new_data[2].title()
    branch = new_data[3].capitalize()
    print(f"{name} is {age} years old and study {branch} at {university}")
# print(lines)
#  creating a cvs file
# csv_create = " ,".join(["Rolf", "19", "CSE", "MIT"])
# print(csv_create)
# file = open("csv_data.txt", "w")
#
# file.write(f"{csv_create}")
