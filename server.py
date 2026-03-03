import socket

addr = ("127.0.0.1", 4080)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(addr)
    server_socket.listen(1)
    print(f"server is listening on {addr}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Accepted connection from {client_addr}")

        request = client_socket.recv(1024)

        header = request.decode().split("\n")[0]
        print(header)

        mtd = header.split(" ")[0]

        if mtd == "GET":
            fin = open("./frontend/index.html", "rb")
            response = b"HTTP/1.1 200 OK\r\n\r\n" + fin.read()
            fin.close()
        else:
            response = b"HTTP/1.1 404 Not Found\r\n\r\nNot Found"

        client_socket.sendall(response)
        client_socket.close()


start_server()
# A simple web server in python
