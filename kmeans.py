def create_text_render(string,COLOR):
    font = pygame.font.SysFont('san', 40)
    return font.render(string, True, COLOR)
def create_text_render_black(string,COLOR):
    font = pygame.font.SysFont('san', 20)
    return font.render(string, True, COLOR)
import pygame
from random import randint
pygame.init()
screen= pygame.display.set_mode((1200,700))
pygame.display.set_caption('kmeans visualization')
running=True
clock=pygame.time.Clock()
BACKGROUND=(214,214,214)
BLACK=(0,0,0)
WHITE=(255,255,255)
BACKGROUND_PANEL=(249,255,230)
K=0
points=[]
Clusters=[]

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #Draw interface

    #Draw panel
    pygame.draw.rect(screen,BLACK,(50,50,700,500))
    pygame.draw.rect(screen,BACKGROUND_PANEL,(55,55,690,490))
    #K button +
    pygame.draw.rect(screen,BLACK,(850,50,50,50))
    screen.blit(create_text_render(("+"),WHITE),(860,55))
    #K button  -
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(create_text_render(("-"),WHITE), (960, 55))
    #k value
    screen.blit(create_text_render(("K =" + str(K)),BLACK), (1050, 55))
    #Run
    pygame.draw.rect(screen, BLACK, (850,150,150,50))
    screen.blit(create_text_render(("Run"), WHITE), (900,150))
    #Random
    pygame.draw.rect(screen, BLACK, (850,250,150,50))
    screen.blit(create_text_render(("RANDOM"), WHITE), (850,250))


    #Reset
    pygame.draw.rect(screen, BLACK, (850,550,150,50))
    screen.blit(create_text_render(("RESET"), WHITE), (850,550))
    #Algorithm
    pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
    screen.blit(create_text_render(("Algorithm"), WHITE), (850, 450))

    #End draw interface

    if 55<mouse_x<55+690 and 55<mouse_y<55+490:
        screen.blit(create_text_render_black(('('+str(mouse_x-50)+','+ str(mouse_y-50)+')'),BLACK),(mouse_x+10,mouse_y))
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            # Create point of panel:
            if 50< mouse_x < 750 and 50 < mouse_y < 550:
                point=[mouse_x-50,mouse_y-50]
                points.append(point)
                print(points)
            #change k button+
            if 850<mouse_x<900 and 55<mouse_y<100:
                K+=1
            if 950<mouse_x<1000 and 55<mouse_y<105:
                if K>0:
                    K-=1
                    print('pressed k')
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                print("run pressed")

            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                for i in range(K):
                    random_point= [randint(50,690),randint(50,500)]
                    Clusters.append(random_point)
                print("random pressed")

            # Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                print("reset button pressed")

            # Algorithm
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                print("Algorithm button pressed")
    # Draw cluster:
    for i in range(len(Clusters)):
        pygame.draw.circle(screen,BLACK,(Clusters[i][0],Clusters[i][1]),10)

    # Draw point :
    for i in range(len(points)):
        pygame.draw.circle(screen,BLACK,(points[i][0]+50,points[i][1]+50),5)
        pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 4)


    pygame.display.flip()
pygame.quit()