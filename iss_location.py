import urllib.request
import json

def get_iss_location():
    
    
    url = "http://api.open-notify.org/iss-now.json"

    try:
    
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
    except:
        raise Exception("Did not read")
        return 0.0,0.0

    location = result["iss_position"]
    latitude = float(location['latitude'])
    longitude = float(location['longitude'])
    
    return latitude, longitude

if __name__ == "__main__":
    lat, lon = get_iss_location()
    print(f"Current ISS Latitude: {lat}")
    print(f"Current ISS Longitude: {lon}")