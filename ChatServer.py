import socket 
import select

serveur = socket.socket()
host, port = "127.0.0.3", 9000
serveur.bind((host, port))
serveur.listen(4)
ClientCo = True 
socket_objs = [serveur]

print("Bienvenue dans le tchat")

while ClientCo:
    liste_lu, liste_acce_Ecrit, exeption = select.select(socket_objs, [], socket_objs)
    for socket_objs in liste_lu:
        if socket_objs is serveur:
            client, adresse = serveur.accept()
            socket_objs.apend(socket_obj)
            
        else:
            donnees_recues = socket_obj.recv(128).decode("utf-8")

        if donnees_recues:
            print(donees_recues)

        else:
            socket_objs.remove(socket_obj)
            print("1 individu deconnecte")
print(f"{len(socket_objs) - 1} individus restants")
