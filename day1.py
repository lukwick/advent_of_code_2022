

from functions import open_data


# Task 1
def calories_counter1(input_data):

    calories_temp = 0
    calories_leader = 0

    for calories in input_data:    
        calories_temp += calories
        if calories == 0:
            if calories_temp > calories_leader:
                calories_leader = calories_temp
            calories_temp = 0

    print(calories_leader)

calories_counter1(open_data("day1_input_example.txt"))
# 24000 is correct
calories_counter1(open_data("day1_input.txt"))
# 70296 is correct



# Task 2
def calories_counter2(input_data):
    
    top3_elves = [0, 0, 0]
    calories_temp = 0

    for calories in input_data:        
        if calories > 0:
            calories_temp += calories

        if calories == 0:
            if calories_temp > top3_elves[0]:
                top3_elves[0] = calories_temp
                top3_elves.sort()
            calories_temp = 0
    if calories_temp > top3_elves[0]:
                top3_elves[0] = calories_temp

    print(top3_elves, top3_elves[0] + top3_elves[1] + top3_elves[2])

calories_counter2(open_data("day1_input_example.txt"))
# 45000 is correct
calories_counter2(open_data("day1_input.txt"))
# 205381 is correct