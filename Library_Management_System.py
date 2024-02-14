library = []

def add_book(title, author, year):
    book = {'title': bookTitle, 'author': bookAuthor, 'year': bookPublicationYear}
    library.append(book)
    print(f"Book '{title}' added to the Library.")

bookCount = int(input('How many books you want to add in library: '))
for i in range(bookCount):
    bookTitle = input('Enter the Book Name: ')
    bookAuthor = input('Enter the Book Author Name: ')
    bookPublicationYear = int(input('Enter the Book Publication Year: '))
    add_book(bookTitle, bookAuthor, bookPublicationYear)


def display_library(library):
    if not library:
        print("The library is empty.")
    else:
        print('\n'+"Library Books: ")
        for book in library:
            print(f"The {book['title']} by {book['author']} ({book['year']})")

display_library(library)


def search_book(library,title):
    for book in library:
        if title ==book['title']:
            print(f"Book '{title}' found in the library.")
            print(f"Author : {book['author']}, Year : {book['year']}") 
            break
        if not title:
            print(f"Sorry '{title}' book is not in the library.")
              
search_book(library,input('\n'+'Enter the book title you want to search: '))