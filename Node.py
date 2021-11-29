class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = None

    # def getVal(self):
    #     return self.value

    # def printVal(self):
    #     if (self.left is None):
    #         left = "None"
    #     else:
    #         left = str(self.left.getVal())

    #     if (self.right is None):
    #         right = "None"
    #     else:
    #         right = str(self.right.getVal())

    #     print("VAL:", self.value, "LEFT:", left, "RIGHT:", right)
