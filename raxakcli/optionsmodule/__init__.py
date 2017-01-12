import sys 
import dashboard

# method which shows the dialog that handles the 'ESC' 'Cancel' events
def handle_exit_code(d, code):
	# if the users clicks 'Cancel' or presses 'ESC' button
	if code in (d.DIALOG_CANCEL, d.DIALOG_ESC):
		# if the user clicks the 'Cancel button'
		if code == d.DIALOG_CANCEL:
			msg = "Are you sure you want to exit?"
		
		else:	# case for 'ESC'
			msg = "You pressed ESC. Do you really want to quit?"
			
		if d.yesno(msg) == d.DIALOG_OK: 	# if the user clicks 'OK' further, app terminates
			# write a snippet here to go back to main menu
			d.msgbox('Good Bye!', width = 30, height = 5)
			sys.exit(0)
			return 0
			
	else:
		return 1


# method to execute the command
def show_options(d, answer):
	if answer == 'DashBoard':
		dashboard.config()
		#print ''
		
	#if answer == 'SelectProfile':
	#	print 

def choose_option(d):
	while 1:
		(code, tag) = d.menu("Select an option", width=60, 
			choices=[("DashBoard", ""),""])

		if handle_exit_code(d, code):	# if the user presses 'ESC' or clicks 'Cancel' option
			break			# exit from the app
			
	return tag


