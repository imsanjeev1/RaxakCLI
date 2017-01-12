#!/usr/bin/python
import dialog, sys
import loginmodule
import commands, os
import commands,os
from time import strftime
	
def config():
	# instantiate the dialog class. here d is the instance of the class Dialog
	d = dialog.Dialog(dialog="dialog")

	d.add_persistent_args(["--backtitle", "Raxak/ %s" % strftime('%d-%b-%Y %H:%M:%S')])
	answer = loginmodule.get_password(d)

# main method which calls all the required sub modules.
# the main dialog is called in the method config().
# this contains all the dialogs in the cli application
def main():
        try:
                # try block for getting any exception
                config()

        # exception handler
        except dialog.error, exc_instance:
                sys.stderr.write("Error:\n\n%s\n" % exc_instance.complete_message())
                return 1

        return 0

# call the main function. this is the starting point of a program
if __name__ == "__main__": main()
