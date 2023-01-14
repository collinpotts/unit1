my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def print_dictionary(dict):
    return f"This book is called {dict['title']} and was written by {dict['author']}. It was published in {dict['year']} and is {dict['pages']} pages long. This book has a rating of {dict['rating']}"


print(print_dictionary(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_title(dict):
    return dict["title"]

def get_author(dict):
    return dict["author"]

def get_year(dict):
    return dict["year"]

def get_rating(dict):
    return dict["rating"]

def get_pages(dict):
    return dict["pages"]


print(get_title(my_book))
print(get_author(my_book))
print(get_year(my_book))
print(get_rating(my_book))
print(get_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below