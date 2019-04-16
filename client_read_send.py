import socket
import time

import serial


def main():
    serial_conn = serial.Serial('/dev/ttyUSB0', 115200)
    client = socket.socket()
    host = '192.168.1.105'
    port = 10010
    client.connect((host, port))
    while True:
        try:
            hex_data = serial_conn.read()
            client.send(hex_data)
            print('ok')
            time.sleep(1)
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

