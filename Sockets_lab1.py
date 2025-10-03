import socket

print ("----------------Activity 1: Import socket and get basic info ------------------")
host_name = socket.gethostname()
print("Your Hostname is:", host_name)


ip_address = socket.gethostbyname(host_name)
print("Your IP Address is:", ip_address)

print ("---------------Activity 2: Wrap into a function-------------------")

def get_local_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(f"Host Name: {host_name}")
    print(f"IP Address: {ip_address}")

get_local_machine_info()

print ("-----------------Activity 3: Fully Qualified Domain Name -----------------")

fqdn = socket.getfqdn()
print("Fully Qualified Domain Name:", fqdn)



print ("---------------Activity 4: Converting IPV4 Address to Different Formats-------------------")
import binascii

for ip in ['127.0.0.1', '192.168.0.1']:
    packed = socket.inet_aton(ip)
    unpacked = socket.inet_ntoa(packed)
    print(f"IP: {ip} => Packed: {binascii.hexlify(packed)} => Unpacked: {unpacked}")

print ("----------------Activity 5: Finding a Service Name (Port -> Service)------------------")

def find_service_name():
    import socket
    for port in [80, 25]:
        for proto in ['tcp', 'udp']:
            print(f"Port {port}/{proto} => {socket.getservbyport(port, proto)}")


print ("----------------Activity 6: Converting Integers (Host <-> Network Byte Order)------------------")
data = 12345
print("Original:", data)
print("Network byte order:", socket.htonl(data))
print("Host byte order:", socket.ntohl(socket.htonl(data)))

print ("----------------Activity 7: Setting and Getting Socket Timeout------------------")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Default timeout:", s.gettimeout())
s.settimeout(5)
print("Updated timeout:", s.gettimeout())
