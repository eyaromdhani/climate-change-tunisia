import geopandas as gpd
import matplotlib.pyplot as plt

# Path to the shapefile
file_path = r'C:\Users\SBS\Downloads\gadm41_TUN_shp\gadm41_TUN_0.shp'

try:
    tunisia = gpd.read_file(file_path)
except Exception as e:
    print(f"Error reading shapefile: {e}")
    tunisia = None

# Check if tunisia was successfully read
if tunisia is not None:
    # Plot the base map of Tunisia
    tunisia.plot()

    # Overlay colors for specific areas
    
    # Example: Adding points (replace with your actual points data)
    # Coordinates example
    points_data = {
        'Latitude': [33.8869, 36.8065, 34.4208],
        'Longitude': [9.5375, 10.1815, 8.7808],
        'Label': ['Point A', 'Point B', 'Point C']
    }
    
    plt.scatter(points_data['Longitude'], points_data['Latitude'], color='black', marker='o', label='Points')

    # Customize plot
    plt.title("Map of Tunisia")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()

    # Show plot
    plt.show()
else:
    print("Shapefile was not loaded successfully.")
x = np.random.random(200)
y = np.random.random(200)

classes = np.random.randint(0, 3, 200)

plt.scatter(x, y, c=classes, cmap='copper')
plt.show()