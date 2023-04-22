import requests

# Enter your Google Maps API key here
API_KEY = "YOUR_API_KEY"

# Enter the latitude and longitude of the location you want to search from
LATITUDE = "37.7749"
LONGITUDE = "-122.4194"

# Set the type of place you want to search for (in this case, a hospital)
PLACE_TYPE = "hospital"



# Set the radius for the search (in meters)
RADIUS = 5000

# Define the API endpoint and parameters for the Nearby Search request
NEARBY_SEARCH_ENDPOINT = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
nearby_search_params = {
    "location": f"{LATITUDE},{LONGITUDE}",
    "radius": RADIUS,
    "type": PLACE_TYPE,
    "key": API_KEY
}

# Send the Nearby Search API request
nearby_search_response = requests.get(NEARBY_SEARCH_ENDPOINT, params=nearby_search_params)
nearby_search_data = nearby_search_response.json()

# Extract the Place ID of the nearest hospital
place_id = nearby_search_data["results"][0]["place_id"]

# Define the API endpoint and parameters for the Place Details request
PLACE_DETAILS_ENDPOINT = "https://maps.googleapis.com/maps/api/place/details/json"
place_details_params = {
    "place_id": place_id,
    "fields": "name,formatted_address,formatted_phone_number,website",
    "key": API_KEY
}

# Send the Place Details API request
place_details_response = requests.get(PLACE_DETAILS_ENDPOINT, params=place_details_params)
place_details_data = place_details_response.json()

# Extract the phone number and website URL of the nearest hospital
phone_number = place_details_data["result"].get("formatted_phone_number", "Phone number not available")
website = place_details_data["result"].get("website", "Website not available")

# Print the phone number and website URL of the nearest hospital
print(f"Phone number: {phone_number}")
print(f"Website: {website}")



# -----------------------------------------------------------------------------------------
import pytz
def unix_to_local(unix_timestamp, timezone):
    utc_time = datetime.utcfromtimestamp(unix_timestamp)
    utc_time = pytz.utc.localize(utc_time)
    local_time = utc_time.astimezone(pytz.timezone(timezone))
    return local_time.replace(tzinfo=None)

ct=0


# -------------------------------------------------------------------------------------------------------------------------------------------------
