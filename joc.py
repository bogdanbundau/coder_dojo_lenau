import random as r
import pygame as p
import math as m
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
p.init()
HEIGHT = 500
window = p.display.set_mode((HEIGHT, HEIGHT), p.RESIZABLE)
print(window.get_size())
running = True
scor = 0
x_rosu = r.randint(0, HEIGHT)
y_rosu = r.randint(0, HEIGHT)
x = HEIGHT/2
y = HEIGHT/2
rad = 20
w=False
a=False
s=False
d=False
viteza = 0.1
mancare_spawned = False
cords_list_m = []
colors = [[191, 0, 230], [35, 0, 150], [3, 173, 32], [235, 150, 5], [193, 227, 2]]
mancare_rad = [3, 4, 5]
myFont = p.font.SysFont("Comic Sans MS", 18)

#image = p.image.load(r'C:\Users\Utilizator\OneDrive\Imagini\Screenshots\Captură ecran (2).png')

def mancare(cate):
    global mancare_x
    global mancare_y
    for i in range(cate):
            mancare_x = r.randint(0, HEIGHT)
            mancare_y = r.randint(0, HEIGHT)
            cords_list_m.append([mancare_x, mancare_y, r.choice(colors), r.choice(mancare_rad)])

mancare(40)
while running:

    #window.blit(image, (0, 0))

    score_caption = myFont.render("Score:", 1, (0,0,0))
    ScoreDisplay = myFont.render(str(scor), 1, (0,0,0))
    window.blit(score_caption, (HEIGHT-100, 20))
    window.blit(ScoreDisplay, (HEIGHT-100, 40))

    coordMouseX,coordMouseY = p.mouse.get_pos()
    vecDirectieX = coordMouseX - x
    vecDirectieY = coordMouseY - y

    unghiRad = m.atan2(vecDirectieY, vecDirectieX)
    unghiGrade = (unghiRad*180)/m.pi

    x += m.cos(unghiRad)*viteza 
    y += m.sin(unghiRad)*viteza

    events = p.event.get()
    for event in events:
        if event.type == p.KEYDOWN:
            if event.key == K_UP:
                w=True
                
            
        if event.type == p.KEYDOWN:
            if event.key == K_DOWN:
                s=True
                
            if event.key == K_LEFT:
                a=True
                
            if event.key == K_RIGHT:
                d=True
                
        if event.type == p.QUIT:
            running = False

        if event.type == p.KEYUP:
            if event.key == K_UP:
                w=False
                
            
        
            if event.key == K_DOWN:
                s=False
                

        
            if event.key == K_LEFT:
                
                a=False
       
            if event.key == K_RIGHT:
                
                d=False

    if w:
        y-=0.1
    elif s:
        y+=0.1
    elif a:
        x-=0.1
    elif d:
        x+=0.1
    
    if (x_rosu - x)**2 + (y_rosu - y)**2 < rad**2:
        rad+=5
        scor+=1
        x_rosu = r.randint(0, HEIGHT)
        y_rosu = r.randint(0, HEIGHT)

    for i in range(len(cords_list_m)):


        if (cords_list_m[i][0] - x)**2 + (cords_list_m[i][1] - y)**2 < rad**2:
            cords_list_m[i][0] = r.randint(0, HEIGHT)
            cords_list_m[i][1] = r.randint(0, HEIGHT)
            rad = m.sqrt(rad*rad+cords_list_m[i][3]*cords_list_m[i][3])
            scor+=1



        p.draw.circle(window,cords_list_m[i][2], (cords_list_m[i][0],cords_list_m[i][1]),cords_list_m[i][3])
    p.draw.circle(window,(255, 0, 0), (x_rosu, y_rosu), 15 )
    p.draw.circle(window, (0, 201, 167), (x, y), rad)
    
    p.display.update()
    
    p.display.flip()
    window.fill((196, 252, 239))
p.quit()
print("Scorul tau este " + str(scor))
