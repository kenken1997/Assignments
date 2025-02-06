#initializing the books variable as an empty list
books = []

#initializing the loop for program
while True:

    # Display welcome message and menu options
    print('Welcome to the Book Title Library')

    print('''Select one of these options to continue:
1. Add a Book
2. Remove a Book
3. View All Books
4. Exit
''')
    
    # Get the user's menu choice
    choice = int(input('enter your preferred option: '))

    # Option 1: Add a book (or multiple books)
    if choice == 1:
        print('Great! Which book would you be adding today?')
        add_book = [title.strip() for title in input('Type in title of book (Multiple book entries should be separated by a comma): ').split(',')]
        print(f'{add_book} have been added')
        # Append the new books to the existing list
        books.extend(add_book)
        print(f'This is all the books in the library: {books}')

    # Option 2: Remove a book (one at a time)
    elif choice == 2:
        print('Which book would you like to delete today? (Only one entry can be deleted at a time)')
        del_book = input('enter book title you want deleted: ')
        if del_book in books:
            books.remove(del_book)
        else:
            print('invalid entry. book not found')
        print(f'your updated list of books is {books}')
    
    # Option 3: View all books in the library
    elif choice == 3:
        print(f'all the books you have logged are {books}')
 
    # Option 4: Exit the program 
    elif choice == 4:
        break

    # Handle any invalid choices
    else:
        print('invalid choice. try again')




