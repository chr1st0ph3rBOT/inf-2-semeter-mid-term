from datetime import date

class Book:
    def __init__(self, title, author, publish_year):
        self.title = title
        self.author = author
        self.publish_year = publish_year

    def get_years_since_publication(self):
        current_year = date.today().year # date.today() -> datetime.date(2025, 7, 17)
        return current_year - self.publish_year
    
book = Book('Demian', 'Herman Hesse', 1919)
print(book.get_years_since_publication())