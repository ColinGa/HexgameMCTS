
class Noeud(object):
    def __init__(self, noeudParent, x, y, value):
        self.x = x
        self.y = y
        self.value = value

        self.parent = noeudParent
        self.children = []

        self.GetChildren()

    def Growth(self):
        pass

    def GetChildren(self):
        pass

    def GetFullTree(self):
        if self.parent is not None:
            return self.parent.getFullTree() + " " + self.ToString()
        else:
            return self.ToString()

    def ToString(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.value)
