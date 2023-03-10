import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris Game")

# Setting up the game board
BLOCK_SIZE = 20
BOARD_WIDTH = WINDOW_WIDTH // BLOCK_SIZE
BOARD_HEIGHT = WINDOW_HEIGHT // BLOCK_SIZE
game_board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

def check_collision(piece, board):
    for y in range(len(piece.shape)):
        for x in range(len(piece.shape[0])):
            if piece.shape[y][x] == 1:
                if piece.y + y >= len(board):
                    return True
                if piece.x + x < 0 or piece.x + x >= len(board[0]):
                    return True
                if piece.y + y < 0:
                    return True
                if board[piece.y + y][piece.x + x] != 0:
                    return True
    return False

def add_to_board(piece, board):
    for y in range(len(piece.shape)):
        for x in range(len(piece.shape[0])):
            if piece.shape[y][x] == 1 and piece.y + y >= 0:
                board[piece.y + y][piece.x + x] = piece.color

def clear_lines(board):
    num_lines_cleared = 0
    for y in range(len(board)):
        if 0 not in board[y]:
            num_lines_cleared += 1
            del board[y]
            board.insert(0, [0] * len(board[0]))
    return num_lines_cleared

def draw_piece(piece):
    for y in range(len(piece.shape)):
        for x in range(len(piece.shape[0])):
            if piece.shape[y][x] == 1:
                pygame.draw.rect(game_window, piece.color, ((piece.x + x) * BLOCK_SIZE, (piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_board(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            color = board[y][x]
            pygame.draw.rect(game_window, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def check_game_over(board):
    # Check if the board is completely filled with pieces
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return False
    return True

class Piece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = BOARD_WIDTH // 2
        self.y = 0

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def rotate(self):
        # Transpose the shape
        self.shape = [[self.shape[j][i] for j in range(len(self.shape))] for i in range(len(self.shape[0]))]
        # Reverse the rows to get the rotation effect
        self.shape = [row[::-1] for row in self.shape]

def generate_piece():
    shapes = [
        [[1, 1], [1, 1]],  # Square
        [[0, 1, 0], [1, 1, 1]],  # L-shaped
        [[0, 1, 1], [1, 1, 0]],  # Reverse L-shaped
        [[1, 1, 1, 1]],  # Line
        [[0, 1, 1], [1, 1, 0]],  # S-shaped
        [[1, 1, 0], [0, 1, 1]],  # Z-shaped
        [[1, 0, 0], [1, 1, 1]]  # T-shaped
    ]
    colors = [
        (255, 255, 0),  # Yellow
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
        (255, 128, 0)  # Orange
    ]
    shape = random.choice(shapes)
    color = random.choice(colors)
    return Piece(shape, color)

def update_score(num_lines_cleared):
    if num_lines_cleared == 1:
        return 10
    elif num_lines_cleared == 2:
        return 30
    elif num_lines_cleared == 3:
        return 60
    elif num_lines_cleared == 4:
        return 100
    else:
        return 0

#Main game loop
game_running = True
clock = pygame.time.Clock()
score = 0

# Generate the first piece
current_piece = generate_piece()

while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_piece.move_left()
                if check_collision(current_piece, game_board):
                    current_piece.move_right()
            if event.key == pygame.K_RIGHT:
                current_piece.move_right()
                if check_collision(current_piece, game_board):
                    current_piece.move_left()
            if event.key == pygame.K_DOWN:
                current_piece.move_down()
                if check_collision(current_piece, game_board):
                    current_piece.move_up()
            if event.key == pygame.K_SPACE:
                current_piece.rotate()
                if check_collision(current_piece, game_board):
                    current_piece.rotate()

    # Move the current piece down
    current_piece.move_down()

    # Check for collision
    if check_collision(current_piece, game_board):
        # Move the current piece up
        current_piece.move_up()

        # Add the piece to the game board
        add_to_board(current_piece, game_board)

        # Generate a new piece
        current_piece = generate_piece()

        # Clear lines and update the score
        num_lines_cleared = clear_lines(game_board)
        score += update_score(num_lines_cleared)

    # Draw the game board and the current piece
    draw_board(game_board)
    draw_piece(current_piece)

    pygame.display.update()

    # Limit the frame rate
    clock.tick(10)

    # Check for game over

    if check_game_over(game_board):
        print("Game over! Your score was:", score)
        pygame.time.delay(3000) # Pause for 1 second
        game_running = False



# Clean up
pygame.quit()
