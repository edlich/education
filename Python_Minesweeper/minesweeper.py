# minesweeper.py
# Objektorientierte Skriptsprachen ESA2
# 23.05.2025

__author__ = 'Stefan Mietchen'

import pygame
import random
import sys

# Einstellungen hier vornehmen
SPIELFELDGROESSE = (320, 320)
ANZAHL_SPALTEN, ANZAHL_ZEILEN = 8, 8
ZELLENGROESSE = SPIELFELDGROESSE[0] // ANZAHL_SPALTEN
ANZAHL_MINEN = 10

# Klasse für eine Zelle
class Zelle:
    def __init__(self, zeile, spalte):
        self.zeile = zeile
        self.spalte = spalte
        self.ist_mine = False
        self.aufgedeckt = False
        self.markiert = False
        self.angenzende_minen = 0

    def zeichne(self):
        x = self.zeile * ZELLENGROESSE
        y = self.spalte * ZELLENGROESSE
        rect = pygame.Rect(x, y, ZELLENGROESSE, ZELLENGROESSE)

        if self.aufgedeckt:
            pygame.draw.rect(screen, pygame.Color('white'), rect)
            pygame.draw.rect(screen, pygame.Color('black'), rect, 1)
            if self.ist_mine:
                pygame.draw.circle(screen, pygame.Color('black'), rect.center, ZELLENGROESSE // 4)
            elif self.angenzende_minen > 0:
                zahl = schriftart.render(str(self.angenzende_minen), True, pygame.Color('black'))
                screen.blit(zahl, zahl.get_rect(center = rect.center))
        else:
            pygame.draw.rect(screen, pygame.Color('grey'), rect)
            pygame.draw.rect(screen, pygame.Color('black'), rect, 1)
            if self.markiert:
                flagge_rect = flagge.get_rect(center = rect.center)
                screen.blit(flagge, flagge_rect)

# zufällige Minen platzieren
def platziere_minen():
    minen_platziert = 0
    while minen_platziert < ANZAHL_MINEN:
        zeile = random.randint(0, ANZAHL_SPALTEN - 1)
        spalte = random.randint(0, ANZAHL_SPALTEN - 1)
        if not spielfeld[zeile][spalte].ist_mine:
            spielfeld[zeile][spalte].ist_mine = True
            minen_platziert += 1

# angenzende Minen zählen
def zaehle_angrenzende_minen():
    for zeile in range(ANZAHL_ZEILEN):
        for spalte in range(ANZAHL_SPALTEN):
            if spielfeld[zeile][spalte].ist_mine:
                continue # wenn die Zelle eine Mine ist, brauche ich die angrenzenden Minen nicht zu zählen

            # gucke in die 8 Nachbarfelder jeder Zelle und zähle die Anzahl Minen
            anzahl_minen = 0
            for delta_zeile in [-1, 0, 1]:
                for delta_spalte in [-1, 0, 1]:
                    naechste_zeile, naechste_spalte = zeile + delta_zeile, spalte + delta_spalte
                    if 0 <= naechste_zeile < ANZAHL_ZEILEN and 0 <= naechste_spalte < ANZAHL_SPALTEN and spielfeld[naechste_zeile][naechste_spalte].ist_mine:
                        anzahl_minen += 1
            spielfeld[zeile][spalte].angenzende_minen = anzahl_minen

# Spielfeld rekursiv aufdecken
def zelle_aufdecken(zeile, spalte):
    zelle = spielfeld[zeile][spalte]
    if zelle.aufgedeckt or zelle.markiert:
        return

    zelle.aufgedeckt = True
    if zelle.angenzende_minen == 0 and not zelle.ist_mine:
        for delta_zeile in [-1, 0, 1]:
            for delta_spalte in [-1, 0, 1]:
                naechste_zeile, naechste_spalte = zeile + delta_zeile, spalte + delta_spalte
                if 0 <= naechste_zeile < ANZAHL_ZEILEN and 0 <= naechste_spalte < ANZAHL_SPALTEN:
                    zelle_aufdecken(naechste_zeile, naechste_spalte)

# Spiel beenden
def spiel_beenden(gewonnen):
    for zeile in spielfeld:
        for zelle in zeile:
            zelle.aufgedeckt = True
    pygame.display.flip()
    print("GEWONNEN") if gewonnen else print("VERLOREN")
    pygame.quit()
    sys.exit()

# Spiel vorbereiten
pygame.init()
screen = pygame.display.set_mode(SPIELFELDGROESSE)
pygame.display.set_caption('Minesweeper')
schriftart = pygame.font.SysFont(None, 24)

spielfeld = [[Zelle(zeile, spalte) for zeile in range(ANZAHL_SPALTEN)] for spalte in range(ANZAHL_SPALTEN)]
platziere_minen()
zaehle_angrenzende_minen()

flagge = pygame.image.load("flagge.png")
flagge = pygame.transform.scale(flagge, (ZELLENGROESSE - 10, ZELLENGROESSE - 10))

# Hauptschleife
weiter = True
while weiter:
    screen.fill(pygame.Color('black'))
    for zeile in spielfeld:
        for zelle in zeile:
            zelle.zeichne()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            weiter = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            zeile, spalte = y // ZELLENGROESSE, x // ZELLENGROESSE
            zelle = spielfeld[zeile][spalte]

            if event.button == 1: # Linksklick
                if zelle.ist_mine:
                    spiel_beenden(False)
                else:
                    zelle_aufdecken(zeile, spalte)
            elif event.button == 3: # Rechtsklick
                if not zelle.aufgedeckt:
                    zelle.markiert = not zelle.markiert

    # Gewinnbedingung
    nicht_aufgedeckt = [zelle for zeile in spielfeld for zelle in zeile if not zelle.aufgedeckt]
    if len(nicht_aufgedeckt) == ANZAHL_MINEN:
        spiel_beenden(True)

pygame.quit()