#### IMPORTS #########
import records
db = records.Database("postgres://localhost/atm")

############## Database Interactions ####################

def make_deposit(db, bank_value, deposit_amount):
    sql = "UPDATE atm_table SET bank_value = bank_value + deposit_amount"
    return db.query(sql)

def make_withdrawal(db, bank_value, withdrawl_amount):
    sql = "UPDATE atm_table SET bank_value = bank_value - withdrawl_amount"
    return db.query(sql)

def locate_balance(db):
    sql = "SELECT bank_value FROM atm_table"
    return db.query(sql)

######################## MENU ###########################
def main_menu():    # <------Defines Menu Class #
    print("1) Check Balance")
    print("2) Make a Deposit")
    print("3) Make a Withdrawal")
    print("4) Exit the ATM Interface")
    choice = input("> ")
    return choice   # <------ Returns the users input to be used #

##################### USER INTERFACE ######################

def ui_check_balance(db):
    print("Your Balance is: ")
    balances = locate_balance(db)
    for balance in balances:
        print(f" ${balance.bank_value}")

def ui_make_deposit(db):
    print("Making a Deposit -- ")
    deposit_amount = input("Choose an amount to deposit: ")
    make_deposit(db, deposit_amount)


def ui_make_withdrawal(db):
    print("Youve Withdrawn: ")
    Withdrawal_amount = input("Choose an amount to Withdrawal: ")
    make_withdrawal(db, withdrawl_amount)


################ Running Program #######################
print(f"Welcome to your Personal Bank Account {user_name}")   # <--------- Welcome Message #

############### Menu Functions ##########################
while True:
    userinput = main_menu()   # <----- Defines Main menu Input #
    if userinput == "1":
        ui_check_balance(db) # <----- Checks Balance
    elif userinput == "2":
        ui_make_deposit(db) # <----- Makes a Deposit
    elif userinput == "3":
        ui_make_withdrawal(db) # <----- Makes a Withdrawal
    elif userinput == "4":
        exit(db) # <----- Exits the Program
