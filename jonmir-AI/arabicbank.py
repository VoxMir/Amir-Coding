# Make a banking login that prints out a welcome message and ask for username and password
# if they are correct then show the bank balance else quit the program with an error message
import time
from jonmirAI.fish import thankuser

import arabic_reshaper
from bidi.algorithm import get_display


def input_a(text):
    # Shape Arabic letters
    reshaped = arabic_reshaper.reshape(text)

    # Reorder for display in LTR environments
    display_text = get_display(reshaped)

    return input(display_text)

def print_a(text):
    # Shape Arabic letters
    reshaped = arabic_reshaper.reshape(text)

    # Reorder for display in LTR environments
    display_text = get_display(reshaped)

    print(display_text)


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

        amountcheck = input_a("فحص مبلغ البنك (1) - العودة (2)")
        if amountcheck.lower() == "1":
            amount = saveamount.check_balance()
            print_a(f"رصيدك الحالي هو: ${amount}")
            time.sleep(1)
            return

        else:
            if amountcheck.lower() == "2":
                return


def otherhelp():
    while(True):
        support = input_a("هل ترغب في الحصول على المساعدة؟ (Y/N): ")
        if support.lower() == "y".lower():
            contactoption = input_a("حجز موعد (B) / التواصل مع الدعم (C): ")
            if contactoption.lower() == "b".lower():
                bookappointment = input_a("يعمل البنك خلال أيام الأسبوع، يرجى إدخال اليوم الذي ترغب بالحجز فيه: ")
                if bookappointment.lower() in ["الاثنين", "الثلاثاء", "الاربعاء", "الخميس", "الجمعة"]:
                    print_a("نعمل من الساعة 8 صباحًا حتى الساعة 4 مساءً.")
                    time.sleep(2)
                    print_a("يستغرق كل موعد ساعة واحدة.")
                    time.sleep(2)

                    appointmenttime = int(input_a("يرجى إدخال الساعة المناسبة لك: "))
                    if appointmenttime in [8, 9, 10, 11, 12, 13, 14, 15, 16]:
                        print_a("تم حجز موعدك بنجاح!")
                        time.sleep(2)
                        return

                    elif appointmenttime > 16 or appointmenttime < 7:
                        print_a("إدخال غير صالح")
                        time.sleep(1)

                else:
                    print_a("إدخال غير صالح")
                    time.sleep(1)


            elif contactoption.lower() == "c".lower():
                while(True):
                    supporthelp = input ("إرسال بريد إلكتروني / رقم هاتف البنك: ")
                    
                    if supporthelp.lower() == "رسال بريد إلكتروني".lower():
                        while (True):
                            emailconfirmation = input_a("يرجى إدخال أو تأكيد بريدك الإلكتروني: ")
                            if "@" in emailconfirmation and ".com" in emailconfirmation:
                                print_a("شكرًا للتأكيد. تأكد من صحة بريدك الإلكتروني.")
                                time.sleep(2)
                                confirmemail = input_a("إذا كان بريدك الإلكتروني صحيحًا فاكتب Y (أو N إذا لم يكن كذلك: ")
                                if confirmemail.lower() == "y".lower():
                                    while(True):
                                        emailmessage = input_a("اكتب رسالتك: ")
                                        if emailmessage != "":
                                            print_a("تم إرسال رسالتك إلى نظامنا.")
                                            time.sleep(1)
                                            print_a("ستتلقى ردًا على بريدك الإلكتروني خلال 3 أيام عمل.")
                                            time.sleep(2)
                                            thankuser()
                                        
                                        else:
                                            print_a("لم تكتب أي رسالة بعد.")
                                            time.sleep(1)
                                            stillsendmessage = input_a("هل ما زلت ترغب في إرسال رسالة؟ (Y/N): ")
                                            if stillsendmessage.lower() == "y".lower():
                                                continue
                                            else:
                                                thankuser()
                                        
                                    
                                elif confirmemail.lower() == "n".lower():
                                    continue
                                    
                                
                            else:
                                print_a("إدخال غير صالح")
                                time.sleep(2)
                                
                    elif supporthelp.lower() == "رقم هاتف البنك".lower():
                        print_a("يعمل مركز خدمة العملاء يوميًا من الساعة 8:00 صباحًا حتى 2:00 مساءً.")
                        time.sleep(1)
                        print_a("رقم بنك جونمير: +64 0223456789")
                        time.sleep(2)
                        thankuser()
                    
                    else:
                        print_a("إدخال غير صالح")
                        
                        
                    
                
        elif support.lower() == "n".lower():
            thankuser()
            time.sleep(1)
            exit()



            
            
def other_menu():
    
    while(True):
        other = input_a("إعادة تعيين كلمة المرور (R) / رصيد الحساب (B) / رجوع (G) / الدعم (C): ")
        if other.lower() == "r".lower():
            newpassword = input_a("يرجى إدخال كلمة المرور الجديدة (7 أحرف أو أكثر): ")
            if len(newpassword) < 7:
                print_a("يرجى إدخال كلمة مرور مكونة من 7 أحرف أو أكثر!")
                time.sleep(1)
            
            else:
                savepassword(newpassword)
                print_a("تم حفظ كلمة المرور بنجاح! :)")
                time.sleep(2)
                return 

        elif other.lower() == "b".lower():
            amountcheck = input_a("التحقق من رصيد الحساب (C) / رجوع (G): ")
            if amountcheck.lower() == "c".lower():
                with open("jonmiramount.txt") as file:
                    amount = file.read().strip()

                print_a(f"رصيد حسابك هو ${amount}")
                time.sleep(1)
                return
            
        elif other.lower() == "g".lower():
            return
        
        elif other.lower() == "c".lower():
            otherhelp()
        

def arabic_main():
    print_a("بنك جونمير - أهلاً بك")
    time.sleep(3)

    username = input_a("يرجى إدخال اسم المستخدم بالانكليزي: ")


    if getusername().lower() in username.lower():
        print_a(f"اهلا بك! {username}")

    else:
        raise ValueError("هذا المستخدم غير مسجل في نظامنا.")



    password = input_a("يرجى إدخال كلمة المرور بالانكليزي: ")


    if getpassword().lower() in password.lower():
        print_a(f"مرحبًا بك في بنك جونمير! {username}.")

        with open("jonmiramount.txt") as file:
            balance = int(file.read().strip())

    else:
        raise ValueError ("كلمة المرور غير صحيحة.")

    while(True):
        banking = input_a("اختر عملية: إيداع (D) / سحب (W) / خيارات أخرى (O) / خروج (E): ")
        if banking.lower() == "d".lower():
            while(True):
                depositing = input_a("أدخل مبلغ الإيداع (أو اكتب 0 للخروج): ")
                if check_amount_input(depositing, 5000) == False:
                    print_a("إدخال غير صالح")
                    time.sleep(1)
                
                else:
                    break
            balance = balance + int(depositing)
            print_a(f"تم الإيداع بنجاح. الرصيد الحالي: ${balance}")
            time.sleep(3)
            otherhelp()


        elif banking.lower() == "W".lower():
            while(True):
                withdrawing = input_a("أدخل مبلغ السحب (أو اكتب 0 للخروج): ")
                if check_amount_input(withdrawing, 10000) == False:
                    print_a("إدخال غير صالح")
                    time.sleep(1)

                else:
                    break
            balance = balance - int(withdrawing)
            print (f"تم السحب بنجاح. الرصيد الحالي: ${balance}")
            time.sleep(2)
            otherhelp()

        elif banking.lower() == "e".lower():
            thankuser()

        elif banking.lower() == "o".lower():
            other_menu()