def get_iss_pass_times(latitude, longitude, altitude=0, num_passes=5):
    url = f"http://api.open-notify.org/iss-pass.json?lat={latitude}&lon={longitude}&alt={altitude}&n={num_passes}"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    return result["response"]

if __name__ == "__main__":
    # Example: Pass times over a specific location (e.g., London)
    london_lat = 51.5
    london_lon = -0.1
    pass_times = get_iss_pass_times(london_lat, london_lon)
    
    print(f"Next {len(pass_times)} ISS passes over London:")
    for p in pass_times:
        print(f"  Risetime: {time.ctime(p['risetime'])}, Duration: {p['duration']} seconds")