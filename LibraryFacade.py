from Library import Library
from bookfactory import ConcreteBookFactory
from MemberFactory import ConcreteMemberFactory
from Loan import Loan

class LibraryFacade:
    def __init__(self):
        self.library = Library()
        self.book_factory = ConcreteBookFactory()
        self.member_factory = ConcreteMemberFactory()

    def add_book(self, title, author, isbn):
        book = self.book_factory.create_book(title, author, isbn)
        self.library.add_book(book)

    def register_member(self, name, member_id):
        member = self.member_factory.create_member(name, member_id)
        self.library.register_member(member)
        self.library.attach(member)

    def loan_book(self, isbn, member_id):
        book = next((b for b in self.library.books if b.isbn == isbn), None)
        member = next((m for m in self.library.members if m.member_id == member_id), None)
        if book and member:
            if book.available:
                book.available = False
                loan = Loan(book, member)
                self.library.loans.append(loan)
                member.borrowed_books.append(book)
                print(f"Book loaned: {book} to {member}")
            else:
                print(f"Book '{book.title}' is currently not available.")
        else:
            print("Book or member not found.")

    def return_book(self, isbn, member_id):
        loan = next((l for l in self.library.loans if l.book.isbn == isbn and l.member.member_id == member_id and l.return_date is None), None)
        if loan:
            loan.mark_returned()
            loan.book.available = True
            loan.member.borrowed_books.remove(loan.book)
            print(f"Book returned: {loan.book} by {loan.member}")
            self.library.notify(loan.book)
        else:
            print("Active loan not found for this book and member.")

    def search_books(self, title=None, author=None):
        results = self.library.books
        if title:
            results = [b for b in results if title.lower() in b.title.lower()]
        if author:
            results = [b for b in results if author.lower() in b.author.lower()]
        print("Search results:")
        for book in results:
            status = "Available" if book.available else "Not Available"
            print(f"{book} - {status}")

    def list_borrowed_books(self, member_id):
        member = next((m for m in self.library.members if m.member_id == member_id), None)
        if member:
            print(f"Borrowed books for {member}:")
            for book in member.borrowed_books:
                print(book)
        else:
            print("Member not found.")

    def reserve_book(self, isbn, member_id):
        book = next((b for b in self.library.books if b.isbn == isbn), None)
        member = next((m for m in self.library.members if m.member_id == member_id), None)
        if book and member:
            if book.available:
                print(f"Book '{book.title}' is available. No need to reserve.")
            elif book.reserved_by is None:
                book.reserved_by = member
                member.reserved_books.append(book)
                print(f"Book '{book.title}' has been reserved by {member}.")
            else:
                print(f"Book '{book.title}' is already reserved by another member.")
        else:
            print("Book or member not found.")
