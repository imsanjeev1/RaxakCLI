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


def get_password(d):
        while 1:
                (code, password) = d.passwordbox("Please Enter Your CLI password", width = 60)

                if handle_exit_code(d, code):
                        break
        return password

if d.yesno("Are you REALLY sure you want to see this?") == d.OK:
    d.passwordbox("Please Enter Your CLI password", width = 60)
    d.msgbox("You have been warned...")

    # We could put non-empty items here (not only the tag for each entry)
    code, tags = d.checklist("What sandwich toppings do you like?",
                             choices=[("Catsup", "",             False),
                                      ("Mustard", "",            False),
                                      ("Pesto", "",              False),
                                      ("Mayonnaise", "",         True),
                                      ("Horse radish","",        True),
                                      ("Sun-dried tomatoes", "", True)],
                             title="Do you prefer ham or spam?",
                             backtitle="And now, for something "
                             "completely different...")
    if code == d.OK:
        # 'tags' now contains a list of the toppings chosen by the user
        pass
else:
    code, tag = d.menu("OK, then you have two options:",
                       choices=[("(1)", "Leave this fascinating example"),
                                ("(2)", "Leave this fascinating example")])
    if code == d.OK:
        # 'tag' is now either "(1)" or "(2)"
        pass
