## Name: Glenn Smartt
## Date: 2/20/2024
## Title: Module 2 Python Assignment Number 2 Part 2
## Summary: The first function reads if the last 5 chracters are a valid zip code and will write to 
##  the new function a zip code without a zip code. This version is made as stand alone file and not
##  for the field calculator.
## File: M2_Assignment2_P2.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import arcpy

def change_address_2():
    ## Location of the table that we are acessing
    coffee_path = r"C:\Users\Glenn\Documents\GIS\EWU_School\GEOS_471\M2_Assignment_2\ArcPy3DATA.gdb\Cheney_Coffee_Places_Copy"
    ## Declaration of Valid Zipcodes
    valid_zips = ["99004","99001","99022","99224"]
   
    ## Creation of the new field
    arcpy.management.AddField(coffee_path,"NewAddress","TEXT")
    change_fields = ["StreetName","NewAddress"]
    
    ## UpdateCursor used to read the old field and write to the new field
    with arcpy.da.UpdateCursor(coffee_path,change_fields) as cursor:
        ## Iteration through every row in the table
        for row in cursor:
            new_address = row[0]

            # Isolation of the last 5 chars of the inputted address
            l5_zip = new_address[-5:]
            ## If Statement to check if the last 5 chracters of a string are a valid zip
            ##  If True the string is updated and the 5 characters of the string are removed.
            if l5_zip in valid_zips:
                new_address = new_address[:-6]
            row[1] = new_address
            ## Edits to row are written to the table
            cursor.updateRow(row)

## Function call to test function's functionality
change_address_2()
