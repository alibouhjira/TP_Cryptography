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

def decrypt_data_with_password(encrypted_data, password):
    # Déchiffrer les données avec un mot de passe
    result = subprocess.run(
        ["openssl", "enc", "-d", "-aes-256-cbc", "-salt", "-pbkdf2", "-k", password],
        input=encrypted_data,
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

    mykey = generate_random_key()

    crypt = encrypt_file_with_password("mdp.txt", mykey)

    # Chiffrer mdpcrypt.txt avec le premier mot de passe
    create_folder_if_not_exists("cle1")
    encrypt_data_with_password(crypt, password1, "cle1/crypt.txt")

    # Chiffrer myKey.txt avec le deuxième mot de passe
    create_folder_if_not_exists("cle2")
    encrypt_data_with_password(mykey, password2, "cle2/keycrypt.txt")

    print("Opérations de chiffrement terminées avec succès.")

def updtateMdp(updatedmdp, password1, password2):

    mykey = generate_random_key()

    crypt = encrypt_data_with_password2(updatedmdp, mykey)

    # Chiffrer mdpcrypt.txt avec le premier mot de passe
    create_folder_if_not_exists("cle1")
    encrypt_data_with_password(crypt, password1, "cle1/crypt.txt")

    # Chiffrer myKey.txt avec le deuxième mot de passe
    create_folder_if_not_exists("cle2")
    encrypt_data_with_password(mykey, password2, "cle2/keycrypt.txt")

    print("Opérations de chiffrement terminées avec succès.")



def test_supp(supprimer,mdp):

        if supprimer == False:
            nom = input("entré un nom  a tester ")
            numero = input("entré un numero de carte a tester ")
        else:
            nom = input("entré un nom  a supprmer ")
            numero = input("entré un numero de carte a supprimer ")

        pair_to_test = f"{nom}:{numero}".encode()
        lines = mdp.split(b'\n')
        
        
        if pair_to_test.decode() in mdp.decode(errors='ignore'):
            print(f"La paire '{pair_to_test}' est présente dans le fichier ")
            if supprimer == True:
                lines.remove(pair_to_test)
                print("paire supprimé avec succée")

        else:
            print(f"La paire '{pair_to_test}' n'est pas présente dans le fichier")



       
def decrypt(file1, file2):
    try:  
        password1 = getpass.getpass(prompt="Veuillez entrer le mot de passe de l'admin 1 ou de sont representant : ")
        password2 = getpass.getpass(prompt="Veuillez entrer le mot de passe de l'admin 2 ou de sont representant : ")

        # Déchiffrer mdpcrypt.txt avec le premier mot de passe
        encrypted_data1 = open(file1, "rb").read()
        decrypted_data1 = decrypt_data_with_password(encrypted_data1, password1)

        # Déchiffrer myKey.txt avec le deuxième mot de passe
        encrypted_data2 = open(file2, "rb").read()
        decrypted_data2 = decrypt_data_with_password(encrypted_data2, password2)
        mdp = decrypt_data_with_password(decrypted_data1, decrypted_data2)
        first_line = mdp.split(b'\n')[0].decode(errors='ignore')

        if first_line == "mdp:":
            print("Opérations de déchiffrement terminées avec succès.")
            return mdp
        else:
            return False
    except FileNotFoundError:
        return False

    except subprocess.CalledProcessError as e:
        return False

    except Exception as e:
        return False


def apply_function_to_files(directory, directory2, function_to_apply):
    # Liste tous les fichiers dans le répertoire
    files1 = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Applique la fonction à chaque fichier
    for file in files1:
        if file== "crypt.txt":
            file_path = os.path.join(directory, file)
            if os.path.exists(directory2+"keycrypt.txt"):
                return function_to_apply(file_path, directory2+"keycrypt.txt")
        
        if file== "crypt2.txt":
            file_path = os.path.join(directory, file)
            if os.path.exists(directory2+"keycrypt2.txt"):
                return function_to_apply(file_path, directory2+"keycrypt2.txt")
        

        if file== "crypt3.txt":
            file_path = os.path.join(directory, file)
            if os.path.exists(directory2+"keycrypt3.txt"):
                return function_to_apply(file_path, directory2+"keycrypt3.txt")
            
        if file== "crypt4.txt":
            file_path = os.path.join(directory, file)
            if os.path.exists(directory2+"keycrypt4.txt"):
                return function_to_apply(file_path, directory2+"keycrypt4.txt")
    return False
        

trouve = False   

try: 
    trouve = apply_function_to_files("cle1/", "cle2/",decrypt)
except FileNotFoundError:
    trouve = False

if trouve == False:
    try:
        trouve = apply_function_to_files("cle1/", "cle4/",decrypt)
    except FileNotFoundError:
        trouve = False

if trouve == False:
    try:
        trouve = apply_function_to_files("cle2/", "cle3/",decrypt)
    except FileNotFoundError:
        trouve = False

if trouve == False:
    try:
        trouve = apply_function_to_files("cle3/", "cle4/",decrypt)
    except FileNotFoundError:
        trouve = False

if trouve == False :
    print("erreur de dechiffrement")
    exit()




while True:
    print("\nMenu:")
    print("1. tester une paire")
    print("2. supprimer une paire")
    print("3. Quitter")

    choice = input("Choisissez une option (1, 2 ou 3 ) : ")

    if choice == "1":
        test_supp(False,trouve)
    elif choice == "2":
        test_supp(True,trouve)
    elif choice == "3":
        break
    else:
        print("Option invalide. Veuillez choisir 1, 2, ou 3.")