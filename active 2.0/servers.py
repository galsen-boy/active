import socket
import threading
import signal
import sys
import argparse

def start_tcp_server(port):
    global running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen()
        server_socket.settimeout(1)  # Set timeout for accept operation
        print(f"TCP server listening on port {port}")
        while running:
            try:
                conn, addr = server_socket.accept()
            except socket.timeout:
                continue  # Go back to the top of the loop and check running flag
            except Exception as e:
                break  # Handle other exceptions or break
            with conn:
                print(f"Connected by {addr}")
                # Handle the connection
        print(f"TCP server on port {port} shutting down")

def start_udp_server(port):
    global running
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('0.0.0.0', port))
        server_socket.settimeout(1)  # Set timeout for recvfrom operation
        print(f"UDP server listening on port {port}")
        while running:
            try:
                data, addr = server_socket.recvfrom(1024)
            except socket.timeout:
                continue  # Go back to the top of the loop and check running flag
            except Exception as e:
                break  # Handle other exceptions or break
            print(f"Received message from {addr}")
            # Handle data here
        print(f"UDP server on port {port} shutting down")

def signal_handler(signal, frame):
    global running
    print('Exiting gracefully...')
    running = False

def main():
    parser = argparse.ArgumentParser(description="Start TCP and UDP servers on consecutive ports.")
    parser.add_argument("start_port", type=int, help="The starting port number for the servers")
    parser.add_argument("num_servers", type=int, help="The number of servers to start")
    args = parser.parse_args()

    global running
    running = True

    threads = []
    for i in range(args.start_port, args.start_port + args.num_servers):
        if i % 2 == 0:
            thread = threading.Thread(target=start_tcp_server, args=(i,))
        else:
            thread = threading.Thread(target=start_udp_server, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main()
