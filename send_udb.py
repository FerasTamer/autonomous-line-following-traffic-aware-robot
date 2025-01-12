import socket
import time

def send_udp_message(message, ip_address, port):
    # Create a new socket using the given network family and socket type
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send the message to the specified address and port
        sock.sendto(message.encode(), (ip_address, port))
    finally:
        # Close the socket
        sock.close()
