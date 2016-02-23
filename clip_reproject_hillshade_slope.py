# This script takes a raw elevation dataset (such as a DEM), clips it to a study area,
# creates both hillshade and slope rasters, and projects them into the
# Land Trust of Virginia's most commonly used projection.

try: 
		import arcgisscripting
		gp = arcgisscripting.create(9.3)
		gp.OverwriteOutput = True
		
		gp.workspace = "path\\to\\workspace"
		dem = "path\\to\\dem"
		
		# CLIP DEM TO STUDY AREA
		# Construct the output path
		outClipRaster = "dem_clip"
		# Perform the clip (based on lat/long values of the bottom right and top left corners of study area, though you can use other inputs) and report what happened
		gp.clip_management(dem, "-77.813 38.938 -77.957 39.002", outClipRaster)
		gp.AddMessage("Wrote clipped file " + outClipRaster + ". ")
		print "Wrote clipped file " + outClipRaster + ". "
		
		# REPROJECT CLIPPED DEM
		# Get a description for the raster
		desc = gp.Describe(outClipRaster)
		# Get the spatial reference of the raster
		sr = desc.SpatialReference
		# Construct the output path
		outProjectRaster = "dem_project"
		# Perform the reprojection and report what happened
		# Compare the spatial reference of the feature class with that of the target dataset
		# and, if they do not match, perform the reprojection and report what happened
		targetSr = "C:\\Program Files\\ArcGIS\\Coordinate Systems\\Projected Coordinate Systems\\State Plane\\NAD 1983 HARN\\NAD 1983 HARN StatePlane Virginia North FIPS 4501.prj"
		#do the reprojection
		gp.ProjectRaster_management(outClipRaster, outProjectRaster, targetSr, "NEAREST", "", "NAD_1983_To_HARN_Virginia")
		gp.AddMessage("Projected " + outProjectRaster + " successfully. ")
		print "Projected " + outProjectRaster + " successfully. "
		
		# CALCULATE SLOPE
		inSlopeRaster = "dem_project"
		outSlopeRaster = "slope"
		inMeasurementType = "PERCENT_RISE"
		
		# Check out ArcGIS Spatial Analyst extension license
		gp.CheckOutExtension("Spatial")
		
		# Process: Slope
		gp.Slope_sa(inSlopeRaster, outSlopeRaster, inMeasurementType)
		gp.AddMessage("Created slope successfully. ")
		print "Created slope successfully. "
		
		# CALCULATE HILLSHADE
		#Set local variables
		hillshadeInRaster = "slope"
		hillshadeOutRaster = "hillshade"
		
		# Check out ArcGIS Spatial Analyst extension license
		gp.CheckOutExtension("Spatial")
		
		# Process: Hillshade
		gp.Hillshade_sa(hillshadeInRaster, hillshadeOutRaster)
		gp.AddMessage("Created hillshade successfully. ")
		print "Created hillshade successfully. "
		
except:

		# Report if there was an error
		print gp.GetMessages(2)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		