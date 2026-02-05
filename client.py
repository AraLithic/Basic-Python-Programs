import socket

def run_client():
    HOST = '127.0.0.1'
    PORT = 9999

    # Create the same type of socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # CONNECT: Active attempt to reach the Server
        print(f"[*] Connecting to {HOST}:{PORT}...")
        client_socket.connect((HOST, PORT))
        
        # SEND: Push data to the server
        message = "Hello from the other side!"
        client_socket.sendall(message.encode('utf-8'))

        # RECEIVE: Wait for the server's reply
        response = client_socket.recv(1024).decode('utf-8')
        print(f"[<] Server responded: {response}")

    except ConnectionRefusedError:
        print("[X] Error: Server is not active.")
    except Exception as e:
        print(f"[X] Client Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()
