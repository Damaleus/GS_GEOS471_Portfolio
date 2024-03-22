## Name: Glenn Smartt
## Date: 02/06/2024 
## Title: Module 2 Python Assignment Number 1 Part 2
## Summary: Definition of 2 Functions that can be called in the field calculator to complete 
##  complete the given instructions using the provided sample 
## File: Arcpy_Basic_Functions.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Name: find_era():
## Inputs: interger year value for a features  
## Outputs: string that is the corresponding phase of the inputted feature.
## Functionality: Function that uses the features year field to calculate what phase the that
##  feature is from given the provided era classification schema.
def find_era(year):
    new_era = "NA"
    if year < 1950:
        new_era = "Phase One"
    elif (year >= 1950) and (year < 1990):
        new_era = "Phase Two"
    else:
        new_era = "Phase Three"
    return new_era   

## Name: gen_fullname():
## Inputs: string name of a features  
## Outputs: string that is the corresponding full name for the featyure.
## Functionality: Checks whether or not the Name starts with "Palos Verdes", If returns TRUE the
## name is unchanged, If returns False the name with "Palos Verdes" added to the front. 
## Comment: Function is specifically made obtuse in its evaluation of whether or not the inputted
##  string start with "Palos Verde" instead of just checking if the string containing "Palos Verde"
##  due the specifity of the given instructions.
def gen_fullname(name):
    fullname = name
    if fullname[0:12] != "Palos Verdes":
        fullname = "Palos Verdes " + name
    return fullname