from book_class import Book
import csv
import json

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
    library = []
    genre_collection = []
    with open('library.csv', newline='') as csvfile:
        book_reader = csv.DictReader(csvfile, delimiter=',')
        for row in book_reader:
            #check if genres exists in list of genres. If not on list, add genre to list
            # print(row["genres"])
            # print(row["genres"].strip("[]"))
            # print(row["genres"].strip("[]").split(", "))
            genre_list = row["genres"].strip("[]").split(", ")
            for el in genre_list:
                new_el = el[1:-1]
                print(el, " => ", new_el)
                print(el, " => ", el.replace("'", ""))
            print(genre_list)


        #    genres_stripped = row["genres"].strip("[]")
        #    genres_stripped2 = genres_stripped.strip(",")
        #    genres_stripped3 = genres_stripped2.strip('""')
        #    genres_split = genres_stripped3.split("''")
        #    print(genres_stripped)
        #    print(genres_split)
        #    print(type(genres_split))
            break                    
        


# print(library[1])
# print(library)

new()
        