import serial
import time

# Replace this with your actual AT port
SERIAL_PORT = 'COM6'  # Windows example
# SERIAL_PORT = '/dev/ttyUSB2'  # Linux example

BAUD_RATE = 115200  # Default for Cavli modules

def send_at_command(command):
    try:
        # Open serial connection
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
            ser.flushInput()
            ser.write((command + '\r\n').encode())
            time.sleep(1)
            
            # Read response
            response = ser.readlines()
            print("Response from module:")
            for line in response:
                print(line.decode(errors='ignore').strip())

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    send_at_command("AT+CPIN?")
