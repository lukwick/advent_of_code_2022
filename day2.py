
import csv
from functions import export_data


# === Import Data ===
# ========================================================================

def import_data(filename): 
    with open(filename,"r") as file:
        csvfile = csv.reader(file)
        input_data = list()
        for line in csvfile:
            input_data.append(str(line[0]))       
    return input_data




# === Part One ===
# ========================================================================

def predict_score(games):

    # Scores possibilities
    scores = {
    "A Y": 2 + 6,   # A = Rock,     2 = Y = Paper,      6 = Won
    "A X": 1 + 3,
    "A Z": 3 + 0,
    "B Y": 2 + 3,
    "B X": 1 + 0,   # B = Paper,    1 = X = Rock,       0 = Loss
    "B Z": 3 + 6,
    "C Y": 2 + 0,
    "C X": 1 + 6,
    "C Z": 3 + 3    # C = Scissors, 3 = Z = Scissors,   3 = Draw
    }
    
    total_score = 0

    # Loop through all games
    for game in games:

        # Add score according to dict
        total_score += scores[game]

    return total_score


export_data("day2", "1.0:", predict_score(import_data("day2_input_example.txt")))
export_data("day2", "1.1:", predict_score(import_data("day2_input.txt")))




# === Part Two ===
# ========================================================================

def predict_score2(games):

    # Basically the exact same code
    # Adjusted only the scores dict

    scores = {
    "A Y": 3 + 1,   # A = Rock,     Y = Draw = 3,   Rock = 1
    "A X": 0 + 3,   # Scissors = 3
    "A Z": 6 + 2,   # Paper = 2 
    "B Y": 3 + 2,
    "B X": 0 + 1,   # B = Paper,    X = Loss = 0,   Rock = 1
    "B Z": 6 + 3,
    "C Y": 3 + 3,
    "C X": 0 + 2,
    "C Z": 6 + 1    # C = Scissors, Z = Win = 6,    Rock = 1
    }
    
    total_score = 0

    for game in games:
        total_score += scores[game]

    return total_score

export_data("day2", "2.0:", predict_score2(import_data("day2_input_example.txt")))
export_data("day2", "2.1:", predict_score2(import_data("day2_input.txt")))