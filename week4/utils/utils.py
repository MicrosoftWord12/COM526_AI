from week4.base.agent import Agent
from week4.water_station import WaterStation
from week4.robot import Robot
from week4.flame import Flame


def is_robot(object: Agent):
    if isinstance(object, Robot):
        return True
    return False


def is_water_station(object: Agent):
    if isinstance(object, WaterStation):
        return True
    return False


def is_flame(object: Agent):
    if isinstance(object, Flame):
        return True
    return False