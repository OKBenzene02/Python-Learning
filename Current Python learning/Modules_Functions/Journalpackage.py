class Journal:
    def __init__(self, journal_id, journal, experience):
        self.journal = journal
        self.journal_id = journal_id
        self.experience = experience

    def details(self):
        print(f"Name: Liyakhat yousuf mogal\n"
              f"Jounral ID: {self.journal_id}\n"
              f"Journal: {self.journal}\n"
              f"Journal Experience: {self.experience}")


printing = Journal("The Travel logs", 12093, "Adventurous and Thrilling")