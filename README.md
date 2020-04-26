# Futoshiki Validator
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/shradhatyagi11/futoshiki) 

# There are three main components of this project 

## Futoshiki_solver.py : 
  contains driver code and main method
## validators.py : 
  contains all the validations
## models.json : 
  contains different models of different grid size and sample solution to those models
  
## Executing Code :
  To execute the code you can either fork this repo or download complete solution and run futoshiki_solver.py
  
  Alternatively you can also visit [![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/shradhatyagi11/futoshiki)  to open virtual workspace   and execute code on GitPod.
  
  Execute <b><i><u>pip install numpy</i></u></b> on gitpod terminal to download required dependencies.

## Adding new Models or Grid Sizes: 
  To add new models make an entry in models.json, code will randomly pick any model of chosen grid size and will present it     end user.

## Algorithm:
    1) User has the option to choose the grid size
    2) Depending upon user's choice, models are fetched from models.json and displayed for the user to solve
    3) User enters the solution as input
    4) User input is validated for length
    5) User input is validated for digits (should be between 1 and grid length)
    6) User Input is validated for repeated digits in row and column (property of Sudoku)
    7) If all the above validations pass, grid cell constraints are evaluated
    8) Upon successful evaluation of constraints, user values are substituted in model and displayed to user
    9) If any validation fails, message is displayed and option is given to the user to try again or display the correct solution.

## Test Cases:
   Grid Sizes of 4x4 and 5x5 are added in the models.json.
   Below you can find the puzzles and their correspinding solutions:
   
    4*4:
    
    Model_1:
    _ _>_ _
           
    _ _>_ _
      ^    
    _>_ _ _
          ^
    _ _ _ _
    
    Solution: 1432321443212143
    
    Model_2:
    _>_ _ _
           
    _>_ _ _
    ^      
    _<_ _>_
           
    _ _ _ _
    
    Solution: 4312213434211243
    
    Model_3:
    _ _ _ _
    v     v
    _ _ _ _
        ^  
    _ _ _ _
           
    _ _>_<_
    
    Solution: 4213243131421324
    
    
    5*5:
    
    Model_1:
    _>_ _ _ _
            ^
    _>_ _ _ _
      ^ ^   ^
    _>_ _ _ _
             
    _ _ _ _>_
          v v
    _ _ _ _ _
    
    Solution: 2154332154432151543254321
    
    Model_2:
    _ _ _ _<_
        v    
    _ _>_ _ _
    v       ^
    _ _<_ _ _
            ^
    _<_ _ _ _
        ^   ^
    _ _ _ _ _
    
    Solution: 4132554231134522514332514
    
    Model_3:
    _<_ _<_ _
            v
    _ _ _>_ _
      ^      
    _ _ _ _ _
    ^ v      
    _ _ _<_ _
    ^   v    
    _<_ _ _ _
    
    
    Solution: 3412552413135422135445231
    
    
    
