## Name: Glenn Smartt
## Date: 02/06/2024 
## Title: Module 2 Python Assignment Number 1 Part 1
## Summary: First Exploration into using ArcGIS Specific python modules to do both basic python and
##  Arcgis Specific tasks with sample GIS Data. This file is a transcript of python console inputs
##  and outputs with # representing console outputs
## File: M2_Assignment1_P1.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Loading the of the current project as a an objects and accessing the project's inherent
##  attributes to dissect what we are able to access and interact with within the classes that
##  arcpy has for GIS objects. Additionally, we use iterators and print() to get an idea of how 
##  arcpy and ArcGIS store and treat the layers/data we use in it.
aprx = arcpy.mp.ArcGISProject("CURRENT")
theMap = aprx.activeMap
theLayers = theMap.listLayers()

for eachlayer in theLayers:
    print(eachlayer.name)
# NationalRegisterHistoricPoints_PVP
# PVPSites
# World Topographic Map
# World Hillshade
    
thisLayer = theLayers[1]
thisLayer.name
# 'PVPSites'

thisLayer.dataSource
#'C:\\Users\\Glenn\\Documents\\GIS\\EWU_School\\GEOS_471\\M2_Assignment_1\\ArcPy_1_Dataset.gdb\\PVPSites'

thisLayer.transparency
# 0.0

thisLayer.isFeatureLayer
# True

## Comment "Did the wrong command here but I left it in.
PVPFields = arcpy.ListFields(thisLayer)
for iField in PVPFields:
    print(iField)
# <geoprocessing describe field object object at 0x000001C1A3C800D0>
# <geoprocessing describe field object object at 0x000001C1A3C80690>
# <geoprocessing describe field object object at 0x000001C1A3C801D0>
# <geoprocessing describe field object object at 0x000001C1A3C80E90>
# <geoprocessing describe field object object at 0x000001C1A3C80DB0>
# <geoprocessing describe field object object at 0x000001C1A3C80C50>
    
for iField in PVPFields:
    print(iField.name)
# OBJECTID
# Shape
# Name
# YearOpen
# Shape_Length
# Shape_Area
