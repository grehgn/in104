import pygame
from pygame.locals import *
pygame.init()



#variable de décompte de points
#un point supplémentaire lorsqu'on clique sur le logo
points = 0


#création d'une fonte pour l'affichage du score
score_font = pygame.font.Font(None, 35)
couleur_font = (0, 0, 0) #couleur de la fonte (ici rouge)
#surface de score
score_surface = score_font.render("Score : {:6d} points".format(points), 50, couleur_font)
#rectangle de positionnement de la surface de fonte
score_rect = score_surface.get_rect()
score_rect.bottomleft = ecran_rect.bottomleft


#blit de la surface de score sur l'écran d'affichage
ecran.blit(score_surface, score_rect)
#mise à jour de l'affichage 
pygame.display.flip()



#création d'un chronometre
chrono = pygame.time.Clock() 
#declenchement du chrono
chrono.tick()

#Boucle externe d'animation
continuer = True

bonus = 0 """Marqueur permettent de gerer la durée du bonus lorsqu'on rencontre 'O'"""

while continuer:
    
    #Controle de la vitesse maximale à 300 frame par secondes
    chrono.tick(300)
    
    #boucle interne de récupération des événements
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    
    #Modification du score en fonction de ce que rencontre pacman sur le terrain 
    if pacman.tab[i][j] == 'O':
	point += 20
	bonus = 30
    if bonus > 0:
    	if pacman.tab[i][j] == 'o':
        	point += 20
    	if pacman.tab[i][j] == 'F':
		point += 100
    else:
    	if pacman.tab[i][j] == 'o':
		point += 10
    bonus -= 1              

	#modification du score
        score_surface = score_font.render("Score : {:6d} points".format(points), 1, couleur_font)
    #mise à jour des sprites
  
    #blitter le fond, le score et le logo à sa nouvelle position sur l'écran
    ecran.blit(score_surface, score_rect)
