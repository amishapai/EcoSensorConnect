import serial
import csv
import datetime

# Serial port configuration (adjust COM port accordingly)
serial_port = "COM3"
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=3)
i=0
# Open a file for writing
file_name = "C:\\Users\\amish\\Git Repos\\EcoSensorConnect\\SensorReading.csv"
with open(file_name, "w", newline='') as csvfile:
    # Create a CSV writer
    csv_writer = csv.writer(csvfile)

    try:
        # Write header to CSV file
        csv_writer.writerow(["Timestamp", "MQ Value"])

        while i<=10:
            # Read a line from the serial port
            line = ser.readline().decode("utf-8").strip()

            # Print the received data
            print(line)

            # Split the line into components
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            mq_value = line.split(": ")[-1]

            # Write data to the CSV file
            csv_writer.writerow([timestamp, mq_value])
            i+=1

    except KeyboardInterrupt:
        print("Script terminated by user.")

    finally:
        # Close the serial port
        ser.close()
        



'''
import serial
import datetime

# Serial port configuration (adjust COM port accordingly)
serial_port = "COM3"
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)
i=0
# Open a file for writing
file_name = "C:\\Users\\amish\\Git Repos\\EcoSensorConnect\\sensor_readings_2024-01-24_18-01-36.txt"
with open(file_name, "w") as file:
    try:
        while i<=10:
            # Read a line from the serial port
            line = ser.readline().decode("utf-8").strip()
            
            # Check if the line is not empty
            if line:
                # Print the received data
                print(line)
                
                # Write data to the file
                file.write(line + "\n")
                i+=1

    except KeyboardInterrupt:
        print("Script terminated by user.")

    finally:
        # Close the serial port
        ser.close()
        file.close()
'''

