class Books:
    def __init__(self, book_id, access_number, book_name, author, publication):
        self.id = book_id
        self.number = access_number
        self.name = book_name
        self.author = author
        self.publication = publication

    def details(self):
        print(f"Book ID: {self.id}\n"
              f"Book Number: {self.number}\n"
              f"Book Name: {self.name} \n"
              f"Book Author: {self.author} \n"
              f"Book Publication: {self.publication}")


Printing = Books("BA-101", 123234, "Mighty Python", "Harry Bhai", "Dewaan Productions")