import tkinter as tk
from tkintermapview import TkinterMapView

# Create the main window
root = tk.Tk()
root.title("Widgets and Map View Example")
root.geometry("800x600")

# Create a frame for widgets
widget_frame = tk.Frame(root)
widget_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Add some widgets to the frame
label = tk.Label(widget_frame, text="Enter Location:")
label.pack(pady=5)

entry = tk.Entry(widget_frame)
entry.pack(pady=5)

button = tk.Button(widget_frame, text="Search")
button.pack(pady=5)

# Create the map view
map_widget = TkinterMapView(root, width=600, height=600)
map_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Set default map location
map_widget.set_position(36.1408, -5.3536)  # Example: Gibraltar coordinates
map_widget.set_zoom(12)

# Run the application
iss = 
root.mainloop()
