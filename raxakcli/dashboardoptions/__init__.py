import sys,commands 
#import changedns
import  options
import  dashboard
import totalmachine
import dashboardoptions
# method which shows the dialog that handles the 'ESC' 'Cancel' events
def handle_exit_code(d, code):
	# if the users clicks 'Cancel' or presses 'ESC' button
	if code in (d.DIALOG_CANCEL, d.DIALOG_ESC):
		options.config()
		return 0

	else:
		return 1


# method to execute the command
def show_options(d, answer):
	if answer == 'Total Machine':
		#totalmachine.config()
		d.msgbox("Hello World", title="Raxak Information")
		dashboardoptions.choose_option(d)
		#print ''
		
	#if answer == 'Running Machine':
	#	totalmachine.config()
		
	#if answer == 'Schedular':
	#	totalmachine.config()
		#volumeinfo.config()
	#	print 
		
	#if answer == 'Rule status':
	#	totalmachine.config()
		#shutrestart.config()
		#diskinfo.config()
	#	print 
		
# method to show the menu dialog 'set date' and 'set time'
def choose_option(d):
	while 1:
		(code, tag) = d.menu("Select an option", width=60, 
			choices=[("Total Machine", ""),
				])
					
					
		if handle_exit_code(d, code):	# if the user presses 'ESC' or clicks 'Cancel' option
			break			# exit from the app
			
	return tag


