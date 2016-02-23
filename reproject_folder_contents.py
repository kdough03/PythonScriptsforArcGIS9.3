# This script reprojects all the files in a folder to match the projection of a target dataset (in this case, the one used by the Land Trust of Virginia), 
#and skips a file if it's already in the target projection.

# Create the geoprocessor object

import arcgisscripting
gp = arcgisscripting.create(9.3)

#Setting OverWriteOutput to True allows geoprocessing tools to overwrite the output if it already exists.
gp.OverWriteOutput = 1

try:

		# Create path variables
		targetFolder = "path\\to\\target\\folder"
		targetProjectionDataset = "path\\to\\dataset\\with\\desired\\projection"
		
		# Get the spatial reference of the target dataset
		descTgtData = gp.Describe(targetProjectionDataset)
		srTgtData = descTgtData.SpatialReference
		
		#Get a list of all feature classes in the target folder
		gp.Workspace = targetFolder
		featureClassList = gp.ListFeatureClasses()
		
		# Loop through all target folder feature classes 
		for featureClass in featureClassList:
		
			# Get the name of the feature class
			desc = gp.Describe(featureClass)
			featureClassName = desc.Name
			
			# Get the spatial reference of the feature class
			sr = desc.SpatialReference
		
			# Construct the output path
			rootName = featureClassName[:-4]
			outProjectFeatureClass = targetFolder + "\\" + rootName + "_projected" + ".shp"
		
			# Compare the spatial reference of the feature class with that of the target dataset, and if they do not match,
			# perform the projection and report what happened
			if sr.Name != srTgtData.Name:
				gp.project_management(featureClass, outProjectFeatureClass, srTgtData)
				gp.AddMessage("Projected " + featureClassName + " successfully. ")	
				print "Projected " + featureClassName + " successfully. "
			else:
				# skip
				continue
				
except:

			# Report if there was an error
			print gp.GetMessages(2)