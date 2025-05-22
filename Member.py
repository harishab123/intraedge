class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.reserved_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

    def update(self, book):
        print(f"Notification: {self.name}, the book '{book.title}' is now available.")
