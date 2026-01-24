import pygame
import sys
from constant import * 
from display import *       
from game import *
from score import *
from word import *
from sound import *


pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")
load_sounds()

icon=pygame.image.load("assets/images/game_logo.png") 
pygame.display.set_icon(icon)

    

def menu():
    
    current_state="MENU"
    current_game=None
    player_name=""
    user_input_word=""
    
    clock=pygame.time.Clock()

    while True:
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

          
            if current_state=="MENU":
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_1:
                        current_game=Game("easy")
                        current_state="GAME"
                    elif event.key==pygame.K_2:
                        current_game=Game("medium")
                        current_state="GAME"
                    elif event.key==pygame.K_3:
                        current_game=Game("hard")
                        current_state="GAME"
                    elif event.key==pygame.K_s:
                        current_state="SCORES"
                    elif event.key==pygame.K_p:
                        current_state="ADD_WORD"
                        user_input_word=""
          
            elif current_state=="GAME":
                if event.type==pygame.KEYDOWN:
                    
                    if event.key==pygame.K_RETURN or event.key==pygame.K_ESCAPE:
                       current_state="MENU"
                    
                    elif event.unicode.isalpha():
                        letter=event.unicode.upper()
                        old_lives=current_game.lives
                        old_score=current_game.score
                        already_played=current_game.guess_letter(letter)

                        if already_played:
                            if current_game.lives<old_lives:
                               play_sound('wrong')
                            else:
                                play_sound('chalk')
                                if current_game.score>old_score:
                                 play_sound('score')
                            
                        if current_game.finished:
                            if current_game.won:
                                current_state="VICTORY"
                            else:
                                current_state="GAME_OVER"
         
            elif current_state in ["VICTORY", "GAME_OVER"]:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN or event.key==pygame.K_ESCAPE:
                        if current_state=="VICTORY":
                            player_name=""
                            current_state="INPUT_NAME"
                        else:
                            current_state="MENU"

   
            elif current_state=="INPUT_NAME":
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        if player_name:
                            save_score(player_name, current_game.score)
                        current_state="SCORES"

                    elif event.key==pygame.K_BACKSPACE:
                         player_name=player_name[:-1]
                    else:
                        if len(player_name)<10 and event.unicode.isalnum():
                           player_name+=event.unicode.upper()

            
            elif current_state=="SCORES":
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN or event.key==pygame.K_ESCAPE:
                        current_state="MENU"

            elif current_state=="ADD_WORD":
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE or event.key==pygame.K_RETURN:
                      
                        if event.key==pygame.K_RETURN and len(user_input_word)>2:
                            add_word(user_input_word) 
                        current_state="MENU"
                        
                    elif event.key==pygame.K_BACKSPACE:
                        user_input_word=user_input_word[:-1]
                    else:
                        if event.unicode.isalpha():
                            user_input_word+=event.unicode.upper()


        if current_state=="MENU":
            play_music('menu')
            display_menu(screen)
            
        elif current_state=="GAME":
            play_music('game')
            if current_game and current_game.word:
                max_lives=current_game._get_lives(current_game.difficulty)
                errors=max_lives - current_game.lives
                display_game(screen, errors, list(current_game.found_letters), current_game.word, current_game.score, current_game.lives, max_lives)
            else:
                current_state="MENU"

        elif current_state=="VICTORY":
            play_music('victory', loop=False)
            if current_game and current_game.word:
              display_victory(screen, current_game.word, current_game.score)

        elif current_state=="GAME_OVER":
             play_music('gameover', loop=False)
             if current_game and current_game.word:
                 display_game_over(screen, current_game.word)
             else:
                 current_state="MENU"

        elif current_state=="INPUT_NAME":
             play_music('menu')
             display_input_name(player_name, screen)

        elif current_state=="SCORES":
            play_music('menu')
            best_scores=read_scores()
            display_score(screen, best_scores)
        
        elif current_state=="ADD_WORD":
            play_music('menu')
            display_personnalized(user_input_word, screen)

        pygame.display.update()
        clock.tick(60)
