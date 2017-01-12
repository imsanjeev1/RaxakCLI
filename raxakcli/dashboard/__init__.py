import dialog, sys 
import dashboardoptions
	
def config():
	# instantiate the dialog class. here d is the instance of the class Dialog
	d = dialog.Dialog(dialog="dialog")

	d.add_persistent_args(["--backtitle", "Raxak"])

	# display options window or menu screen.
	answer = dashboardoptions.choose_option(d)
	dashboardoptions.show_options(d, answer)
