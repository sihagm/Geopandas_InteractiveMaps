# Geopandas_InteractiveMaps
Create HTML-based interactive maps with Geopandas, where you can add a custom shapefile or Geotiff

Make sure you have geopandas installed - the easierst way is to download Anaconda, open the Anaconda CMD as administrator and use conda install geopandas
Then you can use Spyder to work on the anaconda-python version, where geopandas is installed
Also make sure "rasterio" and "folium" is installed

Use one of the two python scripts:

InteractiveMap_AddRaster.py
Make sure the input Geotiff is in WGS84, EPSG=4326 and that it is not bigger than ~1Gb (there is a restriction of ~300'000'000 Pixels in the html)


InteractiveMap_AddShapefile.py
Change the "CELLCODE" attribute to the name you want to be displayed for each shape and play with the symbology

