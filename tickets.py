'''
This programs is used to buy tickets for the movie Robot wars
It uses tkinter as GUI
'''

from tkinter import *
import tkinter as tk
from datetime import datetime
import sys

values = []
now = datetime.now()


def first_screen():
    '''
    This function is called by the main function.
    It shows the welocme screen and asks the user to purchase tickets
    '''
    global screen
    screen = tk.Tk()
    screen.geometry("400x550")
    screen.title("E-tickets")
    stars = "*  " * 15
    Label(text="\n \n").pack()
    Label(text=stars, font=("Luminari", 20)).pack()
    Label(text="W E L C O M E", font=("Arial", 30)).pack()
    Label(text="TO THE E-TICKETS APP", font=("Arial", 15)).pack()
    Label(text=stars + "\n \n", font=("Luminari", 20)).pack()
    Label(text="Please click here to purchase your tickets \n",
          font=("Arial", 14)).pack()
    Button(text='Purchase tickets', height="4", width="30",
           font=("Times New Roman", 17), command=purchase).pack()
    Label(text="").pack()
    Label(text="program developer: charan \n student ID: 34567",
          font=("Times new roman", 20)).pack(side='left')

    tk.mainloop()


def purchase():
    '''
    This function is called when the clicks on the button to purchase tickets
    It takes the number of  children, adults, seniors and veterans from the
    user and sends the data to the verify function.
    '''
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("400x550")
    screen1.title("E-tickets")
    global child, adult, senior, veteran
    child = StringVar()
    adult = StringVar()
    senior = StringVar()
    veteran = StringVar()
    Label(screen1, text="Please enter the no of tickets you want to buy \n \n",
          font=("Times new roman", 20)).pack()

    Label(screen1, text="Child    15$ each",
          font=("Times new roman", 20)).pack()
    child_entry = Entry(screen1, textvariable=child)
    child_entry.pack()
    Label(screen1, text="Adult    30$ each",
          font=("Times new roman", 20)).pack()
    adult_entry = Entry(screen1, textvariable=adult)
    adult_entry.pack()
    Label(screen1, text="Senior    20$ each",
          font=("Times new roman", 20)).pack()
    senior_entry = Entry(screen1, textvariable=senior)
    senior_entry.pack()
    Label(screen1, text="Veteran concession    20$ each",
          font=("Times new roman", 20)).pack()
    veteran_entry = Entry(screen1, textvariable=veteran)
    veteran_entry.pack()
    Button(screen1, text="Submit", width=10,
           height=1, command=verify).pack()


def verify():
    '''
    This function verifies the data and appends it to the values list.
    It also calculates the total price th euser has to pay.
    '''
    global screen2
    screen2 = Toplevel(screen1)
    screen2.geometry("400x550")
    screen2.title("E-tickets")
    child_entry = child.get()
    adult_entry = adult.get()
    senior_entry = senior.get()
    veteran_entry = veteran.get()

    Label(screen2, text="Verify your transaction", bg="#787878",
          width="300", height="2", font=("Luminari", 17),
          fg="white").pack()
    Label(screen2, text="\n \n").pack()
    Label(screen2, text="Your selection \n", fg="red",
          font=("Times new roman", 25)).pack()

    if child_entry.isnumeric():
        values.append(int(child_entry))
        Label(screen2, text="Children: " + child_entry + " * 15$",
              font=("Times new roman", 20)).pack()
    else:
        values.append(0)

    if adult_entry.isnumeric():
        values.append(int(adult_entry))
        Label(screen2, text="Adults: " + adult_entry + " * 30$",
              font=("Times new roman", 20)).pack()
    else:
        values.append(0)

    if senior_entry.isnumeric():
        values.append(int(senior_entry))
        Label(screen2, text="Seniors: " + senior_entry + " * 20$",
              font=("Times new roman", 20)).pack()
    else:
        values.append(0)

    if veteran_entry.isnumeric():
        values.append(int(veteran_entry))
        Label(screen2, text="Veteran consession: " + veteran_entry + " * 20$",
              font=("Times new roman", 20)).pack()
    else:
        values.append(0)

    total = values[0] * 15 + values[1] * 30 + values[2] * 20 + values[3] * 20
    verify.total = str(total)

    Label(screen2, text="Total: " + verify.total + "$",
          font=("Times 20 bold underline")).pack()
    Label(screen2, text="\n \n").pack()
    Button(screen2, text="Confirm", width=10,
           height=1, command=checkout).pack()


def checkout():
    '''
    If the user confirms the total, it calls the checkout function.
    THis function takes the credit card details of the user.

    '''
    global screen3
    screen3 = Toplevel(screen1)
    screen3.geometry("400x550")
    screen3.title("E-tickets")
    global credit_number, credit_name, mmyy, cvv

    credit_number = StringVar()
    credit_name = StringVar()
    mmyy = StringVar()
    cvv = StringVar()

    Label(screen3, text="Checkout", bg="#787878", width="300", height="2",
          font=("Luminari", 17), fg="white").pack()

    Label(screen3, text="Please enter your credit card number",
          font=("Times 20 italic")).pack()
    credit_number_entry = Entry(screen3, textvariable=credit_number)
    credit_number_entry.pack()
    Label(screen3, text="Name on credit card", font=("Times 20 italic")).pack()
    credit_name_entry = Entry(screen3, textvariable=credit_name)
    credit_name_entry.pack()
    Label(screen3, text="Expiry month/year in mmyy format",
          font=("Times 20 italic")).pack()
    credit_mmyy_entry = Entry(screen3, textvariable=mmyy)
    credit_mmyy_entry.pack()
    Label(screen3, text="CVV", font=("Times 15 italic")).pack()
    credit_cvv_entry = Entry(screen3, textvariable=cvv)
    credit_cvv_entry.pack()
    Label(screen3, text="\n \n").pack()
    Label(screen3, text="Total amount to be paid: " + verify.total + "$ \n",
          fg="green", font=("Times 20 italic")).pack()

    Button(screen3, text="Submit", width=10,
           height=1, command=transaction_check).pack()


def transaction_check():
    '''
    This function check sthe validity of the credit card and if
    correct then adds the transaction details to  transactions.txt file
    It also calls the transaction function.
    '''
    credit_number_entry = credit_number.get()
    credit_name_entry = credit_name.get()
    credit_mmyy_entry = mmyy.get()
    credit_cvv_entry = cvv.get()

    if (credit_number_entry.isnumeric() and
        credit_number_entry != '' and
        credit_name_entry != '' and
        len(credit_mmyy_entry) == 4 and
        credit_mmyy_entry != '' and
        credit_mmyy_entry.isnumeric() and
        credit_cvv_entry.isnumeric() and
        credit_cvv_entry != '' and
        len(credit_cvv_entry) == 3):

        data = {'credt_card_number': credit_number_entry,
                'credit_card_name': credit_name_entry,
                'credit_card_expiry': credit_mmyy_entry,
                'tickets sold': str(values[0]) +
                " children, " + str(values[1]) +
                " adults, " + str(values[2]) +
                " seniors, " + str(values[3]) + " veterans",
                'transaction time': str(now)}

        datas = str(data) + "\n"
        print (datas)
        f2 = open("transactions.txt", "a+")
        f2.write(datas)
        f2.close()
        transaction()

    else:
        Label(screen3, text="**Please verify the fields you entered**",
              fg="red", font=("Times 20 italic")).pack()


def transaction():
    '''
    This function gives the reciept of the transaction to the user.
    '''
    global screen4
    screen4 = Toplevel(screen1)
    screen4.geometry("400x550")
    screen4.title("E-tickets")
    Label(screen4, text="Receipt", bg="#787878",
          width="300", height="2", fg="white", font=("Luminari 17 bold")
          ).pack()

    Label(screen4, text="Transaction successful",
          fg="green", font=("Times 20 italic")).pack()
    Label(screen4, text="Receipt", fg="blue",
          font=("Times 20 italic underline bold")).pack()
    Label(screen4, text="Movie: Robot Wars \n tickets booked for \n" +
          str(values[0]) + " children, \n " + str(values[1]) + " adults, \n" +
          str(values[2]) + " seniors, \n" + str(values[3]) + " veterans",
          font=("Times 20")).pack()

    Label(screen4, text="Total amount paid: " + verify.total + "$",
          font=("Times 20")).pack()
    Label(screen4, text="Transaction time: " + str(now),
          font=("Times 20 italic")).pack()
    Label(screen4, text="").pack()

    Button(screen4, text="Quit", width=10,
           height=1, command=quit).pack()
    Label(screen4, text="\n \n").pack()
    Label(screen4, text="* please present this reciept at the movie theatre",
          fg="red", font=("Times 20 italic")).pack()


def quit():
    '''
    This function is called when you are done
    with your transaction and want to quit the program.
    Uses sys module.
    '''
    sys.exit(0)


if __name__ == '__main__':
    '''
    This is the main function which only calls the first screen function.
    '''
    first_screen()
