import requests
import json
import tkinter as tk
from tkinter import ttk, messagebox, TOP, LEFT
from PIL import Image, ImageTk
from datetime import datetime
from requests.exceptions import ConnectionError
import io


class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.tree_displayed = False

        self.root = tk.Tk()
        self.root.title("Weather App")

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Create a Frame to hold the Treeview widget and the sizegrip
        self.frame = ttk.Frame(self.root)
        self.frame.pack(side=TOP, pady=10, padx=10)

        # Create a label and text box for the location
        self.location_label = ttk.Label(self.frame, text="Enter specific Location (Use correct city name):")
        self.location_label.grid(row=0, column=0, sticky="w")
        self.location_entry = ttk.Entry(self.frame)
        self.location_entry.grid(row=0, column=1, )

        # Create a button to get the weather data
        self.get_weather_button = ttk.Button(self.frame, text="Get Weather", command=self.get_weather_data)
        self.get_weather_button.grid(row=0, column=2, pady=5)
        # Create a label and image box for the weather icon
        self.icon_label = ttk.Label(self.frame, text="Icon:")
        self.icon_label.grid(row=1, column=0, sticky="w", pady=5)
        self.icon_box = tk.Canvas(self.frame, width=100, height=100)
        self.icon_box.grid(row=1, column=1, pady=5)
        # Create a Treeview widget to display the weather data
        self.tree = ttk.Treeview(self.frame, columns=("one", "two"), show="headings", height=30)
        self.tree.heading("#0", text="Weather Data", anchor="w")
        self.tree.heading("one", text="Label", anchor="w")
        self.tree.heading("two", text="Value", anchor="w")
        self.tree.column("#0", width=200)
        self.tree.column("one", width=200)
        self.tree.column("two", width=200)
        self.tree.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
        if not self.tree_displayed:
            self.tree.grid_remove()  # hide the table

    def get_weather_data(self):
        # Clear the old data from the tree view
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Get the location from the text box
        location = self.location_entry.get()

        # Make the API call
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}"
        try:
            response = requests.get(url)

            # Extract the weather data from the JSON response
            weather_data = json.loads(response.content)
            print(weather_data)

            # Check if the response was successful
            if response.status_code == 200:
                if not self.tree_displayed:
                    self.tree_displayed = True
                    self.tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
                # Insert the weather data into the Treeview widget
                self.tree.tag_configure("styles", background="yellow", font="TkDefaultFont 9 bold")
                self.tree.insert("", "end", values=("Coordinates", ""), tags=("styles",))
                self.tree.insert("", "end", text=" ", values=("Latitude", weather_data['coord']['lat']))
                self.tree.insert("", "end", text=" ", values=("Longitude", weather_data['coord']['lon']))
                self.tree.insert("", "end", values=("Timezone", ""), tags=("styles",))
                self.tree.insert("", "end", values=(" ", weather_data['timezone']))
                self.tree.insert("", "end", values=("Current Weather", ""), tags=("styles",))
                self.tree.insert("", "end", text=" ",
                                 values=("Date and Time", datetime.fromtimestamp(weather_data['dt'])))

                self.tree.insert("", "end", values=("Sunrise", datetime.fromtimestamp(weather_data['sys']['sunrise'])))
                self.tree.insert("", "end", values=("Sunset", datetime.fromtimestamp(weather_data['sys']['sunset'])))
                self.tree.insert("", "end", values=("Temperature", ""), tags=("styles",))
                self.tree.insert("", "end", text=" ", values=("Current", f"{weather_data['main']['temp']} °F"))
                self.tree.insert("", "end", text=" ", values=("Feels like", f"{weather_data['main']['feels_like']} °F"))
                self.tree.insert("", "end", text=" ", values=("Min", f"{weather_data['main']['temp_min']} °F"))
                self.tree.insert("", "end", text=" ", values=("Max", f"{weather_data['main']['temp_max']} °F"))
                self.tree.insert("", "end", values=("Humidity", f"{weather_data['main']['humidity']}%"))
                self.tree.insert("", "end", values=("Pressure", f"{weather_data['main']['pressure']} hPa"))

                self.tree.insert("", "end", values=("Wind", ""), tags=("styles",))
                self.tree.insert("", "end", text=" ", values=("Speed", f"{weather_data['wind']['speed']} mph"))
                self.tree.insert("", "end", text=" ", values=("Direction", f"{weather_data['wind']['deg']} °"))

                self.tree.insert("", "end", values=("Visibility", f"{weather_data['visibility']} m"))

                self.tree.insert("", "end", values=("Weather Description", ""), tags=("styles",))
                self.tree.insert("", "end", values=(" ", weather_data['weather'][0]['description'].capitalize()))

                self.tree.insert("", "end", values=("Cloudiness", f"{weather_data['clouds']['all']}%"))

                self.tree.insert("", "end", values=("Rainfall", ""), tags=("styles",))
                if 'rain' in weather_data:
                    self.tree.insert("", "end", text=" ", values=("Last Hour", f"{weather_data['rain']['1h']} mm"))
                    self.tree.insert("", "end", text=" ", values=("Last 3 Hours", f"{weather_data['rain']['3h']} mm"))
                else:
                    self.tree.insert("", "end", text=" ", values=("Last Hour", "N/A"))
                    self.tree.insert("", "end", text=" ", values=("Last 3 Hours", "N/A"))

                self.tree.insert("", "end", values=("Snowfall", ""), tags=("styles",))
                if 'snow' in weather_data:
                    self.tree.insert("", "end", text=" ", values=("Last Hour", f"{weather_data['snow']['1h']} mm"))
                    try:
                        self.tree.insert("", "end", text=" ",
                                         values=("Last 3 Hours", f"{weather_data['snow']['3h']} mm"))
                    except KeyError:
                        self.tree.insert("", "end", text=" ", values=("Last 3 Hours", "N/A"))
                else:
                    self.tree.insert("", "end", text=" ", values=("Last Hour", "N/A"))
                    self.tree.insert("", "end", text=" ", values=("Last 3 Hours", "N/A"))
                # Get the weather icon and display it
                icon_id = weather_data['weather'][0]['icon']
                icon_url = f"https://openweathermap.org/img/w/{icon_id}.png"
                icon_response = requests.get(icon_url)
                icon_data = icon_response.content

                with open("icon.png", "wb") as f:
                    f.write(icon_data)

                icon = Image.open("icon.png")
                icon = icon.resize((100, 100), Image.ANTIALIAS)
                icon = ImageTk.PhotoImage(icon)
                self.icon_box.create_image(0, 0, anchor="nw", image=icon)
                self.icon_box.image = icon
            else:
                # Remove the Treeview widget if it's displayed
                if self.tree_displayed:
                    self.tree_displayed = False
                    self.tree.pack_forget()
                # Display an error message
                messagebox.showerror("Error",
                                     "Unable to retrieve weather data. Please check the location and try again.")
        except ConnectionError:
            # handle the connection error here
            messagebox.showerror("Error", "No internet connection. Please check your connection and try again later.")


app = WeatherApp(api_key="0636808542fc8295e8d2cd1a5fb0e20f")
