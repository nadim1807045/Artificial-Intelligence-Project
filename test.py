import numpy as np
import pygame
import sys




global row
global column
board = np.array([[0]*10]*10)


class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

def player_grid_size():
    global row
    global column
    pygame.init()

    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 1200
    WINDOW_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
    pygame.display.set_caption("Chomp Game")

    human_img = pygame.image.load('human-icon.png').convert_alpha()
    ai_img = pygame.image.load('ai-icon.png').convert_alpha()

#create button instances
    human_button = Button(225, 111, human_img, 0.4)
    ai_button = Button(620, 111, ai_img, 0.4)

    select_bord_size = pygame.image.load('grid_size.png').convert_alpha()
    bord_size_button = Button(255, 75, select_bord_size, 0.5)

    num_3 = pygame.image.load('3.png').convert_alpha()
    num_3_button = Button(250, 180, num_3, 1)

    num_4 = pygame.image.load('4.png').convert_alpha()
    num_4_button = Button(350, 180, num_4, 1)

    num_5 = pygame.image.load('5.png').convert_alpha()
    num_5_button = Button(450, 180, num_5, 1)

    num_6 = pygame.image.load('6.png').convert_alpha()
    num_6_button = Button(550, 180, num_6, 1)

    num_7 = pygame.image.load('7.png').convert_alpha()
    num_7_button = Button(650, 180, num_7, 1)

    num_32 = pygame.image.load('3.png').convert_alpha()
    num_32_button = Button(250, 340, num_3, 1)

    num_42 = pygame.image.load('4.png').convert_alpha()
    num_42_button = Button(350, 340, num_4, 1)

    num_52 = pygame.image.load('5.png').convert_alpha()
    num_52_button = Button(450, 340, num_5, 1)

    num_62 = pygame.image.load('6.png').convert_alpha()
    num_62_button = Button(550, 340, num_6, 1)

    num_72 = pygame.image.load('7.png').convert_alpha()
    num_72_button = Button(650, 340, num_7, 1)



    player_first=''
    grid_size_x = 0
    grid_size_y = 0

    #game loop
    run = True
    while run:
        screen.fill((202, 228, 241))

        if human_button.draw(screen):
               print("HUMAN")
               player_first="Human"
               run = False
        if ai_button.draw(screen):
               print("AI")
               player_first = "AI"
               run = False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               run = False
        #   if human_button.draw(screen):
        #        print("HUMAN")
        #        player_first="Human"
        #        run = False
        #   if ai_button.draw(screen):
        #        print("AI")
        #        player_first = "AI"
        #        run = False
        pygame.display.update()


    run = True
    while run:
        screen.fill((202, 228, 241))

        if bord_size_button.draw(screen):
               pass
        if num_3_button.draw(screen):
               grid_size_x=3
               print("--3--")
               run = False
        if num_4_button.draw(screen):
               grid_size_x=4
               print("--4--")
               run = False
        if num_5_button.draw(screen):
               grid_size_x=5
               print("--5--")
               run = False
        if num_6_button.draw(screen):
               grid_size_x=6
               print("--6--")
               run = False
        if num_7_button.draw(screen):
               grid_size_x=7
               print("--7--")
               run = False

        for event in pygame.event.get():
          if event.type==pygame.QUIT:
               run = False
    
        pygame.display.update()

    run = True
    while run:
        screen.fill((202, 228, 241))

        if bord_size_button.draw(screen):
               pass
        if num_32_button.draw(screen):
               grid_size_y=3
               print("--3-2-")
               run = False
        if num_42_button.draw(screen):
               grid_size_y=4
               print("--42--")
               run = False
        if num_52_button.draw(screen):
               grid_size_y=5
               print("--5-2-")
               run = False
        if num_62_button.draw(screen):
               grid_size_y=6
               print("--6-2-")
               run = False
        if num_72_button.draw(screen):
               grid_size_y=7
               print("--7-2-")
               run = False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               run = False
    
        pygame.display.update()

	# screen.fill((202, 228, 241))
    pygame.quit()
    row = grid_size_x
    column = grid_size_y
    return (player_first, grid_size_x, grid_size_y)





def get_board():
    return board
def set_last_value():
    board[row-1][column-1] = 5
def set_last_value0():
    board[0][0] = 5
def set_last_value1():
    board[row-1][0] = 5
def set_last_value2():
    board[row-1][column-1] = 5
def set_last_value3():
    board[0][column-1] = 5

def output_board():

    for i in board:
        for j in i:
            print(j, end=" ")
        print()

def check_win():
    if board[row-2][column-1] == 0 or board[row-1][column-2] == 0:
        return False
    return True

def check_win0():
    if board[0][1] == 0 or board[1][0] == 0:
        return False
    return True

def check_win1():
    if board[row-2][0] == 0 or board[row-1][1] == 0:
        return False
    return True

def check_win2():
    if board[row-2][column-1] == 0 or board[row-1][column-2] == 0:
        return False
    return True

def check_win3():
    if board[0][column-2] == 0 or board[1][column-1] == 0:
        return False
    return True

def change_state(m, n):
    for i in range(m+1):
        for j in range(n+1):
            board[i][j] = 1
def change_state0(m, n):
    for i in range(m,row):
        for j in range(n,column):
            board[i][j] = 1
def change_state1(m, n):
    for i in range(m+1):
        for j in range(n,column):
            board[i][j] = 1
def change_state2(m, n):
    for i in range(m+1):
        for j in range(n+1):
            board[i][j] = 1
def change_state3(m, n):
    for i in range(m,row):
        for j in range(n+1):
            board[i][j] = 1

def revert(b):
    for i, j in enumerate(b):
        board[i] = j

def minimax(is_max, alpha, beta, steps):
    steps += 1
    if check_win():
        # print("Steps ",steps)
        if is_max:
            return -1000 + steps
        else:
            return 1000 - steps

    b = board.copy()
    if is_max:
        best_score = -1000000
        for i in range(5):
            for j in range(5):
                if (i!=4 or j!=4) and board[i][j] ==0:
                    change_state(i, j)
                    best_score = max(best_score, minimax(False, alpha, beta, steps))
                    alpha = max(alpha, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

    else:
        best_score = 1000000
        for i in range(5):
            for j in range(5):
                if (i!=4 or j!=4) and board[i][j] ==0:
                    change_state(i, j)
                    best_score = min(best_score, minimax(True, alpha, beta, steps))
                    beta = min(beta, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score
    
def minimax0(is_max, alpha, beta, steps):
    steps += 1
    if check_win0():
        # print("Steps ",steps)
        if is_max:
            return -1000 + steps
        else:
            return 1000 - steps

    b = board.copy()
    if is_max:
        best_score = -1000000
        for i in range(row):
            for j in range(column):
                if (i!=0 or j!=0) and board[i][j] ==0:
                    change_state0(i, j)
                    best_score = max(best_score, minimax0(False, alpha, beta, steps))
                    alpha = max(alpha, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

    else:
        best_score = 1000000
        for i in range(row):
            for j in range(column):
                if (i!=0 or j!=0) and board[i][j] ==0:
                    change_state0(i, j)
                    best_score = min(best_score, minimax0(True, alpha, beta, steps))
                    beta = min(beta, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score
def minimax1(is_max, alpha, beta, steps):
    steps += 1
    if check_win1():
        # print("Steps ",steps)
        if is_max:
            return -1000 + steps
        else:
            return 1000 - steps

    b = board.copy()
    if is_max:
        best_score = -1000000
        for i in range(row):
            for j in range(column):
                if (i!=(row-1) or j!=0) and board[i][j] ==0:
                    change_state1(i, j)
                    best_score = max(best_score, minimax1(False, alpha, beta, steps))
                    alpha = max(alpha, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

    else:
        best_score = 1000000
        for i in range(row):
            for j in range(column):
                if (i!=(row-1) or j!=0) and board[i][j] ==0:
                    change_state1(i, j)
                    best_score = min(best_score, minimax1(True, alpha, beta, steps))
                    beta = min(beta, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

def minimax2(is_max, alpha, beta, steps):
    steps += 1
    if check_win2():
        # print("Steps ",steps)
        if is_max:
            return -1000 + steps
        else:
            return 1000 - steps

    b = board.copy()
    if is_max:
        best_score = -1000000
        for i in range(row):
            for j in range(column):
                if (i!=(row-1) or j!=(column-1)) and board[i][j] ==0:
                    change_state2(i, j)
                    best_score = max(best_score, minimax2(False, alpha, beta, steps))
                    alpha = max(alpha, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

    else:
        best_score = 1000000
        for i in range(row):
            for j in range(column):
                if (i!=(row-1) or j!=(column-1)) and board[i][j] ==0:
                    change_state2(i, j)
                    best_score = min(best_score, minimax2(True, alpha, beta, steps))
                    beta = min(beta, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

def minimax3(is_max, alpha, beta, steps):
    steps += 1
    if check_win3():
        # print("Steps ",steps)
        if is_max:
            return -1000 + steps
        else:
            return 1000 - steps

    b = board.copy()
    if is_max:
        best_score = -1000000
        for i in range(row):
            for j in range(column):
                if (i!=0 or j!=(column-1)) and board[i][j] ==0:
                    change_state3(i, j)
                    best_score = max(best_score, minimax3(False, alpha, beta, steps))
                    alpha = max(alpha, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

    else:
        best_score = 1000000
        for i in range(row):
            for j in range(column):
                if (i!=0 or j!=(column-1)) and board[i][j] ==0:
                    change_state3(i, j)
                    best_score = min(best_score, minimax3(True, alpha, beta, steps))
                    beta = min(beta, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

def ai_move():
    print("AI turn")
    bi = 0
    bj = 0
    b = board.copy()
    
    best_score = 1000000
    for i in range(row):
        for j in range(column):
            if (i!=(row-1) or j!=(column-1)) and board[i][j] ==0:
                change_state(i, j)
                s = minimax(True, -1000000, 1000000, 0)
                if best_score > s:
                    best_score = s
                    bi = i
                    bj = j
                revert(b)

    change_state(bi, bj)
    print(f"AI chose {bi+1} row, {bj+1} column")
    return (bi,bj)

def ai_move0():
    print("AI turn")
    bi = 0
    bj = 0
    b = board.copy()
    
    best_score = 1000000
    for i in range(row):
        for j in range(column):
            if (i!=0 or j!=0) and board[i][j] ==0:
                change_state0(i, j)
                s = minimax0(True, -1000000, 1000000, 0)
                if best_score > s:
                    best_score = s
                    bi = i
                    bj = j
                revert(b)

    change_state0(bi, bj)
    print(f"AI chose {bi+1} row, {bj+1} column")
    return (bi,bj)

def ai_move1():
    print("AI turn")
    bi = 0
    bj = 0
    b = board.copy()
    
    best_score = 1000000
    for i in range(row):
        for j in range(column):
            if (i!=(row-1) or j!=0) and board[i][j] ==0:
                change_state1(i, j)
                s = minimax1(True, -1000000, 1000000, 0)
                if best_score > s:
                    best_score = s
                    bi = i
                    bj = j
                revert(b)

    change_state1(bi, bj)
    print(f"AI chose {bi+1} row, {bj+1} column")
    return (bi,bj)

def ai_move2():
    print("AI turn")
    bi = 0
    bj = 0
    b = board.copy()
    
    best_score = 1000000
    for i in range(row):
        for j in range(column):
            if (i!=(row-1) or j!=(column-1)) and board[i][j] ==0:
                change_state2(i, j)
                s = minimax2(True, -1000000, 1000000, 0)
                if best_score > s:
                    best_score = s
                    bi = i
                    bj = j
                revert(b)

    change_state2(bi, bj)
    print(f"AI chose {bi+1} row, {bj+1} column")
    return (bi,bj)

def ai_move3():
    print("AI turn")
    bi = 0
    bj = 0
    b = board.copy()
    
    best_score = 1000000
    for i in range(row):
        for j in range(column):
            if (i!=0 or j!=(column-1)) and board[i][j] ==0:
                change_state3(i, j)
                s = minimax3(True, -1000000, 1000000, 0)
                if best_score > s:
                    best_score = s
                    bi = i
                    bj = j
                revert(b)

    change_state3(bi, bj)
    print(f"AI chose {bi+1} row, {bj+1} column")
    return (bi,bj)


def player(up_left_down_right):
    print("Your turn")

    user_clicked = False
    while not user_clicked:
        for event in pygame.event.get():  # Human player did something
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_clicked = True
                # Human player clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (40 + 10) #width = 20, margin = 5, height = 20
                row = pos[1] // (40 + 10)
                print("Click ", pos, "Grid coordinates: ", row, column)
                # Make sure there is still cookie
                if board[row,column] == 0:
                    user_clicked = True

                if column == 4 and row == 4:
                    print("You selected poison block")
                    print("You lost!")
                    return

                if board[column][row] != 0:
                    print("Invalid move.... Please enter a valid move")
        pygame.display.flip()
    if(up_left_down_right==0):
        change_state0(row, column)
    elif(up_left_down_right==1):
        change_state1(row, column)
    elif(up_left_down_right==2):
        change_state2(row, column)
    elif(up_left_down_right==3):
        change_state3(row, column)
    return (row, column)



def human_first_move():
    print("Your turn")

    user_clicked = False
    while not user_clicked:
        for event in pygame.event.get():  # Human player did something
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_clicked = True
                # Human player clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (40 + 10) #width = 20, margin = 5, height = 20
                row = pos[1] // (40 + 10)
                print("Click ", pos, "Grid coordinates: ", row, column)
                # Make sure there is still cookie
                if board[row,column] == 0:
                    user_clicked = True

                if column == 4 and row == 4:
                    print("You selected poison block")
                    print("You lost!")
                    return

                if board[column][row] != 0:
                    print("Invalid move.... Please enter a valid move")
    return (row, column)




#main function
    
# a = 0
# set_last_value()
# output_board()

# player_move="Human"

# while True:
#     if a%2==0:
#         if check_win():
#             print("AI won")
#             sys.exit(0)
        
#         player()
#         a += 1
#         output_board()

#     else:
#         if check_win():
#             print("Congratulations, you won")
#             sys.exit(0)

#         ai_move()
#         a += 1
#         output_board()


