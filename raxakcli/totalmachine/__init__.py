import dialog 
import dashboardoptions
import  sys
import  commands
import sys
import ast
sys.path.append('/home/raxak/raxak1/')
import cloudraxak
def get_info():
	output = cloudraxak.getIPs('sanjeev@esoftech.com')
	get_output=str(output).replace("'","")
	get_lst = ast.literal_eval(get_output)
	get_information = ''
	get_access = ''
	get_line = ''
	for x in get_lst:
		access = x["access"]
		if access == "-2":
			get_access = 'Not reachable'
		elif(access == "1"):
			get_access = 'reachable'
		elif(access == "-3"):
			get_access = "notreachablesip"
		get_line ="\t\t"+x["ip"]+"\t\t"+x["nickname"]+"\t\t"+get_access+"\n\n"
		get_information = get_information+get_line
	return get_information

# method to call the different dialog methods depending on the user's selection
def config():
        # instantiate the dialog class. here d is the instance of the class Dialog
        d = dialog.Dialog(dialog="dialog")
        d.add_persistent_args(["--backtitle", "Raxak"])
	#username = whoami_api["user"]
	user_file = open('usernamefile', 'r')
	username_read = user_file.readlines();
	usernameget = str(username_read).replace('[','') 
	username = str(usernameget).replace(']','') 
	output = get_info()
	output = '\t\tUsername\t\tNicknamet\t\t\tStatus\n\n\n' + str(output);
	d.scrollbox("%s" % output, title="Raxak")
	#answer = dashboardoptions.choose_option(d)   
    #dashboardoptions.show_options(d, answer)     
