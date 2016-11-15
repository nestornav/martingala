from random import randrange

def contains(val, set):
    if val in set:
        return True
    else:
        return False

def isPair(val):
    if val % 2 == 0:
        return True
    else:
        return False

def play_color(gamble, toss):
    red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
    black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
     
    if contains(toss, red):
        print ('red', toss)
        return = 'red'
    elif contains(toss, black):
        print ('black', toss)
        return = 'black'
    else:
        print ('none', toss)
        return = 'none'

def play_nones(gamble, runs):
    pass

def get_statistics():
    pass

def do_play(game, gamble, runs, budget):

    current_budget = budget
    max_bet = 500
    min_bet = 2
    bet = min_bet
    tosses = 0
    loose = 0
    
    for toss in runs:
        tosses += 1
        bet = bet * 2

        if current_budget >= bet || bet > max_bet:

            if game == 'color':
                played = play_color(toss)

                if not played ==  gamble:
                    loose += 1
                    current_budget = current_budget - bet
                else:
                    return 'win'
                
            elif game == 'none':
                play_nones(gamble, toss)
        else:
            print('broken')
            return 'lost'

if __name__ ==  '__main__':
    runs = [randrange(0, 36) for i in range(0, 30)]
    budget = 1000

    print(runs)
    
    do_play(game, gamble, runs, budget)
