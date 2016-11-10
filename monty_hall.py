import random


def placeprize():
    behind_doors = [6, 7, 8]
    random.shuffle(behind_doors)
    truth = []
    for item in behind_doors:
        if item == 6:
            truth.append('Big_Prize')
        elif item == 7:
            truth.append('Goat')
        elif item == 8:
            truth.append('Goat')
    return truth


def player_choice():
    choiceA = random.randint(1, 3)
    return choiceA


def host_take(trueplace, firstchoice):
    if firstchoice == 1:
        if trueplace[0] == 'Big_Prize':
            picks = random.randint(2, 3)
            return picks
        elif trueplace[1] == 'Big_Prize':
            return 3
        elif trueplace[2] == 'Big_Prize':
            return 2
    elif firstchoice == 2:
        if trueplace[0] == 'Big_Prize':
            return 3
        elif trueplace[1] == 'Big_Prize':
            dice = random.choice([1, 3])
            return dice
        elif trueplace[2] == 'Big_Prize':
            return 1
    elif firstchoice == 3:
        if trueplace[0] == 'Big_Prize':
            return 2
        elif trueplace[1] == 'Big_Prize':
            return 1
        elif trueplace[2] == 'Big_Prize':
            card = random.randint(1, 2)
            return card


def swap_or_stay(strategy, firstdoorchosen, hosts):
    if strategy == 'stay':
        return firstdoorchosen
    elif strategy == 'swap':
        list1 = [1, 2, 3]
        list1.remove(firstdoorchosen)
        list1.remove(hosts)
        new_door = sum(list1)
        return new_door
    else:
        list4 = [1, 2, 3]
        list4.remove(hosts)
        new_door2 = random.choice(list4)
        return new_door2


def wins(secondchoice, locationprize):
    if locationprize[0] == 'Big_Prize':
        if secondchoice == 1:
            return 1
        else:
            return 0
    elif locationprize[1] == 'Big_Prize':
        if secondchoice == 2:
            return 1
        else:
            return 0
    elif locationprize[2] == 'Big_Prize':
        if secondchoice == 3:
            return 1
        else:
            return 0


def choice_of_three(decision):
    answer = placeprize()
    door_pick = player_choice()
    minus_door = host_take(answer, door_pick)
    what_to_do = decision
    door_pick2 = swap_or_stay(what_to_do, door_pick, minus_door)
    finale = wins(door_pick2, answer)
    return finale


def main():
    print("The results of 1000 rounds when you stay with your initial choice:")
    static = 'stay'
    tests1 = 0
    win_count1 = []
    while tests1 < 1000:
        result1 = choice_of_three(static)
        win_count1.append(result1)
        tests1 += 1
    wins_for_stay = sum(win_count1)
    print("Staying leads to {} wins".format(wins_for_stay))
    print("The results of 1000 rounds when you swap from your initial choice:")
    flip = 'swap'
    tests2 = 0
    win_count2 = []
    while tests2 < 1000:
        result2 = choice_of_three(flip)
        win_count2.append(result2)
        tests2 += 1
    wins_for_swap = sum(win_count2)
    print("Swaping leads to {} wins".format(wins_for_swap))
    print("The results of 1000 goes when you randomly decide the final door:")
    loose_guess = 'randomly'
    tests3 = 0
    win_count3 = []
    while tests3 < 1000:
        result3 = choice_of_three(loose_guess)
        win_count3.append(result3)
        tests3 += 1
    wins_for_random = sum(win_count3)
    print("A second random choice leads to {} wins".format(wins_for_random))
    percent_stay = (wins_for_stay/10)
    percent_swap = (wins_for_swap/10)
    percent_randomly = (wins_for_random/10)
    print("""The strategy of consistently swapping resulted in {} percent wins,
    while the strategy of randomly choosing a second time was a bit lower with
    {} percent wins, and the strategy of staying resulted in only {} percent
    wins.""".format(percent_swap, percent_randomly, percent_stay))


if __name__ == "__main__":
    main()
