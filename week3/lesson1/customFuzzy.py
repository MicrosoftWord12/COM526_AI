import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# yeah fuck knows tbh
timeToFinish = ctrl.Antecedent(np.arange(0, 24, 1), 'timeToFinish')

# Complexity Levels from 1 - 10
complexity = ctrl.Antecedent(np.arange(0, 11, 1), 'complexity')

# Amount of extra hours required
hours = ctrl.Consequent(np.arange(0, 24, 1), 'hours')

# time
# complexity
# hours

timeToFinish["low"] = fuzz.zmf(timeToFinish.universe, 0, 4)
timeToFinish["medium"] = fuzz.trapmf(timeToFinish.universe, [4, 8, 12, 16])
timeToFinish["high"] = fuzz.smf(timeToFinish.universe, 16, 24)

complexity["easy"] = fuzz.zmf(complexity.universe, 0, 2)
complexity["medium"] = fuzz.trapmf(complexity.universe, [2, 3, 4, 5])
complexity["hard"] = fuzz.smf(complexity.universe, 5, 10)

hours["low"] = fuzz.zmf(hours.universe, 0, 4)
hours["medium"] = fuzz.trapmf(hours.universe, [4, 8, 12, 16])
hours["high"] = fuzz.smf(hours.universe, 16, 24)

timeToFinish.view()
complexity.view()
hours.view()

rule1 = ctrl.Rule(timeToFinish["medium"] | complexity["medium"], hours["high"])
rule2 = ctrl.Rule(complexity["medium"], hours["medium"])
rule3 = ctrl.Rule(timeToFinish["high"] & complexity["easy"], hours["low"])
rule4 = ctrl.Rule(timeToFinish["high"] & complexity["hard"], hours["high"])

ctrlSystem = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
ctrlSim = ctrl.ControlSystemSimulation(ctrlSystem)

ctrlSim.input["timeToFinish"] = 2
ctrlSim.input["complexity"] = 2


ctrlSim.compute()

print(ctrlSim.output["hours"])

hours.view(sim=ctrlSim)