
---

### **delete.md**
```markdown
# Delete Operation

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

## output ##
(1, {'app_name.Book': 1})   # delete confirmation (number of objects deleted)

<QuerySet []>
