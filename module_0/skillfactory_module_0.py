import numpy as np


def score_game(game_core):
    """Run the game 1000 times to find out how fast the game guesses the number"""

    count_ls = []
    np.random.seed(1)  # Set RANDOM SEED, so that your experiment can be replicated

    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))

    print(f"Your algorithm guesses the number in mean of {score} attempts")
    return score


def game_core_v3(number):
    """First set any random number. Then by comparing it with our
    "unknown" number, sets upper and lower limits for next random number"""

    count = 1
    lower_limit = 1
    upper_limit = 101

    predict = np.random.randint(lower_limit, upper_limit)
    while number != predict:
        count += 1
        if number > predict:
            lower_limit = predict
        elif number < predict:
            upper_limit = predict
        predict = np.random.randint(lower_limit, upper_limit)

    return count  # Out of loop, if it guessed

score_game(game_core_v3)