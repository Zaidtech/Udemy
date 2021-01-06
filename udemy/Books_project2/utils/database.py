"""
Concerned with csv's
name#author#read \n

"""
books_file = 'books.txt'
read_status = False


def create_book_table():
    with open(books_file, 'w') as file:
        pass
#  creating a method just to make sure file exits.

def add_books(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0 \n')


def get_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]  # [[name,author,read], [name,author,read]]
        return [
            {'name': line[0], 'author': line[1], 'read_status': line[2]}
            for line in lines
        ]


def mark_read(name):
    books = get_books()
    for book in books:
        if book['name'] == name:
            book['read_status'] = '1'
            _save_all_books(books)
            # making a private function although python dosen't have such functions but starting a name with
            # implies it


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f'{book["name"], book["author"], book["read_status"]}\n')


def delete_books(name):
    books = get_books()
    books = [book for book in books if book['name']!=name]
    _save_all_books(books)