
# run_tic_tac_toe.py

import pygame
import sys
from laura_tic_tac_toe import *
from ai import *
# import time

pygame.init()

print("\nWelcome to Laura\'s Tic-Tac-Toe!\n")

while True:
    
    window = open_window() # open window
    create_board(window) # create board
    state = ["0", "1", "2", "3", "4", "5", "6", "7", "8"] # initialize board state
    terminal_state = False # initialize terminal state

    ai = choose_ai() # choose ai: random, minimax, full alpha-beta
    
    # look for pygame events until terminal state occurs
    while not terminal_state:
        
        for event in pygame.event.get():
            
            # if quit event
            if event.type == pygame.QUIT: 
                 sys.exit(0) # close window     
                 
            # if mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN: 
                
                # human player goes
                player = "X"

                pos = pygame.mouse.get_pos() # get mouse click position
                region = map_to_grid(pos)  # map mouse click position to board region 0 - 8
                empty_regions = find_empty_regions(state) # find empty regions
                                
                # if clicked region is empty  
                if str(region) in empty_regions:
                    place_on_grid(window, region, player) # place marker on window
                    state[region] = player # update board state
                    empty_regions = find_empty_regions(state) # find empty regions
                    game_over = terminal_test(state, player) # check for terminal state
                    # if terminal state is found
                    if game_over:
                        pygame.event.get()
                        terminal_state = play_again()
                        
                    # ai player goes
                    player = "O"
                    # if there are empty regions remaining
                    if len(empty_regions) != 0:

                        # start = time.clock()

                        # randomly place ai
                        if ai == 1:
                            ai_region = random_ai(empty_regions) # call ai() to find best position

                        # minimax to place ai
                        if ai == 2:
                            my_state = state[:] # create copy of state list for scope
                            best = minimax(my_state, player)
                            ai_region = int(best[0])

                        # alphabeta to place ai
                        if ai == 3:
                            my_state = state[:] # create copy of state list for scope
                            best = alphabeta(my_state, -float("inf"), float("inf"), player)
                            ai_region = int(best[0])

                        if ai == 4:
                            my_state = state[:]  # create copy of state list for scope
                            best = alphabeta_cutoff(my_state, -float("inf"), float("inf"), 0, player)
                            ai_region = int(best[0])


                        place_on_grid(window, ai_region, player)  # place ai marker on window
                        state[ai_region] = player # update board state

                        # stop = time.clock()
                        # elapsed = stop - start
                        # print("AI time: " + str(elapsed))

                        game_over = terminal_test(state,player) # check for terminal state

                        # terminal state is found
                        if game_over:
                            pygame.event.get()
                            terminal_state = play_again()

    # repeat game robustness - handle Yes No Y N ... or pop up?
      
pygame.quit()