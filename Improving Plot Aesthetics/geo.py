import pandas as pd
import matplotlib.pyplot as plt

airlines = pd.read_csv('../csvs/geo/airlines.csv')
airports = pd.read_csv('../csvs/geo/airports.csv')
routes = pd.read_csv('../csvs/geo/routes.csv')
first_airline = airlines.iloc[0]
first_airport= airports.iloc[0]
first_route = routes.iloc[0]
print(first_airline)
print(first_airport)
print(first_route)

# m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
# longitudes = airports["longitude"].tolist()
# latitudes = airports["latitude"].tolist()
# x, y = m(longitudes, latitudes)
# fig, ax = plt.subplots(figsize=(15,20))
# m.scatter(x, y, s=1)
# m.drawcoastlines()
# ax.set_title("Scaled Up Earth With Coastlines")
# plt.show()

geo_routes = pd.read_csv('../csvs/geo/geo_routes.csv')
dfw = geo_routes.loc[geo_routes['source'] == 'DFW']
print(dfw)