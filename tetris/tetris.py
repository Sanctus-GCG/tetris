# inspiration from https://data-flair.training/blogs/python-tetris-game-pygame/
import pygame
import random
from dataclasses import dataclass

import game_globals as gl


@dataclass
class Block:
    x: int = 0
    y: int = 0
    n: int = 0

    def __post_init__(self):
        self.type: int = self.n
        self.color: int = self.n
        self.rotation: int = 0

    def image(self) -> list:
        return gl.shapes[self.type][self.rotation]

    def rotate(self) -> int:
        self.rotation = (self.rotation + 1) % len(gl.shapes[self.type])
        return self.rotation


@dataclass()
class Tetris:
    height: int = 0
    width: int = 0

    def __post_init__(self):
        self.level: int = 2
        self.score: int = 0
        self.state: str = "start"
        self.board: list = []
        self.zoom: int = 20
        self.x: int = 100
        self.y: int = 60
        self.block = None
        self.nextBlock = None

        for i in range(gl.screen_height):
            new_line = []
            for j in range(gl.screen_width):
                new_line.append(0)
            self.board.append(new_line)

    # Create new block
    def new_block(self) -> Block:
        self.block = Block(3, 0, random.randint(0, len(gl.shapes) - 1))
        return self.block

    def next_block(self):
        self.nextBlock = Block(4, 0, random.randint(0, len(gl.shapes) - 1))
        return self.nextBlock

    # Checks position of block
    def intersects(self) -> bool:
        intersection: bool = False

        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    if i + self.block.y > self.height - 1\
                            or j + self.block.x > self.width - 1\
                            or j + self.block.x < 0\
                            or self.board[i + self.block.y][j + self.block.x] > 0:
                        intersection = True

        return intersection

    # Checks if a row is formed and destroys that line
    def break_lines(self) -> int:
        lines: int = 0

        for i in range(1, self.height):
            zeros: int = 0
            for j in range(self.width):
                if self.board[i][j] == 0:
                    zeros += 1

            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.board[i1][j] = self.board[i1 - 1][j]

        self.score += lines ** 2

        return self.score

    def draw_next_block(self, screen) -> None:
        font = pygame.font.SysFont("Calibri", 30)
        label = font.render("Next Shape", 1, (128, 128, 128))

        sx: float = gl.topLeft_x + gl.gameWidth + 50
        sy: float = gl.topLeft_y + gl.gameHeight / 2 - 100
        format = self.nextBlock.image()
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.nextBlock.image():
                    pygame.draw.rect(screen, gl.shapeColors[self.nextBlock.color], (sx + j * 30, sy + i * 30, 30, 30), 0)

    # Moves the block to the bottom
    def moveBottom(self) -> None:
        while not self.intersects():
            self.block.y += 1
        self.block.y -= 1
        self.freeze()

    # Moves the block down by a unit
    def moveDown(self) -> None:
        self.block.y += 1
        if self.intersects():
            self.block.y -= 1
            self.freeze()

    # runs once the block reaches the bottom.
    def freeze(self) -> None:
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    self.board[i + self.block.y][j + self.block.x] = self.block.color
        self.break_lines()  # Checking if any row is formed
        self.block = self.nextBlock
        self.next_block()  # Creating a new block
        if self.intersects():  # If blocks touch the top of the board, then ending the game by setting status as gameover
            self.state = "gameover"

    # Moves the block horizontally
    def moveHoriz(self, dx: int) -> None:
        old_x = self.block.x
        self.block.x += dx
        if self.intersects():
            self.block.x = old_x

    # Rotates the block
    def rotate(self) -> None:
        old_rotation = self.block.rotation
        self.block.rotate()
        if self.intersects():
            self.block.rotation = old_rotation

    # Moves the block down by a unit
    def go_down(self) -> None:
        self.block.y += 1
        if self.intersects():
            self.block.y -= 1
            self.freeze()

    # Moves the block to the bottom of grid
    def go_space(self) -> None:
        while not self.intersects():
            self.block.y += 1
        self.block.y -= 1
        self.freeze()

