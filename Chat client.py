import socket

client = socket.socket()

host ,port = "127.0.0.3", 9000

client.connect,((host, port))

nom = input("Pseudo : ")

if __name__ == "__main__":

    

    while True:

        message = input(f"{nom} > ")

        client.socket.send(f"{nom} > {message}".encode("utf-8"))

        	
