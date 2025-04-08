import socket

def test_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Successfully connected to {host}:{port}")
        except Exception as e:
            print(f"Failed to connect to {host}:{port} - {e}")

if __name__ == "__main__":
    test_server("127.0.0.1", 8000)
    test_server("0.0.0.0", 8000)