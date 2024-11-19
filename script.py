import pygame
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ROW, COLS = len(board), len(board[0])

        def countneigh(r, c):
            neigh = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or (i < 0 or j < 0) or i >= ROW or j >= COLS:
                        continue
                    if board[i][j] in [1, 3]:
                        neigh += 1
            return neigh

        for i in range(ROW):
            for j in range(COLS):
                neigh = countneigh(i, j)
                if board[i][j] == 1 and (neigh in [2, 3]):
                    board[i][j] = 3
                elif board[i][j] == 1 and (neigh < 2 or neigh > 3):
                    board[i][j] = 0  # Dead
                elif board[i][j] == 0 and neigh == 3:
                    board[i][j] = 2  # Birth

        for i in range(ROW):
            for j in range(COLS):
                if board[i][j] in [2, 3]:
                    board[i][j] = 1  # Alive
                elif board[i][j] == 1:
                    board[i][j] = 0  # Dead

    def draw_board(self, screen, cell_size, board: List[List[int]]):
        for i in range(len(board)):
            for j in range(len(board[0])):
                color = (255, 255, 255) if board[i][j] == 1 else (0, 0, 0)
                pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

# Pygame setup
pygame.init()
width, height = 600, 600
rows, cols = 50, 50
cell_size = width // cols

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

# Initialize the board
board = [
 [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
 [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
 [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
 [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
 [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1],
 [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
 [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
 [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
 [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
 [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
 [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
 [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
 [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
 [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
 [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
 [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
 [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
 [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
 [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
 [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
 [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
 ]


# Create Solution object and start the game loop
game = Solution()

running = True
while running:
    screen.fill((0, 0, 0))  # Black background
    game.draw_board(screen, cell_size, board)
    game.gameOfLife(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(10)  # Update the board at 10 frames per second

pygame.quit()
