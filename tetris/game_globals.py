# Blocks - Shapes
shapes = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[4, 5, 9, 10], [2, 6, 5, 9]],
    [[6, 7, 9, 10], [1, 5, 6, 10]],
    [[2, 1, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
    # [[1, 6, 10, 11]]
]

# Blocks - Colors
shapeColors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (205, 200, 0), (255, 165, 0), (0, 0, 205), (128, 0, 128)]

# Game - Screen settings
screen_width = 700
screen_height = 600
gameWidth = 100  # meaning 300 // 10 = 30 width per block
gameHeight = 400  # meaning 600 // 20 = 20 height per block
topLeft_x = (screen_width - gameWidth) // 2
topLeft_y = screen_height - gameHeight - 50
