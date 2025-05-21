import pygame, sys
from pygame.locals import *

pygame.init()  # Inicjalizacja biblioteki pygame

FPS = 60  # Liczba klatek na sekundę (płynność animacji)
fpsClock = pygame.time.Clock()  # Obiekt do kontrolowania czasu

# Utworzenie okna gry o wymiarach 400x300 pikseli
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')  # Ustawienie tytułu okna

WHITE = (255, 255, 255)  # Definicja koloru białego (RGB)
catImg1 = pygame.image.load('cat.png')   # Wczytanie obrazka pierwszego kota
catImg2 = pygame.image.load('cat2.png')  # Wczytanie obrazka drugiego kota

# Pozycja i kierunek pierwszego kota
catx1 = 10      # Początkowa pozycja X kota 1
caty1 = 10      # Początkowa pozycja Y kota 1
direction1 = 'right'  # Początkowy kierunek ruchu kota 1

# Pozycja i kierunek drugiego kota
catx2 = 300     # Początkowa pozycja X kota 2
caty2 = 200     # Początkowa pozycja Y kota 2
direction2 = 'left'   # Początkowy kierunek ruchu kota 2

while True:  # Główna pętla gry
    DISPLAYSURF.fill(WHITE)  # Wypełnienie tła kolorem białym

    # --- Ruch kota 1 ---
    if direction1 == 'right':
        catx1 += 5  # Przesunięcie w prawo
        if catx1 == 280:  # Sprawdzenie, czy kot dotarł do prawej krawędzi
            direction1 = 'down'  # Zmiana kierunku na dół
    elif direction1 == 'down':
        caty1 += 5  # Przesunięcie w dół
        if caty1 == 220:  # Sprawdzenie, czy kot dotarł do dolnej krawędzi
            direction1 = 'left'  # Zmiana kierunku na lewo
    elif direction1 == 'left':
        catx1 -= 5  # Przesunięcie w lewo
        if catx1 == 10:  # Sprawdzenie, czy kot dotarł do lewej krawędzi
            direction1 = 'up'  # Zmiana kierunku na górę
    elif direction1 == 'up':
        caty1 -= 5  # Przesunięcie w górę
        if caty1 == 10:  # Sprawdzenie, czy kot dotarł do górnej krawędzi
            direction1 = 'right'  # Zmiana kierunku na prawo

    # --- Ruch kota 2 (niezależny, inne kierunki) ---
    if direction2 == 'left':
        catx2 -= 5  # Przesunięcie w lewo
        if catx2 == 10:  # Sprawdzenie, czy kot dotarł do lewej krawędzi
            direction2 = 'up'  # Zmiana kierunku na górę
    elif direction2 == 'up':
        caty2 -= 5  # Przesunięcie w górę
        if caty2 == 10:  # Sprawdzenie, czy kot dotarł do górnej krawędzi
            direction2 = 'right'  # Zmiana kierunku na prawo
    elif direction2 == 'right':
        catx2 += 5  # Przesunięcie w prawo
        if catx2 == 280:  # Sprawdzenie, czy kot dotarł do prawej krawędzi
            direction2 = 'down'  # Zmiana kierunku na dół
    elif direction2 == 'down':
        caty2 += 5  # Przesunięcie w dół
        if caty2 == 220:  # Sprawdzenie, czy kot dotarł do dolnej krawędzi
            direction2 = 'left'  # Zmiana kierunku na lewo

    # Rysowanie obu kotów na ekranie w ich aktualnych pozycjach
    DISPLAYSURF.blit(catImg1, (catx1, caty1))
    DISPLAYSURF.blit(catImg2, (catx2, caty2))

    # Obsługa zdarzeń (np. zamknięcie okna gry)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Aktualizacja wyświetlacza
    fpsClock.tick(FPS)       # Ograniczenie liczby klatek na sekundę