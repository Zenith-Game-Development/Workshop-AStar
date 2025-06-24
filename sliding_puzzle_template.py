import heapq
import time
import pygame

# The goal is to have the blank tile (0) in the bottom right cell, and everything else in
# ascending order.
GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0),
)
# Constants used for rendering.
TILE_SIZE = 100
FONT_SIZE = 60
MARGIN = 8
FPS = 60
WAIT_TIME = 0.5


def find_blank(board):
    """
    Finds the blank cell on the board.

    Parameters:
        board (list): The puzzle board we are searching for the blank cell.
    """
    # Task 1:
    # Remember that the position is not (x, y) but rather (row, column).

    # For each value, check if it's the blank cell. If it is, return it's position.

    # Remove once you add your implementation.
    return (0, 0)


def move_blank(board, direction):
    """
    Moves the blank cell in the specified direction.

     Parameters:
         board (list): The puzzle board we are moving the blank cell around in.
         direction (tuple): The direction we are moving the blank cell in.
    """
    # Task 2:
    # Remember that the direction is not (x, y) but rather (row, coloumn)!

    # Find the blank cell.

    # Determine the new position.

    # If the new position is within bounds of the board, swap the cells.

    # Remove once you add your implementation.
    return


def manhattan_distance(state):
    """
    Calculates the Manhattan distance between a puzzle state and the goal state. Does this by
    determining the "distance" of each cell from its goal position. For example, if tile 5 is
    currently at (0, 0) and it's goal position is (1, 1), then it's distance would be 2. Does
    this for each tile and returns the total distance of the puzzle state.

    Parameters:
        state (PuzzleState): The current state of the puzzle we are calculating the distance for.
    Returns:
        int: The distance of this puzzle state to the goal state.
    :param state:
    :return:
    """
    # Task 3:

    # Initially, distance should be zero.

    # For each value in the board.

            # Get the value of the cell.

            # If this is the blank cell, skip this value.

            # Get the goal position of this value.

            # Calculate the distance of the tiles position to the goal position, and add it to
            # the puzzle's total distance.

    # Return the final distance.

    # Remove once you add your implementation.
    return 0

def astar(start_state):
    """
    Explores the states of the puzzle using the A* algorithm until it finds an optimal path to
    the goal state. Follows the paths discovered that are closest to the goal state and have
    the lowest cost so far. If it finds a path that leads to the goal state, it returns it.

    Parameters:
        start_state (PuzzleState): The current state of the puzzle we are starting from.
    Returns:
        list: The path of moves that is found to reach the goal state at the lowest cost.
    """
    # Task 4:

    # A priority queue of possible puzzle states we want to explore.
    # Sorted in ascending order by cost.
    frontier = []
    # Push the distance of the initial state to the goal state (priority), the cost to get up to
    # this state from the start state, and the state itself into frontier.
    heapq.heappush(frontier, (manhattan_distance(start_state), 0, start_state))
    # To remember the shortest known cost of the path to each state.
    # The start_state's cost is 0 always.
    cost_so_far = {start_state : 0}

    # While there are still nodes to explore in frontier.

        # Pop the state with the lowest cost.

        # If the current state's board is the goal state, return the path of this state.

        # Otherwise, search through the neighboring moves of the blank cell.

            # The new cost should be the original cost, plus one move.

            # If the state is new or it costs less than previous paths to that state.

                # Add its cost to the dictionary of costs so far.

                # Calculate its priority (Manhattan distance).

                # Push the state's priority, cost, and state into frontier, so it can be explored
                # as well.

    # If no path is found, return None.
    return None


### Used to run the game, do not modify past this line! ###

def draw_board(screen, board, font):
    """
    Draws the puzzle board on the screen.

    Parameters:
        screen (pygame.Surface): The pygame screen.
        board (list): The puzzle board we are drawing.
        font (pygame.font.SysFont): The font we use to draw the numbers on the tiles.
    """
    # Draw the background.
    screen.fill((255, 255, 255))
    # For each tile.
    for r in range(3):
        for c in range(3):
            # Get the value.
            value = board[r][c]
            # If not the blank tile, draw it and the number.
            if value != 0:
                rect = pygame.Rect(c * TILE_SIZE + MARGIN, r * TILE_SIZE + MARGIN, TILE_SIZE, TILE_SIZE)
                # Draw the blue square.
                pygame.draw.rect(screen, (100, 100, 255), rect)
                # Draw the black outline.
                pygame.draw.rect(screen, (0, 0, 0), rect, 3)
                # Draw the tile's value.
                text = font.render(str(value), True, (255, 255, 255))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    # Update the screen.
    pygame.display.flip()


def main():
    """The main game code."""
    pygame.init()

    screen = pygame.display.set_mode((TILE_SIZE * 3 + MARGIN * 2, TILE_SIZE * 3 + MARGIN * 2))
    pygame.display.set_caption("A* Puzzle Solver")
    font = pygame.font.Font(None, FONT_SIZE)
    clock = pygame.time.Clock()

    board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # Wait before exit
    running = True
    while running:
        # Draw the board.
        draw_board(screen, board, font)
        for event in pygame.event.get():
            # If we close the window.
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Close the program if the escape key is pressed.
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Moving the blank tile with the arrow keys.
                elif event.key == pygame.K_UP:
                    move_blank(board, (-1, 0))
                elif event.key == pygame.K_DOWN:
                    move_blank(board, (1, 0))
                elif event.key == pygame.K_LEFT:
                    move_blank(board, (0, -1))
                elif event.key == pygame.K_RIGHT:
                    move_blank(board, (0, 1))
                # Solve the board when you press enter.
                elif event.key == pygame.K_RETURN:
                    initial = tuple(tuple(row) for row in board)
                    start = PuzzleState(initial)
                    path = astar(start)
                    state = start
                    state_list = [state]
                    # Append the states in the path to the state_list to animate later.
                    for move in path:
                        for neighbor in state.get_neighbors():
                            if neighbor.path == state.path + [move]:
                                state = neighbor
                                state_list.append(neighbor)
                                break

                    # Animate each step the A* algorithm used to solve the board.
                    for s in state_list:
                        # Update the board, so it doesn't reset at the end.
                        board = list(list(row) for row in s.board)
                        # Draw the board.
                        draw_board(screen, board, font)
                        # Pause before the next step.
                        time.sleep(WAIT_TIME)

        clock.tick(FPS)
    pygame.quit()


class PuzzleState:
    """
    Represents a single instance of a puzzle, including its board, the path so far, and the cost
    to solve the puzzle.
    """

    def __init__(self, board, path = None, cost = 0):

        self.board = board
        self.path = path if path is not None else []
        self.cost = cost
        self.heuristic = manhattan_distance(self)

    def __hash__(self):
        """Needed to be able to add the puzzle state to a dictionary."""
        return hash(self.board)

    def __eq__(self, other):
        """Needed to be able to use the equality operator (==) to compare puzzle states."""
        return self.board == other.board

    def __lt__(self, other):
        """
        Needed to be able to use the priority queue, which uses the less than operator (<) to
        compare puzzle states.
        """
        # f(n) = g(n) + h(n)
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def find_blank(self):
        """Finds the position of the blank cell (0)."""
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == 0:
                    return (r, c)

    def get_neighbors(self):
        """
        Gathers a list of all neighboring moves to the blank cell. Returns a list of new puzzle
        states that represent the board after a particular move as been made.

        Returns:
            list: A list of the puzzle states of neighboring moves to the blank cell.
            Has a maximum of four states (all four directions the blank can move to).
        """
        neighbors = []
        # Get the blank cell.
        r, c = self.find_blank()
        directions = {"UP" : (-1, 0), "DOWN" : (1, 0), "LEFT" : (0, -1), "RIGHT" : (0, 1)}
        # For each possible move, generate a new board.
        for move, (dir_r, dir_c) in directions.items():
            new_r, new_c = r + dir_r, c + dir_c
            # If the move is within the bounds of the board.
            if 0 <= new_r < len(self.board) and 0 <= new_c < len(self.board[0]):
                # Copy the original board.
                new_board = [list(row) for row in self.board]
                # Move the tile to the blank cell (swap them!).
                new_board[r][c], new_board[new_r][new_c] = new_board[new_r][new_c], new_board[r][c]
                # Turn it back into a tuple (an immutable list).
                new_board = tuple(tuple(row) for row in new_board)
                # Create a new puzzle state with this move and add it to neighbors.
                neighbors.append(PuzzleState(new_board, self.path + [move], self.cost + 1))
        return neighbors


if __name__ == "__main__":

    main()