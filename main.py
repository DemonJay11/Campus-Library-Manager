
from models import LibraryItem, Book, Magazine, DVD, Member


# 1. Create library items
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Naruto", 2, 102)
dvd = DVD("Python - Zero to Hero", 3, 90)


# 2. Create members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)


# 3. Borrowing items
print("\n========== BORROWING ITEMS ==========")

try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.borrow(dvd)
    print("Alice borrowed:", dvd.describe())
except ValueError as e:
    print("Could not borrow:", e)


# 4. Attempt to borrow an already borrowed item
print("\n========== ITEM AVAILABILITY ==========")

try:
    bob.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)


# 5. Attempt to borrow the same item twice
print("\n========== DUPLICATE BORROWING ==========")

try:
    alice.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)


# 6. Borrowing limit test
print("\n========== BORROWING LIMIT ==========")

try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.borrow(dvd)
except ValueError as e:
    print("Could not borrow:", e)


# 7. Return an item that was never borrowed
print("\n========== INVALID RETURN ==========")

try:
    bob.return_item(dvd)
except ValueError as e:
    print("Could not return:", e)


# 8. Return a borrowed item with late fee
print("\n========== VALID RETURN ==========")

try:
    fee = bob.return_item(magazine, days_late=7)

    print("Magazine returned successfully.")
    print("Late fee: Rs", fee)

except ValueError as e:
    print("Could not return:", e)


# 9. Polymorphism
print("\n========== POLYMORPHISM ==========")

items = [book, magazine, dvd]

for item in items:
    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )


# 10. Class attribute
print("\n========== CLASS ATTRIBUTE ==========")

print("Total items created:", LibraryItem.total_items)


# 11. Borrowed titles
print("\n========== BORROWED TITLES ==========")

print("Alice:", alice.borrowed_titles())
print("Bob:", bob.borrowed_titles())


# 12. Encapsulation
print("\n========== ENCAPSULATION ==========")

try:
    print(book.__available)
except AttributeError:
    print("Cannot access private availability directly.")

print("Book availability:", book.is_available())
