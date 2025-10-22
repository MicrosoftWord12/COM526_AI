from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt

# #### HELPFUL PROVIDED FUNCTIONS

# Credit: stack overflow - https://stackoverflow.com/questions/70625490/how-to-print-the-printing-full-cpd-from-pgmpy
def print_full(cpd):
    backup = TabularCPD._truncate_strtable
    TabularCPD._truncate_strtable = lambda self, x: x
    print(cpd)
    TabularCPD._truncate_strtable = backup


def print_cpds(bayes_model):
    for cpd in bayes_model.get_cpds():
         print_full(cpd)


def display_model(bayes_model):
    model_daft = model.to_daft()
    model_daft.render()
    plt.show()


# #### END OF HELPFUL PROVIDED FUNCTIONS

model = DiscreteBayesianNetwork([
     ('Winter', 'Rain'),
     ('Rain', 'Accident'),
     ('RushHour', 'TrafficJam'),
     ('Accident', 'TrafficJam'),
     ('Roadworks', 'TrafficJam'),
])

# Conditional probability distributions (CPDs)
cpdWinter = TabularCPD(variable="Winter", variable_card=2, values=[[0.49], [0.51]])
cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.59, 0.41],
                                                                [0.41, 0.59]], evidence=['Winter'], evidence_card=[2])
cpdRushHour = TabularCPD(variable='RushHour', variable_card=2, values=[[0.49], [0.51]])
cpd_accident = TabularCPD(variable='Accident', variable_card=2, values=[[0.89, 0.11], [0.11, 0.89]], evidence=['Rain'], evidence_card=[2])
cpd_roadworks = TabularCPD(variable='Roadworks', variable_card=2, values=[[0.9], [0.1]])

# No Idea how this is working
# Not a clue of what this is doing
cpd_trafficjam = TabularCPD(variable='TrafficJam', variable_card=2, values=[[0.69, 0.75, 0.25, 0.65, 0.99, 0.45, 0.4, 0.2], [0.31, 0.25, 0.75, 0.35, 0.01, 0.55, 0.6, 0.8]], evidence=['RushHour','Accident', 'Roadworks'], evidence_card=[2, 2, 2])

# Add CPDs to the model and check validity
model.add_cpds(cpdWinter, cpd_rain, cpdRushHour, cpd_accident, cpd_roadworks, cpd_trafficjam)
assert model.check_model()

# Inference
inference = VariableElimination(model)
query_result = inference.query(variables=['TrafficJam'], evidence={'Winter': 0, 'Rain': 0, 'Accident': 0, 'Roadworks': 0})

# print(query_result)
# display_model(model)      # Uncomment to visually see your model
print_cpds(model)         # Uncomment to see the CPD tables for each node