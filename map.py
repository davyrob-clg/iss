import folium
import time
from iss_location import get_iss_location

# Assuming get_iss_location() from above is available



def visualize_iss_on_map():

    latitude=0.0
    longitude=0.0
    iss_map = folium.Map(location=[0, 0], zoom_start=2) # Centered on [0,0] initially
    
    iss_map.save("iss_tracker.html") # Save the map to an HTML file
    print(f"Map updated with ISS at Lat: {latitude}, Lon: {longitude}")
    
    # Clear previous markers (if any)
    for key in list(iss_map._children.keys()):
        if key.startswith('marker'):
            del iss_map._children[key]

    '''
    icon = folium.features.CustomIcon('http://www.pngall.com/wp-content/uploads/2016/05/Iron-Man.png', icon_size=(50,50))
    folium.Marker(location=[latitude, longitude],
            popup="International Space Station",            
            
              icon=icon
              ).add_to(iss_map)
    '''
     
    folium.Marker(
        location=[latitude, longitude],
        popup="International Space Station",
        icon=folium.Icon(color='red', icon='satellite')
    ).add_to(iss_map)
    
        
    


        
    while True:

            
        current_latitude = latitude
        current_longitude = longitude
        error_count=0
        update_map = False

        try: 
            latitude, longitude = get_iss_location()
            error_count = error_count +1
            print("error count: ",error_count)
            update_map=True
            
            folium.Marker([latitude, longitude]);
            time.sleep(5)

        except Exception as e:
            print(f"An error occurred: {e}")
            # Something didnt work - whhich is cool but we need a counter 
            current_latitude = latitude
            current_longitude = longitude
            error_count+-1
            update_map = False
          
        # Handle any other exception

        else:
        # Runs if no exception occurs
            print("Operation successful!")
            
        finally:
            print("Finally ran")
            # Always runs, whether an exception occurred or not


        
        



        

if __name__ == "__main__":
    visualize_iss_on_map()