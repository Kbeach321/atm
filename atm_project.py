#### IMPORTS #########
import records
db = records.Database("postgres://localhost/atm")

############## Database Interactions ####################

def track_transactions(db, transactions): # <---- Calls database --> Updated_Field --> Update_Value
    sql = "INSERT INTO atm_table (transactions) VALUES (:transactions)"
    return db.query(sql,transactions=transactions)

def locate_balance(db): # <---- Calls database for bank_value #
    sql = "SELECT SUM(transactions) FROM atm_table;"
    return db.query(sql)

######################## MENU ###########################
def main_menu():    # <------ Defines Menu Class #
    print("1) Check Balance")
    print("2) Make a Deposit")
    print("3) Make a Withdrawal")
    print("4) Exit the ATM Interface")
    choice = input("> ")
    return choice   # <------ Returns the users input to be used #

##################### USER INTERFACE ######################

def ui_check_balance(db):   # <-- Menu Option to check Balance #
    print("Your Balance is: ")
    balances = locate_balance(db)
    for balance in balances:
        print(f" ${balance.sum}")

def ui_make_deposit(db):    # <-- Menu Option w/ input to Deposit #
    print("Making a Deposit -- ")
    deposit_amount = input("Choose an amount to deposit: ")
    deposit = 0 + int(deposit_amount)
    track_transactions(db, deposit)

def ui_make_withdrawal(db):     # <-- Menu Option w/ input to Withdrawal #
    print("Making a Withdrawal -- ")
    withdrawal_amount = input("Choose an amount to Withdrawal: ")
    withdraw = 0 - int(withdrawal_amount)
    track_transactions(db, withdraw)

################ Running Program #######################
print(f"Welcome to your Personal Bank Account:")   # <--------- Welcome Message #

############### Menu Functions ##########################
while True:
    userinput = main_menu()   # <----- Defines Main menu Input #
    if userinput == "1":
        ui_check_balance(db) # <----- Checks Balance #
    elif userinput == "2":
        ui_make_deposit(db) # <----- Makes a Deposit #
    elif userinput == "3":
        ui_make_withdrawal(db) # <----- Makes a Withdrawal #
    elif userinput == "4":
        exit(db) # <----- Exits the Program #
