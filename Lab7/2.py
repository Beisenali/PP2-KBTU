import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_DIR = "music/"
if not os.path.exists(MUSIC_DIR):
    os.makedirs(MUSIC_DIR)

playlist = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
current_track = 0

def play_music():
    if playlist:
        pygame.mixer.music.load(os.path.join(MUSIC_DIR, playlist[current_track]))
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    if playlist:
        current_track = (current_track + 1) % len(playlist)
        play_music()

def previous_track():
    global current_track
    if playlist:
        current_track = (current_track - 1) % len(playlist)
        play_music()

screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Music Player")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()

pygame.quit()