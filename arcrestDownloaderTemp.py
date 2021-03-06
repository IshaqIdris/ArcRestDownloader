"""This program is for downloading Feature service files from arcgis.com with a query of choice"""
"""READ THE README BEFORE USE"""

from arcrest.manageorg import Administration
from arcrest import AGOLTokenSecurityHandler
from arcrest.agol import FeatureService
from arcrest.common.filters import LayerDefinitionFilter
import datetime
import os

def download_features(fs_url, date, out_path):
    
    #creates a empty GDB
    arcpy.workspace = cwd 
    out_folder_path = cwd + '/Shapefiles'
    out_name = "test.gdb"
    arcpy.CreateFileGDB_management(out_folder_path, out_name)
    print ("Creating a empty GDB....")
    
    '''downloads a hosted service features into a feature class'''
    agol_securityHandler = AGOLTokenSecurityHandler('Username','Password','http://company.maps.arcgis.com/')
    agol_org_obj = Administration(securityHandler=agol_securityHandler,initialize=True)

    fs = FeatureService(url=fs_url,securityHandler=agol_securityHandler,initialize=True)

    ldf = LayerDefinitionFilter()

    #CHANGE CONDITION AFTER THE "and" TO QUERY SOMETHING ELSE OTHER THAN DATE
    #e.g. "ref='EBN_BDP_006_TAP'"
    #Date format mm/dd/yyyy
    ldf.addFilter(0, where="1=1" and "date> date\'" + date + "\'")
    print ("Querying data....")
    print (fs.query(layerDefsFilter=ldf,returnCountOnly=True))

    queryResults = fs.query(layerDefsFilter=ldf,returnCountOnly=False,returnGeometry=True)
    result = queryResults[0].save(r'in_memory','SampleCities')
    print ("Saved results....")
    arcpy.CopyFeatures_management(result,out_path)
    print ("Features exported")
    print ("All done!")

print("Welcome to the ArcRestDownloader!")
print("Please make sure you have added a valid date in the LastDate.txt")

#Read through text file for date filter and file counter
print("Reading LastDate.txt....")
f = open('C:/Users/ishaq.idris/Documents/Shapefiles/LastDate.txt', 'r')
f.readline()    #skip line
date = f.readline()
print("Only downloading data from " + date + "onwards....")
f.readline()    #skip line
counter = f.readline() #ONLY USED FOR FILE NAMING PUSPOSES

now = datetime.datetime.now()

#Output folder CHANGE THIS TO DESIRED DESTINATION OF FILES
folder = "Documents/Shapefiles/{0}{1}{2}_{3}f/".format(now.year, "0"*(2-len(str(now.month)))+str(now.month), "0"*(2-len(str(now.day)))+str(now.day), counter)
if not os.path.isdir(folder):
    print("Making output folder at " + folder + "....")
    os.makedirs(folder)
f.close()

#update counter
lines = open('LastDate.txt', 'r').readlines()
print ("length " + str(len(lines)))
counter = int(counter) + 1
print("Counter incremented....")
lines[len(lines)-1] = str(counter)
open('LastDate.txt', 'w').writelines(lines)
f.close()

#CHANGE THE VALUE IN QUOTATIONS TO CHANGE OUTPUT FILES NAME
cwd = os.getcwd() #gets current working directory of this python file(not required)
out_path = folder + 'test.gdb/shapes'

#This is the feature service URL CHANGE THIS TO THE DESIRED FEATURE SERVICE URL
fs_url = r'https://services.arcgis.com/FeatureServer'

download_features(fs_url, date, out_path)
