class TooManyPagesError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f'<Book {self.name}, read {self.pages_read} out of {self.page_count}>'
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesError(
                f'You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages.'
            )
        self.pages_read += pages
        print(
            f'You have now read {self.pages_read} pages out of {self.page_count}.')


py101 = Book('Py101', 50)

try:
    py101.read(35)
    py101.read(50)
except TooManyPagesError as e:
    print(e)
