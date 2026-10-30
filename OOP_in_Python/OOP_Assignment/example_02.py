# Create a class with the following attributes:
# • title
# • author
# • list of reviews
# And add methods to:
# • add a new review
# • count reviews
# • display all reviews
# Concept: Encapsulation



class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__reviews = [] 
        
    def add_review(self, review):
        if review:
            self.__reviews.append(review)
            print(f"Review added successfully for '{self.title}'.")
        else:
            print("Review cannot be empty!")
            

    def count_reviews(self):
        return len(self.__reviews)
        

    def display_reviews(self):
        print(f"\n--- Reviews for '{self.title}' by {self.author} ---")
        if not self.__reviews:
            print("No reviews yet.")
        else:
            for index, review in enumerate(self.__reviews, start=1):
                print(f"{index}. {review}")
        print(f"Total Reviews: {self.count_reviews()}\n")

#======================================================


my_book = book("Python Programming", "John Doe")


my_book.add_review("Great book for beginners!")
my_book.add_review("Very clear explanations and examples.")
my_book.add_review("Loved the OOP chapters.")


my_book.display_reviews()