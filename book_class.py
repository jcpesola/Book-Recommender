import uuid

class Book:
    def __init__(self, title, series, author, rating, description, genres):
        self.uuid = uuid.uuid1()
        self.title = title
        self.series = series
        self.author = author
        self.rating = rating
        self.description = description
        self.genres = genres
    
    def __repr__(self) -> str:
        genre_string = ""
        for genre in self.genres:
            genre_string = genre_string + genre + ", "
        genre_string = genre_string[:-2]
        description = "\n\nThe book '{title}' by {author} has a rating of {rating} out of 5 stars and is categorized as {genres}. The description is as follows: {description}".format(title=self.title, author=self.author, rating=self.rating, genres=genre_string, description=self.description)
        return description
    
# test = Book("Hunger Games", "Hunger Games", "Suzanne Collins", "5.0", "In a post-apocolyptic world, Katniss tries to save her sister", ["teen", "fantasy", "dystopian"])
# print(test)