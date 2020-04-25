import json
import random

import numpy as np
import validators as validate


###
# Driver Code
# Steps Followed :
#   1) USER INPUT: User got the option of choosing grid size
#   2) Depending upon user's choice models are fetched from models.json and present in front of user to solve
#   3) USER INPUT: User enters the solution
#   4) User input is validated for length
#   5) User input is validated for digits (should be between 1 and grid length)
#   6) User Input is validated for repeated digits in row and column (property of Sudoku)
#   7) If all the above validations are passed user input is validated for cell constraints of Futoshiki
#   8) Upon successful validation of constraints, user values are substituted in model and displayed to user
#   9) If any validation is failed. Failure message is displayed and option is given to user to see solution.
###

def main():
    game_level = int(input("Welcome to Futoshiki! Choose the grid size:\n 1. 4*4 \n 2. 5*5 \n(1/2) : "))

    if game_level == 1:
        grid = '4*4'
    elif game_level == 2:
        grid = '5*5'
    else:
        print("Wrong Option.")
        return

    # Load models from Json file
    with open('models.json') as json_file:
        loaded_json = json.load(json_file)

    num_of_models = loaded_json[grid]['num_of_models']
    selected_model = 'model_' + str(random.randint(1, num_of_models))

    model = loaded_json[grid]['models'][selected_model]
    puzzle_size = loaded_json[grid]['puzzle_size']
    grid_length = loaded_json[grid]['grid_length']
    sum_result = (puzzle_size * (puzzle_size + 1)) / 2

    print("\nBelow is your puzzle :\n")
    print(model.replace('.', ' '))

    input_string = input("\nTake your time and submit your solution. \n"
                         "If your answer is \n1 2 3 4\n2 3 4 1\n2 4 3 1\n1 2 3 4\n"
                         "Please enter as 1234234124311234\n"
                         "Your Answer : ")

    if process_input(input_string, puzzle_size, grid_length, sum_result, model):
        print("Futoshiki Solved")
    else:
        try_again = 'y'
        while try_again == 'y':
            try_again = input("Try Again?Y/N : ").lower()
            if try_again == 'y':
                input_string = input("Your Answer : ")
                if process_input(input_string, puzzle_size, grid_length, sum_result, model):
                    print("Futoshiki Solved")
                    try_again = 'n'
            else:
                print("Below is the correct solution:\n")
                process_input(loaded_json[grid]['solutions'][selected_model], puzzle_size, grid_length, sum_result,
                              model)


def process_input(input_string, puzzle_size, grid_length, sum_result, model):
    if len(input_string) != puzzle_size * puzzle_size:
        print("Wrong solution. Please provide " + str(puzzle_size * puzzle_size) + " digits")
    else:
        is_solution_valid = False
        input_string = list(input_string)
        if validate.check_if_valid(input_string, puzzle_size):
            solution = np.reshape(input_string, (puzzle_size, puzzle_size))
            solution.astype(int)
            # print(solution)
            is_solution_valid = validate.validate_for_duplicate_values(solution, sum_result)
            if is_solution_valid:
                is_solution_valid = validate.validate_futoshiki(solution, grid_length, model)
            else:
                print("Rows and Columns have duplicate values. Solution Invalid.")
        return is_solution_valid


if __name__ == "__main__":
    main()
