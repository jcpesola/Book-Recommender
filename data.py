from book_class import Book
import csv
from hashmap import HashMap

def old():
    library = []
    genre_collection = []
    with open('library.csv', newline='') as csvfile:
        book_reader = csv.DictReader(csvfile, delimiter=',')
        for row in book_reader:
            #check if genres exists in list of genres. If not on list, add genre to list
            book_genres = []
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
                            book_genres.append(genre)
                    
        
            #create a book object
            inst_name = row['title'].strip()
            globals()[inst_name] = Book(row['title'], row['series'],row['author'], row['rating'], row['description'], book_genres)
            library.append(globals()[inst_name]) 
            #add book object to library

def new():
    genre_collection = set()
    book_count = 0
    library_count = 60000
    library = HashMap(library_count)


    with open('library.csv', newline='') as csvfile:
        book_reader = csv.DictReader(csvfile, delimiter=',')
        for row in book_reader:
            book_count += 1
            #create list of genres
            genre_list = row["genres"].strip("[]").replace("'", "").split(", ")

            #add genres to genre set
            for genre in genre_list:
                genre_collection.add(genre)

            #create hash for each each book object
            title_key = row["title"].replace(" ", "")

            #create object for each book
            book_object = Book(row['title'], row['series'],row['author'], row['rating'], row['description'], genre_list)
            
            #create hashmap of book objects
            library.assign(title_key, book_object)


    print(library.retrieve("thehungergames"))

new()

        