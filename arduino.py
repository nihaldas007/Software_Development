import serial
import time

# Replace with the correct port where Arduino is connected (e.g., COM3 or /dev/ttyUSB0)
arduino = serial.Serial('COM9', 9600)
time.sleep(2)  # Wait for the Arduino to initialize

# Simulate food.get() and num.get()
food = "Pizza"
num = 5

# Create the formatted message
message = f'The Robot Will the {food} on the table number {num}'

# Send the formatted message to Arduino
arduino.write(message.encode())

# Close the serial connection
arduino.close()
