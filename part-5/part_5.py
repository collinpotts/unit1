### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
# def create_new_book(book_input):
#     title = input("\nWhat is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     try:
#         year = int(input("What year was this book published? - "))
#     except:
#         year = int(input("Please type a number? - "))
#     try:
#         rating = float(input("What rating out of 5 would you give this book? - "))
#     except:
#         rating = int(input("Please type a number? - "))
#     try:
#         pages = int(input("What is the page count of the book? - "))
#     except:
#         pages = int(input("Please type a number? - "))

#     with open(book_input, "a") as file:
#         file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
# def print_all_books(book_input):

#     print("\nHere are all your books...\n")
    
#     with open(book_input, "r") as f:
#         file = f.readlines()
        
#         for line in file:
#             title, author, year, rating, pages = line.split(", ")

#             print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def create_new_book(book_input):
    title = input("\nWhat is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type a number? - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = int(input("Please type a number? - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please type a number? - "))

    with open(book_input, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

def get_books_as_list(book_input):
    library_list = []
    with open(book_input, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            library_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return library_list

def print_all_books(book_input):
    print("\nHere are all your books...\n")
    for book in get_books_as_list(book_input):
        get_book(book)

def get_book(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")

def get_highest_rated_book(book_input):
    list = get_books_as_list(book_input)
    return max(list, key=lambda i: int(i["rating"]))

def get_lowest_rated_book(book_input):
    list = get_books_as_list(book_input)
    return min(list, key=lambda i: int(i["rating"]))

def main_menu(book_input):

    requiring_input = True

    while requiring_input:
        choice = input("\nChoose 1 to add a book...\nChoose 2 to see all your books...\nChoose 3 to see a total page count of all of your books in your library...\nChoose 4 to get your highest rated book...\nChoose 5 to get your lowest rated book...\nChoose 6 to exit.\nEnter here: ")

        if choice == "1":
           create_new_book(book_input)
        elif choice == "2":
            print_all_books(book_input)
        elif choice == "3":
            print(f"\nYou books page count totals {sum([i['pages'] for i in get_books_as_list(book_input)])} pages!\n")
        elif choice == "4":
            print("\nHere is your highest rated book...\n")
            get_book(get_highest_rated_book(book_input))
        elif choice == "5":
            print("\nHere is your lowest rated book...\n")
            get_book(get_lowest_rated_book(book_input))
        elif choice == "6":
            print("\nThanks")
            requiring_input = False
        else:
            print("\nSorry please type a number for one of the options.\n")

if __name__ == "__main__":
    main_menu("library.txt")