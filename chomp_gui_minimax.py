

import sys
import pygame
import numpy as np
import test

AI_limit = 12
global game_over


def click_animation(coordinates, player):
    '''
    '''
    if coordinates != ('NULL', 'NULL'):
        if player == 'Human':
            color = RED
        else:
            color = BLUE
        pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * coordinates[1] + MARGIN, (MARGIN + HEIGHT) * coordinates[0] + MARGIN, WIDTH, HEIGHT])

        pygame.display.flip()
        pygame.time.wait(500)

def referee(coordinates, player):
    global game_over

    if coordinates == (4,4):
        if player == 'Human':
            winner = 'AI'
        else:
            winner = 'Human'

        print('Winner: ' + winner)
        game_over = True

        return winner

def draw_board(board):
    for row in range(ROW):
        for column in range(COLUMN):
            color = WHITE
            if board[row,column] == 1:
                color = GRAY
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    pygame.display.flip() #update the selected display instead of full

def draw_board0(board):
    for row in range(ROW):
        for column in range(COLUMN):
            color = WHITE
            if board[row,column] == 1:
                color = GRAY
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    color = ORANGE
    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * 0 + MARGIN, (MARGIN + HEIGHT) * 0 + MARGIN, WIDTH, HEIGHT])

    pygame.display.flip() 

def draw_board1(board):
    for row in range(ROW):
        for column in range(COLUMN):
            color = WHITE
            if board[row,column] == 1:
                color = GRAY
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Draw poisonous cookie
    color = ORANGE
    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * 0 + MARGIN, (MARGIN + HEIGHT) * (ROW-1) + MARGIN, WIDTH, HEIGHT])

    pygame.display.flip() #update the selected display instead of full

def draw_board2(board):
    for row in range(ROW):
        for column in range(COLUMN):
            color = WHITE
            if board[row,column] == 1:
                color = GRAY
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])


    color = ORANGE
    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * (COLUMN-1) + MARGIN, (MARGIN + HEIGHT) * (ROW-1) + MARGIN, WIDTH, HEIGHT])

    pygame.display.flip() 

def draw_board3(board):
    for row in range(ROW):
        for column in range(COLUMN):
            color = WHITE
            if board[row,column] == 1:
                color = GRAY
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    color = ORANGE
    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * (COLUMN-1) + MARGIN, (MARGIN + HEIGHT) * 0 + MARGIN, WIDTH, HEIGHT])

    pygame.display.flip() #update the selected display instead of full

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
def select_side():
    pygame.init()
    SCREEN_HEIGHT = 250
    SCREEN_WIDTH = 400
    WINDOW_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    left = pygame.image.load('left.png').convert_alpha()
    right = pygame.image.load('right.png').convert_alpha()
    up = pygame.image.load('up.png').convert_alpha()
    down = pygame.image.load('down.png').convert_alpha()

    left_b = Button(32, 75, left, 0.4)
    right_b = Button(135, 75, right, 0.4)
    up_b = Button(85, 25, up, 0.4)
    down_b = Button(85, 145, down, 0.4)

    up_left_down_right=[False,False,False,False]
    run = True
    while run:
        screen.fill((202, 228, 241))

        if left_b.draw(screen):
               print("left")
               up_left_down_right[1]=True
               run = False
        if right_b.draw(screen):
               print("right")
               up_left_down_right[3]=True
               run = False
        if up_b.draw(screen):
               print("up")
               up_left_down_right[0]=True
               run = False
        if down_b.draw(screen):
               print("down")
               up_left_down_right[2]=True
               run = False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               run = False
        pygame.display.flip()
    pygame.quit()
    return up_left_down_right

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 128, 0)




WIDTH = 40
HEIGHT = 40


MARGIN = 10

# ROW = 5
# COLUMN = 5


board = test.get_board()

(player_move, ROW, COLUMN)= test.player_grid_size()

print("In main gui ")
print(player_move)
print(ROW)
print(COLUMN)

pygame.init()


board_size_x = int((WIDTH + MARGIN) * COLUMN)
board_size_y = int((HEIGHT + MARGIN) * ROW)

window_size_x = int(board_size_x*1.1)
window_size_y = int(board_size_y * 1.5)

WINDOW_SIZE = [window_size_x, window_size_y]
screen = pygame.display.set_mode(WINDOW_SIZE)



clock = pygame.time.Clock()


clock.tick(60)


screen.fill(BLACK)




# # Players switches to play
# while not game_over:
#     print("In gui")
#     if player_goes == 'AI':
#         # Add some AI delay
#         #pygame.time.wait(500)
#         # AI make strategy
#         if test.check_win():
#             print("Human win")
#             game_over=True
#             break
#         (row, column) = test.ai_move()
#         test.output_board()
        

#     elif player_goes == 'Human':
#         user_clicked = False
#         if test.check_win():
#             print("AI won")
#             game_over=True
#             break
#         while not user_clicked:
#             for event in pygame.event.get():  # Human player did something
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     user_clicked = True
#                     # Human player clicks the mouse. Get the position
#                     pos = pygame.mouse.get_pos()
#                     # Change the x/y screen coordinates to grid coordinates
#                     column = pos[0] // (WIDTH + MARGIN)
#                     row = pos[1] // (HEIGHT + MARGIN)
#                     print("Click ", pos, "Grid coordinates: ", row, column)
#                     # Make sure there is still cookie
#                     # if board[row,column] == 0:
#                     #     user_clicked = True

#                     if column == 4 and row == 4:
#                         print("You selected poison block")
#                         print("You lost!")
#                         sys.exit(0)

#                     if board[column][row] != 0:
#                         print("Invalid move.... Please enter a valid move")
#                     test.change_state(row, column)
#         test.output_board()
    
#     # # Eat cookies
#     # board[:row+1,:column+1] = 1
#     board = test.get_board()

#     # Click animation
#     click_animation(coordinates = (row,column), player = player_goes)

#     # Draw the grid
#     draw_board(board)

#     # Check whether the game ends and determine the winner
#     b = test.check_win()
#     if(b):
#         if player_goes == 'AI':
#             winner = 'Human'
#             print("Human win")
#         elif player_goes == 'Human':
#             winner = 'AI'
#             print("AI win")

#     # Switch player
#     if player_goes == 'AI':
#         player_goes = 'Human'
#     elif player_goes == 'Human':
#         player_goes = 'AI'

# # Print winner information
# # Select the font to use, size, bold, italics
# font_size = int(0.1 * window_size_y)
# font = pygame.font.SysFont('Calibri', font_size, True, False)
# message = 'Winner: ' + winner
# # Measure the size of message text
# message_size = font.size(message) #(width, height)
# text = font.render(message, True, WHITE)
# text_coordinates = [int(board_size_x*0.5-message_size[0]*0.5),int(board_size_y*1.25-message_size[1]*0.5)]
# # Put the image of the text on the screen at 250x250
# screen.blit(text, text_coordinates)
# pygame.display.flip()
# pygame.time.wait(2000)

# # Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
# pygame.quit()

#main function

test.output_board()
draw_board(board)

if player_move == "Human":
    (r_,c_) = test.human_first_move()
    click_animation(coordinates = (r_,c_), player = player_move)
    pygame.quit()
    up_left_down_right = select_side()
    pygame.init()
    board_size_x = int((WIDTH + MARGIN) * COLUMN)
    board_size_y = int((HEIGHT + MARGIN) * ROW)
    window_size_x = int(board_size_x*1.1)
    window_size_y = int(board_size_y * 1.5)
    WINDOW_SIZE = [window_size_x, window_size_y]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(BLACK)
    draw_board(board)
    if(up_left_down_right[0]==True):
        test.change_state0(r_,c_)
        test.set_last_value0()
        board = test.get_board()
        draw_board0(board)
    elif(up_left_down_right[1]==True):
        test.change_state1(r_,c_)
        test.set_last_value1()
        board = test.get_board()
        draw_board1(board)
    elif(up_left_down_right[2]==True):
        test.change_state2(r_,c_)
        test.set_last_value2()
        board = test.get_board()
        draw_board2(board)
    elif(up_left_down_right[3]==True):
        test.change_state3(r_,c_)
        test.set_last_value3()
        board = test.get_board()
        draw_board3(board)
    player_move="AI"
    test.output_board()
    pygame.display.flip()
elif player_move == "AI":
    pygame.quit()
    up_left_down_right = select_side()
    pygame.init()
    board_size_x = int((WIDTH + MARGIN) * COLUMN)
    board_size_y = int((HEIGHT + MARGIN) * ROW)
    window_size_x = int(board_size_x*1.1)
    window_size_y = int(board_size_y * 1.5)
    WINDOW_SIZE = [window_size_x, window_size_y]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(BLACK)
    draw_board(board)
    if(up_left_down_right[0]==True):
        (r__,c__) =test.ai_move0()
        click_animation(coordinates = (r__,c__), player = player_move)
        test.set_last_value0()
        test.output_board()
        draw_board0(board)
    elif(up_left_down_right[1]==True):
        (r__,c__) =test.ai_move1()
        click_animation(coordinates = (r__,c__), player = player_move)
        test.set_last_value1()
        test.output_board()
        draw_board1(board)
    elif(up_left_down_right[2]==True):
        (r__,c__) =test.ai_move2()
        click_animation(coordinates = (r__,c__), player = player_move)
        test.set_last_value2()
        test.output_board()
        draw_board2(board)
    elif(up_left_down_right[3]==True):
        (r__,c__) =test.ai_move3()
        click_animation(coordinates = (r__,c__), player = player_move)
        test.set_last_value3()
        test.output_board()
        draw_board3(board)
    player_move = "Human"



game_over = False

winner = ''

# def switch(up_left_down_right):
#     if up_left_down_right[0] == True:
#         up_left_down_right[1]=False
#         up_left_down_right[2]=False
#         up_left_down_right[3]=False
#     elif up_left_down_right[1] == True:
#         up_left_down_right[0]=False
#         up_left_down_right[2]=False
#         up_left_down_right[3]=False
#     elif up_left_down_right[2]==True:
#         up_left_down_right[0]=False
#         up_left_down_right[1]=False
#         up_left_down_right[3]=False
#     elif up_left_down_right[3]==True:
#         up_left_down_right[0]=False
#         up_left_down_right[1]=False
#         up_left_down_right[2]=False
#     else:
#         raise Exception("Improper value of Up left down right")
    

while(up_left_down_right[0]==True):
    while not game_over:
        r,c=(0,0)
        if player_move=="Human":
            if test.check_win0():
                print("AI won")
                winner = "AI"
                game_over = True
                up_left_down_right[0]=False
                font_size = int(0.1 * window_size_y)
                font = pygame.font.SysFont('Calibri', font_size, True, False)
                message = 'Winner: ' + winner

                message_size = font.size(message) #(width, height)
                text = font.render(message, True, WHITE)
                text_coordinates = [int(board_size_x*0.5-message_size[0]*0.5),int(board_size_y*1.25-message_size[1]*0.5)]
                screen.blit(text, text_coordinates)
                pygame.display.flip()
                pygame.time.wait(2000)
                pygame.quit()
                break
        
            (r,c) =test.player(0)
            click_animation(coordinates = (r,c), player = player_move)
            player_move="AI"
            test.output_board()

        else:
            if test.check_win0():
                print("Congratulations, you won")
                game_over = True
                up_left_down_right[0]=False
                winner = "Human"
                break

            (r,c) =test.ai_move0()
            player_move="Human"
            test.output_board()
            click_animation(coordinates = (r,c), player = player_move)
            draw_board0(board)
            pygame.display.flip()

while(up_left_down_right[1]==True):
    while not game_over:
        r,c=(0,0)
        if player_move=="Human":
            if test.check_win1():
                print("AI won")
                winner = "AI"
                game_over = True
                up_left_down_right[1]=False
                break
        
            (r,c) =test.player(1)
            player_move="AI"
            test.output_board()

        else:
            if test.check_win1():
                print("Congratulations, you won")
                game_over = True
                up_left_down_right[1]=False
                winner = "Human"
                break

            (r,c) =test.ai_move1()
            player_move="Human"
            test.output_board()
        click_animation(coordinates = (r,c), player = player_move)
        board = test.get_board()
        draw_board1(board)
        pygame.display.flip()

while(up_left_down_right[2]==True):
    while not game_over:
        r,c=(0,0)
        if player_move=="Human":
            if test.check_win2():
                print("AI won")
                winner = "AI"
                game_over = True
                up_left_down_right[2]=False
                break
        
            (r,c) =test.player(2)
            player_move="AI"
            test.output_board()

        else:
            if test.check_win2():
                print("Congratulations, you won")
                game_over = True
                up_left_down_right[2]=False
                winner = "Human"
                break

            (r,c) =test.ai_move2()
            player_move="Human"
            test.output_board()
        click_animation(coordinates = (r,c), player = player_move)
        board = test.get_board()
        draw_board2(board)
        pygame.display.flip()

while(up_left_down_right[3]==True):
    while not game_over:
        r,c=(0,0)
        if player_move=="Human":
            if test.check_win3():
                print("AI won")
                winner = "AI"
                game_over = True
                up_left_down_right[3]=False
                break
        
            (r,c) =test.player(3)
            player_move="AI"
            test.output_board()

        else:
            if test.check_win3():
                print("Congratulations, you won")
                game_over = True
                up_left_down_right[3]=False
                winner = "Human"
                break

            (r,c) =test.ai_move3()
            player_move="Human"
            test.output_board()
        click_animation(coordinates = (r,c), player = player_move)
        board = test.get_board()
        draw_board3(board)
        pygame.display.flip()


font_size = int(0.1 * window_size_y)
font = pygame.font.SysFont('Calibri', font_size, True, False)
message = 'Winner: ' + winner

message_size = font.size(message) #(width, height)
text = font.render(message, True, WHITE)
text_coordinates = [int(board_size_x*0.5-message_size[0]*0.5),int(board_size_y*1.25-message_size[1]*0.5)]
screen.blit(text, text_coordinates)
pygame.display.flip()
pygame.time.wait(2000)

pygame.quit()

