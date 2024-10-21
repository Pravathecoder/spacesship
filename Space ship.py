import pygame
pygame.font.init()

screen = pygame.display.set_mode((700,700))
pygame.display.set_caption('Welcome to war!!')

space = pygame.image.load('images/background1.png')
redship1 = pygame.image.load('images/spaceship2.png')
yellowship2 = pygame.image.load('images/Spaceship1.png')

space = pygame.transform.scale(space,(700,700))
redship1 = pygame.transform.scale(redship1,(100,100))
redship1 = pygame.transform.rotate(redship1,90)

yellowship2 = pygame.transform.scale(yellowship2,(100,100))
yellowship2 = pygame.transform.rotate(yellowship2,270)

border = pygame.Rect(350,0,10,700)

red_bullets = []
yellow_bullets =[]

red_health = 5
yellow_health = 5

healthfont = pygame.font.SysFont('georgia', 30)


def draw():
    global yellow_health , red_health
    screen.blit(space, (0,0))
    text = healthfont.render('Health:'+str(red_health), True,'red')
    screen.blit(text,(0,0))
    screen.blit(redship1, (red.x ,red.y))
    text1 = healthfont.render('Health:'+str(yellow_health), True,'yellow')
    screen.blit(text1,(580,0))
    screen.blit(yellowship2,(yellow.x,yellow.y))
    pygame.draw.rect(screen,'black',border)
    for b in red_bullets:
        pygame.draw.rect(screen, 'red' , b )
    for b in yellow_bullets:
        pygame.draw.rect(screen, 'yellow' , b )

    if yellow_health <= 0:
        text2 = healthfont.render('Red wins!', True,'red')
        screen.blit(text2,(200,300))
        yellow_health = 0

    if red_health <= 0:
       text3 = healthfont.render('Yellow wins!',True,'yellow')
       screen.blit(text3,(500,300))
       red_health = 0

    pygame.display.update()


def bullet_movement():
    global yellow_health ,red_health
    for red1 in red_bullets:
        red1.x = red1.x +3
        if yellow.colliderect(red1):
            red_bullets.remove(red1)
            yellow_health = yellow_health-1

    for yellow1 in yellow_bullets:
        yellow1.x = yellow1.x -3
        if red.colliderect(yellow1):
            yellow_bullets.remove(yellow1)
            red_health = red_health-1


def red_movement():
    keys = pygame.key.get_pressed()
    if keys [pygame.K_w] and red.y > 0:     
        red.y = red.y - 4                                   
    if keys[pygame.K_s] and red.y < 600:
        red.y = red.y +4
    if keys[pygame.K_d] and red.x < 260:
        red.x = red.x +4
    if keys[pygame.K_a] and red.x > 0:
        red.x = red.x -4
    
def yellow_movement():
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP] and yellow.y > 0:     
         yellow.y =  yellow.y - 4                                   
    if keys[pygame.K_DOWN] and yellow.y < 600:
         yellow.y =  yellow.y +4
    if keys[pygame.K_RIGHT] and yellow.x < 600:
        yellow.x =  yellow.x +4
    if keys[pygame.K_LEFT] and yellow.x > 350:
        yellow.x =  yellow.x -4





red = pygame.Rect(0,300,80,80)
yellow = pygame.Rect(550,300,80,80)
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    draw()
    red_movement()
    yellow_movement()
    bullet_movement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_1:
                redbullet = pygame.Rect(red.x +90 ,red.y +40,10,10)
                red_bullets.append(redbullet)
            if event.key == pygame.K_3:
                yellowbullet = pygame.Rect(yellow.x ,yellow.y +40,10,10)
                yellow_bullets.append(yellowbullet)
                print(yellow_bullets)            

