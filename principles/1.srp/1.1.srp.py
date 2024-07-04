"""
SRC: Single Responsibility Principle
Also known as
SOC: Separation of Concerns


SRP says the class should have its primary responsibility.
It should not take other responsibilities.
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

if __name__ == "__main__":
    j = Journal()
    j.add_entries("I ate today.")
    j.add_entries("I had tea today.")
    print(f"Journal entries:\n{j}")


#NOTE: Above code serves SRP properly.