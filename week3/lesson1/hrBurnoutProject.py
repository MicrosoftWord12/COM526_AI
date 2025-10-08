import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 24 hours span
planningTime = ctrl.Antecedent(np.arange(0, 23, 1), 'planningTime')
payPerHour = ctrl.Antecedent(np.arange(0, 16, 1), 'payPerHour')

# How many projects ONE person can do consecutively
# 0 - 10 cases (hopefully)
workload = ctrl.Consequent(np.arange(0, 11, 1), 'workload')

# ideas
# currentTask, mentalHealth, overtime, deadlines


planningTime["low"] = fuzz.zmf(planningTime.universe, 0, 4)
planningTime["medium"] = fuzz.trapmf(planningTime.universe, [4, 8, 12, 16])
planningTime["high"] = fuzz.smf(planningTime.universe, 16, 24)

payPerHour["small"] = fuzz.zmf(payPerHour.universe, 0, 6)
payPerHour["ok"] = fuzz.trapmf(payPerHour.universe, [6, 8, 10, 12])
payPerHour["expensive"] = fuzz.smf(payPerHour.universe, 13, 16)

workload["low"] = fuzz.zmf(workload.universe, 1, 3)
workload["medium"] = fuzz.trapmf(workload.universe, [3, 4, 5, 6])
workload["high"] = fuzz.smf(workload.universe, 6, 10)

budgetFriendlyRule = ctrl.Rule(planningTime["low"] & payPerHour["small"], workload["high"])
expensiveBudget = ctrl.Rule(planningTime["high"] & payPerHour["expensive"], workload["low"])
mediocreBudget = ctrl.Rule(planningTime["medium"] | payPerHour["ok"], workload["medium"])
highPlanOkPay = ctrl.Rule(planningTime["high"] | payPerHour["ok"], workload["low"])

hrControlSys = ctrl.ControlSystem([budgetFriendlyRule, expensiveBudget, mediocreBudget, highPlanOkPay])
hrControlSysSim = ctrl.ControlSystemSimulation(hrControlSys)

# 0 - 23
hrControlSysSim.input["planningTime"] = 5

# 0 - 16
hrControlSysSim.input["payPerHour"] = 3

hrControlSysSim.compute()

print(hrControlSysSim.output["workload"])

workload.view(sim=hrControlSysSim)
# gradcracker