def title ():
	print("Welcome to Encryptor and Decryptor")

def main_menu():
    print ("Choose the operation")
    print ("1.Encryptor")
    print ("2.Decryptor")
    print ("3.Exit")

    choice = input()
    return choice

def type ():
	print("Select the type:")
	print("0.Return")
	print("1.Text")
	print("2.File")

	choice = input()
	return choice

def encrypt_text():
  print (" [Encypt text] ")
  pass

def decrypt_text():
  print (" [Decrypt Text]")
  pass

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