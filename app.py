import tkinter as tk
from ttkbootstrap import Style
import random
import threading
import time

# Mock sensor data for testing
def get_sensor_data():
    # Replace this with actual I2C or UART data retrieval logic
    return {
        "CO2": random.uniform(200, 600),
        "PM2.5": random.uniform(10, 100),
        "PM10": random.uniform(20, 150),
        "Humidity": random.uniform(30, 70),
        "Temperature": random.uniform(20, 35),
    }

class AirSensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Air Sensor Monitor")
        self.root.geometry("800x600")

        # Configure ttkbootstrap style
        self.style = Style(theme="darkly")

        # Canvas setup
        self.canvas = tk.Canvas(self.root, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Create gradient background
        self.create_gradient_background()

        # Bubble configuration
        self.bubbles = {}
        self.init_bubbles()

        # Start updating data
        self.update_data()

    def create_gradient_background(self):
        # Create a vertical gradient
        for i in range(600):
            red = max(0, min(255, int(255 - i * 0.4)))
            green = max(0, min(255, int(100 + i * 0.25)))
            blue = max(0, min(255, int(200 + i * 0.1)))
            color = f"#{red:02x}{green:02x}{blue:02x}"
            self.canvas.create_line(0, i, 800, i, fill=color)

    def init_bubbles(self):
        positions = [(500, 100), (500, 250), (500, 350), (500, 450), (500, 550)]
        colors = ["#FF6347", "#32CD32", "#4682B4", "#FFD700", "#00CED1"]
        labels = ["CO2", "PM2.5", "PM10", "Humidity", "Temperature"]

        for i, label in enumerate(labels):
            x, y = positions[i]
            self.bubbles[label] = {
                "x": x,
                "y": y,
                "radius": 50,
                "color": colors[i],
                "circle": self.canvas.create_oval(x - 50, y - 50, x + 50, y + 50, fill=colors[i], outline="white", width=2),
                "text": self.canvas.create_text(200, y, text=f"{label}: 0", fill="white", font=("Helvetica", 14, "bold"), anchor="w")
            }

    def update_bubbles(self, data):
        for label, value in data.items():
            bubble = self.bubbles[label]
            radius = 30 + value / 15
            x, y = bubble["x"], bubble["y"]

            # Update circle size
            self.canvas.coords(bubble["circle"], x - radius, y - radius, x + radius, y + radius)

            # Update text
            self.canvas.itemconfig(bubble["text"], text=f"{label}: {value:.1f}")

    def update_data(self):
        def task():
            while True:
                data = get_sensor_data()
                self.update_bubbles(data)
                self.root.update_idletasks()
                self.root.update()
                time.sleep(1)

        thread = threading.Thread(target=task, daemon=True)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = AirSensorApp(root)
    root.mainloop()
