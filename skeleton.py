def title ():
	print("Welcome to Encryptor and Decryptor")

def main_menu():
    print ("Choose the operation")
    print ("1.Encryptor")
    print ("2.Decryptor")
    print ("3.Exit")

    choice = input("=")
    return choice

def type ():
	print("Select the type:")
	print("0.Return")
	print("1.Text")
	print("2.File")

	choice = input("=")
	return choice

def encrypt_text():
    print (" [Encypt text] ")
    text = input("Enter the text to be encrypted: ")
    key = input("Enter the secret key: ")
    shift = 0
    for char in key:
      shift += ord(char)

    encrypted_text = ""

    for char in text:
      encrypted_text += chr((ord(char) + shift) % 256)
    print(f"Encrypted Text: {encrypted_text}") 


def decrypt_text():
    print (" [Decrypt Text]")
    text = input("Enter the text to be Decrypted: ")
    key = input("Enter the secret key: ")
    shift = 0
    for char in key:
      shift += ord(char)

    decrypted_text = ""
    
    for char in text:
       decrypted_text += chr(ord(char) - shift)

    print(f"Decrypted Text: {decrypted_text}")     

def encrypt_file():
  print (" [Encrypt File]")
  pass

def decrypt_file():
  print (" [Decrypt File] ")
  pass

def main ():
   while True:
       title()
       choice=main_menu()

       if choice == '1':
         data_choice = type()

         if data_choice == '1':
             encrypt_text()
         elif data_choice == '2':
         	encrypt_file()
         elif data_choice == '0':
            continue  	
         else:
           print ("Invalid Choice")

       elif choice == '2':
         data_choice = type()

         if data_choice == '1':
           decrypt_text()
         elif data_choice == '2':
           decrypt_file()
         elif data_choice == '0':
            continue  
         else :
           print("Invalid Choice")        	
       elif choice == "3":
         print ("Exiting Program")
         break
       else:
         print ("Invalid Choice")


if __name__ == "__main__":
   main()            