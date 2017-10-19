def fonctionEvaluation(x, y, plateau, joueur):
    value = 10  # min : 1    max : 50

    nbAdjacentsAlly = nbAdjacents(x, y, plateau, joueur)
    value += nbAdjacentsAlly * 5
    if nbAdjacentsAlly == 3 and triangle(x, y, plateau, joueur):
        value += 10
    if nbAdjacentsAlly == 2 and opposite(x, y, plateau, joueur):
        value += 8
    if already2Near(x, y, plateau, joueur):
        value -= 20

    nbAdjacentsEnemy = nbAdjacents(x, y, plateau, -joueur)
    if nbAdjacentsEnemy == 2 and opposite(x, y, plateau, -joueur):
        value += 11
    if nbAdjacentsEnemy == 3 and opposite(x, y, plateau, -joueur):
        value += 15

    if (x == 0 or x == 10) and nearBorderX(x, y, plateau, joueur):
        value += 12

    if (y == 0 or y == 10) and nearBorderY(x, y, plateau, joueur):
        value += 12

    if value < 1:
        return 1
    else:
        return value


def nbAdjacents(x, y, tableau, joueur):
    nb = 0
    for i in range(x - 1, x + 1):
        for j in range(y - 1, y + 1):
            if j != i and tableau[i][j] and isLegal(i, j) == joueur: nb += 1
    return nb


def triangle(x, y, tableau, joueur):
    if x in range(1, 10) and y in range(1, 10):
        if (tableau[x - 1][y + 1] == joueur and tableau[x][y - 1] == joueur and tableau[x + 1][y] == joueur) \
                or (tableau[x - 1][y] == joueur and tableau[x][y + 1] == joueur and tableau[x + 1][y - 1] == joueur):
            return True
    else:
        return False


def opposite(x, y, tableau, joueur):
    if x in range(1, 10) and y in range(1, 10):
        if (tableau[x][y - 1] == joueur and tableau[x][y + 1] == joueur) \
                or (tableau[x - 1][y] == joueur and tableau[x + 1][y] == joueur) \
                or (tableau[x - 1][y + 1] == joueur and tableau[x + 1][y - 1] == joueur):
            return True
    else:
        return False


def already2Near(x, y, tableau, joueur):
    if x in range(1, 10) and y in range(1, 10):
        coups = coupsAutour(x, y, tableau)
        for i in range(5):
            if coups[i] == coups[i + 1] and coups[i] == joueur:
                return True
        if coups[5] == coups[0] and coups[0] == joueur:
            return True
    return False


def isLegal(x, y):
    if x in range(0, 11) and y in range(0, 11):
        return True
    else:
        return False


def coupsAutour(x, y, tableau):
    coups = []
    if x in range(1, 10) and y in range(1, 10):
        coups.append(tableau[x][y - 1])
        coups.append(tableau[x + 1][y - 1])
        coups.append(tableau[x + 1][y])
        coups.append(tableau[x][y + 1])
        coups.append(tableau[x - 1][y + 1])
        coups.append(tableau[x - 1][y])
    return coups


def nearBorderX(x, y, tableau, joueur):
    if x == 0:
        if tableau[1][y] == joueur:
            return True

        if y > 1 and tableau[1][y - 1] == joueur:
            return True

    if x == 10:
        if tableau[9][y] == joueur:
            return True

        if y > 1 and tableau[9][y + 1] == joueur:
            return True
    return False


def nearBorderY(x, y, tableau, joueur):
    if y == 0:
        if tableau[x][1] == joueur:
            return True

        if y < 10 and tableau[x - 1][1] == joueur:
            return True

    if y == 10:
        if tableau[x][9] == joueur:
            return True

        if x < 10 and tableau[x + 1][y + 1] == joueur:
            return True
    return False
