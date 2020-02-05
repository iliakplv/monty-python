from random import random
from random import randint


# Simulation of a random game with variable win ratio


def play(win_ratio):
    return random() <= win_ratio


def simulate():
    prizes_left = 3000
    iterations = 10
    games_per_iter_min = 800
    games_per_iter_max = 1200
    games_per_iter_predicted = (games_per_iter_min + games_per_iter_max) / 2

    for iter in range(0, iterations):
        iterations_left = iterations - iter
        win_ratio = prizes_left / (games_per_iter_predicted * iterations_left)
        prizes_won = 0
        games = randint(games_per_iter_min, games_per_iter_max)

        for game in range(0, games):
            game_won = play(win_ratio)
            if game_won:
                prizes_won += 1
                prizes_left -= 1

        print(f"Iter: {iter:2} | Games: {games:4} | Prizes won: {prizes_won:3} | Prizes left: {prizes_left:4} | Win ratio: {win_ratio}")


if __name__ == '__main__':
    simulate()
