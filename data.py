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
    user_input_1 = input("Would you like to narrow down your search? Enter Y for yes and N for no.\n\n").lower()
    if user_input_1 != "y" and user_input_1 != "n":
        user_input_1 = input("\n\nSorry, your response is not recognizable. Please try again. Enter Y for yes and N for no.\n\n").lower()
    while user_input_1 == "y":
        selected_genre = choose_genre(relevant_uuid)
        relevant_uuid = narrow_down(selected_genre, relevant_uuid) 
        user_input_1 = input("\n\nThere are {num} books in this collection. Would you like to narrow down your search? Enter Y for yes and N for no.\n\n".format(num=len(relevant_uuid))).lower()
    sorted_uuids = bubble_sort(relevant_uuid)
    see_book_info = input("\n\nWould you like to see information on any of the titles listed? Enter Y for yes and N for no.\n\n").lower()
    if see_book_info != "y" and see_book_info != "n":
        see_book_info = input("\n\nSorry, your response is not recognizable. Please try again. Enter Y for yes and N for no.\n\n").lower()
    while see_book_info.lower() == "y":
        book_info = get_info(sorted_uuids)
        print(book_info)
        see_book_info = input("\n\nWould you like to see information on any of the titles listed? Enter Y for yes and N for no.\n\n").lower()
    print("\n\nThanks for using Julia's Book Library! \n\nGoodbye!\n")
            
def choose_genre(relevant_uuid: set) -> str:
    genre_array = list()
    for uuid in relevant_uuid:
        for genre in library[uuid].genres:
            lower_genre = genre.lower()
            if lower_genre not in genre_array:
                genre_array.append(lower_genre)
    genre_display = input("\n\nThere are {num} genres. Would you like to see the list of genre options? Enter Y for yes and N for no.\n\n".format(num=len(genre_array))).lower()
    if genre_display != "y" and genre_display != "n":
        genre_display = input("\n\nSorry, your response is not recognizable. Please try again. Enter Y for yes and N for no.\n\n").lower()
    elif genre_display == "y":
        genre_string = ""
        for genre in genre_array:
            genre_string = genre_string + genre + ", "
        genre_string = genre_string[:-2]
        print("\n\n" + genre_string)   
    genre = input("\n\nPlease enter in a genre:\n\n").lower()
    if genre in genre_array:
        return genre
    else:
        print("\n\nSorry, but that genre doesn't exist. Press enter to try again.\n\n")
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
    book_number = input("\n\nPlease enter in the number of the title you would like to see more information on:\n\n")
    book_idx = int(book_number) - 1
    if book_idx < len(sorted_uuids):
        return library[sorted_uuids[book_idx]]
    else:
        print("\n\nSorry, but that number was not recognized. Please try again.\n\n")
        return get_info(sorted_uuids)
    
    
    
user_interaction()

