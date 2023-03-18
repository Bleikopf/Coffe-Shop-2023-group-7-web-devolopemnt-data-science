import pandas as pd
import geopandas as gpd


df1 = gpd.read_file("C:/PythonTechLabs-Project/coffeeshop_market_insights.geojson")


df1['Stadtbezirk'] = df1['Stadtbezirk'].astype('object')

df2 = pd.read_csv("C:\PythonTechLabs-Project\Mietpreise.csv")


merged_df = df1.merge(df2, on="Stadtteil Name")

merged_df.to_file("C:/PythonTechLabs-Project/merged_data.geojson", driver="GeoJSON")

data = gpd.read_file("C:\PythonTechLabs-Project\merged_data.geojson")
data['Mietpreis'] = data['Mietpreis'] / 100

data.to_file('C:\PythonTechLabs-Project\merged_data.geojson', driver='GeoJSON')


