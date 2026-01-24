import pygame

pygame.mixer.init()

sounds={}
musics={}

sound_files={
    'chalk':'assets/sounds/new_letter.wav',
    'wrong':'assets/sounds/wrong_letter.wav',
    'score':'assets/sounds/score_level.wav'
}

music_files={
    'menu':'assets/sounds/background_loop.wav',
    'game':'assets/sounds/background_game.wav',
    'victory':'assets/sounds/victory.wav',
    'gameover':'assets/sounds/game_over.wav'
}

_state={
    'current_music': None
}

def load_sounds():
    
    for name, file in sound_files.items():
        try:
            sounds[name]=pygame.mixer.Sound(file)
            sounds[name].set_volume(0.6)    
        except:
            sounds[name]=None
      

def play_sound(name):
    if name in sounds and sounds[name]:
        sounds[name].play()

def play_music(name, loop=True):
    if _state['current_music']==name:
        return
    
    
    pygame.mixer.music.stop()

    if name in music_files:
        try:
            pygame.mixer.music.load(music_files[name])
            pygame.mixer.music.set_volume(0.3)
            if loop:
                pygame.mixer.music.play(-1) 
            else:
                pygame.mixer.music.play()
            _state['current_music']=name
        except:
            _state['current_music']=None

def stop_music():
    pygame.mixer.music.stop()
    _state['current_music']=None