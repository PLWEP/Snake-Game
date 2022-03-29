# Membuat game ular ularan
# menggunakan random dan pygame

import pygame
import random

# Menginisialisasi pygame
pygame.init

# Pemberian warna
putih = (255, 255, 255) 
merah = (255, 0, 0)
hitam = (0, 0, 0)

# Window
screen_width = 700
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width,screen_width))

# Judul
pygame.display.set_caption("Ular-Ularan")

# Persiapan jam
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Fungsi display
def text_screen(text, colour, x, y) :
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x,y])

# Membuat ular
def plot_snake(gameWindow, colour, list_ular, size_ular) :
    for x,y in list_ular :
        pygame.draw.rect(gameWindow, colour, [x, y, size_ular, size_ular])

# Fungsi UTAMA
def gameloop() :
    exit_game = False
    game_over = False
    ular_x = 45
    ular_y = 55
    velocity_x = 0
    velocity_y = 0
    list_ular = []
    panjang_ular = 1

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(60, screen_width - 20)
    score = 0
    init_velocity = 4
    size_ular = 25
    fps = 60

    while not exit_game :
        if game_over :
            gameWindow.fill(putih)
            text_screen("Game Over!! Tekan Enter", merah, 100, 250)

            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    exit_game = True

                if event.type == pygame.K_RETURN :
                    gameloop()
        else :

            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    exit_game = True

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT :
                        velocity_x = init_velocity
                        velocity_y = 0                

                    if event.key == pygame.K_LEFT :
                        velocity_x = - init_velocity
                        velocity_y = 0                

                    if event.key == pygame.K_UP :
                        velocity_x = 0
                        velocity_y = - init_velocity

                    if event.key == pygame.K_DOWN :
                        velocity_x = 0
                        velocity_y = init_velocity  

                ular_x = ular_x + velocity_x
                ular_y = ular_y + velocity_y

                if abs(ular_x - food_x) < 10 and abs(ular_y - food_y) < 10 :
                    score += 1
                    food_y = random.randint(20, screen_width - 30)
                    food_x = random.randint(20, screen_height - 30)
                    panjang_ular += 5

                gameWindow.fill(putih)
                text_screen("score : " + str(score * 10), merah, 5, 5)
                pygame.draw.rect(gameWindow, merah, [food_x, food_y, size_ular, size_ular])
                pygame.draw.line(gameWindow,merah, (0,40), (900,40), 5)

                kepala = []
                kepala.append(ular_x)
                kepala.append(ular_y)
                list_ular.append(kepala)

                if len(list_ular) > panjang_ular :
                    del list_ular[0]

                if kepala in list_ular[:-1] :
                    game_over = True

                if ular_x < 0 or ular_x > screen_width - 20 or ular_y < 50 or ular_y > screen_height - 20 :
                    game_over = True
                
                plot_snake(gameWindow, hitam, list_ular, size_ular)
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
        quit()

gameloop()

                    