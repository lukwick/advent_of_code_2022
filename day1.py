
import csv
from functions import export_data


# Import Data
# ========================================================================

def open_data(filename):
    with open(filename,"r") as file:
        csvfile = csv.reader(file)
        input_data = []
        for line in csvfile:
            try: 
                input_data.append(int(line[0]))
            except IndexError:
                input_data.append(int(0))        
    return input_data




# Part One
# ========================================================================

def count_calories(data_list):

    # Keep track of the calories and calories bags
    bag = 0
    bag_list = []

    # Loop through each elf
    for calories in data_list:
        if calories > 0:
            bag += calories
        else:
            bag_list.append(bag)
            bag_list.sort()
            bag = 0
    
    # Check also the last remaining elf
    bag_list.append(bag)
    bag_list.sort()
    
    # Return highest value in list
    return bag_list[-1]


export_data("day1", "1.0:", count_calories(open_data("day1_input_example.txt")))
export_data("day1", "1.1:", count_calories(open_data("day1_input.txt")))




# Part Two
# ========================================================================

def count_calories2(data_list):

    # Keep track of the calories and calories bags
    bag = 0
    bag_list = []

     # Loop through each elf
    for calories in data_list:
        if calories > 0:
            bag += calories
        else:
            bag_list.append(bag)
            bag_list.sort()
            bag = 0
    
    # Check also the last remaining elf
    bag_list.append(bag)
    bag_list.sort()
    
    # Return the sum of the three highest values in list
    return sum(bag_list[-3:])


export_data("day1", "2.0", count_calories2(open_data("day1_input_example.txt")))
export_data("day1", "2.1", count_calories2(open_data("day1_input.txt")))