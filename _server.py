import socket

def main():
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host = 'localhost'
	port = 12345
	server.bind((host,port))
	server.listen(1)
	print("server is on")
	client,address = server.accept()
	print(f"server connected with {address}")
	
	while True:
		data = client.recv(1024).decode()
		print(f"reply >> {data}")
		if data.lower() == "stop":
			break
		
		message = input("message >> ").encode()
		client.sendall(message)
		if message.lower() == "stop":
			break
	client.close()
	server.close()
	
if __name__ == "__main__":
	main()
