from random import choice
from tqdm import tqdm


TRIALS = 10**6
DOORS = ["A","B","C"]


def doors_normal(prize, doors=DOORS):
    """
    If door removing not happens.
    returns True for a win, False for a lose
    """
    selected = choice(doors)
    return True if selected==prize else False


def door_no_change(prize, doors=DOORS):
    """
    If same door is selected after door removal.
    returns True for a win, False for a lose
    """
    drs = doors.copy()
    selected = choice(drs)
    temp = [prize, selected]   
    drs.remove(choice([d for d in drs if d not in temp]))
    return True if selected==prize else False


def door_change(prize, doors=DOORS):
    """
    If door is changed after door removal.
    returns True for a win, False for a lose
    """
    drs = doors.copy()
    selected = choice(drs)
    temp = [prize, selected]
    drs.remove(choice([d for d in drs if d not in temp]))
    selected = [d for d in drs if d != selected][0]
    return True if selected==prize else False


def experiment(doors=DOORS, trials=TRIALS, ):
    """
    Empirical proof to Month Hall problem. Three different
    possible conditions are compared and results are returned.

    doors -> list: a list of door names
    trials -> int: total trial amount

    total -> int: current amount of trials
    win_normal -> int: amount of wins without door removal - control
    win_no_change -> int: amount of wins with door removal without door change
    win_change -> int: amount of wins with door removal and door change
    """
    total, win_normal, win_no_change, win_change = 0, 0, 0, 0
    for i in tqdm(range(trials)):
        prize = choice(doors)
        total += 1
        win_normal += doors_normal(prize)
        win_no_change += door_no_change(prize)
        win_change += door_change(prize)
    return total, win_normal, win_no_change, win_change

    
if __name__=="__main__":
    total, win_normal, win_no_change, win_change = experiment()

    print(f"\ntotal: {total}\twin_normal: {win_normal}\tratio: {(win_normal*100)/total}%")
    print(f"total: {total}\twin_no_change: {win_no_change}\tratio: {(win_no_change*100)/total}%")
    print(f"total: {total}\twin_change: {win_change}\tratio: {(win_change*100)/total}%")
