import folium
import rasterio as rio

#function to create a html
def embed_map(m, file_name):
        from IPython.display import IFrame
        m.save(file_name)
        return IFrame(file_name, width='100%', height='500px')


#Add the geotiff
#image has to be a geotiff and in EPSG= 4326 (wgs84)  
with rio.open('D:/PythonScripts/test/test.tif') as src: 
    img = src.read()
    min_lon, min_lat, max_lon, max_lat = src.bounds    
    


#basemaps
m = folium.Map(location=[46.677,9.675], tiles='openstreetmap', zoom_start=14)
folium.TileLayer(tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', attr="<a ref</a>").add_to(m)
folium.TileLayer('stamenterrain', attr="<a ref</a>").add_to(m)
folium.TileLayer('cartodbpositron', attr="<a ref</a>").add_to(m)

m.add_child(folium.raster_layers.ImageOverlay(
    name="Viadukt",
    image=img.transpose(1, 2, 0),
    bounds = [[min_lat, min_lon], [max_lat, max_lon]],
    opacity=1,
    interactive=True,
    cross_origin=False,
    zindex=1,
    ))
m


# Create a layer control panel and add it to our map instance
folium.LayerControl().add_to(m)


#create the htlm  
embed_map(m, 'q_2.html')