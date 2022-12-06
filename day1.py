

from functions import open_data


# Task 1
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

    # Print result
    print(calories_leader)

calories_counter1(open_data("day1_input_example.txt"))
# 24000 is correct
calories_counter1(open_data("day1_input.txt"))
# 70296 is correct



# Task 2
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

    # Print result
    print(top3_elves, sum(top3_elves))


calories_counter2(open_data("day1_input_example.txt"))
# 45000 is correct
calories_counter2(open_data("day1_input.txt"))
# 205381 is correct