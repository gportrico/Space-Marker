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

#SAVE
def salvar_marcacoes():
    data = {
        "estrelas": []
    }
    for pos, nome in marcacoes.items():
        dado_estrela = {
            "nome": nome,
            "posicao": pos
        }
        data["estrelas"].append(dado_estrela)
    
    try:
        with open("assets/marcacoes.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Marcacoes salvas com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar marcacoes: {e}")

#LOAD
def carregar_marcacoes():
    global marcacoes, posicoes_estrelas
    try:
        with open("assets/marcacoes.json", "r") as f:
            data = json.load(f)
            marcacoes.clear()
            posicoes_estrelas.clear()
            for dado_estrela in data["estrelas"]:
                pos = tuple(dado_estrela["posicao"])
                nome = dado_estrela["nome"]
                marcacoes[pos] = nome
                posicoes_estrelas.append(pos)
            
    except Exception as e:
        print(f"Erro ao carregar marcacoes: {e}")
        
#Limpar Estrelas
def limpar_tela():
    global marcacoes, posicoes_estrelas
    marcacoes.clear()
    posicoes_estrelas.clear()    

#Limpar Save
def excluir_marcacoes_e_arquivo():
    limpar_tela()
    if os.path.exists("assets/marcacoes.json"):
        os.remove("assets/marcacoes.json")
