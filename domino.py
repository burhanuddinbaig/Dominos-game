class domino: 
    def __init__(self, t):
        self.t = t
        self.left = self.left()
        self.right = self.right()
    """
        t is a tuple (left,right) containing the left and right values
    """

    def left(self):
        return self.t[0]

    def right(self):
        return self.t[1]

    def invert(self):
        tmp1 = self.t[0]
        tmp2 = self.t[1]

        return domino((tmp2, tmp1))

    def __str__(self):
        return "[{0}|{1}]".format(self.t[0], self.t[1])

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.t[0] == other[1] or (self.t[0] == other[0] and self.t[1] == other[1])
        else:
            return self.t[0] == other.t[1] or (self.t[0] == other.t[0] and self.t[1] == other.t[1])
        # return True if the two dominos, self and other, have the same
        # values even if self is the 'mirror' of the other

    def __contains__(self,n):
        return self.t[1] == n or self.t[0] == n
        # return True if n is equal to either left or right


    ### IGNORE ###

    """ def left(self):
        # return the "left" domino value
        self.p = list(self.p)
        left= self.p[0]
        return left
    

    def right(self):
        # return the "right" domino value
        self.p = list(self.p)
        right = self.p[1]
        return right

    def invert(self):
        # return a new domino with left, right swapped
        
        self.p = list(self.p) #new instance?*
        self.p[0], self.p[1] = self.p[1], self.p[0] 
 
        self.p= (self.p[0], self.p[1]) #DOUBLE CHECK/ REVIEW**
        return self.p

    def __str__(self):
        # return a string representation of the domino
        return "[{}|{}]".format(self.p[0], self.p[1])

    def __eq__(self, other):
        # return True if the two dominos, self and other, have the same
        # values even if self is the 'mirror' of the other
        
        if (self.left == other.left() or other.right()) and (self.right == other.right or other.left) :
            return True 
        else: return False 

    def __contains__(self,n):
        # return True if n is equal to either left or right
        for x in self.p:
            if x == n:
                return True 
            else: return False 

#test
# game1= domino((4, 5))
# d3= game1.invert()
# #print(game1.__str__()) #REVIEW  why is there no left attribute after inverted  
# #print(str(game1))
# print(d3.left()) """