from typing import Dict
from book_class import Book
import csv
import uuid

genre_collection: Dict[str, set] = dict()
book_count = 0
library_count = 60000
library: Dict[uuid.UUID, Book] = dict()

with open('library.csv', newline='') as csvfile:
    book_reader = csv.DictReader(csvfile, delimiter=',')
    for row in book_reader:
        book_count += 1
        #create list of genres
        genre_list = row["genres"].strip("[]").replace("'", "").split(", ")

        #create object for each book
        book_object = Book(row['title'], row['series'],row['author'], row['rating'], row['description'], genre_list)
        library.update({book_object.uuid: book_object})
            
        #add genres and book UUID's to genre dictionary
        for genre in genre_list:
            lower_genre = genre.lower()
            if lower_genre not in genre_collection:
                genre_collection[lower_genre] = set()
            genre_collection[lower_genre].add(book_object.uuid)

def user_interaction():
    print("\n\nWelcome to Julia's Library!\n\nWe have over 50,000 books for you to choose from!\n\nLet's get started!")
    # genre_1 = choose_genre(genre_collection)
    narrow_down_1 = narrow_down(genre_collection)
      

def choose_genre(genre_dictionary: Dict[str, set]) -> str:
    genre_display = input("\nThere are {} genres. Would you like to see the list of options? Enter Y for yes and N for no.".format(len(genre_dictionary)))
    if genre_display == "y":
        genre_list = (genre_dictionary.keys())
        print(genre_list)   
    genre = input("\n\nPlease enter in a genre:\n\n").lower()
    if genre in genre_dictionary:
        return genre
    else:
        print("\n\nSorry, but that genre doesn't exist. Press enter to try again.")
        return choose_genre(genre_dictionary)
    
def narrow_down(genre_dictionary: Dict[str, set]):
    current_set = genre_dictionary[choose_genre(genre_dictionary)]
    print("There are {} books.\n\n".format(len(current_set)))
    repeat_intersection = input("Would you like to narrow down your search further? Enter y for yes. Enter n for no.")
    while (repeat_intersection == "y") is True:
        new_set = current_set.intersection(genre_dictionary[choose_genre(genre_dictionary)])
        if new_set is None:
            print("\n\nThere are no books available.")
            repeat_intersection = input("Would you like to edit your search and try again? Enter y for yes. Enter n for no.")
        else:
            current_set = new_set
            print("\n\nThere are {num} books.\n\n".format(num=len(current_set)))
            repeat_intersection = input("Would you like to narrow down your search further? Enter y for yes. Enter n for no.")
    return current_set

def bubble_sort(collection):
    pass
    #input is a dictionary from narrow_down function {genre: set(UUIDs)}
    #prints a list of books in alphabetical order that is numbered. (ie: 1. Harry Potter, 2. Percy Jackson, etc)
    #output is a new dictionary sorted alphabetically by title 

def get_info(collection):
    pass
    #input is a dictionary{book number, UUID}
    #user types in book number (ie: 3) and the book info is returned (library[UUID])
    
user_interaction()

