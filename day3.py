
import csv
from functions import export_data



# Import Data
# ========================================================================

def open_data(filename): 
    with open(filename,"r") as file:
        csvfile = csv.reader(file)
        input_data = list()
        for line in csvfile:
            input_data.append(str(line[0]))       
    return input_data



# Part One
# ========================================================================

def split_rucksack(rucksacks):

    splitted_rucksacks = list()

    for rucksack in rucksacks:

        # Determine rucksack length and divide it by 2
        half_rucksack = int(len(rucksack) / 2)

        # Create two lists which represent each compartment, inset them into splitted rucksacks list
        splitted_rucksacks.append([
            rucksack[:half_rucksack],
            rucksack[half_rucksack:]
            ])
    
    return splitted_rucksacks


def compare_compartment(splitted_rucksacks):

    leftover_item_list = list()

    # Loop through all rucksacks with their compartments
    for splitted_rucksack in splitted_rucksacks:

        # Loop through all items (letters) in the compartment nr.1
        for item in splitted_rucksack[0]:

            # If the same item is part of compartment nr.2, add it to the leftover item list
            if item in splitted_rucksack[1]:

                leftover_item_list.append(item)

                # If the same item is found, stop the loop
                break

    return leftover_item_list


def calculate_score(leftover_item_list):
    score = 0

    # Dict of all priority scores of each item (letter)
    scores = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52
    }

    # Add up score
    for item in leftover_item_list:
        score += scores[item]

    return score


def calculate_priority(input_data):
    
    # Merge all functions together
    return calculate_score((compare_compartment(split_rucksack(input_data))))


export_data("day3", "1.0:", calculate_priority(open_data("day3_input_example.txt")))
export_data("day3", "1.1:", calculate_priority(open_data("day3_input.txt")))



# Part Two
# ========================================================================

def group_rucksack(rucksacks):
    
    grouped_rucksacks = list()

    # Loop through every third rucksack
    for rucksack in range(0, len(rucksacks), 3):

        # Group three rucksacks together
        grouped_rucksacks.append([
            rucksacks[rucksack],
            rucksacks[rucksack + 1],
            rucksacks[rucksack + 2]
            ])
    
    # Return list with group of three rucksacks
    return grouped_rucksacks


def compare_compartment(grouped_rucksacks):

    badge_list = list()

    # Loop through each group of three rucksacks
    for group in grouped_rucksacks:

        # Loop through each item of rucksack nr. 1
        for item in group[0]:

            # Check if item appears also in rucksack nr. 2's and nr. 3's rucksack
            if item in group[1] and group[2]:

                # If so, add to the badge list
                badge_list.append(item)

                # If the unique badge is found, stop the loop
                break
                
    return badge_list


def calculate_priority_2(input_data):
    
    # Merge all functions together
    return calculate_score(compare_compartment(group_rucksack(input_data)))



export_data("day3", "2.0:", calculate_priority_2(open_data("day3_input_example.txt")))
# 70 = Correct answer

export_data("day3", "2.1:", calculate_priority_2(open_data("day3_input.txt")))
# 2719 = Wrong answer