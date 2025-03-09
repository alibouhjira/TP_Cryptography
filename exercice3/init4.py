import subprocess
import getpass
import os
from io import BytesIO


def generate_random_key():
    # Générer une clé aléatoire
    process = subprocess.run(["openssl", "rand", "32"], stdout=subprocess.PIPE, text=False)
    return process.stdout

def encrypt_file_with_password(input_filename, password):
    # Chiffrer les données avec un mot de passe
    result = subprocess.run(
        ["openssl", "enc", "-aes-256-cbc", "-salt","-pbkdf2", "-in", input_filename, "-k", password],
        stdout=subprocess.PIPE,
        text=False,
    )
    return result.stdout

def encrypt_data_with_password(data, password, output_filename):
    # Chiffrer les données avec un mot de passe
    result = subprocess.run(
        ["openssl", "enc", "-aes-256-cbc", "-salt","-pbkdf2", "-out", output_filename, "-k", password],
        input=data,
        stdout=subprocess.PIPE,
        text=False,
    )
    return result.stdout

def encrypt_data_with_password2(data, password):
    # Chiffrer les données avec un mot de passe
    result = subprocess.run(
        ["openssl", "enc", "-aes-256-cbc", "-salt","-pbkdf2", "-k", password],
        input=data,
        stdout=subprocess.PIPE,
        text=False,
    )
    return result.stdout

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def init():
    password1 = getpass.getpass(prompt="Veuillez entrer le mot de passe de l'admin 1 : ")
    password2 = getpass.getpass(prompt="Veuillez entrer le mot de passe de l'admin 2 : ")
    password3 = getpass.getpass(prompt="Veuillez entrer le mot de passe du representant 1 : ")
    password4 = getpass.getpass(prompt="Veuillez entrer le mot de passe du representant 2 : ")

    mykey = generate_random_key()

    crypt = encrypt_file_with_password("mdp.txt", mykey)
    #crypt 1-2

    create_folder_if_not_exists("cle1")
    encrypt_data_with_password(crypt, password1, "cle1/crypt.txt")

    create_folder_if_not_exists("cle2")
    encrypt_data_with_password(mykey, password2, "cle2/keycrypt.txt")


    #crypt 1-4
    create_folder_if_not_exists("cle1")
    encrypt_data_with_password(crypt, password1, "cle1/crypt2.txt")

    create_folder_if_not_exists("cle4")
    encrypt_data_with_password(mykey, password4, "cle4/keycrypt2.txt")

    #crypt 2-3
    create_folder_if_not_exists("cle2")
    encrypt_data_with_password(crypt, password2, "cle2/crypt3.txt")

    create_folder_if_not_exists("cle3")
    encrypt_data_with_password(mykey, password3, "cle3/keycrypt3.txt")

    #crypt 3-4
    create_folder_if_not_exists("cle3")
    encrypt_data_with_password(crypt, password3, "cle3/crypt4.txt")

    create_folder_if_not_exists("cle4")
    encrypt_data_with_password(mykey, password4, "cle4/keycrypt4.txt")

    print("Opérations de chiffrement terminées avec succès.")



init()