POINTSADJACENTS = 5
POINTSD2 = 10
POINTTRIANGLE = 15
POINTSBLOCK = 15

tableau = []
joueur = 1
for i in range(11):
    tableau.append([0] * 11)

coupsDispo = []

for x,y in coupsDispo:
    value = 0
    nbAdjacents = nbAdjacentsAlly(x,y)
    value +=  nbAdjacents * POINTSADJACENTS
    if nbAdjacents == 3 and triangle(x,y):
        value += POINTTRIANGLE




def nbAdjacentsAlly(x,y):
    nb = 0
    for i in range(x-1,x+1):
        for j in range(y-1,y+1):
            if j!=i and tableau[i][j] and isLegal(i,j) == joueur: nb+=1
    return nb

def nbAdjacentsEnemy(x,y):
    nb = 0
    for i in range(x-1,x+1):
        for j in range(y-1,y+1):
            if j!=i and tableau[i][j] and isLegal(i,j) == -joueur: nb+=1
    return nb

def triangle(x,y):
    if x in range(1,9) and y in range(1,9):
        if (tableau[x-1][y+1] == joueur and tableau[x][y-1] == joueur and tableau[x+1][y] == joueur)\
        or (tableau[x-1][y] == joueur and tableau[x][y+1] == joueur and tableau[x+1][y-1] == joueur):
            return true
    else : return false

def opposite(x,y):
    #todo
    pass

def isLegal(x,y):
    if x in range(0,10) and y in range(0,10):
        return true
    else : return false