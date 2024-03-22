#Glenn Smartt | Assignement 3 Module 2 | 2/20/2024
## Name: Glenn Smartt
## Date: 2/20/2024
## Title: Module 2 Python Assignment Number 3
## Summary: This is a function that iterates through every raster within a directory and uses a
##  sellected a polygon to clip each raster.
## File: M2_Assignment3.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import arcpy
import os

## Gets the 3 inputs from ArcGIS the clipping feature class, the directory for the raster and the
##  location for outputting the files.
clipFClass = arcpy.GetParameterAsText(0)
workspace = arcpy.GetParameterAsText(1)
outLocation = arcpy.GetParameterAsText(2)

## List is created to containe the input and output paths for the string.
inout_rasters = []

## Walk is used to itterate through all the files and the directory and compile a list of files that
## are of the type RasterDataset
walk = arcpy.da.Walk(workspace,datatype="RasterDataset")

## Using a nested for loop for the objects found by walk a tuple is appended to the list with the 
## input and output paths being the objects in the tuple.
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        inout_rasters.append((os.path.join(dirpath, filename),os.path.join(outLocation, "clipped_"+filename)))

## Update message stating the the number of raster identified by the script as well as other
## message stating the input and output files.
arcpy.AddMessage("Script has identified " + str(len(inout_rasters))+" Rasters." )
for x in inout_rasters:
    arcpy.AddMessage("Input Found: " + str(x[0]) + "!")
    arcpy.AddMessage("Output Set: " + str(x[1]) + "!")

## Counter declaration for output messages
    
## Iteration through every input using the inputted raster to clip each raster which are then
##  outputted to the selected directory.
counter = 0
for raster in inout_rasters:
    arcpy.management.Clip(raster[0],clipFClass,raster[1],clipFClass,"0","ClippingGeometry")
    counter=counter+1
    ## Update message shown for each iteration to indicate progress or the script
    arcpy.AddMessage("Finished clip Operation! " + str(counter) + " of " + str(len(inout_rasters)))

## Update message indicating the script is complete.
arcpy.AddMessage("Finished without crashing!")
