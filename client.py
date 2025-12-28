import socket
import json
import uuid
import time


SERVER_IP = "172.31.2.193"
SERVER_PORT = 5000

def rpc_call(method, params):
    req_id = str(uuid.uuid4())
    req = {"request_id": req_id, "method": method, "params": params}

    for attempt in range(3)
        try:
            print(f"Sending request {req_id} (Attempt {attempt+1})...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((SERVER_IP, SERVER_PORT))
            sock.sendall(json.dumps(req).encode())
            response = sock.recv(1024).decode()
            sock.close()
            return json.loads(response)
        except Exception as e:
            print(f"Error: {e}. Retrying...")
            time.sleep(1)
    return None

if __name__ == "__main__":
    resp = rpc_call("add", {"a": 10, "b": 20})
    print("Response:", resp)
