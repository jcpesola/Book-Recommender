import requests
from typing import Dict
from book_class import Book
import uuid

genre_collection: Dict[str, set] = dict()
library: Dict[uuid.UUID, Book] = dict()

def fetch_books_by_genre(genre: str):
    """Fetch books for a specific genre (subject) and add them to the genre_collection."""
    print(f"Fetching books for genre (subject): {genre}...")
    url = f"https://openlibrary.org/subjects/{genre.replace(' ', '_').lower()}.json?limit=50"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            works = data.get("works", [])
            
            if works:
                for book in works:
                    title = book.get("title", "Unknown Title")
                    author = ", ".join([a.get("name", "Unknown Author") for a in book.get("authors", [])])
                    description = (
                        book.get("description", "No description available.")
                        if isinstance(book.get("description"), str)
                        else "No description available."
                    )
                    subjects = book.get("subject", [])
                    rating = "N/A"  # Rating not available in the API
                    
                    # Convert subjects to lowercase for consistent searching
                    genres = [s.lower() for s in subjects] if subjects else [genre.lower()]
                    
                    book_object = Book(title, None, author, rating, description, genres)
                    library[book_object.uuid] = book_object
                    
                    for subject in genres:
                        if subject not in genre_collection:
                            genre_collection[subject] = set()
                        genre_collection[subject].add(book_object.uuid)
                        
                print(f"Books for genre '{genre}' fetched successfully.")
            else:
                print(f"No books found for genre '{genre}'.")
        else:
            print(f"Failed to fetch books for genre '{genre}'. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching books for genre '{genre}'. Please try again later. Error: {e}")

def initialize_genres():
    """Initialize a predefined list of genres and handle user input to display them."""
    print("Initializing genre list...")
    all_subjects = [
        "Arts", "Architecture", "Art Instruction", "Art History", "Dance", "Design", "Fashion", "Film", "Graphic Design", 
        "Music", "Music Theory", "Painting", "Photography", "Animals", "Bears", "Cats", "Kittens", "Dogs", "Puppies", 
        "Fiction", "Fantasy", "Historical Fiction", "Horror", "Humor", "Literature", "Magic", 
        "Mystery and detective stories", "Plays", "Poetry", "Romance", "Science Fiction", "Short Stories", "Thriller", 
        "Young Adult", "Science & Mathematics", "Biology", "Chemistry", "Mathematics", "Physics", "Programming", 
        "Business & Finance", "Management", "Entrepreneurship", "Business Economics", "Business Success", "Finance", 
        "Children's", "Kids Books", "Stories in Rhyme", "Baby Books", "Bedtime Books", "Picture Books", "History", 
        "Ancient Civilization", "Archaeology", "Anthropology", "World War II", "Social Life and Customs", "Health & Wellness", 
        "Cooking", "Cookbooks", "Mental Health", "Exercise", "Nutrition", "Self-help", "Biography", "Autobiographies", 
        "History", "Politics and Government", "World War II", "Women", "Kings and Rulers", "Composers", "Artists", 
        "Social Sciences", "Anthropology", "Religion", "Political Science", "Psychology", "Places", "Brazil", "India", 
        "Indonesia", "United States", "Textbooks", "History", "Mathematics", "Geography", "Psychology", "Algebra", 
        "Education", "Business & Economics", "Science", "Chemistry", "English Language", "Physics", "Computer Science", 
        "Books by Language", "English", "French", "Spanish", "German", "Russian", "Italian", "Chinese", "Japanese"
    ]

    # Add all subjects to the genre collection
    for subject in all_subjects:
        genre_collection[subject.lower()] = set()  # Initialize empty sets for each genre

    # Prompt the user if they want to see the genres
    show_genres = input("\nWould you like to see a list of available genres? Enter Y for yes and N for no.\n\n").lower()

    while show_genres not in ["y", "n"]:
        show_genres = input("\nInvalid response. Please enter Y for yes or N for no.\n\n").lower()

    if show_genres == "y":
        print("\nAvailable genres:")
        print(", ".join(all_subjects))
    elif show_genres == "n":
        print("\nOkay! You can still search by genre later in the program.")

def user_interaction():
    print("\n\nWelcome to Julia's Library!\n\nWe have a curated selection of books for you!\n\nLet's get started!\n\n")
    initialize_genres()  # Populate genres at the start
    relevant_uuid = set()
    user_input_1 = input("\nWould you like to narrow down your search by genres? Enter Y for yes and N for no.\n\n").lower()
    
    while user_input_1 not in ["y", "n"]:
        user_input_1 = input("\n\nSorry, your response is not recognizable. Please enter Y for yes and N for no.\n\n").lower()
    
    if user_input_1 == "n":
        print("\n\nThanks for using Julia's Book Library! We hope you find your next favorite read. \n\nGoodbye!")
        return

    while user_input_1 == "y":
        # Show list of genres if user wants
        show_genres = input("\nWould you like to see a list of all genres? Enter Y for yes and N for no.\n\n").lower()
        while show_genres not in ["y", "n"]:
            show_genres = input("\n\nSorry, your response is not recognizable. Please enter Y for yes and N for no.\n\n").lower()
        if show_genres == "y":
            print("\nAvailable genres:")
            print(", ".join(genre_collection.keys()))

        genre = input("\nPlease enter a genre (e.g., fantasy, science_fiction, mystery):\n\n").lower()
        
        # Always fetch books for the selected genre
        fetch_books_by_genre(genre)
        
        # Check if the genre has any books
        if genre in genre_collection and genre_collection[genre]:
            # Combine with existing relevant UUIDs if narrowing the search
            if not relevant_uuid:
                relevant_uuid = genre_collection[genre]
            else:
                relevant_uuid = relevant_uuid.intersection(genre_collection[genre])
            
            if not relevant_uuid:
                print("\nNo books found matching the selected filters.")
                retry = input("\nWould you like to start a new search? Enter Y for yes and N for no.\n\n").lower()
                while retry not in ["y", "n"]:
                    retry = input("\n\nSorry, your response is not recognizable. Please enter Y for yes and N for no.\n\n").lower()
                if retry == "y":
                    relevant_uuid.clear()
                    continue
                else:
                    print("\n\nThanks for using Julia's Book Library! We hope you find your next favorite read. \n\nGoodbye!")
                    return
            
            # Show limited books
            sorted_uuids = sort_and_display_books(relevant_uuid, limit=10)

            # Ask if user wants to see book details
            see_book_info = input("\n\nWould you like to see information on any of the titles listed? Enter Y for yes and N for no.\n\n").lower()
            while see_book_info not in ["y", "n"]:
                see_book_info = input("\n\nSorry, your response is not recognizable. Please enter Y for yes and N for no.\n\n").lower()
            
            while see_book_info == "y":
                book_info = get_info(sorted_uuids)
                print(book_info)
                see_book_info = input("\n\nWould you like to see information on any other title? Enter Y for yes and N for no.\n\n").lower()
                while see_book_info not in ["y", "n"]:
                    see_book_info = input("\n\nSorry, your response is not recognizable. Please enter Y for yes and N for no.\n\n").lower()
        else:
            print("\n\nSorry, we couldn't find books for that genre. Please try again.")

        # Ask to narrow down further
        user_input_1 = input("\n\nWould you like to narrow down your search further by selecting another genre? Enter Y for yes and N for no.\n\n").lower()
        while user_input_1 not in ["y", "n"]:
            user_input_1 = input("\n\nSorry, your response is not recognizable. Please enter Y for yes and N for no.\n\n").lower()

    if user_input_1 == "n":
        print("\n\nThanks for using Julia's Book Library! We hope you find your next favorite read. \n\nGoodbye!")

def sort_and_display_books(relevant_uuid: set, limit=10) -> list:
    uuid_array = merge_sort(list(relevant_uuid))
    count = 1
    displayed_uuids = []
    for uuid in uuid_array[:limit]:
        print(f"\n{count}. {library[uuid].title}")
        displayed_uuids.append(uuid)
        count += 1
    return displayed_uuids

def merge_sort(relevant_uuid: list) -> list:
    if len(relevant_uuid) <= 1:
        return relevant_uuid

    mid = len(relevant_uuid) // 2
    left_half = merge_sort(relevant_uuid[:mid])
    right_half = merge_sort(relevant_uuid[mid:])

    return merge(left_half, right_half)

def merge(left: list, right: list) -> list:
    sorted_list = []
    while left and right:
        if library[left[0]].title <= library[right[0]].title:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    sorted_list.extend(left)
    sorted_list.extend(right)
    return sorted_list

def get_info(sorted_uuids: list):
    book_number = input("\n\nPlease enter the number of the title you would like to see more information on:\n\n")
    book_idx = int(book_number) - 1
    if 0 <= book_idx < len(sorted_uuids):
        return library[sorted_uuids[book_idx]]
    else:
        print("\n\nSorry, that number was not recognized. Please try again.\n\n")
        return get_info(sorted_uuids)

# Start the program
user_interaction()

