
from common_func import open_data

def calories_counter(input_data):

    calories_temp = 0
    calories_leader = 0

    for calories in input_data:    
        calories_temp += calories
        if calories == 0:
            if calories_temp > calories_leader:
                calories_leader = calories_temp
            calories_temp = 0

    print(calories_leader)



calories_counter(open_data("day1_input_example.txt")) # 24000 is correct
calories_counter(open_data("day1_input.txt")) # 70296 is correct