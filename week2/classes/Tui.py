class Tui:
    def __init__(self):
        self.facts = []

    def __addFact(self, fact):
        self.facts.append(fact)

    def askQuestion(self, fact):
        if fact not in self.facts:
            response = input(f"Is it {fact}? (yes/no): ").strip().lower()

            if response == 'yes':
                self.__addFact(fact)

