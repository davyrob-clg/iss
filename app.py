import tkinter as tk
from tkintermapview import TkinterMapView
import requests
import time

from PIL import Image, ImageTk



# 
class ISSTrackerApp:

    custom_image: tk.PhotoImage

    def __init__(self, master):

        self.master = master
        master.title("ISS Tracker")

          # Create a Menu Bar
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        # Create a 'File' Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=master.quit)

        # Create an 'Edit' Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        edit_menu.add_command(label="Redo", command=self.redo_action)

        button_frame = tk.Frame(master, bg="lightgray", width=200) # Optional: set a background color and width for visibility
        button_frame.pack(side=tk.RIGHT, fill=tk.Y) # Pack the frame to the RIGHT


        self.map_widget = TkinterMapView(master, width=1000, height=600, corner_radius=0)
        self.map_widget.pack(fill="both", expand=True)

        # Set initial map view (e.g., world view)
        #self.map_widget.set_position(0, 0) 
        self.map_widget.set_zoom(1)

        self.iss_marker = None

        image_path = "iss.png"  # Replace with the actual path to your image
        dot_path = "dot.ico"  # Replace with the actual path to your image
        
        original_image = Image.open(image_path)
        dot_image = Image.open(dot_path)
        
        resized_image = original_image.resize((32, 32), Image.LANCZOS) # Image.LANCZOS for high-quality downsampling
 
        self.custom_image = ImageTk.PhotoImage(resized_image)
        self.dot_image = ImageTk.PhotoImage(dot_image)
        

        
        latitude = float(0)
        longitude = float(0)

        #marker = self.map_widget.set_marker(52.5200, 13.4050, icon=self.custom_image)

        button_1 = tk.Button(button_frame, text="Button 1", command=self.button_command_1)
        button_1.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X) # Center horizontally within frame

        button_2 = tk.Button(button_frame, text="Button 2", command=self.button_command_2)
        button_2.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)

        self.update_iss_location()
    
    def new_file(event):
        pass

    def open_file(event):
        
        pass        
    
    def undo_action(event):

        pass        
    def redo_action(event):
        pass        

    def button_command_1(event):
        print("Button 1 clicked")

    def button_command_2(event):
        print("Button 2 clicked")

    def get_iss_location(self):

        """ 
            This is the docstring for my_function.
            It explains what the function does and what its parameters are.
        """
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
            
            self.iss_marker_dot = self.map_widget.set_marker(latitude, longitude,icon=self.dot_image)
            self.iss_marker = self.map_widget.set_marker(latitude, longitude, icon=self.custom_image)
            
        
        self.master.after(5000, self.update_iss_location) # Update every 5 seconds

if __name__ == "__main__":
    
    root = tk.Tk()
    app = ISSTrackerApp(root)
    root.mainloop()