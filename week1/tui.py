import pathfinding
import utils


def display_map(maze):
    mazeCopy = [row for row in maze]
    return "\n".join("".join(row) for row in mazeCopy)


def show_path(maze, path):
    maze_copy = [row for row in maze]

    for (x, y) in path:
        if maze_copy[y][x] not in ('s', 'g'):
            maze_copy[y][x] = '*'

    return "\n".join("".join(row) for row in maze_copy)

if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze1.txt")
    start = utils.locate(maze_map, 's')
    goal = utils.locate(maze_map, 'g')

    print(show_path(maze_map, pathfinding.a_star(maze_map, start, goal)))