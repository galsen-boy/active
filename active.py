import socket
import argparse

def scan_port(host, port, protocol):
    try:
        if protocol == "tcp":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((host, port)) == 0:
                    return "open"
                else:
                    return "closed"
        elif protocol == "udp":
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(1)
                s.sendto(b"", (host, port))
                try:
                    s.recvfrom(1024)
                    return "open"
                except socket.timeout:
                    return "closed"
    except Exception as e:
        return f"error ({e})"

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("host", type=str, help="Target host IP")
    parser.add_argument("-p", "--ports", type=str, required=True, help="Port or range of ports to scan")
    parser.add_argument("-t", action="store_true", help="TCP scan")
    parser.add_argument("-u", action="store_true", help="UDP scan")
    args = parser.parse_args()

    protocol = "tcp" if args.t else "udp" if args.u else None
    if not protocol:
        print("Specify either -t (TCP) or -u (UDP) scan.")
        return

    ports = []
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)
    else:
        ports = [int(args.ports)]

    for port in ports:
        status = scan_port(args.host, port, protocol)
        print(f"Port {port} is {status}")

if __name__ == "__main__":
    main()
 