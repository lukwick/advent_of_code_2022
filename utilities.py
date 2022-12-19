
## Define functions which I am going to reuse for each exercise

def export_data(day, task, result):
    """Creates data export file to save the results."""

    with open(f"{day}/results.txt", "w" if task == "1.0:" else "a") as file:

        # Write header
        file.write(task)
        file.write("\n")

        # Write result
        file.write(str(result))
        file.write("\n")
        file.write("\n")