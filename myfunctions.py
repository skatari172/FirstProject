import os
from cryptography.fernet import Fernet




'''def writeKey():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)'''

def loadKey():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

key = loadKey()
f = Fernet(key)


def view():

  with open('passwords.txt', 'r') as file:
    for line in file.readlines():
      decryptedMessage = f.decrypt(line)
      decryptedMessage = decryptedMessage.decode('utf-8')
      data = decryptedMessage.rstrip()
      user, userid, passw = data.split("|")


      print("\n" + "Account: " +  user + "\n" + "Username: " + userid + "\n" + "Password: " + passw + "\n")

def add():
  name = input("Account: ")
  username = input("Username: ")
  pwd = input("Password: ")
  if emptyInput(name, username, pwd) == 0:
    print("\nPlease enter a value for each field\n")
    add()
    
  if dupAccount(name) == 0:
    print("\nYou have already created an account under this name\n")
    return

  if emptyInput(name, username, pwd) == 1 and dupAccount(name) == 1:

    string = name + "|" + username + "|" + pwd + "\n"
    string = string.encode('utf-8')
    finalString = f.encrypt(string)
  
    with open('passwords.txt', 'ab') as file:
      file.write(finalString)
      file.write(b"\n")
  print("\nAccount successfully added!\n")

def delete():
  deleteName = input("Which account do you want to delete? ").lower()
  if emptyInput(deleteName, deleteName, deleteName) == 0:
    print("\nPlease enter in a valid input\n")
    delete()
    return
  count = 0
  flag = True
  



  inputFile = "passwords.txt"

  with open(inputFile, 'r') as filedata:
     inputFilelines = filedata.readlines()
     lineindex = 0

     with open('passwords.txt', 'r') as file:
       for line in file.readlines():
        count += 1
        decryptedMessage = f.decrypt(line)
        decryptedMessage = decryptedMessage.decode('utf-8')
        data = decryptedMessage.rstrip()
        accountName, userName, passWord = data.split("|")
         
        if(deleteName == accountName.lower()):
          flag = False
          break
           
    
     deleteLine = count

     if flag:
      print("\nAccount not Found")
      return
     with open(inputFile, 'w') as filedata:


        for textline in inputFilelines:
           # Checking whether the line index(line number) is
           # not equal to a given delete line number
           lineindex += 1
           if lineindex != deleteLine:
              # If it is true, then write that corresponding line into file

              filedata.write(textline)
              # Increase the value of line index(line number) value by 1
  
  print("\n")
  print("Account deleted \n")
  return

def noAccount():
  if os.path.getsize('passwords.txt') == 0:
    return 0

def emptyInput(a, b, c):
  if(a == "" or b == "" or c == ""):
    return 0 
  return 1

def dupAccount(name):
  
  with open('passwords.txt', 'r') as file:
    for line in file.readlines():
      decryptedMessage = f.decrypt(line)
      decryptedMessage = decryptedMessage.decode('utf-8')
      data = decryptedMessage.rstrip()
      accountName, userName, passWord = data.split("|")

      if(name.lower() == accountName.lower()):
          return 0 
          
  return 1
          
  
