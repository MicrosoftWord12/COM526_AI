from week2.classes.ExpertSystem import ExpertSystem
from week2.classes.Rule import Rule

# Example usage
if __name__ == "__main__":
    # Create an expert system
    es = ExpertSystem()
    # Add rules
    # es.add_rule(Rule(["sunny", "rainy"], "wear_sunglasses"))
    es.add_rule(Rule(["sunny", "rainy"], ["wear_sunglasses", "wear_jacket"]))
    es.add_rule(Rule(["rainy"], ["bring_umbrella"]))
    es.add_rule(Rule(["stormy", "rainy", "cold"], ["bring_coat", "bring_thermals"]))
    # es.add_rule(Rule(["rainy"], "take_umbrella"))
    # es.add_rule(Rule(["sunny", "weekend"], "go_to_beach"))
    # Perform inference
    conclusions = es.infer()

    if type(conclusions) == list:
        for conclusion in conclusions:
            print(f"I Suggest you: {conclusion}")
    else:
        print("Hmm, Unsure!!")
    # Print final facts
    # print("Final facts:", es.facts)