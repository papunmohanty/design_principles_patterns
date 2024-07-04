"""
Below code violates SRP
by giving the ability for a journal to save in a file, load
from the file, load from web.
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

    # Bad idea to give the extra ability to save to file.
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()
    
    # Bad idea to give the extra ability to load from file.
    def load(self, filename):
        pass

    
    # Bad idea to give the extra ability to load from web.
    def load_from_web(self, uri):
        pass


if __name__ == "__main__":
    j = Journal()
    j.add_entries("I ate today.")
    j.add_entries("I had tea today.")
    print(f"Journal entries:\n{j}")
    j.save("journal.txt")
