import folium
import pandas

data_location = 'Webmap_datasources/'

volcano_data = pandas.read_csv(data_location + 'Volcanoes.txt')

# Create map object by passing a starting location
# We will set the White House as the starting location but it can be anywhere
# location=[latitude, longitude]
# Latitudes and longitudes are a coordinate system used to locate point in the world
# Latitudes - lateral line, east to west, measures how far north or south a point lies from the equator, [-90, 90]
# Longitudes - vertical line, east to west, measures how far from the prime meridian a point lies, [-180, 180]
# The prime meridian is a vertical line that passess through Greenwich, England, UK.
map = folium.Map(location=[38.897822402954226, -
                           77.03649225134664], zoom_start=4)

# FeatureGroups - grouping of a map object's features such as markers
fg = folium.FeatureGroup(name='Web Map')

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
# iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new
# iterator.
for idx, row in volcano_data.iterrows():
    lat = row['LAT']
    lon = row['LON']
    volcano_name = row['NAME']

    fg.add_child(folium.Marker(
        location=[lat, lon], popup='Volcano ' + volcano_name, icon=folium.Icon(color='red')))

fg.add_child(folium.GeoJson())

map.add_child(fg)

# Save the map object to a html file
map.save('map1.html')
