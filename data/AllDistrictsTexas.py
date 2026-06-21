import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Load your file – adjust the filename if needed
file_path = "C:\\Users\\Maricia.Alleman\Downloads\\zipcodes.xlsx"  # assuming your file is named this
df = pd.read_excel(file_path)

# Initialize the Nominatim geocoder with a unique user agent
geolocator = Nominatim(user_agent="tx_district_geocoder")
# Use a rate limiter to avoid hitting usage limits (1 request per second)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Prepare lists to store the latitude and longitude
latitudes = []
longitudes = []

# Loop over each district in the "DISTNAME" column
for district in df["DISTNAME"]:
    # Append ", Texas" to improve geocoding accuracy
    query = f"{district}, Texas"
    try:
        location = geocode(query)
        if location:
            lat = location.latitude
            lon = location.longitude
            print(f"Found {district}: ({lat}, {lon})")
        else:
            lat = None
            lon = None
            print(f"No result for {district}")
    except Exception as e:
        print(f"Error for {district}: {e}")
        lat = None
        lon = None
    latitudes.append(lat)
    longitudes.append(lon)

# Add the results to the DataFrame
df["Latitude"] = latitudes
df["Longitude"] = longitudes

# Save the updated DataFrame to a new Excel file
output_file = "C:\\Users\\Maricia.Alleman\Downloads\\tx_districts_with_coordinates.xlsx"
df.to_excel(output_file, index=False)
print(f"Updated file with coordinates saved as {output_file}")
