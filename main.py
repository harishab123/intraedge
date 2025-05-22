from LibraryFacade  import LibraryFacade


def main():

    facade = LibraryFacade()

    facade.add_book("The Harish", "Testing", "1234567890")
    facade.add_book("1984", "Testing", "1234567891")

    facade.register_member("test1", "M001")
    facade.register_member("Test2", "M002")


    facade.loan_book("1234567890", "M001")


    facade.return_book("1234567890", "M001")

  
    facade.search_books(title="1984")


    facade.list_borrowed_books("M001")

    facade.reserve_book("1234567891", "M002")

if __name__ == "__main__":
    main()