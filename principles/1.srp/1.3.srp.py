"""
Below code fixes the SRP violation of the Journal class
handling persistance of journal entries,
by creating a separate PersistanceManager class,
which will be responsible for saving the object to a perticular file.
"""

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entries(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    journal = Journal()
    journal.add_entries("First entry")
    journal.add_entries("Second entry")
    journal.add_entries("Third entry")
    # print(journal)
    file = "journal_srp.txt"
    PersistanceManager.save_to_file(journal, file)

    with open(file, "r") as f:
        print(f.read())
