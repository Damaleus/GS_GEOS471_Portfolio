## Name: Glenn Smartt
## Date: 2/20/2024
## Title: Module 2 Python Assignment Number 2 Part 1
## Summary: These are functions for the field calculator that have been copied out into its own .py
##  file.
##  The first function reads if the last 5 chracters are a valid zip code and will write to the new
##   function a zip code without a zip code.
##  The second function use the given categorization schema which has been turned into a list of 
##    of tuples containing a list and a string. The Function interates through each tuple in the  
##    list checks if the given input string and checks if it matchs a list item, if it does the 
##    Function returns the associated string.
## File: Arcpy_List_Functions.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def change_address(i_address):
    #Declaration of return variable that defaults to the inputted address and will
    #changed if zip is found and extracted
    new_address = i_address
    #Isolation of the last 5 chars of the inputted address
    l5_zip = i_address[-5:]
    #Declaration of Valid Zipcodes
    valid_zips = ["99004","99001","99022","99224"]
    #checks if last 5 chars is in list of valid address
    if l5_zip in valid_zips:
        new_address =i_address[:-6]
    return new_address
        
def test_change_address():
#Test of Function: test_change_address()
    print("Testing change_address()")
    test1 = "48 Simpson Pkwy 99004"
    final_addr = change_address(test1)
    print("Input: "+test1)
    print("Output: "+final_addr)

def assign_r_category(i_resource):
    # Declare and assign the return variable as the catch-all/default value
    a_category = "other"
    # Declare a list of tuples representing the categories
    # Index 0 of the tuple is the list of key words associated with a category
    # Index 1 of the tuple is the category name 
    r_categories = [(["Auditorium", "Club", "Ranch", "Villa"],"Gathering Place"),
                    (["School"],"Education"), (["Church", "Chapel"],"Religious"),
                    (["Battery", "Barracks", "S. S."],"Military"),
                    (["House", "Apartments", "Residence"],"Residential")]
    # Loop that navigates through every category in the list
    for t_key in r_categories:
         # Loop that navigates through every keyword in a category
        for key_cat in t_key[0]:
            #if statement to check if keyword is in the inputed resource string
            if key_cat in i_resource:
                #if keyword is in the string the category is set
                a_category = t_key[1]
    return a_category            

def test_assign_r_category():
    #Test of Function: test_assign_r_category()
    print("Testing assign_r_category()")
    test1 = "Auditorium"
    result1 = assign_r_category(test1)
    print("Input 1: "+test1)
    print("Output 1: "+result1)
    test2 = "Second Church of Christ Scientist"
    result2 = assign_r_category(test2)
    print("Input 2: "+test2)
    print("Output 2: "+result2)


## Function calls to test functions' functionality
test_change_address()
test_assign_r_category()
