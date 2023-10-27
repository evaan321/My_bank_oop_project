from Bank import Bank, User


def main():
    Dbbl = Bank("Dbbl")
    print("----------------- Welcome To Dbbl ----------------")
    while True:

        print("Press 1 for Admin Access Press 2 for User Access")

        choice = input()

        if choice == "1":
            print("Enter Pass")
            if input() == '123':
                print("Login Successful \n \n")
            while True:
                print("Enter 1 to create An account")
                print("Enter 2 to Delete Account")
                print("Enter 3 to See All Accounts")
                print("Enter 4 to Check Available Balance of Bank")
                print("Enter 5 to Check Loan History")
                print("Enter 6 to turn on or off the Loan feature")
                print("Enter 7 to exit Admin Panel")
                choice1 = input()
                if choice1 == "1":
                    print("Enter Name , Email and The type of account u want to open")
                    name = input()
                    email = input()
                    acType = input()
                    user1 = User(name, email, acType)
                    Dbbl.ac_holders[user1.acNumber] = user1
                    print(
                        f'\n \n --------- Account successfully created account number : {user1.acNumber}    ------------\n \n')

                if choice1 == "2":
                    print("Enter Ac Number of the account you want to delete")
                    acN = input()
                    if acN in Dbbl.ac_holders:
                        del Dbbl.ac_holders[acN]

                    else:
                        print("Account doesn't Exist")

                if choice1 == "3":
                    i=1
                    for key, value in Dbbl.ac_holders.items():
                        print(f'{i}: Account Number: {key}, Account name: {value.name}, Account Email: {value.email} , Account Type: {value.acType}')

                        i+=1
                    i=1
                if choice1 == "4":

                    print(Dbbl.bank_balance)

                if choice1 == "5":
                    print(Dbbl.loan_amount)

                if choice1 == "6":


                    print("Enter 1 to Turn on the Loan Feature")
                    print("Enter 2 to Turn off the Loan Feature")
                    lnFeature = input()
                    if lnFeature == "1": Dbbl.loan_on()
                    if lnFeature == "2": Dbbl.loan_off()
                if choice1 == "7":

                    break

            else:
                print("Wrong Password")

        if choice == "2":
            while True:
                print("Enter 1 to create An account")
                print("Enter 2 to Deposit balance")
                print("Enter 3 to Withdraw Balance")
                print("Enter 4 to Check Available Balance")
                print("Enter 5 to Check Transaction history")
                print("Enter 6 to take loan")
                print("Enter 7 to transfer money to Other Account")
                print("Enter 8 to exit User Panel")
                choice1 = input()

                if choice1 == "1":
                    print("Enter Name , Email and The type of account u want to open")
                    name = input()
                    email = input()
                    acType = input()
                    user1 = User(name, email, acType)
                    Dbbl.ac_holders[user1.acNumber] = user1
                    print(
                        f'\n \n --------- Account successfully created account number : {user1.acNumber}------------\n \n')
                if choice1 == "2":
                    print("Enter ur Account number")
                    acN = input()
                    if acN in Dbbl.ac_holders:
                        print("Enter the Amount you want to deposit")
                        amnt = int(input())
                        Dbbl.ac_holders[acN].deposit_money(amnt)
                        Dbbl.bank_balance += amnt

                    else:
                        print("   Account Doesnot Exist   ")
                if choice1 == "3":
                    print("Enter ur Account number")
                    acN = input()
                    if acN in Dbbl.ac_holders:
                        print("Enter the Amount you want to Withdraw")
                        amnt = int(input())
                        if Dbbl.bank_balance >= amnt:
                            Dbbl.ac_holders[acN].withdraw_money(amnt)
                        else:
                            print("Bankrupt")
                    else:
                        print("   Account Doesnot Exist   ")
                if choice1 == "4":
                    print("Enter ur Account number")
                    acN = input()
                    if acN in Dbbl.ac_holders:
                        Dbbl.ac_holders[acN].check_balance()
                if choice1 == "5":
                    print("Enter ur Account number")
                    acN = input()
                    if acN in Dbbl.ac_holders:
                        Dbbl.ac_holders[acN].transaction_history()
                    else:
                        print("   Account Doesnot Exist   ")
                if choice1 == "6":
                    print("Enter ur Account number")
                    acN = input()
                    if acN in Dbbl.ac_holders:
                        if Dbbl.ac_holders[acN].loan_taken < Dbbl.loan_limit:
                            print("Enter how much Loan u want")
                            loan_amnt = int(input())
                            if loan_amnt <= Dbbl.bank_balance:
                                Dbbl.ac_holders[acN].balance += loan_amnt
                                Dbbl.ac_holders[acN].loan_taken += 1
                                Dbbl.loan_amount += loan_amnt
                                Dbbl.ac_holders[acN].transHistory.append(f"Loan Taken from bank {loan_amnt} Taka")
                                print(f"Loan Taken from bank {loan_amnt} Taka Now Balance {Dbbl.ac_holders[acN].balance} Taka")
                            else:
                                print("Bankrupt")
                        else:
                            print("Cant take anymore Loan")
                    else:
                        print("   Account Doesnot Exist   ")
                if choice1 == "7":
                    print("Enter ur Account number")
                    acN = input()
                    print("Enter Account number u want to send")
                    SacN = input()

                    if acN in Dbbl.ac_holders and SacN in Dbbl.ac_holders:
                        print("Enter the Amount U want to send ")
                        amnt = int(input())
                        if amnt <= Dbbl.bank_balance and amnt <= Dbbl.ac_holders[acN].balance:
                            Dbbl.ac_holders[acN].balance -= amnt
                            Dbbl.ac_holders[SacN].balance += amnt
                            Dbbl.ac_holders[acN].transHistory.append(f"Money Send To {SacN} : {amnt} Taka")
                            Dbbl.ac_holders[SacN].transHistory.append(f"Money Recieved From {SacN} : {amnt} Taka")
                        else:
                            print("Not Enough Balance")

                    else:
                        print("Wrong Account number")

                if choice1 == "8":
                    break


main()
