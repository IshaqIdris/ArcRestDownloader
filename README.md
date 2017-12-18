# ArcRestDownloader
ArcRestDownloader.py README
============================

The ArcRestDownloader.py will download feature data from a feature service URL into a new Geo database. This feature service URL has to be changed to the desired feature you are wanting to get the data from. 

**READ THE IMPLEMENTATION COMMENTS**

NOTE: The ArcRestDownloader creates a new empty Geo Database to put the features in however this can be disregarded very easily in the program by commenting out the geo database code and changing the output path to anywhere of your choosing.

To get the feature service url:
- log into arcgis.com
- click -> content 
- scroll down till you find your desired project
- open the project
- click the desired feature that you want captured 
- click feature url
- copy the url all the way to the end of "/Feature Service"

To choose what date to dowload feature clas data from :
- open the "LastDate.txt" file
- change the date in the file to desired date
NOTE: Make sure date is in exact format as required (mm/dd/yyyy) and also DO NOT change anything else in the file
