from library_manager import Library, generate_report

library = Library()
library.add_book("1984", "George Orwell", "Dystopia")
library.add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
library.add_book("Brave New World", "Aldous Huxley", "Dystopia")

print("Поиск по жанру Dystopia:")
for book in library.find_by_genre("Dystopia"):
    print(book)

print("\nУдаляем книгу '1984'")
library.remove_book("1984")

print("\nОтчёт:")
print(generate_report(library))
