class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_rented = False

    def __str__(self):
        return f'{self.title}'
    
class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.rented_books = []

    def rent_a_book(self, book):
        if not book.is_rented:
            book.is_rented = True
            self.rented_books.append(book)
            return f'{self.name}이/가 {book.title}를 빌려감'
        else:
            f'{book.title}은 이미 대여중'

소나기 = Book('소나기', '황순원')
은세 = Student('은세', '1308')

print(은세.rent_a_book(소나기))