
## Define functions which I am going to reuse for each exercise

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