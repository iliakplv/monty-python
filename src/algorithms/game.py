from random import random

# Simulation of a random game with variable win ratio

prizes_left = 3000
iterations = 10
games_per_iter = 1000  # TODO this might be variable
win_ratio = 1  # updated every iteration


def play():
    return random() <= win_ratio


for iter in range(0, iterations):
    iterations_left = iterations - iter
    win_ratio = prizes_left / (games_per_iter * iterations_left)
    prizes_won = 0

    for game in range(0, games_per_iter):
        game_won = play()
        if game_won:
            prizes_won += 1
            prizes_left -= 1

    print(f"Iter: {iter}, Prizes won: {prizes_won}, Prizes left: {prizes_left}, \tWin ratio: {win_ratio}")
