from book import Book

print("Library Name:", Book.library_name)

Book.change_library_name("Downtown Library")
print("Updated Library Name:", Book.library_name)

print("\n--- Title Validation ---")
print("Valid title ('1984'):", Book.is_valid_title("1984"))
print("Valid title ('   '):", Book.is_valid_title("   "))

book1 = Book("1984", "George Orwell", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", False)

print("\n--- Initial Book Info ---")
book1.display_info()
book2.display_info()

print("\n--- Borrowing Book 1 ---")
book1.borrow()
book1.display_info()

print("\n--- Trying to Borrow Book 2 ---")
book2.borrow()

print("\n--- Returning Book 2 ---")
book2.return_book()
book2.display_info()