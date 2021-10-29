class board:
    bd = []
    def __init__(self):
        self.bd = []
        """
        create an empty board
        """

    def empty(self):
        return len(self.bd) <= 0

        """
        return True if the board is empty
        """

    def left(self):
        return self.bd[0]
        """
        return the value on the left of the board (or None for an empty board)
        """

    def right(self):
        return self.bd[len(self.bd)-1]
        """
        return the value on the right of the board (or None)
        """

    def play(self, d, r):
        if r:
            self.bd.append(d)
        else:
            self.bd.insert(0, d)
        """
        play a domino on the right (True) or left
        invert the tile if necessary when inserting in the board
        return True if the play was completed
        """
    def __str__(self):
        tmp = ','.join(map(str, self.bd))
        return '[' + tmp + ']'
    #    return "Board have {0} dominies".format(len(self.bd))

    def __len__(self):
        return len(self.bd)
        """
        Return a string representation of board.  Must match
        the examples in the handout.
        """