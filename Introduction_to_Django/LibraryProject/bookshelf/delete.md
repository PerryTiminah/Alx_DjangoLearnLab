# Delete Operation

```python
from bookshelf.models import Book

# First, get the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by checking all books
Book.objects.all()

# Output
<QuerySet []>

