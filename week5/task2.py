from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt


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
    ('AbsenceHistory', 'MotivationLevel'),
    ('UpcomingAssessment', 'MotivationLevel'),
    ('AbsenceHistory', 'Attendance'),
    ('MotivationLevel', 'Attendance'),
    ('DaysOfWeek', 'Attendance'),
    ('Weather', 'Attendance')
])

# Independence
weatherCpd = TabularCPD('Weather', variable_card=2, values=[[0.5], [0.5]])
daysOfWeek = TabularCPD("DaysOfWeek", variable_card=5, values=[[0.1], [0.4], [0.2], [0.2], [0.1]])
absenceHistory = TabularCPD('AbsenceHistory', variable_card=2, values=[[0.13], [0.87]])
upcomingAssessment = TabularCPD('UpcomingAssessment', variable_card=2, values=[[0.5], [0.5]])

# Lowest Level Nodes
motivationLevel = TabularCPD('MotivationLevel', variable_card=2, values=[[0.57, 0.72, 0.31, 0.95],
                                                                                 [0.43, 0.28, 0.69, 0.05]], evidence=["AbsenceHistory", "UpcomingAssessment"], evidence_card=[2, 2])
attendance = TabularCPD('Attendance', variable_card=2, values=[[0.1, 0.43, 0.33, 0.25, 0.89, 0.77, 0.64, 0.43, 0.9, 0.99, 0.1, 0.43, 0.33, 0.25, 0.89, 0.77, 0.64, 0.43, 0.9, 0.99, 0.1, 0.43, 0.33, 0.25, 0.89, 0.77, 0.64, 0.43, 0.9, 0.99, 0.1, 0.43, 0.33, 0.25, 0.89, 0.77, 0.64, 0.43, 0.9, 0.99],
                                                                       [0.9, 0.57, 0.67, 0.75, 0.11, 0.23, 0.36, 0.57, 0.1, 0.01, 0.9, 0.57, 0.67, 0.75, 0.11, 0.23, 0.36, 0.57, 0.1, 0.01, 0.9, 0.57, 0.67, 0.75, 0.11, 0.23, 0.36, 0.57, 0.1, 0.01, 0.9, 0.57, 0.67, 0.75, 0.11, 0.23, 0.36, 0.57, 0.1, 0.01]], evidence=['AbsenceHistory', 'MotivationLevel', 'DaysOfWeek', 'Weather'], evidence_card=[2, 2, 5, 2])

model.add_cpds(weatherCpd, daysOfWeek, absenceHistory, upcomingAssessment, motivationLevel, attendance)
assert model.check_model()

# Inference
inference = VariableElimination(model)
query_result = inference.query(variables=['Attendance'], evidence={'Weather': 0, 'DaysOfWeek': 0, 'AbsenceHistory': 0, 'UpcomingAssessment': 0, 'MotivationLevel': 0})

# print(query_result)
# display_model(model)      # Uncomment to visually see your model
print_cpds(model)         # Uncomment to see the CPD tables for each node