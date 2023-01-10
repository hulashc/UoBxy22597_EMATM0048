usernames_passwords={}
global wallet_list
wallet_list = []
global system_account
system_account =0.0

def get_id(user_name):
  user_exist  = 0
  max_value = 0 
  num_id = 0
  # interating through the list of users names 
  for index in range(len(wallet_list)):
    list_local1 = []
    list_local1 = wallet_list[index]
    hh = list_local1[0]

    # getting max vale of the id list 

    if(max_value <= wallet_list[index][1]):
      max_value = wallet_list[index][1]

    # checking user exist or not if not exist assign zero as num_id is declared as zero  
    if(hh == user_name):
      user_exist  = 1

  if(user_exist == 1 ):
    # assiging max value of list and adding one number extra for the list
    num_id = max_value 
    num_id = num_id + 1 

  return num_id 



class Customer_Account() :
    def __init__(self):
      pass 

    def trans_page(self, user_name):
      print("customer Screen---------------")
      print("Enter C to create new wallet: ")
      print("Enter D to delete wallet :")
      print("Enter T to make a transcation Deposit/Transfer  :")
      print( "Enter L to log out :" )
      print("Enter W to Withdraw :")
      print("Enter S to Display all the wallet information of customer:")
      type_owl = input() 
      if type_owl == "C" or type_owl == "c" :
        # calling create wallet 
        self.create_wallet(user_name)
      elif type_owl=="D" or type_owl=="d":
        # calling delete wallet 
        self.delete_wallet(user_name)
      elif type_owl=="t" or type_owl=="T":
        # calling transfer 
        self.trans_wallet(user_name)
      elif type_owl=="W" or type_owl=="w":
        # calling for withdraw 
        self.withdraw_wallet(user_name)

      elif type_owl=="L" or type_owl=="l":
        # going back to main menuus as user has been logout
        self.mainmenu()

      elif type_owl=="s" or type_owl=="S":
        # function callback to print to display data 
        self. print_wallet(user_name)

  
      else :
        print ("entered wrong inputs ")
        self.trans_page(user_name)


# function for withdraw 

    def withdraw_wallet(self, useer_nmaedw):
      wallet_index = 0 
      amountw =0 
      # taking inputs from user 
      print("enter wallet id you want to withdraw amount from")
      type_dlw = input() 
      wallet_index = int (type_dlw)

      # taking amount for withdraw 
      print("Enter the amount to withdraw ")
      type_dlwa = input()
      amountw = int (type_dlwa)

      # checking for valid numbers 
      if(type_dlw.isnumeric() and type_dlwa.isnumeric()):
        # iterating through list 
        for index in range(len(wallet_list)):
          list_dlocal = []
          list_dlocal = wallet_list[index]
          hh = list_dlocal[0]
          comp= int(type_dlw)
          # checking for the user name and id in the list 
        
          if(hh == useer_nmaedw and  list_dlocal[1]  == comp):
            wallet_list[wallet_index][2] =  wallet_list[wallet_index][2] - amountw
          else :
            print("entr a valid id ")

      else :
        print("enter a valid id for withdraw ")
        self.withdraw_wallet(useer_nmaedw)



# FUNCTION FOR DELETE WALLLET 

    def delete_wallet(self, user_named):
      print("enter the wallet id  you want to remove")
      # GETTING INPUTS FROM USER 
      type_dl = input() 
      delete_me  = 0
      # CHECKING INPUT IS NUMBER OR NOT 
      if(type_dl.isnumeric()):
        for index in range(len(wallet_list)):   # INTERATING THROUGH THE LIST 
          list_dlocal = []
          list_dlocal = wallet_list[index]   # READING  EACH LIST AND STORING TO LOCAL 
          hh = list_dlocal[0]
          comp= int(type_dl)

          # COMPARING THE USER NAME ENTERED BY THE USER TO LIST AND ENTERED ID FRO THE USER 
          if(hh == user_named and  list_dlocal[1]  == comp):
            # DECLARING THE INDEX OF THE LIST TO BE REMOVED 
            delete_me = index

        if(delete_me!=0):
          wallet_list.pop(delete_me)
        else :
          print("enter a valid id ")
          self.delete_wallet(user_named)      
        # self.print_wallet(user_named)
      else :
        print("enter a valid id ")
        self.delete_wallet(user_named)



# FUNCTION FOR TRANSCATION 

    def trans_wallet(self, user_namet):
      print("enter d for deposit and t for transfer")
      type_tl = input()
      if type_tl=="D" or type_tl=="d":
        # GOING TO DEPOSIT FUNCTION 
        self.deposit(user_namet)
        self. print_wallet(user_namet)

      elif type_tl=="t" or type_tl=="T":
        # GOING TO TRNSFR FUNCTION 
        self.transfer(user_namet)
        self. print_wallet(user_namet)
      
      else:
        self.trans_wallet(user_namet)


    def deposit(self, user_nametd):
      # TAKING THE AMOUNT NEEDED TO BE DEPOSITED BY THE USER 
      print("enter the amount for deposit")
      td= input()
      # TAKING THE ID TO DEPOSIT 
      print("enter the id of the wallet for deposit")
      id_t = input()

      #  ITERATING THROUGHT THE LIST AND COMPARING THE USER ENTERED DETAILS 
      for index in range(len(wallet_list)):
        list_dlocal = []
        list_dlocal = wallet_list[index]
        hth = list_dlocal[0]
        comp= int(id_t)

        # COMPARING THE USER NAME ND ID 
        if(hth == user_nametd and  list_dlocal[1]  == comp):
          balance = int (td)
          # UPADATING THE BALANCE 
          list_dlocal[2] =  list_dlocal[2] + balance
          list_dlocal[3] = " \"Deposit \" "
    


    def transfer (self , user_namettt ):
      # LOCAL VARIABLES  
      ser = 0
      rer = 0
      sen_row = 0
      rer_row =0 
      highest_index = 0
      highest_amount  = 0
      use_highest = 0 
      percentge_amount = 0.0
      tbalance = 0.0

# TAKING INPUTS FROM THE USER 
      print("please enter the  FROM(sender) wallet id ")
      tttd1  = input()
      print("please enter the TO(receiver) Wallet id")
      tttd2  = input ()
      print("please enter the amount ")
      tttda2  = input ()
      amount = int (tttda2)
      percentge_amount = amount * 0.5 *0.01


# READING THROUGH THE LIST 
      for index in range(len(wallet_list)):
        list_tdlocal = []
        list_tdlocal = wallet_list[index]
        thth = list_tdlocal[0]
        comp= int(tttd1)
        comp2 = int(tttd2)
        print("---------------------------------------------")
        
        if(wallet_list[index][4] == "Daily_use"  or wallet_list[index][4] == "Holiday" ):
          if(wallet_list[index][2] > highest_amount  ):
            highest_index = index
          

          # CHECKING FOR THE RECECVIER ID IS VALID OR NOT 
          if(thth == user_namettt and  list_tdlocal[1]  == comp2):
              rer = 1;
              rer_row = int(index)


           # CHECKING FOR THE RECEVIER IS VALID OR NOT 
          if(thth == user_namettt and  list_tdlocal[1]  == comp):
            tbalance  = list_tdlocal[2]
            sen_row = int(index)
            ser = 1;
           
          # SENDERHAS NO ENOUGH AMOUNT SO USING THE OTHER INDEX OF THE WALLLET 
          if(tbalance <= amount ):
            use_highest = 1

        else : 
          print ("could not transfer amount because the wallet type is Mortage or Saving. Use Daily_use wallet/ Holidays ")    

      # DIRECT TRANSER SENDER HAS ENOUGH AMOUNT TO TRANSFER 
      if(ser == 1 and rer ==1 and use_highest == 0):
        global system_account 
        # UPDATING AND DISPLAYING THE SYSTEM ACCOUNT 
        system_account = system_account + percentge_amount
        print("the system percentage is : ")
        print( system_account)

        # updating the sender walllet 
        # sender wallet  update 
        wallet_list[sen_row][2] =  wallet_list[sen_row][2] - (amount + percentge_amount)
        wallet_list[sen_row][3] = "transfer"
        # recervier wallet update 
        wallet_list[rer_row][2]  = wallet_list[rer_row][2]  + amount
        wallet_list[rer_row][3] = "transfer" 
        
        # sender doesnot have  enough momey sending from the highest  wallet  
      elif(ser == 1 and rer ==1 and use_highest == 1):
        # sender walllet update 
        wallet_list[highest_index][2] =  wallet_list[highest_index][2] - (amount + percentge_amount)
        wallet_list[highest_index][3] = " \" transfer \" "
        # recervier account update 
        wallet_list[rer_row][2]  = wallet_list[rer_row][2]  + amount
        wallet_list[rer_row][3] = " \"transfer \" " 

      
        



class wallet(Customer_Account) :
  def __init__(self):
      pass 
  

  def print_wallet(self, user_name):

    # CHECKING FOR WALLETS IN THE USER NAME IF NO WALLETS THEN CALLING CREATE WALLET FUNCTIOON 
    if(len(wallet_list) == 0 ):
      self.create_wallet(user_name)
 
    # ITERATING TO THE LIST OF USERS IN THE WALLET 
    for index in range(len(wallet_list)):
      list_local = []
      list_local = wallet_list[index]
      hh = list_local[0]
      # PRINTING ALL THE USERS WALLETS 
      if(hh == user_name):
        print( ' the wallet id is : ' , list_local[1], "balance : " , list_local[2], "last transcation : ",  list_local[3], "type_of_wallet : " , list_local[4])

    # CALLING TRANSFER PAGE 
    self.trans_page(user_name)



 # function call for creating new walllet from the user input 
  def create_wallet(self, user_name):
    print(" wallet scren ---------------------------------------------")
    print("there are no wallets select the type of wallet you want to add")
    print("Press D for Daily Use Wallet ")
    print("Press S for Saving  Wallet ")
    print("Press H for Holiday Wallet  ")
    print("Press M for Mortage")
     # taking the inputs  from the user 
    type_wl = input() 
    # comparing the user inputs to be valid or not 
    if type_wl=="D" or type_wl=="d":
      type_of_wallet =  "Daily_use" 
    elif type_wl=="s" or type_wl=="S":
      type_of_wallet =  "Saving" 
    elif type_wl=="H" or type_wl=="h":
      type_of_wallet =  "Holiday" 
    elif type_wl=="M" or type_wl=="m":
      type_of_wallet =  "Mortage" 
    else:
      print("please make a valid selection")
      self. create_wallet(user_name)

    # assiging wallet id 
    wallet_id =  get_id(user_name)

    # assiging default values to the wallet 
    balance = 0 
    last_trans = " \"NONE \" "
    b= []
    b = [ user_name, wallet_id, balance, last_trans, type_of_wallet]
    # appeending to the main list 
    wallet_list.append(b)
    # printing the walllet 
    self.print_wallet(user_name)





class Bank_Account(wallet):
    def __init__(self):
      pass 
    
    def register(self):
      print("-------------creating an new account -------")
      # taking inputs from the user 
      firstname = input("Enter your first name : ")
      lastname  = input("Enter your last name : ")
      country   = input("Enter your country of residence : ")
      age   = input("Enter your age : ")
      email   = input("Enter your Email : ")
      username=input("Enter a username : ")
      password=input("Enter a password : ")
      usernames_passwords[username]=password    # STORING TO DICTONARY 
      #self.create_wallet(username)
      self.mainmenu()
    

    def mainmenu(self):
      print("------------MAIN MENU---------------------------------")
      print("Press L for  login : ")
      print("Press R for  making a new account :")
      choice1=input()    # TO TAKE INPUT FROM TERRMINAL 

      # CHECK THE USER INPUTS IS VALID OR NOT 
      if choice1=="L" or choice1=="l":
        self.login()  #GOING TO LOGIN FUNCTION  
      elif choice1=="R" or choice1=="r":
        self.register() # GOING TO REGISTER FUNCTION 
      else:
        print("please make a valid selection") # WRONG INPUT DISPLAY 
        self.mainmenu()
    
    
    def login(self):
      print("--------------LOGIN SCREEN---------------")
      # USER INPUTS 
      username=input("Username: ")   
      password=input("Password: ")
       # COMPARING THE USER INPUTS WITH DICTONARY 

      if username not in usernames_passwords:
        print("The user does not exist")
        self.mainmenu()  # NO USER SO GOING BACK TO MAIN MENU 

      elif usernames_passwords[username]==password:
        print("login sucessful")
        # self.print_wallet(username)
        self.print_wallet(username)     # GOING TO PRINT WALLET FUNCTION 
 
      elif usernames_passwords[username] !=password:
        print("Sorry - wrong combination of user name or password ")
        self.mainmenu() # GOING BACK TO MAIN  MENU 



if __name__ == '__main__': 
  s = Bank_Account()     # CALL CLASS 
  s.mainmenu()
print("after __name__ guard")



