import serial
import time

# Replace 'COM3' with the correct port for your Arduino
ser = serial.Serial('COM3', 9600)
time.sleep(2)

try:
    while True:
        if ser.in_waiting > 0:
            distance = ser.readline().decode('utf-8').strip()
            print(f"Distance: {distance} cm")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
