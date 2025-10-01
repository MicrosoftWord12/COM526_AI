class Rule:
    def __init__(self, conditions: [str], conclusion: [str] or str):
        self.conditions = conditions
        self.conclusion = conclusion

    def __str__(self):
        return f"Conditions: {self.conditions}\nConclusion: {self.conclusion}"