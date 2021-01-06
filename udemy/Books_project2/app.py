from utils.database import add_books, get_books, mark_read, delete_books,create_book_table

User_choice = """ 
Enter :
- 'a' to add a book
- 'l' to list the books     
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
"""


def menu():
    create_book_table()
    user_input = input(User_choice)
    while user_input != 'q':
        if user_input == 'a':
            name = input("Enter the name of the book")
            author = input("Enter the name of the author")
            add_books(name, author)

        elif user_input == 'l':
            get_books()

        elif user_input == 'r':
            name = input("Enter book name to mark as read")
            mark_read(name)

        elif user_input == 'd':
            name = input("Enter the book name to delete")
            delete_books(name)

        user_input = input(User_choice)


menu()
