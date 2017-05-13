class Book:
    def __init__(self, title, author, publishedYear):
        self.title = title
        self.author = author
        self.publishedYear = publishedYear
        self.isAvailable = True
        self.waitingList = []
        self.id = None
        self.description = None
        self.publisher = None
        self.barcode_id = None
