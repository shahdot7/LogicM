import pygame
import board
import heapq
pygame.init()


# الألوان
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

class Node:
    def __init__(self, positions ,g,h):
        self.position = positions
        self.g = g
        self.h = h
        self.f = g+h
        self.parent = None
    def __lt__(self,other):
        return self.f< other.f    
        

def heuristic(postion, goal):
    return abs (postion[0] - goal[0])+ abs (position[1]- goal[1])
# إنشاء مصفوفة ثنائية الأبعاد للرقع
tiles = []
for row in range(n):
    tile_row = []
    for col in range(n):
        tile_row.append({
            'rect': pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size),
            'state': 'empty',
            'piece': None
        })
    tiles.append(tile_row)

class Piece:
    def __init__(self, x, y, piece_type):
        self.x = x
        self.y = y
        self.piece_type = piece_type
        self.color = GRAY if piece_type == "iron" else PURPLE if piece_type == "repel" else RED
        tiles[y][x]['state'] = piece_type
        tiles[y][x]['piece'] = self

    def draw(self):
        pygame.draw.circle(screen, self.color, 
                         (self.x * cell_size + cell_size // 2, 
                          self.y * cell_size + cell_size // 2), 
                         cell_size // 3)

def draw_board():
    screen.fill(WHITE)
    for row in tiles:
        for tile in row:
            pygame.draw.rect(screen, (200, 200, 200), tile['rect'], 1)

def add_new_piece(row, col, piece_type):
    if tiles[row][col]['state'] == 'empty':
        new_piece = Piece(col, row, piece_type)
        pieces.append(new_piece)
        return True
    return False

# تعريف المراحل
levels = {
    1: [
        {"row": 1, "col": 1, "type": "iron"}
    ],
    2: [
        {"row": 1, "col": 1, "type": "iron"},
        {"row": 3, "col": 3, "type": "repel"},
        {"row": 5, "col": 1, "type": "attract"}
    ],
    3: [
        {"row": 0, "col": 0, "type": "iron"},
        {"row": 2, "col": 2, "type": "repel"},
        {"row": 4, "col": 4, "type": "attract"},
        {"row": 6, "col": 6, "type": "iron"}
    ]
}

# تحديد المستوى الحالي
current_level = 1
pieces = []

def load_level(level_number):
    global pieces
    pieces = []
    # مسح جميع الرقع الحالية
    for row in range(n):
        for col in range(n):
            tiles[row][col]['state'] = 'empty'
            tiles[row][col]['piece'] = None
    
    # إضافة القطع الجديدة للمستوى
    for piece_data in levels[level_number]:
        add_new_piece(piece_data["row"], piece_data["col"], piece_data["type"])

# تحميل المستوى الأول مباشرة
load_level(1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col = mouse_x // cell_size
            row = mouse_y // cell_size
            if 0 <= row < n and 0 <= col < n:
                print(f"Clicked tile: {row}, {col}, State: {tiles[row][col]['state']}")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                load_level(1)
            elif event.key == pygame.K_2:
                load_level(2)
            elif event.key == pygame.K_3:
                load_level(3)

    board.draw_board()
    for piece in pieces:
        piece.draw()

    pygame.display.flip()

pygame.quit()
