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
            if genre not in genre_collection:
                genre_collection[genre] = set()
            genre_collection[genre].add(book_object.uuid)

            

    