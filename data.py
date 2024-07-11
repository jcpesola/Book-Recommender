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
        genre_len = len(genre_dictionary[genre])
        print("There are {num} books in this collection.\n\n".format(num=genre_len))
        return genre
    else:
        print("\n\nSorry, but that genre doesn't exist. Press enter to try again.")
        return choose_genre(genre_dictionary)
    

def narrow_down(genre_dictionary: Dict[str, set]):
    genre = choose_genre(genre_dictionary)
    narrow_again = input("Would you like to narrow down your search further? Enter Y for yes. Enter N for no.")
    if narrow_again == "y":
        smaller_genre_dictionary = dict()
        for el in genre_dictionary[genre]:
            el_genres = library[el].genres
            # print(el_genres) --> ['Short Stories', 'Fiction', 'Classics', 'Literature', 'American', 'School', '19th Century', 'Anthologies', 'Adventure', 'American Classics']
            # print(type(el_genres)) --> list
            for genre in el_genres:
                if genre not in smaller_genre_dictionary:
                    smaller_genre_dictionary[genre] = set()
                smaller_genre_dictionary[genre].add(el)
        narrow_down(smaller_genre_dictionary)
    if narrow_again == "n":
        # print(collection) #--> dictionary looks good {genre: UUIDs}
        # print(type(collection)) --> dict
        # print(len(collection)) #--> 609, so less then the original 900
        return genre_dictionary
    else:
        print("Sorry, but that genre does not exist. Please try again.")
        narrow_down(genre_dictionary)

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

