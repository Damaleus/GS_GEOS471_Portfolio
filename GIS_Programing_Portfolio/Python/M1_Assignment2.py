## Name: Glenn Smartt
## Date: 1/29/2024
## Title: Module 1 Python Assignment Number 2
## Summary: Produce python code to complete the provided tasks
## File: M1_Assignment_2.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Task #1: Create a variable named ForestType that contains the value “Deciduous.” Print out the
##  3rd character of that variable.
ForestType = "Deciduous."
print(ForestType[2])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Task #2: Create a variable called ZIP with the value ‘99004-2013’ Find and print out the length
##  of that string.
ZIP = '99004-2013'
print(len(ZIP))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Task #3: If ZIP (from Question #2) was larger than 5, store only the first 5 digits in a new
##  variable called ZIP5.
if len(ZIP) > 5:
    ZIP5 = ZIP[0:5]
    print(ZIP5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Task #4: Make a list that includes [‘Spokane’,’Cheney’,’Medical Lake’]. Convert the list to all
##  upper case. Print it out.
tList = ['Spokane','Cheney','Medical Lake']
x=0
while x < len(tList):
    tList[x]=tList[x].upper()
    x+=1
print(tList)
