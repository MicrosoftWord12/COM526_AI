import utils.utils as utils
# from week4.flame import Flame
# from week4.robot import Robot
# from week4.water_station import WaterStation


class Environment:

    def __init__(self, map_path):
        self.file_path = map_path
        self.world = self.load_assets(self.load_map())

    def load_map(self):
        try:
            with open(self.file_path) as f:
                world_map = row = [[col.lower() for col in line.strip()] for line in f]

                # quick error check
                first_row = len(world_map[0])
                for row in world_map:
                    if len(row) != first_row:
                        raise Exception("Map rows are not even")
                return world_map
        except FileNotFoundError:
            print(f"File not found")
        except PermissionError:
            print(f"File read permissions were denied")
        except IOError as e:
            print(f"IO error: {e}")

        return []

    def load_assets(self, world_map:list):
        for i in range(len(world_map)):
            for j in range(len(world_map[i])):
                if world_map[i][j] == 's':
                    # world_map[i][j] = utils.WaterStation((j, i))
                    world_map[i][j] = utils.WaterStation((j, i))
                elif world_map[i][j] == 'r':
                    world_map[i][j] = utils.Robot((j, i))
                elif world_map[i][j] == '*':
                    world_map[i][j] = utils.Flame()
        return world_map

    def get_cells(self, positions:list) -> dict[tuple[int,int],...]:
        cells = {}
        for pos in positions:
            cells[pos] = self.world[pos[1]][pos[0]]
        return cells

    def __str__(self):
        out = ""
        for row in self.world:
            for col in row:
                out += f"{col}\t"
            out += "\n"
        return out

    def move_to(self, currentPosition, destinationPosition):
        currX, currY = currentPosition
        destX, destY = destinationPosition

        robotInMap: utils.Robot = self.world[currY][currX]

        robotInMap.getRobotMap()[currY][currX] = ""
        self.world[currY][currX] = ""

        robotInMap.getRobotMap()[destY][destX] = robotInMap
        self.world[destY][destX] = robotInMap
        return True



if __name__ == "__main__":
    e = Environment("utils/map.txt")

    # Starting Points
    water: utils.WaterStation = e.world[1][5]
    robot1: utils.Robot = e.world[5][5]

    # print(robot1.displayMap())
    # robot1.water_station_location = e.world[1][5]

    for i in range(25):  # Change 1 simulate more moves. I.e. 100 would simulate 100 moves
        # Call the act method for each agent operating in the environment
        water.act(e)
        # print(e)
        print(robot1.displayMap())
        robot1.act(e)

    robot1.displayMap()





        # return out

        # robot1.calc_path(robot1.position, robot1.water_station_location, "x")




