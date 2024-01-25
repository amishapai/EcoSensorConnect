import serial
import datetime

# Serial port configuration (adjust COM port accordingly)
serial_port = "COM3"
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Open a file for writing
file_name = f"sensor_readings_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
with open(file_name, "w") as file:
    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode("utf-8").strip()
            if line.startswith("MQ Value:"):
                # Print the received data
                print(line)
                
                # Write data to the file
                file.write(line + "\n")

    except KeyboardInterrupt:
        print("Script terminated by user.")

    finally:
        # Close the serial port
        ser.close()
