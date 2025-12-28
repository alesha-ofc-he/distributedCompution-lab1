import socket
import json
import time

def add(a, b):
    return a + b

def handle_request(request_data):
    try:
        req = json.loads(request_data)
        method = req.get("method")
        params = req.get("params")
        req_id = req.get("request_id")

        print(f"Processing Request ID: {req_id}, Method: {method}")


        time.sleep(5)

        result = None
        status = "OK"

        if method == "add":
            result = add(params["a"], params["b"])
        else:
            status = "Method Not Found"

        return json.dumps({"request_id": req_id, "result": result, "status": status})
    except Exception as e:
        return json.dumps({"status": "Error", "message": str(e)})

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(5)
    print("Server listening on port 5000...")
    while True:
        client_sock, addr = server_socket.accept()
        data = client_sock.recv(1024).decode()
        if data:
            response = handle_request(data)
            client_sock.sendall(response.encode())
        client_sock.close()

if __name__ == "__main__":
    start_server()
