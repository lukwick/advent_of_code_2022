
import csv
from functions import export_data


# Import Data
def open_data(filename):
    with open(filename,"r") as file:
        csvfile = csv.reader(file)
        input_data = list()
        for line in csvfile:
            try: 
                input_data.append(int(line[0]))
            except IndexError:
                input_data.append(int(0))        
    return input_data


# Part One
def calories_counter1(data_list):

    # Create counter variables
    calories_temp = 0
    calories_leader = 0

    # Loop through calories list
    for calories in data_list:  

        # Add calories to temp variable  
        calories_temp += calories

        # If no calories are found, stop counting
        if calories == 0:
            
            # Check if temp calories are greater than current calories leader
            if calories_temp > calories_leader:
                
                # If so, replace leader
                calories_leader = calories_temp
            
            # Reset calories temp variable
            calories_temp = 0
    
    # After loop, check if the last calories group is relevant.
    if calories_temp > calories_leader:
        calories_leader = calories_temp

    # Return result
    return calories_leader

export_data("day1", "w", "1.0", calories_counter1(open_data("day1_input_example.txt")))
export_data("day1", "a", "1.1", calories_counter1(open_data("day1_input.txt")))


# Part Two
def calories_counter2(data_list):
    
    # Create counter variables
    top3_elves = [0, 0, 0]
    calories_temp = 0

    # Loop through calories list
    for calories in data_list:  

        # Add calories to temp variable      
        calories_temp += calories

        # If no calories are found, stop counting
        if calories == 0:
            
            # Check if temp calories are bigger than smallest value in top3 list
            if calories_temp > top3_elves[0]:

                # If so, replace first/smallest value with temp calories
                top3_elves[0] = calories_temp

                # Sort list, so that first position is the smallest again
                top3_elves.sort()

            # Reset counter variable    
            calories_temp = 0

    # After loop, check if the last calories group is relevant.
    if calories_temp > top3_elves[0]:
        top3_elves[0] = calories_temp

    # Return result
    return top3_elves, sum(top3_elves)


export_data("day1", "a", "2.0", calories_counter2(open_data("day1_input_example.txt")))
export_data("day1", "a", "2.1", calories_counter2(open_data("day1_input.txt")))