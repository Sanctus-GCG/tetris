import pygame
import tetris as tet
import game_globals as gl


screen = pygame.display.set_mode((gl.screen_width, gl.screen_height))
pygame.display.set_caption("Awesome Tetris Game")
pygame.font.init()


def start_game():
    game: tet = tet.Tetris(20, 10)

    done: bool = False
    clock = pygame.time.Clock()
    fps: int = 25
    counter: int = 0
    pressing_down: bool = False

    while not done:
        # Create a new block if there is no moving block
        if game.block is None:
            game.new_block()
        if game.nextBlock is None:
            game.next_block()
        counter += 1  # Keeping track of the time
        if counter > 100000:
            counter = 0

        # Moving the block continuously with time or when down key is pressed
        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()
        # Checking which key is pressed and running corresponding function
        for event in pygame.event.get():
            # match event.type:
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        game.rotate()
                    case pygame.K_DOWN:
                        game.moveDown()
                    case pygame.K_LEFT:
                        game.moveHoriz(-1)
                    case pygame.K_RIGHT:
                        game.moveHoriz(1)
                    case pygame.K_SPACE:
                        game.moveBottom()
                    # case pygame.K_ESCAPE:
                    #     game = game(20, 10)
        screen.fill('#FFFFFF')

        # Updating the game board regularly
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, '#B2BEB5',
                                 [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.board[i][j] > 0:
                    pygame.draw.rect(screen, gl.shapeColors[game.board[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2,
                                      game.zoom - 1])

        # Updating the board with the moving block
        if game.block is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.block.image():
                        pygame.draw.rect(screen, gl.shapeColors[game.block.color],
                                         [game.x + game.zoom * (j + game.block.x) + 1,
                                          game.y + game.zoom * (i + game.block.y) + 1,
                                          game.zoom - 2, game.zoom - 2])

        # track the score
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render("Score: " + str(game.score), True, '#000000')
        text_game_over = font.render("Game Over", True, '#000000')
        text_game_over1 = font.render("Press ESC", True, '#000000')

        # Ending the game if state is gameover
        screen.blit(text, [300, 0])
        if game.state == "gameover":
            screen.blit(text_game_over, [300, 200])
            screen.blit(text_game_over1, [300, 265])

        game.draw_next_block(screen)

        pygame.display.flip()
        clock.tick(fps)


def main():
    run = True
    while run:
        screen.fill((16, 37, 54))
        font = pygame.font.SysFont("Calibri", 65, bold=True)
        label = font.render("Press any key to start!", True, '#FFFFFF')

        screen.blit(label, (10, 300))
        pygame.display.update()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    run = False
                case pygame.KEYDOWN:
                    start_game()
    pygame.quit()


if __name__ == '__main__':
    main()
