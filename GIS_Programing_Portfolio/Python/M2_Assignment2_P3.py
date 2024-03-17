## Name: Glenn Smartt
## Date: 2/20/2024
## Title: Module 2 Python Assignment Number 2 Part 3
## Summary: File loads open a file and reads what the values in each row of a table using to 
##  calculate the average for each of the 3 field in the dataset. Using the calculated average the 
##  function then iterates through the table again and compares the value of each entry to the 
##  average, writing to new fields in the table that represent the value in the field relative to
##  the average as strings/
## File: M2_Assignment2_P3.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import arcpy

def table_summarize():
    ## Location of the table that we are summarizing
    sum_table = r"C:\Users\Glenn\Documents\GIS\EWU_School\GEOS_471\M2_Assignment_2\ArcPy3DATA.gdb\MustSummarize"
    ## Intergers for calculating the different averages
    avgG = 0.0
    avgS = 0.0
    avgN = 0.0
    count = 0
    ## SearchCursor is used to iterate through every row in the table and grabs the values from 
    ##  each row, being used to total each field while also totalling the number of entries in the
    ##  table.
    with arcpy.da.SearchCursor(sum_table,"*") as cursor:
        for row in cursor:
            avgG = avgG + row[3]
            avgS = avgS + row[4]
            avgN = avgN + row[5]
            count = count+1

    ## Using the row totals and the count the average of each row field is calculated.
    avgG = avgG/count
    avgS = avgS/count
    avgN = avgN/count

    ## Now that the average for the 3 fields are known we create new fields to write to in the table
    arcpy.management.AddField(sum_table,"AveGold","TEXT")
    arcpy.management.AddField(sum_table,"AveSilver","TEXT")
    arcpy.management.AddField(sum_table,"AveNickel","TEXT")

    ## Set the UpdateCursor to Access the old fields and the newly created ones. 
    change_fields = ["Gold","Silver","Nickel","AveGold","AveSilver","AveNickel"]
    with arcpy.da.UpdateCursor(sum_table,change_fields) as cursor:
        ## Interating through every value in the table
        for row in cursor:
            ## Compares the Average to the 'Gold' field for each row and write to the coresponding 
            ##  Text field to describe the value relative to the average either 'Greater', 'Lesser'
            ##  or 'Equal'
            if row[0]>avgG:
                row[3] = "Greater"
            elif row[0]<avgG:
                row[3] = "Lesser"
            else:
                row[3] = "Equal"
            ## Compares the Average to the 'Silver' field for each row and write to the coresponding 
            ##  Text field to describe the value relative to the average either 'Greater', 'Lesser'
            ##  or 'Equal'
            if row[1]>avgG:
                row[4] = "Greater"
            elif row[1]<avgG:
                row[4] = "Lesser"
            else:
                row[4] = "Equal"
            ## Compares the Average to the 'Nickel' field for each row and write to the coresponding 
            ##  Text field to describe the value relative to the average either 'Greater', 'Lesser'
            ##  or 'Equal'
            if row[2]>avgG:
                row[5] = "Greater"
            elif row[2]<avgG:
                row[5] = "Lesser"
            else:
                row[5] = "Equal"
            cursor.updateRow(row)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

            
## Function call to test function's functionality
table_summarize()            
            




    
