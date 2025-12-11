import json
import socket


student_info = {
    "student1" : {
        "name":"mahadi hasan",
        "class": 10,
        "profession":"student",
        "age": 18,
        "address":{
            "gram":"golapgram",
            "thana":"savar",
            "district":"Dhaka",
            "division":"dhaka",
            
        }
    },
    "student2": {
        "name":"imran hasan",
        "class": 12,
        "profession":"student",
        "age": 20,
        "address":{
            "gram":"gopalpur",
            "thana":"gopalpur",
            "district":"tangail",
            "division":"dhaka",
            
        }
            
    },
    "student3" : {
        "name":"labib hasan",
        "class": 8,
        "profession":"student",
        "age": 15,
        "address":{
            "gram":"shimla",
            "thana":"modupur",
            "district":"rajshahi",
            "division":"dhaka",
            
        
        }    
            
    },
    "student4" : {
        "name":"rakib hasan",
        "class": 13,
        "profession":"student",
        "age": 20,
        "address":{
            "gram":"atorbari",
            "thana":"tongi",
            "district":"gazipur",
            "division":"dhaka",
            
        }    
            
    }
}
    
main_data = json.dumps(student_info)

html_code = f"<html> <body> <p>{main_data}</p> </body> </html>"


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
        #message = f"HTTP/1.1 200 OK\r\n\r\n{main_data}"
        client.sendall(message.encode())
        client.close()  
        break  
    server.close() 

if __name__ == "__main__":
    main()