users = {
    "name": "imad_eedine",
    "password": "1234"
}

logged=None
while True:
    command=input("Enter a command(login, exit): ")
    if command=="exit":
        break
    elif command=="login":
        name=input("Enter your name: ")
        password=input("Enter your password: ")
        if name in users and users[name]==password:
            print(" you are now logged in")
            logged_in=name
        else:
             print(" Nom d'utilisateur ou mot de passe incorrect")

users = {
    "name": "imad_eedine",
    "password": "1234"
}
logged=None
while True:
    command=input("Enter a command(login, exit): ")
    if command=="exit":
        print("Programme terminé.")
        break
    elif command=="login":
        name=input("Enter your name: ")
        password=input("Enter your password: ")
        if name in users and users[name]==password:
            print(" you are now logged in")
            logged_in=name
        else:
            print(" Utilisateur non trouvé ou mauvais mot de passe")
            choice=input("Voulez-vous créer un compte ? (yes/no): ")
            if choice=="yes":
                new_password=input("Enter your new password: ")
                while True:
                    new_name=input("Enter your new name: ")
                    if new_name in users:
                        print("Nom d'utilisateur déjà existant")
                    else:
                        break
                new_password=input("Enter your new password: ")
                users[new_name]=new_password
                print(" Inscription réussie ! Vous pouvez maintenant vous connecter.")