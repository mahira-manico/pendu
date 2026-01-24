import pygame
from constant import *

pygame.font.init()

def draw_chalk_line(screen, start, end, width=5):
    pygame.draw.line(screen, WHITE, start, end, width)
    offset=3
    start_shadow=(start[0]+offset, start[1]+offset)
    end_shadow=(end[0]+offset, end[1]+offset)
    pygame.draw.line(screen, (200, 200, 200), start_shadow, end_shadow, 2)

font_titles=pygame.font.Font("chalk.ttf",60)
font_text=pygame.font.Font("chalk.ttf",40)
font_small=pygame.font.Font("chalk.ttf",30)

background=pygame.image.load("assets/images/background.jpg")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))

try:
    logo=pygame.image.load("assets/images/hangman_logo.png")
    logo=pygame.transform.scale(logo,(200,200))
    HAS_LOGO=True
except:
    HAS_LOGO=False


def display_menu(screen):
   screen.blit(background,(0,0))
 
   if HAS_LOGO:
       screen.blit(logo, (650, 20))
  
   txt_title=font_titles.render("HANGMAN GAME",True,BLUE)
   screen.blit(txt_title, (150, 60)) 
   
   txt_game=font_text.render("TO PLAY, CHOOSE LEVEL",True,BLACK)
   screen.blit(txt_game, (150, 170))
   
   txt_easy = font_text.render("[1] EASY", True, GREEN)
   txt_medium = font_text.render("[2] MEDIUM", True, (255, 200, 0))
   txt_hard = font_text.render("[3] HARD", True, RED)
   
   screen.blit(txt_easy, (80, 270))    
   screen.blit(txt_medium, (310, 270)) 
   screen.blit(txt_hard, (600, 270))

   txt_scores=font_text.render("[S] TO SEE SCORES",True,BLACK)
   txt_personnalize=font_text.render("[P] TO ADD WORDS",True, BLACK)
   
   screen.blit(txt_scores, (200, 400))
   screen.blit(txt_personnalize, (200, 480))


def display_game(screen, error, guessed_letter, secret_word, score, lives, max_lives):
    if secret_word is None:
       secret_word="ERROR"
    screen.blit(background,(0,0))

    draw_chalk_line(screen,(600,300),(600,500),5)
    draw_chalk_line(screen,(550,500),(750,500),5)
    draw_chalk_line(screen,(600,301),(700,301),5)
    draw_chalk_line(screen,(700,330),(700,300),5)
    draw_chalk_line(screen,(600, 340), (640, 300),5)
 
    pygame.draw.rect(screen, WHITE, (20, 20, 280, 70), width=3, border_radius=5)
    score_text=font_text.render(f"SCORE: {score}", True, WHITE)
    screen.blit(score_text, (35, 35))

    lives_color=GREEN if lives>max_lives//2 else (ORANGE if lives>2 else RED)
    pygame.draw.rect(screen, lives_color, (320, 20, 260, 70), width=3, border_radius=5)
    lives_text=font_text.render(f"LIVES: {lives}/{max_lives}", True, lives_color)
    screen.blit(lives_text, (335, 35))

    x_start=50
    y_position=450

    for letters in secret_word:
      if letters in guessed_letter:
        letter=font_titles.render(letters,True,WHITE)
      else:
        letter=font_titles.render("_",True,WHITE)

      screen.blit(letter,(x_start,y_position))
      x_start+=50
    
    menu_return=font_small.render("[RETURN] TO MENU",True,GREEN)
    screen.blit(menu_return,(220, 530))
  
    if error>=1:
     pygame.draw.circle(screen,WHITE,(700, 350), 20, width=5)
    if error>=2:
     draw_chalk_line(screen,(700, 370), (700, 410),5)
    if error>=3:
     draw_chalk_line(screen,(700, 380), (660, 400),5)
    if error>=4:
     draw_chalk_line(screen,(700, 380), (740, 400),5)
    if error>=5:
     draw_chalk_line(screen,(700, 410), (680, 460),5)
    if error>=6:
     draw_chalk_line(screen,(700, 410), (720, 460),5)


def display_victory(screen, secret_word, score):
  screen.blit(background,(0,0))

  victory_word=font_titles.render("YOU WON!",True,GREEN)
  screen.blit(victory_word,(250, 100))

  found_word=font_text.render(f"WORD: {secret_word}",True,WHITE)
  word_width=found_word.get_width()
  screen.blit(found_word,((WIDTH-word_width)//2, 220))

  score_display=font_titles.render(f"SCORE: {score}",True,(255,200,0))
  score_width=score_display.get_width()
  screen.blit(score_display,((WIDTH-score_width)//2, 320))

  continue_text=font_text.render("[RETURN] TO CONTINUE",True,GREEN)
  continue_width=continue_text.get_width()
  screen.blit(continue_text,((WIDTH-continue_width)//2, 460))


def display_game_over(screen, secret_word):
  screen.blit(background,(0,0))

  game_over_word=font_titles.render("YOU LOST!",True,RED)
  screen.blit(game_over_word,(270, 100))

  hidden_word=font_text.render(f"THE WORD WAS: {secret_word}",True,WHITE)
  word_width=hidden_word.get_width()
  screen.blit(hidden_word,((WIDTH-word_width)//2, 240))

  menu_return=font_text.render("[RETURN] TO MENU",True,GREEN)
  return_width=menu_return.get_width()
  screen.blit(menu_return,((WIDTH-return_width)//2, 420))


def display_personnalized(current_text, screen):
    current_text=current_text.upper()
    screen.blit(background,(0,0))

    welcome_word=font_text.render("ADD WORDS TO THE LIST!",True,WHITE)
    welcome_width=welcome_word.get_width()
    screen.blit(welcome_word,((WIDTH-welcome_width)//2, 80))
 
    instruction=font_text.render("TYPE YOUR WORD:",True,(200,200,200))
    inst_width=instruction.get_width()
    screen.blit(instruction,((WIDTH-inst_width)//2, 180))
   
    pygame.draw.rect(screen, WHITE, (200, 250, 400, 100), width=3, border_radius=5)
    user_input=font_titles.render(current_text+"_",True,WHITE)
    screen.blit(user_input,(220, 270))
   
    menu_return=font_text.render("[RETURN] SAVE",True,GREEN)
    return_width=menu_return.get_width()
    screen.blit(menu_return,((WIDTH-return_width)//2-80, 420))
   
    esc_text=font_text.render("[ESC] CANCEL",True,RED)
    esc_width=esc_text.get_width()
    screen.blit(esc_text,((WIDTH-esc_width)//2+80, 480))


def display_score(screen, clean_score):
    screen.blit(background,(0,0))
    
    scores_titles=font_titles.render("HALL OF FAME",True,(255,200,0))
    title_width=scores_titles.get_width()
    screen.blit(scores_titles,((WIDTH - title_width)//2, 50))

    table_x=150
    table_y=150
    table_width=500
    table_height=320

    table_surface=pygame.Surface((table_width, table_height))
    table_surface.set_alpha(40)
    table_surface.fill(WHITE)
    screen.blit(table_surface,(table_x, table_y))

    pygame.draw.rect(screen, WHITE,(table_x, table_y, table_width, table_height), width=3, border_radius=10)
  
    header_y=table_y+20
    rank_header=font_text.render("RANK", True, (255,200,0))
    name_header=font_text.render("NAME", True, (255,200,0))
    score_header=font_text.render("SCORE", True, (255,200,0))
    
    screen.blit(rank_header,(table_x+40, header_y))
    screen.blit(name_header,(table_x+200, header_y))
    screen.blit(score_header,(table_x+350, header_y))
 
    pygame.draw.line(screen, WHITE, (table_x+20, header_y+50),(table_x+table_width-20, header_y +50), 2)
    
    if not clean_score:
        no_score=font_text.render("NO SCORES YET",True,RED)
        no_width=no_score.get_width()
        screen.blit(no_score,((WIDTH-no_width)//2, 280))
    else:
        y_position=header_y+75
        
        for i,(player_name, score) in enumerate(clean_score[:5], 1):
            if i==1:
                color=(255,215,0) 
            elif i==2:
                color=(192,192,192) 
            elif i==3:
                color=(205,127,50) 
            else:
                color=WHITE 
            rank_text=font_small.render(f"#{i}", True, color)
            screen.blit(rank_text, (table_x+50, y_position))

            name_text=font_small.render(player_name[:10], True, color)
            screen.blit(name_text, (table_x+200, y_position))
          
            score_text=font_small.render(str(score), True, color)
            screen.blit(score_text, (table_x+390, y_position))
            
            y_position+=50

    menu_return=font_text.render("[RETURN] TO MENU",True,GREEN)
    return_width=menu_return.get_width()
    screen.blit(menu_return,((WIDTH-return_width)//2, 500))


def display_input_name(user_name, screen):
  screen.blit(background,(0,0))
  user_name=user_name.upper()
  
  input_ask=font_titles.render("ENTER YOUR NAME:",True,WHITE)
  ask_width=input_ask.get_width()
  screen.blit(input_ask,((WIDTH-ask_width)//2, 150))

  pygame.draw.rect(screen, WHITE, (200, 260, 400, 100), width=3, border_radius=5)
  
  name=font_titles.render(user_name+"_",True,WHITE)
  screen.blit(name,(220, 280))
  
  instruction=font_text.render("[RETURN] TO SAVE",True,GREEN)
  inst_width=instruction.get_width()
  screen.blit(instruction,((WIDTH-inst_width)//2, 420))