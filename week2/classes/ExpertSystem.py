from week2.classes import Rule
from week2.classes.Tui import Tui


class ExpertSystem:
    def __init__(self):
        # Overall Rules List
        self.rules = []

        # Text User Interface
        self.tui = Tui()

        # Facts from User
        self.facts = set()

        # Conclusions
        self.conclusion = []

    def add_rule(self, rule):
        self.rules.append(rule)

    # def add_fact(self, fact):
    #     self.facts.add(fact)
    #
    # def ask_user_for_fact(self, fact):
    #     if fact not in self.facts:
    #         response = input(f"Is it true that its {fact}? (yes/no): ").strip().lower()
    #         if response == 'yes':
    #             self.add_fact(fact)

    # def infer(self):
    #     new_facts = True
    #     while new_facts:
    #         new_facts = False
    #         for rule in self.rules:
    #             if all(condition in self.facts for condition in rule.conditions) and rule.conclusion not in self.facts:
    #                 self.facts.add(rule.conclusion)
    #                 print(rule.conclusion)
    #                 new_facts = True
    #                 print(f"Inferred: {rule.conclusion}")
    #             elif any(condition not in self.facts for condition in rule.conditions):
    #                 print("Any")
    #                 for condition in rule.conditions:
    #                     if condition not in self.facts:
    #                         self.ask_user_for_fact(condition)
    #                         break # Ask one fact at a time

    def infer(self):
        checkedConditions = []

        for rule in self.rules:
            rule: Rule = rule

            for i in range(len(rule.conditions)):
                if rule.conditions[i] not in checkedConditions:
                    condition = rule.conditions[i]

                    self.tui.askQuestion(condition)
                    checkedConditions.append(rule.conditions[i])



        return self.output(checkedConditions)

    def output(self, checkedConditions):
        currentFacts = self.tui.facts
        conditionsMet = set()

        for condition in checkedConditions:
            if condition in currentFacts:
                conditionsMet.add(condition)

        for rule in self.rules:
            if set(rule.conditions) == conditionsMet:
                return rule.conclusion

        conditionsMet.clear()




