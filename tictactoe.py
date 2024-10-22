import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constantes
LARGEUR, HAUTEUR = 300, 300
TAILLE_CASE = LARGEUR // 3
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Création de la fenêtre
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tic Tac Toe")

# Initialisation de la police
police = pygame.font.Font(None, 36)

# Fonction pour réinitialiser la grille
def reinitialiser_grille():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Initialisation de la grille
grille = reinitialiser_grille()

def dessiner_grille():
    for i in range(1, 3):
        pygame.draw.line(ecran, NOIR, (i * TAILLE_CASE, 0), (i * TAILLE_CASE, HAUTEUR), 2)
        pygame.draw.line(ecran, NOIR, (0, i * TAILLE_CASE), (LARGEUR, i * TAILLE_CASE), 2)

def dessiner_symboles():
    for ligne in range(3):
        for colonne in range(3):
            if grille[ligne][colonne] == 'X':
                pygame.draw.line(ecran, BLEU, (colonne * TAILLE_CASE + 20, ligne * TAILLE_CASE + 20),
                                 ((colonne + 1) * TAILLE_CASE - 20, (ligne + 1) * TAILLE_CASE - 20), 3)
                pygame.draw.line(ecran, BLEU, ((colonne + 1) * TAILLE_CASE - 20, ligne * TAILLE_CASE + 20),
                                 (colonne * TAILLE_CASE + 20, (ligne + 1) * TAILLE_CASE - 20), 3)
            elif grille[ligne][colonne] == 'O':
                pygame.draw.circle(ecran, ROUGE, (colonne * TAILLE_CASE + TAILLE_CASE // 2,
                                   ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 2 - 20, 3)

def verifier_victoire():
    # Vérification des lignes et colonnes
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != ' ':
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] != ' ':
            return True
    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != ' ':
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] != ' ':
        return True
    return False

def afficher_ecran_victoire(message):
    ecran.fill(BLANC)
    texte = police.render(message, True, VERT)
    texte_rect = texte.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 30))
    ecran.blit(texte, texte_rect)
    
    rejouer_texte = police.render("Cliquez pour rejouer", True, NOIR)
    rejouer_rect = rejouer_texte.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 + 30))
    ecran.blit(rejouer_texte, rejouer_rect)
    
    pygame.display.flip()
    
    attente = True
    while attente:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                attente = False
                return True
    return False

def jeu():
    global grille
    tour = 0
    joueur = 'X'
    partie_terminee = False

    while True:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evenement.type == pygame.MOUSEBUTTONDOWN and not partie_terminee:
                x, y = pygame.mouse.get_pos()
                colonne, ligne = x // TAILLE_CASE, y // TAILLE_CASE
                
                if grille[ligne][colonne] == ' ':
                    grille[ligne][colonne] = joueur
                    tour += 1
                    
                    if verifier_victoire():
                        if afficher_ecran_victoire(f"Le joueur {joueur} a gagné!"):
                            grille = reinitialiser_grille()
                            tour = 0
                            joueur = 'X'
                        else:
                            return
                    elif tour == 9:
                        if afficher_ecran_victoire("Match nul!"):
                            grille = reinitialiser_grille()
                            tour = 0
                            joueur = 'X'
                        else:
                            return
                    else:
                        joueur = 'O' if joueur == 'X' else 'X'
        
        ecran.fill(BLANC)
        dessiner_grille()
        dessiner_symboles()
        pygame.display.flip()

if __name__ == "__main__":
    jeu()
