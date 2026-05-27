import pygame

pygame.init()
def image() -> None:
    screen_width = 1200
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))

    
    x_images = 600
    y_images = 250

    
    images_image = pygame.image.load("one peice.png").convert_alpha()
    images_image = pygame.transform.scale(images_image,(1200,500))
    images_rect = images_image.get_rect()
    screen.fill((255, 255, 255)) 

   
    images_rect.center = (x_images, y_images)
    
    screen.blit(images_image, images_rect)


   
    pygame.display.update()

   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.quit()

