class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
            cls._instance.members = []
            cls._instance.loans = []
            cls._instance.observers = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member registered: {member}")

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, book):
        for observer in self.observers:
            observer.update(book)
