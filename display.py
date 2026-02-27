import pygame
from constant import *

pygame.font.init()

# On définit les constantes ici si elles ne sont pas déjà dans constant.py
W_CENTER = 1200 // 2
H_CENTER = 800 // 2

def draw_chalk_line(screen, start, end, width=5):
    pygame.draw.line(screen, WHITE, start, end, width)
    offset = 3
    start_shadow = (start[0] + offset, start[1] + offset)
    end_shadow = (end[0] + offset, end[1] + offset)
    pygame.draw.line(screen, (150, 150, 150), start_shadow, end_shadow, 2)

# Polices adaptées à la nouvelle taille
font_titles = pygame.font.Font("chalk.ttf", 80)
font_text = pygame.font.Font("chalk.ttf", 50)
font_small = pygame.font.Font("chalk.ttf", 35)

background = pygame.image.load("assets/images/background.jpg")
background = pygame.transform.scale(background, (1200, 800))

try:
    logo = pygame.image.load("assets/images/hangman_logo.png")
    logo = pygame.transform.scale(logo, (250, 250))
    HAS_LOGO = True
except:
    HAS_LOGO = False

def display_menu(screen):
    screen.blit(background, (0, 0))
    
    # Titre centré
    txt_title = font_titles.render("HANGMAN GAME", True, BLUE)
    screen.blit(txt_title, (W_CENTER - txt_title.get_width() // 2, 80)) 
    
    if HAS_LOGO:
        screen.blit(logo, (W_CENTER - logo.get_width() // 2, 180))
    
    txt_game = font_text.render("TO PLAY, CHOOSE LEVEL", True, BLACK)
    screen.blit(txt_game, (W_CENTER - txt_game.get_width() // 2, 450))
    
    # Niveaux centrés avec espacement
    txt_easy = font_text.render("[1] EASY", True, GREEN)
    txt_medium = font_text.render("[2] MEDIUM", True, (255, 200, 0))
    txt_hard = font_text.render("[3] HARD", True, RED)
    
    total_width = txt_easy.get_width() + txt_medium.get_width() + txt_hard.get_width() + 100
    start_x = W_CENTER - total_width // 2
    screen.blit(txt_easy, (start_x, 530))    
    screen.blit(txt_medium, (start_x + txt_easy.get_width() + 50, 530)) 
    screen.blit(txt_hard, (start_x + txt_easy.get_width() + txt_medium.get_width() + 100, 530))

    txt_scores = font_text.render("[S] TO SEE SCORES", True, BLACK)
    txt_personnalize = font_text.render("[P] TO ADD WORDS", True, BLACK)
    
    screen.blit(txt_scores, (W_CENTER - txt_scores.get_width() // 2, 630))
    screen.blit(txt_personnalize, (W_CENTER - txt_personnalize.get_width() // 2, 700))

def display_game(screen, error, guessed_letter, secret_word, score, lives, max_lives):
    if secret_word is None: secret_word = "ERROR"
    screen.blit(background, (0, 0))

    # Potence centrée à droite
    p_x, p_y = 800, 250
    draw_chalk_line(screen, (p_x, p_y), (p_x, p_y + 300), 8) # Vertical
    draw_chalk_line(screen, (p_x - 50, p_y + 300), (p_x + 150, p_y + 300), 8) # Base
    draw_chalk_line(screen, (p_x, p_y), (p_x + 120, p_y), 8) # Haut
    draw_chalk_line(screen, (p_x + 120, p_y), (p_x + 120, p_y + 40), 8) # Corde
    draw_chalk_line(screen, (p_x, p_y + 50), (p_x + 50, p_y), 8) # Renfort

    # Score et Vies
    pygame.draw.rect(screen, WHITE, (50, 50, 320, 80), width=4, border_radius=10)
    score_text = font_text.render(f"SCORE: {score}", True, WHITE)
    screen.blit(score_text, (70, 65))

    lives_color = GREEN if lives > max_lives // 2 else (ORANGE if lives > 2 else RED)
    pygame.draw.rect(screen, lives_color, (400, 50, 320, 80), width=4, border_radius=10)
    lives_text = font_text.render(f"LIVES: {lives}/{max_lives}", True, lives_color)
    screen.blit(lives_text, (420, 65))

    # Mot secret centré en bas
    word_surface = font_titles.render(" ".join([l if l in guessed_letter else "_" for l in secret_word]), True, WHITE)
    screen.blit(word_surface, (W_CENTER - word_surface.get_width() // 2, 600))
    
    menu_return = font_small.render("[RETURN] TO MENU", True, GREEN)
    screen.blit(menu_return, (W_CENTER - menu_return.get_width() // 2, 720))
  
    # Bonhomme
    center_man = p_x + 120
    if error >= 1: pygame.draw.circle(screen, WHITE, (center_man, p_y + 70), 30, width=5) # Tête
    if error >= 2: draw_chalk_line(screen, (center_man, p_y + 100), (center_man, p_y + 200), 6) # Corps
    if error >= 3: draw_chalk_line(screen, (center_man, p_y + 120), (center_man - 40, p_y + 170), 6) # Bras G
    if error >= 4: draw_chalk_line(screen, (center_man, p_y + 120), (center_man + 40, p_y + 170), 6) # Bras D
    if error >= 5: draw_chalk_line(screen, (center_man, p_y + 200), (center_man - 40, p_y + 270), 6) # Jambe G
    if error >= 6: draw_chalk_line(screen, (center_man, p_y + 200), (center_man + 40, p_y + 270), 6) # Jambe D

def display_victory(screen, secret_word, score):
    screen.blit(background, (0, 0))
    elements = [
        (font_titles.render("YOU WON!", True, GREEN), 150),
        (font_text.render(f"WORD: {secret_word}", True, WHITE), 300),
        (font_titles.render(f"SCORE: {score}", True, (255, 200, 0)), 420),
        (font_text.render("[RETURN] TO CONTINUE", True, GREEN), 600)
    ]
    for surf, y in elements:
        screen.blit(surf, (W_CENTER - surf.get_width() // 2, y))

def display_game_over(screen, secret_word):
    screen.blit(background, (0, 0))
    elements = [
        (font_titles.render("YOU LOST!", True, RED), 150),
        (font_text.render(f"THE WORD WAS: {secret_word}", True, WHITE), 320),
        (font_text.render("[RETURN] TO MENU", True, GREEN), 550)
    ]
    for surf, y in elements:
        screen.blit(surf, (W_CENTER - surf.get_width() // 2, y))

def display_personnalized(current_text, screen):
    screen.blit(background, (0, 0))
    current_text = current_text.upper()
    
    t1 = font_text.render("ADD WORDS TO THE LIST!", True, WHITE)
    t2 = font_text.render("TYPE YOUR WORD:", True, (200, 200, 200))
    screen.blit(t1, (W_CENTER - t1.get_width() // 2, 100))
    screen.blit(t2, (W_CENTER - t2.get_width() // 2, 220))
   
    # Champ de saisie centré
    box_w, box_h = 600, 120
    pygame.draw.rect(screen, WHITE, (W_CENTER - box_w // 2, 300, box_w, box_h), width=4, border_radius=10)
    user_input = font_titles.render(current_text + "_", True, WHITE)
    screen.blit(user_input, (W_CENTER - user_input.get_width() // 2, 315))
   
    m_ret = font_text.render("[RETURN] SAVE", True, GREEN)
    m_can = font_text.render("[ESC] CANCEL", True, RED)
    screen.blit(m_ret, (W_CENTER - m_ret.get_width() - 50, 500))
    screen.blit(m_can, (W_CENTER + 50, 500))

def display_score(screen, clean_score):
    screen.blit(background, (0, 0))
    title = font_titles.render("HALL OF FAME", True, (255, 200, 0))
    screen.blit(title, (W_CENTER - title.get_width() // 2, 50))

    # Tableau centré
    t_w, t_h = 800, 450
    t_x, t_y = W_CENTER - t_w // 2, 180
    
    surf = pygame.Surface((t_w, t_h))
    surf.set_alpha(60); surf.fill(WHITE)
    screen.blit(surf, (t_x, t_y))
    pygame.draw.rect(screen, WHITE, (t_x, t_y, t_w, t_h), width=4, border_radius=15)
    
    headers = [(font_text.render("RANK", True, (255, 200, 0)), t_x + 50),
               (font_text.render("NAME", True, (255, 200, 0)), t_x + 250),
               (font_text.render("SCORE", True, (255, 200, 0)), t_x + 600)]
    
    for h_surf, h_x in headers:
        screen.blit(h_surf, (h_x, t_y + 20))

    if not clean_score:
        msg = font_text.render("NO SCORES YET", True, RED)
        screen.blit(msg, (W_CENTER - msg.get_width() // 2, t_y + 200))
    else:
        for i, (name, val) in enumerate(clean_score[:5]):
            y = t_y + 100 + (i * 65)
            color = (255, 215, 0) if i == 0 else (192, 192, 192) if i == 1 else (205, 127, 50) if i == 2 else WHITE
            screen.blit(font_small.render(f"#{i+1}", True, color), (t_x + 60, y))
            screen.blit(font_small.render(name[:15], True, color), (t_x + 250, y))
            screen.blit(font_small.render(str(val), True, color), (t_x + 620, y))

    back = font_text.render("[RETURN] TO MENU", True, GREEN)
    screen.blit(back, (W_CENTER - back.get_width() // 2, 700))

def display_input_name(user_name, screen):
    screen.blit(background, (0, 0))
    ask = font_titles.render("ENTER YOUR NAME:", True, WHITE)
    screen.blit(ask, (W_CENTER - ask.get_width() // 2, 200))

    box_w, box_h = 600, 120
    pygame.draw.rect(screen, WHITE, (W_CENTER - box_w // 2, 350, box_w, box_h), width=4, border_radius=10)
    name_surf = font_titles.render(user_name.upper() + "_", True, WHITE)
    screen.blit(name_surf, (W_CENTER - name_surf.get_width() // 2, 365))
    
    inst = font_text.render("[RETURN] TO SAVE", True, GREEN)
    screen.blit(inst, (W_CENTER - inst.get_width() // 2, 550))