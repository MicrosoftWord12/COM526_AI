import utils
import heapq

from week1.utils import manhattan_distance


def a_star(maze, start, goal):
    # Create an empty list tha will act as our priority queue
    queue = []
    # goal is 7, 8
    # print(goal)
    # Using heapq.heappush - add the starting node to the queue with a priority of 0
    heapq.heappush(queue, (0, start))

    # Providing some code for you as they will be helpful shortly
    directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
    }
    predecessors = {start: None}    # Enables the get_path function to backtrack
    g_values = {start: 0}   # The g score for each cell

    # loop through the queue, this is an infinite loop that will only stop if the queue is empty
    while len(queue) > 0:
        # cell is a tuple containing h value?, x and y

        prior, currentCell = heapq.heappop(queue) # get this from the priority queue
        # print(currentCell)
        # print(prior, currentCell)


        # Check if the current cell is the goal:
        if currentCell == goal:
            # print(currentCell)
            # print(goal)
            return get_path(predecessors, start, goal)
            # if it is, run this command:
            # return get_path(predecessors, start, goal)


        # Now lets look at where we can move to from the current cell.
        # For each direction do the following:
        for direction in directions:
            yNew, xNew = directions[direction]
            xCurr, yCurr = currentCell

            neighbourCell = (xCurr + xNew, yCurr + yNew)

            # print(neighbourCell)

            # if neighbourCell == (7, 8) or neighbourCell == (8, 7):
            #     print("Potential Goal Found")
            #     print(goal)



            # Figure out the coordinates of the neighbouring cell - the offsets are provided above.
            # For example, if the direction is 'up' then you would deduct 1 from the y coordinate

            # Check that this neighbouring cell is actually a valid move.

            # MY TAKE######################
            # if neighbourCell[1] < 0 or neighbourCell[1] > len(maze) and neighbourCell[0] < 0 or neighbourCell[0] > len(maze):
            #     print("Out of bounds")
            #     continue

            # cellInMaze = maze[neighbourCell[1]][neighbourCell[0]]
            #
            # if cellInMaze != "x":
            #     pass
            ###############################

            # CHAT GPT
            x, y = neighbourCell

            # if x > 0 or x >= len(maze[0]) or y < 0 or y >= len(maze) or y < 0 or y >= len(maze) and maze[y][x] != "x" and neighbourCell not in g_values:

            if x in range(0, len(maze[1])) and y in range(0, len(maze)) and maze[y][x] == "x" and neighbourCell not in g_values:
                print(neighbourCell)



                # cellInMaze = maze[y][x]
                # if cellInMaze != "x" and neighbourCell not in g_values:

            # if maze[yNew][xNew] != "x" and neighbourCell not in g_values and xNew in range(0, len(maze[0])) and yNew in range(0, len(maze)):


            # if cellInMaze != "x" and neighbourCell not in g_values:

            # An invalid move would be one that goes outside the bounds of the map.
            # A cell that contains an 'x' is also invalid.
            # It should also not consider a cell that already has a value stored in the g_values dict created above
            # If the cell is viable:
                # We need to calculate the cost of the move!
                # Our current cell and its cost should be stored in the dictionary g_values
                # Retrieve that value - add 1 to it and we have out cost for the neighbouring cell

                # Add the neighbouring cell and its cost to the g_values dictionary,
                # Where the (x, y) coordinates are the key and the cost is the value

                # Now calculate the H score.
                # In the utils.py file there is a manhatten_distance function.
                # Use this to calculate the distance between the neighbouring cell and the goal.
                # The value it returns will be the H score

                hScore = manhattan_distance(neighbourCell, goal)
                # cost = g_values[neighbourCell]
                cost = prior + 1
                g_values[neighbourCell] = cost

                fScore = hScore + cost
                heapq.heappush(queue, (fScore, neighbourCell))


                # Using that we can calculate the overall F score by adding the cost and the H score

                # Now we have its F-Score we can add this neighbouring cell (a viable move) to our priority queue
                # You should add the cell coords (x, y) to the queue and the prioirty value should be the f-score

                # Allows the get_path function to backtrack later, do not change
                predecessors[neighbourCell] = currentCell
    return None


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze1.txt")     # Change the path as required.
    start = utils.locate(maze_map, 's')
    goal = utils.locate(maze_map, 'g')
    # Looking at the line above, do the same thing but this time, locate the goal
    # Print out the path returned by the a_star function (after you have completed it)
    print(a_star(maze_map, start, goal))
