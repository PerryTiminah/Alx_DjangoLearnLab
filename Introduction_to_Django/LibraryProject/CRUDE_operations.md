# Create
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book)  
# Output: <Book: 1984 by George Orwell (1949)>


# Retrieve
book = Book.objects.get(title="1984")
print(book.title)             # Output: 1984
print(book.author)            # Output: George Orwell
print(book.publication_year)  # Output: 1949


# Update
book.title = "Nineteen Eighty-Four"
book.save()
print(book)  
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>


# Delete
book.delete()
print(Book.objects.all())  
# Output: <QuerySet []>
