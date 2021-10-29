import random
import domino
import hand

def test_domino():
    d1 = domino.domino((1, 3))
    d2 = domino.domino((2, 3))
    d3 = d1.invert()
    assert(d1 == d3)
    assert(d1 != d2)
    assert(str(d1) == '[1|3]')
    assert(str(d2) == '[2|3]')
    assert(str(d3) == '[3|1]')
    assert(d1.left == d3.right)
    assert(d1.right == d3.left)
    assert(d1.right == d2.right)
    assert(3 in d1)
    assert(1 in d1)
    assert(not 4 in d1)
    print("test_domino PASSED")

def test_hand():
    l = []
    for i in range(4):
        for j in range(3, 4):
            l.append(domino.domino((i, j)))
    h = hand.hand(l, 'test')
    assert(h.has_a(3))
    assert(not h.has_a(6))
    assert(str(h) == '[[0|3],[1|3],[2|3],[3|3]]')
    assert(l[2] in h)
    assert(l[2].invert() in h)
    assert(not (domino.domino((1, 5)) in h))
    assert(h.points() == 18)
    h.play(l[2])
    assert(str(h) == '[[0|3],[1|3],[3|3]]')
    assert(len(h) == 3)
    print("test_hand PASSED")

def test_board():
    # NOTE: You can add additional tests but will not be graded
    pass

def test_game():
    # NOTE: You can add additional tests but will not be graded
    pass

def main():
    test_domino()
    test_hand()
    test_board()
    test_game()

if __name__ == '__main__':
    main()