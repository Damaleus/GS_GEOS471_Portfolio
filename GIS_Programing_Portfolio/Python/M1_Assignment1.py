## Name: Glenn Smartt
## Date: 1/22/2024
## Title: Module 1 Python Assignment Number 1
## Summary: This python files contains the log of python commands given to the python console to
##  demonstarate the functionality available using python. Single '#' represent console outputs.
## File: M1_Assignment1.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Example of String declaration and the print() function.
myMap = "Cheney"
MyMap = "Spokane"
print(myMap)
# Cheney
print(MyMap)
# Spokane


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Examples of using basic conditionals and boolean values.
GISisGREAT = True
if GISisGREAT:
    Greeting = "Hello GIS World"
else:
    Greeting = 12**2
print(Greeting)
# Hello GIS World

## Comment: "The previous code but reversed"
GISisGREAT = True
if GISisGREAT:
    Greeting = 12**2
else:
    Greeting = "Hello GIS World"
print(Greeting)
# 144

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Examples of using declaring ints/floats, using basic arithmetic operators and utilizing them with
##  ore complext print statements.
x=3
y=4
Temp = 43.4
sum = x + y + 15
TempCel = (Temp - 32)*(5/9)
print('The sum is ',sum)
print(Temp,"converted to C is ", TempCel)
# The sum is  22
# 43.4 converted to C is  6.333333333333333

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Examples of strings being used with array indexing to create substrings and fetch and evaluate
##  index values using comparitors
software = "ArcGIS Pro"+" 2.9"
version = software[11:14]
FirstLetter = software[0]
if FirstLetter == '2':
    print('Using version', version)
print(FirstLetter)
# A

## Comment: "The text as written does not actually print the version of the game because the first
## character of software is used instead of the version.I adjust the command statements to complete
## so that it complete in the way I believe is intended."
software = "ArcGIS Pro"+" 2.9"
version = software[11:14]
FirstLetter = version[0]
if FirstLetter == '2':
    print('Using version', version)
# Using version 2.9
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Example of Python's list and list indexs to fetch values stored with in the list as well as using
##  the len() function to determin the number items contained within the list.
mapList = ['Wetlands','Geology','Streams']
LastMap = mapList[2]
print(LastMap)
total = len(mapList)
print('There are',total,'maps in the collection')
# Streams
# There are 3 maps in the collection

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Example of using additionally conditionals to add more conditionals that are resolved linearly.
if version == "2.9":
    print("You are doomed")
elif version == "2.8":
    print("You might be okay")
else:
    print("It's probabaly just fine")
# You are doomed
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Example of a while loop using print() to make repeat statement demonstrating the repeat iteration
##  of code that is present within the loop until the Boolean requirement is resolved.
GISisGREAT = True
count = 0
while GISisGREAT:
    print("still in loop")
    count = count +1
    if count > 10:
        GISisGREAT=False
# still in loop
# still in loop
# still in loop
# still in loop
# still in loop
# still in loop
# still in loop
# still in loop
# still in loop
# still in loop
# still in loop

