from random import randrange

def contains(val, set):
    if val in set:
        return True
    else:
        return False

def do_play(runs):
    red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
    black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)

    for toss in runs:
        if contains(toss, red):
            print ('red', toss)
        elif contains(toss, black):
            print ('black', toss)
        else:
            print ('none', toss)

if __name__ ==  '__main__':
    runs = [randrange(0, 36) for i in range(0, 30)]
    print(runs)
    
    do_play(runs)
