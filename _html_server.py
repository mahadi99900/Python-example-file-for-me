import socket

html_code ="""

<!DOCTYPE html>
<html>
<head>
    <title>Professional Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        
        header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        
        header h1 {
            margin: 0;
        }
        
        nav {
            background-color: #444;
            padding: 10px;
            text-align: center;
        }
        
        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }
        
        nav a:hover {
            color: #ccc;
        }
        
        main {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }
        
        section {
            background-color: #f7f7f7;
            padding: 20px;
            margin: 20px;
            width: 80%;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        
        section h2 {
            margin-top: 0;
        }
        
        footer {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
            clear: both;
        }
    </style>
</head>
<body>
    <header>
        <h1>Professional Website</h1>
    </header>
    <nav>
        <a href="           
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>
    <main>
        <section>
            <h2>Welcome to our website</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section>
            <h2>Our Services</h2>
            <ul>
                <li>Web Development</li>
                <li>Mobile App Development</li>
                <li>Digital Marketing</li>
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Professional Website</p>
    </footer>
</body>
</html>


"""

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 12345
    server.bind((host, port))
    server.listen(1)
    print("server is on")
    client, address = server.accept()
    print(f"server connected with {address}")
    while True:
        data = client.recv(1024).decode()
        print(f"reply >> {data}")
        message = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{html_code}"
        client.sendall(message.encode())
        client.close()  
        break  
    server.close() 

if __name__ == "__main__":
    main()