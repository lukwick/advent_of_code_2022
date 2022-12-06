
## Define functions which I am going to reuse for each exercise

import csv

def open_data(filename):
    """Opens data input file. Returns input data as a list with integers."""
    
    # Open file as csv file
    with open(filename,"r") as file:
        csvfile = csv.reader(file)

        # Create input list
        input_data = list()
        for line in csvfile:
            input_data.append(line)

        # Adjust list into list with integers
        adjusted_input_data = list()
        for input in input_data:
            try:
                adjusted_input_data.append(int(input[0]))
            except IndexError:
                adjusted_input_data.append(int(0))
                
    return adjusted_input_data