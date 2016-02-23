# This script adds XY data (coordinates) from an Excel or text file. It then exports the events file to a new shapefile,
# and reprojects the shapefile into the UTM NAD 83 Zone 15N projection.

import arcgisscripting
gp = arcgisscripting.create(9.3)
gp.OverWriteOutput = False

import arcpy

try:

		# Prepare the variables
		in_Table = getParameterAsText(0)
		SR = arcpy.GetParameter(1)
		in_x_heading = getParameterAsText(2)
		in_y_heading = getParameterAsText(3)
		out_EventsLayer = getParameterAsText(4)
		out_Shapefile = getParameterAsText(5)
		
		# Make the XY event...
		gp.MakeXYEventLayer(in_Table, in_x_heading, in_y_heading, out_EventsLayer, SR)
		print "Events layer created."
		
		# Print the total rows
		pDSC = gp.describe(out_Layer)
		print gp.getcount(out_Layer)
		
		# Save to a layer file
		gp.SaveToLayerFile(out_Layer, out_Shapefile)
		print "Shapefile created."
		
		# This section reprojects the new layer file to UTM Zone 15N
		
		# Construct the output path
		outProjectLayer = getParameterAsText(6)
		
		# Compare the spatial reference of the feature class with that of the target dataset and, if they do not match, perform the projection
		# and report what happened
		
		# Set the Toolbox
		GP.toolbox = "management"
		
		# Set the spatial reference variable
		targetSr = "C:\\Program Files\\ArcGIS\\Coordinate Systems\\Projected Coordinate Systems\\UTM\\NAD 1983\\NAD 1983 UTM Zone 15N.prj"
		
		# do the reprojection
		gp.project(out_Shapefile, outProjectLayer, targetSr, "NEAREST", "", "")
		gp.AddMessage("Projected " + outProjectLayer + " successfully. ")
		print "Projected " + outProjectLayer + " successfully. "
		
except:

	# If an error occurred, print the message to the screen
	print gp.GetMessages()