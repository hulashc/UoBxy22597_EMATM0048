# UoBxy22597_EMATM0048

The readme file consists of steps for running the code and a brief description of code.
# Steps to run the code 

1. Step up the ide of your interest
2. Run the code.
3. Enter the inputs for login/ registration (main menu  part)
4. Enter the details of the user for the registration ( creating an account )
5. After registration it goes back to the main menu so enter the inputs for registration or login of your interest
6. If entered into registration follow step 4
7. Enter the wallet of your choice (wallet part  ) for the type of wallet. Daily_use, Saving, Holiday, Mortage
8. Enter the inputs of your choice (customer part) for creating a wallet, deleting the wallet, transaction (deposit/transfer), withdrawing, logout, displaying the customer wallets information


# BRIEF DESCRIPTION OF THE PROJECT

The user name and password of the customers are stored in a dictionary and it is a global.
The information of the wallet is stored in the multi-dimensional list and updated accordingly and accessed globally.

The class Bank_Account contains the functions for the customer registration (register) and main menu function (main menu part ) and login function (for login)
 	 1 The main menu function takes input from the user for login or making an account and calls the appropriate function respectively.
 	 2. The login function is called if the user enters r/ R and the register function is called if the user inputs R/r
 	 3. The register takes in inputs of the user such as first name, last name, country of residence, age, Email, username, and password. The username and password are stored in a dictionary.
 	 4. The login function compares the entered details with the data in the dictionary and calls the print_wallet function.



The class wallet contains the function for print_wallet, create_walllet , 
	1 The print wallet function shows the wallet information such as wallet id, balance, last transaction, type_of_wallet and calls the customer part (class customer_account in the  function trans_page)  
	2. The create wallet function takes input from the user and creates account multiple wallets such as Daily Use,  Saving, Holiday, and Mortage based on the inputs from the user. after creating it calls the prints wallet. The unique id is given by taking the maximum number of the user list and incrementing by one and assigning it as a new wallet id.
	
	

	
The class customer_account contains trans_page, withdraw_wallet ,delete_wallet,trans_wallet, deposit,transfer

	1 The trans_page function for the customer part which takes input from the user for creating wallet (c/C) calls the create wallet function, deleting wallet(D/d), transaction (t/T), logout (l/L ), withdraw (W/w), and display (S/s).
	2 The create wallet function takes in id number of the wallet and the amount to withdraw and updates the list accordingly based on the user name and id of the wallet.
	3. The delete_wallet takes in the id from the pops the list from the multi-dimensional list by comparing the user name and id of the wallet
	4. The trans_wallet function takes in input from the user and calls the deposit and transfer functions.
	 5. The deposit function takes in the id and amount needed to be deposited and updates the list accordingly. also updates the type of transition
	 6. The transfer function takes in the sender and receiver wallet id and transfers the amount and updates the system account. it also checks if sufficient funds are not available from the wallet it takes the wallet having the highest amount and makes the transaction. it makes sure that is transfer is made in daily use and holiday wallet only.
   
   
   https://github.com/hulashc/UoBxy22597_EMATM0048/edit/main/README.md
