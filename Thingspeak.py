import serial
import thingspeak
import time

# ThingSpeak Channel Information
channel_id = "2374810"
write_key = "YFAPGVS8LVWC8RQ7"

# Serial port configuration (adjust COM port accordingly)
serial_port = "COM3"
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Initialize ThingSpeak channel
channel = thingspeak.Channel(id=channel_id)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode("utf-8").strip()
        if line.startswith("MQ Value:"):
            mq_value = int(line.split(":")[1].strip())

            # Print the received data
            print(f"Received: {mq_value}")

            # Update ThingSpeak channel with write_key
            response = channel.update({'field1': mq_value}, write_key=write_key)
            print(f"ThingSpeak Update: {response}")

        time.sleep(5)  # Adjust the sleep duration based on your needs

except KeyboardInterrupt:
    print("Script terminated by user.")

finally:
    # Close the serial port
    ser.close()
