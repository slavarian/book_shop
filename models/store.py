from book import Book


class Store:
    """Магазин книг."""

    def __init__(
        self,
        address: str,
        books: list[Book]
    ) -> None:
        self.address = address
        self.books = books
