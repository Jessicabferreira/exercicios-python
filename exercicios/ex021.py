"""
Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame  # instalar o pygame
pygame.init()   # init vai iniciar o uso da biblioteca
pygame.mixer.music.load('ex021.mp3')  # vai carregar o áudio
pygame.mixer.music.play()    # vai tocar
input()
pygame.event.wait()   # ele espera tocar o áudio para depois encerrar
