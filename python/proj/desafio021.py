"""faça um programa em phyton que abra e reproduza um audio
em mp3."""

import pygame

pygame.mixer.init()
pygame.init()  # inicia o modulo
pygame.mixer.music.load('superMario.mp3')  # carrega a musica no programa
pygame.mixer.music.play()  # toca a musica
pygame.event.wait()
