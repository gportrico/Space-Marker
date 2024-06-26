import pygame
import tkinter as tk
from tkinter import simpledialog
import json
import os
import random

pygame.init()
pygame.mixer.init()

#SETUP
tamanho_janela = (1000, 560)
tela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("SPACE MARKER")
imagem_fundo = pygame.image.load("assets/bg.jpg")
icone = pygame.image.load("assets/space.png")
pygame.display.set_icon(icone)
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
fonte = pygame.font.Font(None, 24)

marcacoes = {}
posicoes_estrelas = []

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

#Nome da estrela
def obter_nome_estrela():
    root = tk.Tk()
    root.withdraw()
    nome_estrela = simpledialog.askstring("Input", "Nome da Estrela:", parent=root)
    root.destroy()
    return nome_estrela if nome_estrela else "Desconhecido"

