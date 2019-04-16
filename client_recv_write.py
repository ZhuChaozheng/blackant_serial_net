import socket
import time

import serial


def main():
    # read serial
    serial_conn = serial.Serial('/dev/ttyUSB1', 115200)
    client = socket.socket()
    host = '192.168.1.105'
    port = 10011
    client.connect((host, port))

    while True:
        try:
            hex_data = client.recv(1000)
            print('hex_data', hex_data)
            serial_conn.write(hex_data)
        except:
            time.sleep(3)
            break


if __name__ == "__main__":
    while 1:
        try:
            main()
        except:
            time.sleep(5)
            continue
