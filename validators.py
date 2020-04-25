###
# validate digits entered by user
# @param: user_input (input provided by user)
# @param: puzzle_size (depending on choice made by user)
# @return: true or false depending on validation
###
def check_if_valid(user_input, puzzle_size):
    for x in user_input:
        if int(x) < 1 or int(x) > puzzle_size:
            print("Wrong solution. Input digits should be in a range of 1-" + str(puzzle_size))
            return False
    return True


###
# validates if any digit is repeated in solution entered by user either
# in row or in column (property of Sudoku)
# @param: user_solution (input provided by user)
# @param: sum_result (depending on choice made by user)
# @return: true or false depending on validation
###
def validate_for_duplicate_values(user_solution, sum_result):
    rows = len(user_solution)
    cols = len(user_solution[0])
    unique_values_rows = set()
    unique_values_col = set()
    valid = True
    for i in range(rows):
        for j in range(cols):
            unique_values_rows.add(int(user_solution[i][j]))
            unique_values_col.add(int(user_solution[j][i]))

        if sum(unique_values_rows) != sum_result or sum(unique_values_col) != sum_result:
            print("Wrong Input. Values are repeating.")
            valid = False
            break
        else:
            unique_values_rows.clear()
            unique_values_col.clear()
    return valid


###
# validates the constraint on different columns present in model
# in row or in column (property of Sudoku)
# @param: user_solution (input provided by user)
# @param: grid_length (defined in models.json, depending upon choice made by user)
# @param: model (random model picked up from models.json)
# @return: true or false depending on validation
###
def validate_futoshiki(user_solution, grid_length, model):
    rows = len(user_solution)
    cols = len(user_solution[0])
    for i in range(rows):
        for j in range(cols):
            model = model.replace('_', user_solution[i][j], 1)
    print(model.replace('.', ' '))
    model = model.replace('\n', '')
    model = list(model)

    for pos in range(len(model)):
        if model[pos] in ('>', '<'):
            expr = model[pos - 1] + model[pos] + model[pos + 1]
            if not eval(expr):
                print("Expression: " + expr + " resulted false. Invalid Solution")
                return False
        elif model[pos] == '^':
            expr = (model[pos - grid_length] + '<' + model[pos + grid_length])
            if not eval(expr):
                print("Expression: " + expr + " resulted false. Invalid Solution")
                return False
        elif model[pos] == 'v':
            expr = (model[pos - grid_length] + '>' + model[pos + grid_length])
            if not eval(expr):
                print("Expression: " + expr + " resulted false. Invalid Solution")
                return False
    return True
