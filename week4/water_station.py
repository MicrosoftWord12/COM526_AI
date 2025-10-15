import utils.utils as utils
from week4.base.agent import Agent


class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        # print(percept)

        for coords, neighbour in percept.items():
            if utils.is_robot(neighbour):
                return "refill", coords, neighbour

        return "idle", None, None

    def act(self, environment):
        cell = self.sense(environment)
        decision, coords, neighbour = self.decide(cell)

        if decision == "refill":
            neighbour.refill()




    def __str__(self):
        return '💧'
