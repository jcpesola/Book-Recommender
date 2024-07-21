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
        # relevant_uuid.add(book_object.uuid)
            
        #add genres and book UUID's to genre dictionary
        for genre in genre_list:
            lower_genre = genre.lower()
            if lower_genre not in genre_collection:
                genre_collection[lower_genre] = set()
            genre_collection[lower_genre].add(book_object.uuid)

def user_interaction():
    print("\n\nWelcome to Julia's Library!\n\nWe have over 50,000 books for you to choose from!\n\nLet's get started!\n\n")
    relevant_uuid = set(library.keys())
    user_input_1 = input("Would you like to narrow down your search? Enter Y for yes and N for no.").lower()
    while user_input_1 == "y":
        selected_genre = choose_genre(relevant_uuid)
        relevant_uuid = narrow_down(selected_genre, relevant_uuid) 
        user_input_1 = input("There are {num} books in this collection. Would you like to narrow down your search? Enter Y for yes and N for no.".format(num=len(relevant_uuid))).lower()
    sorted_uuids = bubble_sort(relevant_uuid)
    see_book_info = input("Would you like to see information on any of the titles listed? Enter Y for yes and N for no.\n\n")
    if see_book_info.lower() == "y":
        user_input_2 = True 
    if see_book_info.lower() == "n":
        print("Thanks for using Julia's Book Library! \n\nGoodbye!")
    while user_input_2 is True:
        book_info = get_info(sorted_uuids)
        print(book_info)
        see_book_info = input("Would you like to see information on any of the titles listed? Enter Y for yes and N for no.\n\n")


   
            
def choose_genre(relevant_uuid: set) -> str:
    genre_array = list()
    for uuid in relevant_uuid:
        for genre in library[uuid].genres:
            lower_genre = genre.lower()
            if lower_genre not in genre_array:
                genre_array.append(lower_genre)
    genre_display = input("\nThere are {num} genres. Would you like to see the list of genre options? Enter Y for yes and N for no.".format(num=len(genre_array))).lower()
    if genre_display == "y":
        print(genre_array)   
    genre = input("\n\nPlease enter in a genre:\n\n").lower()
    if genre in genre_array:
        return genre
    else:
        print("\n\nSorry, but that genre doesn't exist. Press enter to try again.")
        return choose_genre(relevant_uuid)
    
def narrow_down(genre: str, relevant_uuid) -> set:
    uuids_requested = genre_collection[genre]
    temp_uuid = relevant_uuid.intersection(uuids_requested)
    if temp_uuid is None:
        return None
    else:
        return temp_uuid

def bubble_sort(relevant_uuid) -> list:
    uuid_array = list(relevant_uuid)
    iteration_count = 0
    for i in range(len(uuid_array)):
        for idx in range(len(uuid_array)- i - 1):
            iteration_count += 1
            if library[uuid_array[idx]].title > library[uuid_array[idx + 1]].title:
                library[uuid_array[idx]], library[uuid_array[idx + 1]] = library[uuid_array[idx + 1]], library[uuid_array[idx]]
    count = 1
    for uuid in uuid_array:
        print("\n" + str(count) + ". " + library[uuid].title)
        count += 1
    return uuid_array

def get_info(sorted_uuids: list):
    book_number = input("Please enter in the number of the title you would like to see more information on:\n\n")
    
    
    
user_interaction()

