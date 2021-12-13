# Authort: Nguyen Ngoc Lan Phuong - MSSV 19520227

import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import geopandas

data = geopandas.read_file('../Population_Ward_Level.shp')

#convert data type to epsg=4326 to visualize in map
data = data.to_crs(epsg=4326)

m = folium.Map(location=[11.2, 107.0], zoom_start=10, tiles='CartoDB positron')
for _, r in data.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j,
                           style_function=lambda x: {'fillColor': 'orange'})
    folium.Popup(r['Dist_Name']).add_to(geo_j)
    geo_j.add_to(m)

# Project to NAD83 projected crs
data = data.to_crs(epsg=2263)
 
# Access the centroid attribute of each polygon
data['centroid'] = data.centroid
 
# Project to NAD83 projected crs
data = data.to_crs(epsg=4326)
 
# Access the centroid attribute of each polygon
data['centroid'] = data.centroid
 
for _, r in data.iterrows():
    lat = r['centroid'].y
    lon = r['centroid'].x
    folium.Marker(location=[lat, lon],
                  popup='length: {} <br> area: {}'.format(r['Shape_Leng'], r['Shape_Area'])).add_to(m)