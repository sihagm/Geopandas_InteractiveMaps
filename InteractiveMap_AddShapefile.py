import geopandas as gpd
import folium

#function to create a html
def embed_map(m, file_name):
        from IPython.display import IFrame
        m.save(file_name)
        return IFrame(file_name, width='100%', height='500px')
    # Show the map
    

#read in the shp file
tiles_10km = gpd.read_file("D:/PythonScripts/test/ch_10km.shp")
#convert it to wgs84
tiles_10km_wgs=tiles_10km.to_crs(epsg=4326)
tiles_10km_wgs.head()



#basemaps
m = folium.Map(location=[46.86,8.28], tiles='openstreetmap', zoom_start=9)
folium.TileLayer(tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', attr="<a ref</a>").add_to(m)
folium.TileLayer('stamenterrain', attr="<a ref</a>").add_to(m)
folium.TileLayer('cartodbpositron', attr="<a ref</a>").add_to(m)

#draw the shp into the basemap
for _, r in tiles_10km_wgs.iterrows():
    sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {"fillColor": "orange"})
    folium.Popup(r["CELLCODE"]).add_to(geo_j)
    geo_j.add_to(m)
m


# Create a layer control panel and add it to our map instance
folium.LayerControl().add_to(m)

#write the html    
embed_map(m, 'q_1.html')