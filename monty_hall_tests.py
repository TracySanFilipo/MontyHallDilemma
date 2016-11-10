from monty_hall import placeprize
from monty_hall import player_choice


def test_placeprize():
    results = placeprize()
    goats = 0
    big_prizes = 0
    what = 0
    for prize in results:
        if prize == 'Goat':
            goats += 1
        elif prize == 'Big_Prize':
            big_prizes += 1
        else:
            what += 1
    assert goats == 2 and big_prizes == 1 and what == 0


def test_player_choice():
    assert 0 < player_choice() < 4
