import random as r

from shutil import move
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
HEIGHT = 800
window = p.display.set_mode((HEIGHT, HEIGHT), p.RESIZABLE)
print(window.get_size())
running = True
scor = 0
x_rosu = r.randint(0, HEIGHT)
y_rosu = r.randint(0, HEIGHT)

x_suprema = r.randint(0, HEIGHT)
y_suprema = r.randint(0, HEIGHT)
suprema_culoare=1
caz = 0
timp_suprema = 0

x_adversar = r.randint(0, HEIGHT)
y_adversar = r.randint(0, HEIGHT)
raza_adversar = 15
viteza_adversar = 0.7
eat_adversar = 0
background_color_adversar = (196, 0, 239)

x = HEIGHT/2
y = HEIGHT/2
rad = 20
viteza = 1
background_color = (196, 252, 239)
culori_background = [(0, 200, 100), (120, 12, 45),  (45, 12, 120), (0, 100, 200), (100,100,0), (0, 200, 0)]
culoare = -1
timer_level = 0
level = 1

w=False
a=False
s=False
d=False
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
def traiectorie(pozitieA,pozitieB):
    xPozitieA,yPozitieA=pozitieA
    xPozitieB,yPozitieB=pozitieB
    vecDirectieX = xPozitieA - xPozitieB
    vecDirectieY = yPozitieA - yPozitieB
    unghiRad = m.atan2(vecDirectieY, vecDirectieX)
    return unghiRad

def movement(viteza, trajectory, x, y):
    x += m.cos(trajectory)*viteza
    y += m.sin(trajectory)*viteza
    return x,y

def cel_mai_apropiat(x, y):
    x_bun = 500
    y_bun = 500
    minim = (cords_list_m[0][0] - x)**2 + (cords_list_m[0][1]-y)**2
    for i in range(len(cords_list_m)):
        val = (cords_list_m[i][0]-x)**2 + (cords_list_m[i][1]-y)**2
        if (val < minim):
            minim = val
            x_bun = cords_list_m[i][0]
            y_bun = cords_list_m[i][1]
    return x_bun, y_bun

def verifica_daca_am_mancat(x,y,raza):
    for i in range(len(cords_list_m)):
        if (cords_list_m[i][0] - x)**2 + (cords_list_m[i][1] - y)**2 < raza**2: 
            cords_list_m[i][0] = r.randint(0, HEIGHT)
            cords_list_m[i][1] = r.randint(0, HEIGHT)
            return m.sqrt(raza*raza+cords_list_m[i][3]*cords_list_m[i][3])
    return 0

def verifica_schimbari(caz, viteza, rad, timp_suprema):
    if caz == 1:
        viteza += 0.1
        timp_suprema=0
    if caz == 2:
        rad += 10
    if caz == 3:
        rad -= 10
    return timp_suprema, viteza, rad


while running:
    score_caption = myFont.render("Score:", 1, (0,0,0))
    ScoreDisplay = myFont.render(str(scor), 1, (0,0,0))
    window.blit(score_caption, (HEIGHT-100, 20))
    window.blit(ScoreDisplay, (HEIGHT-100, 40))

    x,y = movement(viteza, traiectorie(p.mouse.get_pos(),(x,y)), x, y)
    if rad < raza_adversar:
        x_adversar, y_adversar = movement(viteza_adversar, traiectorie((x, y), (x_adversar,  y_adversar)), x_adversar, y_adversar)
    else:
        #print(cel_mai_apropiat(x_adversar, y_adversar))
        x_adversar, y_adversar = movement(viteza_adversar, traiectorie(cel_mai_apropiat(x_adversar, y_adversar), (x_adversar,  y_adversar)), x_adversar, y_adversar)

    
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

    if(x_suprema - x)**2 + (y_suprema - y)**2 < rad**2:
        x_suprema = r.randint(0, HEIGHT)
        y_suprema = r.randint(0, HEIGHT)
        caz = r.randint(1,3)
    
    timp_suprema, viteza, rad = verifica_schimbari(caz,viteza,rad, timp_suprema)   
    caz = 0
    timp_suprema+=1
    if timp_suprema == 2000 :
        viteza  = 1

    if (x_adversar - x)**2 + (y_adversar - y)**2 < (raza_adversar+rad)**2:
        if(raza_adversar < rad):
            rad+=5
            scor+=20
            raza_adversar+=10
            eat_adversar += 1
            x_adversar = r.randint(0, HEIGHT)
            y_adversar = r.randint(0, HEIGHT)
        else:
            running = False
            
            print('ai pierdut')

    ############  VERIFICAM DACA AU FOST MANCATE MANCARURI
    ai_a_mancat = verifica_daca_am_mancat(x_adversar, y_adversar, raza_adversar)
    if ai_a_mancat:
        raza_adversar = ai_a_mancat
    
    am_mancat =verifica_daca_am_mancat(x,y,rad)
    if(am_mancat):
        rad = am_mancat 
        scor+=1

    #verificam daca am trecut la nivelul urmator
    if not eat_adversar % 5 and eat_adversar:
        while timer_level < 1000:
            level_caption = myFont.render("LEVEL:", 1, (0,0,0))
            leveldisplay = myFont.render(str(level)+"completed", 1, (0,0,0))
            window.blit(level_caption, (HEIGHT/2, HEIGHT/2))
            window.blit(leveldisplay, (HEIGHT/2, HEIGHT/2 + 20))
            timer_level += 1
            p.display.update()
        timer_level = 0
        rad = 20
        eat_adversar = 0
        raza_adversar = 15
        viteza_adversar += 0.2
        culoare+=1  
        background_color = culori_background[culoare]
        background_color_adversar = culori_background[culoare+1]
        level+=1



    ########### DESENAM PE ECRAN
    for i in range (len(cords_list_m)):
        p.draw.circle(window,cords_list_m[i][2], (cords_list_m[i][0],cords_list_m[i][1]),cords_list_m[i][3])
    p.draw.circle(window,(255, 0, 0), (x_rosu, y_rosu), 15 )
    if suprema_culoare==3:
        p.draw.circle(window,(255, 0, 0), (x_suprema, y_suprema), 15 )
        suprema_culoare=1
    elif suprema_culoare==2:
        p.draw.circle(window,(0, 255, 0), (x_suprema, y_suprema), 15 )
        suprema_culoare+=1
    else:
        p.draw.circle(window,(0, 0, 255), (x_suprema, y_suprema), 15 )
        suprema_culoare+=1
    
    p.draw.circle(window, (0, 201, 167), (x, y), rad)
    p.draw.circle(window, (170, 20, 155), (x_adversar, y_adversar), raza_adversar)
    p.display.update()
    
    p.display.flip()
    if raza_adversar< rad:
        window.fill(background_color)
    else:
        window.fill(background_color_adversar)

p.quit()
print("Scorul tau este " + str(scor))
