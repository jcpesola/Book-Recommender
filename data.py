from book_class import Book
import csv

library = []

with open('Computer Science /Book Recomender/library.csv', newline='') as csvfile:
    book_reader = csv.DictReader(csvfile, delimiter=',')
    for row in book_reader:
        print(row['title'])
