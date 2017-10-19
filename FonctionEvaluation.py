POINTSADJACENTS = 5
POINTSD2 = 10
POINTTRIANGLE = 15
POINTSOPPOSITE = 15

def fonctionEvaluation(x,y,plateau,joueur):
    value = 0

    nbAdjacentsAlly = nbAdjacents(x,y,plateau,joueur)
    value += nbAdjacentsAlly * 5
    if nbAdjacentsAlly == 3 and triangle(x,y,plateau,joueur):
        value += 10
    if nbAdjacentsAlly == 2 and opposite(x,y,plateau,joueur):
        value += 10

    nbAdjacentsEnemy = nbAdjacents(x,y,tableau,-joueur)
    if nbAdjacentsEnemy == 2 and opposite(x,y,plateau,-joueur):
        value += 15
    if nbAdjacentsEnemy == 3 and opposite(x, y , plateau , -joueur):
        value += 15

    return value

def nbAdjacents(x,y,tableau,joueur):
    nb = 0
    for i in range(x-1,x+1):
        for j in range(y-1,y+1):
            if j!=i and tableau[i][j] and isLegal(i,j) == joueur: nb+=1
    return nb

def triangle(x,y,tableau,joueur):
    if x in range(1,10) and y in range(1,10):
        if (tableau[x-1][y+1] == joueur and tableau[x][y-1] == joueur and tableau[x+1][y] == joueur)\
        or (tableau[x-1][y] == joueur and tableau[x][y+1] == joueur and tableau[x+1][y-1] == joueur):
            return true
    else : return false

def opposite(x,y,tableau,joueur):
    if x in  range(1,10) and y in range(1,10):
        if (tableau[x][y-1] == joueur and tableau[x][y+1] == joueur)\
        or (tableau[x-1][y] == joueur and tableau[x+1][y] == joueur) \
        or (tableau[x-1][y+1] == joueur and tableau[x+1][y-1] == joueur):
            return true


def isLegal(x,y):
    if x in range(0,11) and y in range(0,11):
        return true
    else : return false