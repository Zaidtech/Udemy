# filename = "filename.txt"
# content = "\n Hi Zaid welcome back"
#  importing this file in another files


def save_content_to_file(content, filename):
    with open(filename, "a") as file:
        file.write(content)


def read_content(filename):
    with open(filename, "r") as file:
        print(file.read())


