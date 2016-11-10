# h1 MontyHallDilemma

## h5 monty_hall.py
This file contains code to simulate the Monty Hall Dilemma. It is currently set
to be run as a file without user inputs. User inputs could be substituted into
the player_choice and swap_or_stay functions to make a game. As it is, the code
will run the main functions 1000 times for each of the three strategies. The
first strategy is staying with the initial choice, the second is always switching
and the third is to make a second random choice between the two remaining doors.
Each of these three strategies is set up to be run in the main function in a
while loop. To alter the number of times each of these is used, simply change
the terms of the while loop (eg. to run the stay strategy 15 times, change the
while loop to read "while test# < 15")

##h5 monty_hall_tests.py
This file contains two tests that could be run on two of the functions in the
main file.
