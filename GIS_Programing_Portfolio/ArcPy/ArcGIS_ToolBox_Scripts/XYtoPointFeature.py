## Name: Glenn Smartt
## Date: 2/20/2024
## Title: X Y to Point Feature
## Summary: This is an arcpy script that accepts a table, a feature name, a spatial reference
##  (optional), and a output workspace (optional). Using those inputs the script creates a point
##  feature-class the table using X and Y coordinates in the table. The spatial reference currently
##  will default to the current maps if none is given and the output workspace will the be the
##  projects default geo-database 
## File: XYtoPointFeature.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import arcpy
import os

## A non-exhaustive list of names for the X Y of each point in a table might be using.
lat_list = ["y","Y","Lat","Latitude","LATITUDE","latitude","y_coordinate","Y_coordinate","y_coord",
            "Y_coord",]
long_list = ["x","X","Long","LONG","long","Longitude","LONGITUDE","longitude","x_coordinate",
             "X_coordinate","x_coord","X_coord",]

## Current work space is loaded to be used to populate the default value for the optional inputs
aprx = arcpy.mp.ArcGISProject("CURRENT")
theMap = aprx.activeMap

## To ensure that the user only inputs a table the Toolbox is set up to only accept table objects
##  which is fetched using GetParameter as a Table Object
in_table = arcpy.GetParameter(0)

## Fetching of the inputs name for the feature
feature_name = arcpy.GetParameterAsText(1)

## Check if a space is used in the input feature name and attempts to remove the space from the
##  string. Might be worth expanding to check other invalid characters for feature names. Using it
##  a dictionary of valid/invalid chars.
if ' ' in feature_name:
    arcpy.AddMessage("Invalid name detected attemping to fix.")
    feature_name=feature_name.replace(' ','')

## Fetching of the spatial reference selected by the user, if none is selected the program will
##  default to the spatial refernce of current map.
spatial_reference = arcpy.GetParameter(2)
if spatial_reference == "":
    arcpy.AddMessage("No spatial refrence selected by user,")
    arcpy.AddMessage("current maps spatial reference was selected as the default.")
    spatial_reference = theMap.spatialReference

## Fetching of the specified output location selected by the user, if none is selected the script
##  will default to the default geodatabase of the current project.
out_work_space = arcpy.GetParameter(3)
if out_work_space == None:
    arcpy.AddMessage("No output workspace selected by user, "+
                      "current projects default geodatabase was selected as the default.")
    out_work_space = aprx.defaultGeodatabase

## Creation of new feature class based off the inputs  
arcpy.AddMessage("Creating New Feature Class!")
table2 = arcpy.management.CreateFeatureclass(out_work_space, feature_name, "POINT", in_table,
        "DISABLED","DISABLED",spatial_reference.name)
out_table_desc = arcpy.Describe(table2)
out_path = out_table_desc.path+'\\'+out_table_desc.name

## Using the Describe object to get the names of the tables fields and writing those fields to a
## list so we can have a generate name of all the fields 
in_table_desc = arcpy.Describe(in_table)
in_fields = []
for field in in_table_desc.fields:
    in_fields.append(field.name)

## This section is a little complicated, What the bellow code does is check every value in the list
##  of fields names against a predefined set of possible field names for X and Y values and will
##  display a message to indicate if two x and y fields are found. If a field with an appropriate
##  nmae is not found script will try with default values. 
field_find = 0
x_index = 1
y_index = 2
len_index = 0
long_index = 0
## Loop to find Y Coordiante Field
while len_index < len(in_fields):
    if in_fields[len_index] in lat_list:
        y_index = len_index
        field_find = field_find+1
    len_index=len_index+1
## Loop to find X Coordiante Field
while long_index < len(in_fields):
    if in_fields[long_index] in long_list:
        x_index = long_index
        field_find = field_find+1
    long_index=long_index+1
## Check if the the two sets of Field Indices have been found
if field_find != 2:
    arcpy.AddMessage("Script unable locate X & Y Values! Attemping with default values.")
else:
    arcpy.AddMessage("Script located X & Y Values!")

## The fields for the out put are the same as the input with the addition of Geometry fields so,
##  a list of fields that are a copy of the orginal tables field is made to be used with the
##  InsertCursor to add the original tables data as well as geometry data. A copy be made because
##  Just using = will make two variables pointing to the same list. 
out_fields = in_fields.copy()
## Appending the Geometry field to the list copy
out_fields.append("SHAPE@X")
out_fields.append("SHAPE@Y")
## Using the SearchCursor we can interate through every row in the original table
with arcpy.da.SearchCursor(in_table, in_fields) as s_cursor:
    for row in s_cursor:
        ## We create a list for what we want to input into the new feature class's table
        insert_list = []
        ## We grab every item for the current row and add to the that list
        for item in row:
            insert_list.append(item)
        ## We then append the values that represent the X and Y Geometry Postion of the points to
        ##  the end of the list where we insert the GEOMETRY field to the output field list
        insert_list.append(row[x_index])     
        insert_list.append(row[y_index])
        #We access the InsertCursor to add new features to the output feature class       
        with arcpy.da.InsertCursor(out_path, out_fields)as i_cursor:
            ## The Inerset Cursor can accept a tuple of values for what you want to insert so the
            ##  list we created for what we want to insert to the new feature class is casted as a
            ##  tuple and is then inserted into the new row.
            i_cursor.insertRow(tuple(insert_list))

theMap.addDataFromPath(out_path)
## Script Completion Message
arcpy.AddMessage("Finished without crashing!")
