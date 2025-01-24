"""
Author = Akpojotor Oghenerurho
Email = akporurho@proton.me
Date = 12/01/25
play mp3 songs with python using pygames library
"""
import pygame as pg
music = input("Enter mp3 file name here")
pg.mixer.pre_init(frequency=48000, size=16, channels=2, buffer=512)
pg.mixer.init()
pg.mixer.music.load(music+".mp3") #add the mp3 file here
while pygame.mixer.music.get_busy():
  pass
