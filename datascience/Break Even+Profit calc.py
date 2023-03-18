import geopandas as gpd
data = gpd.read_file("C:/PythonTechLabs-Project/merged_data.geojson")


#1 300m^2 & 4 employees
def calculate_min_sales_price1(row):
    if row['Tägliche Kaffeetrinker'] == 0:
        return 0
    else:
        return (row['Mietpreis'] * 300 * 12 + 1.7316251692855331 * row['Tägliche Kaffeetrinker'] * 365 + (4*80000)) / (row['Tägliche Kaffeetrinker'] * 365)

def Profit1(row):
    profit = (4 - calculate_min_sales_price1(row)) * (365 * row["Tägliche Kaffeetrinker"])
    return min(profit, 10000000)  # limit profit to 1 million

data['Mindestverkaufspreis 300m^2 & 4 employees'] = data.apply(calculate_min_sales_price1, axis=1)
data['Profit 300m^2 & 4 employees'] = data.apply(Profit1, axis=1)

#2 25m^2 & 4 employees
def calculate_min_sales_price2(row):
    if row['Tägliche Kaffeetrinker'] == 0:
        return 0
    else:
        return (row['Mietpreis'] * 25 * 12 + 1.7316251692855331 * row['Tägliche Kaffeetrinker'] * 365 + (4*80000)) / (row['Tägliche Kaffeetrinker'] * 365)

def Profit2(row):
    profit = (4 - calculate_min_sales_price2(row)) * (365 * row["Tägliche Kaffeetrinker"])
    return min(profit, 10000000) # limit profit to 1 million

data['Mindestverkaufspreis 25m^2 & 4 employees'] = data.apply(calculate_min_sales_price2, axis=1)
data['Profit 25m^2 & 4 employees'] = data.apply(Profit2, axis=1)

#3 300m^2 & 2 employees
def calculate_min_sales_price3(row):
    if row['Tägliche Kaffeetrinker'] == 0:
        return 0
    else:
        return (row['Mietpreis'] * 300 * 12 + 1.7316251692855331 * row['Tägliche Kaffeetrinker'] * 365 + (2*80000)) / (row['Tägliche Kaffeetrinker'] * 365)

def Profit3(row):
    profit = (4 - calculate_min_sales_price3(row)) * (365 * row["Tägliche Kaffeetrinker"])
    return min(profit, 10000000) # limit profit to 1 million

data['Mindestverkaufspreis 300m^2 & 2 employees'] = data.apply(calculate_min_sales_price3, axis=1)
data['Profit 300m^2 & 2 employees'] = data.apply(Profit3, axis=1)

#4 25m^2 & 2 employees
def calculate_min_sales_price4(row):
    if row['Tägliche Kaffeetrinker'] == 0:
        return 0
    else:
        return (row['Mietpreis'] * 25 * 12 + 1.7316251692855331 * row['Tägliche Kaffeetrinker'] * 365 + (2*80000)) / (row['Tägliche Kaffeetrinker'] * 365)

def Profit4(row):
    profit = (4 - calculate_min_sales_price4(row)) * (365 * row["Tägliche Kaffeetrinker"])
    return min(profit, 10000000) # limit profit to 1 million

data['Mindestverkaufspreis 25m^2 & 2 employees'] = data.apply(calculate_min_sales_price4, axis=1)
data['Profit 25m^2 & 2 employees'] = data.apply(Profit4, axis=1)

data.to_file("C:/PythonTechLabs-Project/updated_data.geojson", driver='GeoJSON')







