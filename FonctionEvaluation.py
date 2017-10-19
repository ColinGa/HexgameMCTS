POINTSADJACENTS = 5
POINTSD2 = 10
POINTTRIANGLE = 15
POINTSBLOCK = 15

tableau = [] #plateau de jeu
joueur = 1 #id du joueur
for i in range(11):
    tableau.append([0] * 11)

coupsDispo = [] #tableau des cases vides
tableauValue = [] #tableau indiquand les valeurs pour chaque coup

for x,y in coupsDispo:
    value = 0
    nbAdjacents = nbAdjacentsAlly(x,y)
    value +=  nbAdjacents * POINTSADJACENTS
    if nbAdjacents == 3 and triangle(x,y):
        value += POINTTRIANGLE
    tableauValue.append((x,y,value))

def fonctionEvaluation(x,y,plateau,joueur):
    #todo
    pass

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
    if x in range(1,10) and y in range(1,10):
        if (tableau[x-1][y+1] == joueur and tableau[x][y-1] == joueur and tableau[x+1][y] == joueur)\
        or (tableau[x-1][y] == joueur and tableau[x][y+1] == joueur and tableau[x+1][y-1] == joueur):
            return true
    else : return false

def opposite(x,y):
    if x in  range(1,10) and y in range(1,10):
        if (tableau[x][y-1] == joueur and tableau[x][y+1] == joueur)\
        or (tableau[x-1][y] == joueur and tableau[x+1][y] == joueur) \
        or (tableau[x-1][y+1] == joueur and tableau[x+1][y-1] == joueur):
            return true


def isLegal(x,y):
    if x in range(0,11) and y in range(0,11):
        return true
    else : return false