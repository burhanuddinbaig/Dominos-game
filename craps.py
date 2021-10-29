##craps
import random as rn

l1 = [7, 11]
l2 = [2, 3, 12]
l3 = [4,5,6,8,9,10]
### PROBLEM 2
def craps():
    i = 1
    lst_sum = 0
    res = ''
    status = True
    while status:
        d1 = rn.randint(1, 6)
        d2 = rn.randint(1, 6)
        sum = d1 + d2

        if i == 1:
            lst_sum = sum

            if lst_sum in l1:
                res = 'WINS'
                status = False                                      #to break loop
            elif lst_sum in l2:
                res = 'LOSES'
                status = False                                      #to break loop
        if sum == lst_sum and i > 1:
            res = 'WINS'
            status = False                                      
        elif sum == 7 and i > 1:
            res = 'LOSES'
            status = False                                      
        elif status:
            res = 'roll again'
        print('{0}: {1} {2}'.format(i, sum, res))
        
        i+=1

    """if you dont get a sum 7/11 on the first try or 
     match your first sum before rolling a 7 , you LOSE""" 

for num_of_games in range(5):
    print(f"Game {num_of_games} begins.")
    craps()
    print(f"Game {num_of_games} ends.\n")