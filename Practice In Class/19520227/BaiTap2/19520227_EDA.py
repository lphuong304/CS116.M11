# Author: Nguyen Ngoc Lan Phuong - MSSV: 19520227
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas

data = geopandas.read_file('Population_Ward_Level.shp')

#Tìm phường có dân số thấp nhất, cao nhất
max_pop = data['Pop_2019'].max()
idxmax_pop = data['Pop_2019'].idxmax()
min_pop = data['Pop_2019'].min()
idxmin_pop = data['Pop_2019'].idxmin()
print('Phường có dân số cao nhất trong năm 2019 là',data['Com_Name'][idxmax_pop] , 'với số dân là: ',max_pop)
print('Phường có dân số cao nhất trong năm 2019 là',data['Com_Name'][idxmin_pop] , 'với số dân là: ',min_pop)

#Tìm phường có diện tích thấp nhất, cao nhất
max_area = data['Shape_Area'].max()
idxmax_area = data['Shape_Area'].idxmax()
min_area = data['Shape_Area'].min()
idxmin_area = data['Shape_Area'].idxmin()
print('Phường có diện tích cao nhất là',data['Com_Name'][idxmax_area] , 'với số là: ',max_area,'km2')
print('Phường có diện tích thấp nhất nhất  là',data['Com_Name'][idxmin_area] , 'với số là: ',min_area,'km2')

#Tìm phường có tốc độ tăng trưởng dân số nhanh nhất, chậm nhất (2009-2019)
data['TocDoTangTruong'] = data['Pop_2019']/data['Pop_2009']
max_tocdo = data['TocDoTangTruong'].max()
idxmax_tocdo = data['TocDoTangTruong'].idxmax()
min_tocdo = data['TocDoTangTruong'].min()
idxmin_tocdo = data['TocDoTangTruong'].idxmin()
print('Phường có tốc độ tăng trưởng cao nhất  là',data['Com_Name'][idxmax_tocdo] , 'với số là: ',max_tocdo)
print('Phường có dân số thấp nhất là',data['Com_Name'][idxmin_tocdo] , 'với số là: ',min_tocdo)

#Tìm phường có biến động thấp nhất, cao nhất
max_biendong = data['Biendong'].max()
idxmax_biendong = data['Biendong'].idxmax()
min_biendong = data['Biendong'].min()
idxmin_biendong = data['Biendong'].idxmin()
print('Phường có biến động  cao nhất  là',data['Com_Name'][idxmax_biendong] , 'với số là: ',max_biendong)
print('Phường có biến động thấp nhất là',data['Com_Name'][idxmin_biendong] , 'với số là: ',min_biendong)
data['Matdo'] = data['Pop_2019']/data['Shape_Area']

#Tìm phường có mật dộ thấp nhất, cao nhất
max_matdo = data['Matdo'].max()
idxmax_matdo = data['Matdo'].idxmax()
min_matdo = data['Matdo'].min()
idxmin_matdo = data['Matdo'].idxmin()
print('Phường có mật độ dân số  cao nhất  là',data['Com_Name'][idxmax_matdo] , 'với số là: ',max_matdo, 'số người/km2')
print('Phường có mật độ thấp nhất là',data['Com_Name'][idxmin_matdo] , 'với số là: ',min_matdo, 'số người/km2')