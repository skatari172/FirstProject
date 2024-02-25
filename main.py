from myfunctions import delete, add, view, noAccount, emptyInput



while True:
  master_pwd = input("What is the Password? \n").lower()
  if emptyInput(master_pwd, master_pwd, master_pwd) == 0:
    print("Please provide a value\n")
    continue
  if (master_pwd == "password"):
    while True:
      mode = input("\n" + "Do you want add, view, or delete an account info? (Press q to quit) \n").lower()
      if emptyInput(mode, mode, mode) == 0:
        print("Please provide a value\n")
        continue
      if mode == "q":
        print("\n")
        break
        
      if mode == "view":
        print("\n")
        if noAccount() == 0:
          print("There are no accounts to view\n")
          continue
        view()
      elif mode == "add":
        print("\n")
        add()
      elif mode == "delete":
        print("\n")
        delete()
      else:
        print("\n")
        print("Invalid mode, try again")
        continue
  else:
    print("\n")
    print("Incorrect Password try again.\n")
    

