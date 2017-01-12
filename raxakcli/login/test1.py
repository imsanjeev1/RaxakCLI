#! /usr/bin/env python

import locale
from dialog import Dialog

d = Dialog(dialog="dialog")

def handle_exit_code(d, code):
        # if the users clicks 'Cancel' or presses 'ESC' button
        if code in (d.DIALOG_CANCEL, d.DIALOG_ESC):
                # if the user clicks the 'Cancel button'
                if code == d.DIALOG_CANCEL:
                        msg = "Are you sure you want to exit?"

                else:   # case for 'ESC'
                        msg = "You pressed ESC. Do you really want to quit?"

                if d.yesno(msg) == d.DIALOG_OK:         # if the user clicks 'OK' further, app terminates
                        # write a snippet here to go back to main menu
                        d.msgbox('Good Bye!', width = 20, height = 5)
                        return 0

        else:
		return 1


#(code, password) = d.passwordbox("Please Enter Your CLI password", width = 60)
d.passwordbox("Please Enter Your CLI password", width = 60)
def get_password(d):
        while 1:
                (code, password) = d.passwordbox("Please Enter Your CLI password", width = 60)

                if handle_exit_code(d, code):
                        break
        return password


# method to show the status message dialog and go back to main menu
def show_message(d, string):
        password = commands.getoutput('grep "Password=" /root/usersfile')

        if string == password:
                fs2cli.config()

        # Added by Mohan for testing purpose
        elif (password == 'Peg@NETWEB@Delhi'):
                print '';

        else:
                d.msgbox("Invalid Password")
                login.config()


# method to execute the command
def show_options(d, answer):
        password = answer

        enpasswd = password.encode("base64", "strict")
        enpasswd = enpasswd.strip()

        pwdstring = 'Password=' + enpasswd

        show_message(d, pwdstring)

#def get_password(d):
#        while 1:
#                (code, password) = d.passwordbox("Please Enter Your CLI password", width = 60)

#                if handle_exit_code(d, code):
#                        break
#        return password
