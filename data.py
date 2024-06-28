from book_class import Book
import csv

library = []
genre_collection = []
with open('library.csv', newline='') as csvfile:
    book_reader = csv.DictReader(csvfile, delimiter=',')
    for row in book_reader:
        #check if genres exists in list of genres. If not on list, add genre to list
        genres = row['genres'].rsplit("'")
        for genre in genres:
           clean_genre = genre.rsplit("'")
           for genre in clean_genre:
              genre.strip()
              genre.strip("'")
              genre.strip("[")
              genre.strip("]")
              if genre not in genre_collection:
                    genre_collection.append(genre)
    
        #create a book object
        #add book object to library

print(genre_collection)
        