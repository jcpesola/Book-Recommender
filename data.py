from book_class import Book
import csv

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
    library = dict()

    # Julia -- This is how you create a set
    books = set()

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
            
            # Julia -- This will print one of your books, take a look at what is getting printed. Take a look at the book class, i made a couple of changes.
            print(book_object)
            # TODO - Comment out this break and run again to see the next thing.
            break

            # Julia -- This is how your "append" something to a dictionary
            library.update({book_object.uuid: book_object})
            # TODO - Comment this break line to see what happens next
            break

            # Julia -- This is how you add something to a set. Now that you know that the Book Object has a UUID attached to it, you can access that UUID like this
            books.add(book_object.uuid)

    # Julia -- Uncomment this line. 
    # Here we have the set - books, we type cast that into a list using `list(books)`, this allows us to access the values inside using an index (like list(books)[0] )
    # Uncomment to see how gets printed
    # print(library.get(list(books)[0]))


    

new()

        