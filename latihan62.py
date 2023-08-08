import pygame

## init
pygame.init()
# variable running game
isrun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10
while isrun:
    pygame.time.delay(10)

    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrun = False

    # ambil semua keyboard press
    key = pygame.key.get_pressed()

    # ambil ke kiri
    if key[pygame.K_LEFT] and x > 0:
        x -= speed  
    
    if key[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed  
    
    if key[pygame.K_DOWN] and x < window_panjang-panjang:
        y += speed  
        
    if key[pygame.K_UP] and x > 0:
        y -= speed  

    # game dynamic

    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))

    # render ke display
    pygame.display.update()

pygame.quit()