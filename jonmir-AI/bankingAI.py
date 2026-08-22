# Make a banking login that prints out a welcome message and ask for username and password
# if they are correct then show the bank balance else quit the program with an error message
import time
from flask import Flask
from fish import thankuser
from arabicbank import arabic_main

def check_amount_input(input, max):
    try:
        integer = int(input)
    except ValueError:
        return False


    if integer == 0:
        thankuser()


    elif integer < 0 or integer > max:
        return False
    else:
        return True
    
def getusername():
    with open("jonmiruser.txt") as usernamefile:
        return usernamefile.read()

def getpassword():
    with open("jonmirpw.txt") as passwordfile:
        return passwordfile.read()

def saveamount(newamount):
    with open("jonmirbankamount.txt") as amountfile:
        amountfile.write(newamount)

def savepassword(newpassword):
    with open("jonmirpw.txt", "w") as passwordfile:
        passwordfile.write(newpassword)
        return

def checkamount(newamount):
    while(True):
        with open("jonmiramount.txt", "w") as accountbalance:
            accountbalance.write(str(newamount))

        amountcheck = input("Check Account Balance (C) / Go Back (G):")
        if amountcheck.lower() == "c".lower():
            amount = saveamount.check_balance()
            print(f"Your account balance is ${amount}")
            time.sleep(1)
            return

        else:
            if amountcheck.lower() == "g".lower():
                return


def otherhelp():
    while(True):
        support = input("Would you like to receive help? Y/N: ")
        if support.lower() == "y".lower():
            contactoption = input("Book an appointment (B) / Contact Support (C): ")
            if contactoption.lower() == "b".lower():
                bookappointment = input("Our Bank Operates on weekdays, please enter the weekday you want to book in: ")
                if bookappointment.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
                    print("We operate from 8 AM until 16 PM.")
                    time.sleep(2)
                    print("Every appointment takes us an hour to finish")
                    time.sleep(2)

                    appointmenttime = int(input("Please enter the hour that fits you well: "))
                    if appointmenttime in [8, 9, 10, 11, 12, 13, 14, 15, 16]:
                        print("Your appointment has been booked!")
                        time.sleep(2)
                        return

                    elif appointmenttime > 16 or appointmenttime < 7:
                        print("Invalid input")
                        time.sleep(1)

                else:
                    print("Invalid input")
                    time.sleep(1)


            elif contactoption.lower() == "c".lower():
                while(True):
                    supporthelp = input ("send an email / bank contact number: ")
                    
                    if supporthelp.lower() == "Send An Email".lower():
                        while (True):
                            emailconfirmation = input("Please enter/confirm your email address: ")
                            if "@" in emailconfirmation and ".com" in emailconfirmation:
                                print("Thank you for confirming. Make sure your email is valid")
                                time.sleep(2)
                                confirmemail = input("If your email is valid, please write Y ('N' if not): ")
                                if confirmemail.lower() == "y".lower():
                                    while(True):
                                        emailmessage = input("Enter your message: ")
                                        if emailmessage != "":
                                            print("Your message has been submitted to our system.")
                                            time.sleep(1)
                                            print("Expect a response back to your email within 3 business days")
                                            time.sleep(2)
                                            thankuser()
                                        
                                        else:
                                            print("You have not written anything yet.")
                                            time.sleep(1)
                                            stillsendmessage = input("Would you like to still send a message? (Y/N)")
                                            if stillsendmessage.lower() == "y".lower():
                                                continue
                                            else:
                                                thankuser()
                                        
                                    
                                elif confirmemail.lower() == "n".lower():
                                    continue
                                    
                                
                            else:
                                print("invalid input.")
                                time.sleep(2)
                                
                    elif supporthelp.lower() == "Bank Contact Number".lower():
                        print("Our Call Support Center Operates Everyday From 8:00 AM until 14:00 PM")
                        time.sleep(1)
                        print("JonMir Bank Number: +64 0223456789")
                        time.sleep(2)
                        thankuser()
                    
                    else:
                        print("Invalid Input")
                        
                        
                    
                
        elif support.lower() == "n".lower():
            thankuser()
            time.sleep(1)
            exit()



            
            
def other_menu():
    
    while(True):
        other = input("Reset Password (R) / Account Balance (B) / Go Back (G) / Contact Support (C): ")
        if other.lower() == "r".lower():
            newpassword = input("Please type your new password (7+): ")
            if len(newpassword) < 7:
                print("Please type a password that is 7 characters or longer!")
                time.sleep(1)
            
            else:
                savepassword(newpassword)
                print("successfully saved your password! :)")
                time.sleep(2)
                return 

        elif other.lower() == "b".lower():
            amountcheck = input("Check Account Balance (C) / Go Back (G):")
            if amountcheck.lower() == "c".lower():
                with open("jonmiramount.txt") as file:
                    amount = file.read().strip()

                print(f"Your account balance is ${amount}")
                time.sleep(1)
                return
            
        elif other.lower() == "g".lower():
            return
        
        elif other.lower() == "c".lower():
            otherhelp()
        

def main():
    print("JonMir Bank - Welcome User")
    time.sleep(3)
    tuple1 = (1,2,3)
    tuple1 = tuple1 * 2
    print(tuple1)
    
    chooselanguage = input("Please choose your preferred language -> English (E) / Arabic (A): ")
    if chooselanguage.lower() == "a".lower():
        arabic_main()
    
    elif chooselanguage.lower() == "e".lower():
        username = input("Please enter your username: ")


        if getusername().lower() in username.lower():
            print(f"Hello {username}")

        else:
            raise ValueError("Member is not registered in our system.")



        password = input("Please enter your password: ")


        if getpassword().lower() in password.lower():
            print(f"Welcome to JonMir Bank, {username}.")

            with open("jonmiramount.txt") as file:
                balance = int(file.read().strip())

        else:
            raise ValueError ("Incorrect Password")

        while(True):
            banking = input("Would you like to: Deposit (D) / Withdraw (W) / Other (O): / Exit (E): ")
            if banking.lower() == "d".lower():
                while(True):
                    depositing = input("Deposit Amount (Or type '0' to exit): ")
                    if check_amount_input(depositing, 5000) == False:
                        print("Invalid input")
                        time.sleep(1)
                    
                    else:
                        break
                balance = balance + int(depositing)
                print(f"Successfully Deposited ${balance}")
                time.sleep(3)
                otherhelp()


            elif banking.lower() == "W".lower():
                while(True):
                    withdrawing = input("Withdraw Amount (Or type '0' to exit): ")
                    if check_amount_input(withdrawing, 10000) == False:
                        print("Invalid input")
                        time.sleep(1)

                    else:
                        break
                balance = balance - int(withdrawing)
                print (f"Successfully Withdrawn ${balance}")
                time.sleep(2)
                otherhelp()

            elif banking.lower() == "e".lower():
                thankuser()

            elif banking.lower() == "o".lower():
                other_menu()
        


if __name__ == "__main__":
    main()