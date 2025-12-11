import socket

host = 'localhost'
port = 12345

def client():
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.connect((host,port))
	print('connected with server')
	while True:
		message = input('message>> ')
		server.sendall(message.encode())
		data = server.recv(1024).decode()
		print(f"reply >> {data}")

if __name__ == '__main__':
	client()