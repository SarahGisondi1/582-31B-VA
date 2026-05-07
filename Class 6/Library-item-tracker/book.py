class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"{self.title.upper()} by {self.author} [{status}]")

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        self.available = True
        print(f"You returned '{self.title}'.")

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name
        
    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title.strip()) > 0