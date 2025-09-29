from relationship_app.models import Author, Book, Library, Librarian

def run_demo():
    # Create an author
    author = Author.objects.create(name="George Orwell")

    # Create a book by the author
    book = Book.objects.create(title="1984", author=author)

    # Create a library
    library = Library.objects.create(name="Central Library")
    library.books.add(book)

    # Create a librarian for the library
    librarian = Librarian.objects.create(name="Martha", library=library)

    # Queries
    print("Books by George Orwell:", [b.title for b in Book.objects.filter(author=author)])
    print("Books in Central Library:", [b.title for b in library.books.all()])
    print("Librarian for Central Library:", librarian.name)

    