#!/usr/bin/python
import  sys
import commands
sys.path.append("../")
import  login
import  options
sys.path.append('/home/raxak/raxak1/')
import cloudraxak

# method which shows the dialog that handles the 'ESC' 'Cancel' events
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
			d.msgbox('Are you sure want to Logout!', width = 20, height = 5)
			#sys.exit(0)	
                        return 0

        else:
                return 1

def get_username(d):
	while 1:
        	(code, username) = d.inputbox("Please Enter Your username", width = 30)
		if handle_exit_code(d, code):
			break
	return username



def get_password(d):
	while 1:
        	(code, password) = d.passwordbox("Please Enter Your CLI password", width = 40)

		if handle_exit_code(d, code):
			break
	return password


# method to show the status message dialog and go back to main menu
def signin(d, usr, passd):
	signin = cloudraxak.Signin(usr,passd)
	status_get = signin['status']
	if status_get == "True":
		user_file = open('usernamefile', 'w')
		user_file.write(usr)
		user_file.close()
		options.config()
		#print 
	else:
		status_get = signin['message']
		d.msgbox(status_get)
		login.config()

