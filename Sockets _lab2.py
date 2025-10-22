import socket
import ntplib
import struct
import time
from time import ctime

# ============================================================
# PART 1 — Modifying a Socket’s Send/Receive Buffer Size
# ============================================================

# Define constants for buffer sizes
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Check default buffer sizes
print("Default Send Buffer:", s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
print("Default Receive Buffer:", s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))

# Modify buffer sizes
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

# Verify updated sizes
print("Updated Send Buffer:", s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
print("Updated Receive Buffer:", s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))


# ============================================================
#  PART 2 — Changing Socket Blocking/Non-Blocking Mode
# ============================================================

# Create socket and bind to local address
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind(('127.0.0.1', 0))  # OS assigns port automatically
print("\nSocket bound to:", s2.getsockname())

# Blocking mode
s2.setblocking(1)
print("Mode: Blocking")

# Non-blocking mode
s2.setblocking(0)
print("Mode: Non-blocking")

# Timeout mode (0.5 seconds)
s2.settimeout(0.5)
print("Mode: Timeout (0.5s)")


# ============================================================
# PART 3 — Getting Time from Internet Time Server (NTP)
# ============================================================

def print_internet_time():
    """Get and print accurate time from an NTP server."""
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    print("\nInternet time:", ctime(response.tx_time))


if __name__ == "__main__":
    print_internet_time()


# ============================================================
#  PART 4 — Writing a Simple SNTP Client (UDP)
# ============================================================

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800  # Epoch reference time

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Prepare and send SNTP packet
data = b'\x1b' + 47 * b'\0'
client.sendto(data, (NTP_SERVER, 123))

# Receive response
data, _ = client.recvfrom(1024)

if data:
    # Unpack and adjust timestamp
    t = struct.unpack('!12I', data)[10] - TIME1970
    print("Current time:", time.ctime(t))
