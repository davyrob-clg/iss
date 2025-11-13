import tkinter as tk
from tkintermapview import TkinterMapView
import requests
import time

class ISSTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("ISS Tracker")

        self.map_widget = TkinterMapView(master, width=800, height=600, corner_radius=0)
        self.map_widget.pack(fill="both", expand=True)

        # Set initial map view (e.g., world view)
        self.map_widget.set_position(0, 0) 
        self.map_widget.set_zoom(1)

        self.iss_marker = None
        self.update_iss_location()

    def get_iss_location(self):
        try:
            response = requests.get("http://api.open-notify.org/iss-now.json")
            data = response.json()
            latitude = float(data["iss_position"]["latitude"])
            longitude = float(data["iss_position"]["longitude"])
            return latitude, longitude
        except requests.exceptions.RequestException as e:
            print(f"Error fetching ISS data: {e}")
            return None, None

    def update_iss_location(self):
        latitude, longitude = self.get_iss_location()
        if latitude is not None and longitude is not None:
            if self.iss_marker:
                self.map_widget.delete(self.iss_marker) # Remove previous marker
            self.iss_marker = self.map_widget.set_marker(latitude, longitude, text="ISS")
        
        self.master.after(5000, self.update_iss_location) # Update every 5 seconds

if __name__ == "__main__":
    
    root = tk.Tk()
    app = ISSTrackerApp(root)
    root.mainloop()