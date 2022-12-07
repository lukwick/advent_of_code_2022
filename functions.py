
## Define functions which I am going to reuse for each exercise

import csv

def open_data(filename, type):
    """Opens data input file. Returns input data as a list with the type of data you prefer. Places zeros in empty spaces."""
    
    # Open file as csv file
    with open(filename,"r") as file:
        csvfile = csv.reader(file)

        # Create input list
        input_data = list()
        for line in csvfile:
            input_data.append(line)

        # Adjust list into list with type = integers/floats/strings
        adjusted_input_data = list()
        for input in input_data:
            try:
                adjusted_input_data.append(type(input[0]))
            except IndexError:
                adjusted_input_data.append(type(0))
                
    return adjusted_input_data


def export_data(day, mode, task, result):
    """Creates data export file to save the results."""

    with open(day + "_results.txt", mode) as file:

        # Write header
        file.write(task)
        file.write("\n")

        # Write result
        file.write(str(result))
        file.write("\n")
        file.write("\n")