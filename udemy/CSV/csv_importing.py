movies = [
    {"name": "The Matrix", "director": "Zaid"},
    {"name": "3 idiots", "director": "Nabiha"},
    {"name": "All is well", "director": "Ali"}
]


def write_to_file(output):
    with open("file.cvs", "w") as f:
        f.write("name , director \n ")
        for line in output:
            f.write(f"{line['name']},{line['director']}\n ")

