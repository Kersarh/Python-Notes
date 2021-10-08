import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Send Message...")
message = "NEW MESSAGE!"
sock.sendto(message.encode(), ("localhost", 8001))
input("press Enter")
