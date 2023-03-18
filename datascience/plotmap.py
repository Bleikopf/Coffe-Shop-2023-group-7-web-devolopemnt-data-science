import geopandas as gpd
import plotly.express as px
import plotly.io as pio

gdf = gpd.read_file('datascience/coffeeshop_profit.geojson')
gdf['rent'] = gdf['Mietpreis']
gdf['daily customers'] = gdf['Tägliche Kaffeetrinker']

def plot_map():
    fig = px.choropleth_mapbox(gdf, 
                        geojson = gdf.geometry, 
                        locations = gdf.index, 
                        color = 'profit',
                        color_continuous_scale=px.colors.diverging.RdYlGn, 
                        color_continuous_midpoint=0,
                        hover_name = 'Stadtteil Name',
                        hover_data = {'profit':True, 'daily customers':True, 'rent':True, 'minimum coffee price':True},
                        mapbox_style = 'carto-positron',
                        zoom = 10, 
                        center = {'lat': 51.225842, 'lon': 6.768077},
                        opacity = 0.5)

    fig.update_coloraxes(cmax=800000, cmin=-200000)  

    fig.show()  


gdf['profit'] = gdf['Profit 25m^2 & 2 employees']
gdf['minimum coffee price'] = gdf['Mindestverkaufspreis 25m^2 & 2 employees']
plot_map()
pio.write_html(fig, file='././maps/25sqm2emp.html', include_plotlyjs=False, full_html=False, div_id='plotly_map' )

gdf['profit'] = gdf['Profit 25m^2 & 4 employees']
gdf['minimum coffee price'] = gdf['Mindestverkaufspreis 25m^2 & 2 employees']
plot_map()
pio.write_html(fig, file='././maps/25sqm4emp.html', include_plotlyjs=False, full_html=False, div_id='plotly_map' )

gdf['profit'] = gdf['Profit 300m^2 & 2 employees']
gdf['minimum coffee price'] = gdf['Mindestverkaufspreis 300m^2 & 4 employees']
plot_map()
pio.write_html(fig, file='././maps/300sqm2emp.html', include_plotlyjs=False, full_html=False, div_id='plotly_map' )

gdf['profit'] = gdf['Profit 300m^2 & 4 employees']
gdf['minimum coffee price'] = gdf['Mindestverkaufspreis 300m^2 & 4 employees']
plot_map()
pio.write_html(fig, file='././maps/300sqm4emp.html', include_plotlyjs=False, full_html=False, div_id='plotly_map' )