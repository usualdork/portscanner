import socket

def scan_port(target_host, target_port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout in seconds
        socket.setdefaulttimeout(1)
        
        # Connect to the target host and port
        client_socket.connect((target_host, target_port))
        
        print(f"[+] Port {target_port} is open")
        
        # Close the socket
        client_socket.close()
    
    except socket.error:
        pass

def main():
    target_host = input("Enter the target host: ")
    port_range = input("Enter the port range (e.g., 1-100): ")
    
    start_port, end_port = map(int, port_range.split('-'))
    
    print(f"Scanning {target_host} for open ports from {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        scan_port(target_host, port)

if __name__ == "__main__":
    main()
