# Simulation to solve FiveThirtyEight's Riddler Classic for the week of April
# 24, 2020
# By Lily Dunk
# I recognize that this is not the most computationally efficient simulation!
# I chose to prioritize clarity over efficiency.

import random

random.seed()

# The three doors are numbered 0, 1, and 2
# You always choose door 0 originally
switch_wins = 0  # Number of times you win by switching
stay_wins = 0  # Number of times you win by staying
switch_trials = 0  # Number of trials where Monty opens a door and you decide
# to switch
stay_trials = 0  # Number of trials where Monty opens a door and you decide
# to stay
n = 1000000  # Number of loops

for i in range(n):
    # Step 1: Decide number of goats
    num_goats = random.choice(range(4))

    # Step 2: Place goats and prizes in doors
    # Goat = False, prize = True
    if num_goats == 0:
        doors = [True, True, True]
    elif num_goats == 1:
        doors = [True, True, True]
        doors[random.choice(range(3))] = False
    elif num_goats == 2:
        doors = [False, False, False]
        doors[random.choice(range(3))] = True
    else:
        doors = [False, False, False]

    # Step 3: Monty opens a door, if he can
    # You initially choose door 0

    # If both door 1 and door 2 have prizes, Monty cannot open a door
    if doors[1] and doors[2]:
        opendoor = -1
    # If both door 1 and door 2 have goats, Monty can randomly choose to open
    # either door
    elif not doors[1] and not doors[2]:
        opendoor = random.choice([1, 2])
    # Otherwise, Monty opens whichever door (1 or 2) contains a goat
    elif not doors[1]:
        opendoor = 1
    else:
        opendoor = 2

    # Step 4: Decide if you want to switch (randomly, assuming you don't know
    # which is the better option)
    switch = random.choice([True, False])

    # Step 5: If you switch, decide which door to switch to
    if opendoor == -1:
        # If Monty doesn't open a door, you can choose randomly
        switchdoor = random.choice([1, 2])
    elif opendoor == 1:
        switchdoor = 2
    else:
        switchdoor = 1

    # Step 6: Find out if you won and add this trial to the score
    # We only care about the results of the trials where Monty opens a door
    if opendoor != -1:
        if switch:
            switch_trials += 1
            if doors[switchdoor]:
                switch_wins += 1
        else:
            stay_trials += 1
            if doors[0]:
                stay_wins += 1

# After all n loops, calculate the results
print("If you switch, your chance of winning is: " + str(round(switch_wins /
                                                               switch_trials,
                                                               3)))
print("If you stay, your chance of winning is: " + str(round(stay_wins /
                                                             stay_trials, 3)))
