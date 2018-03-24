#Modules
import os, sys,time#Import Other Coding languages
try:
	import json
	import socket
	import urllib2
	import random
	import selenium
	import requests
	import optparse
	import colorama
	import pygoogling
	import ConfigParser
	import logging,urllib
	from time import strftime
	from threading import Thread
	from selenium import webdriver
	from optparse import OptionParser
	from colorama import init, Fore, Back, Style
	from pygoogling.googling import GoogleSearch
except ImportError: #If you dont have the required modules this error will help install them for you
	print ('Do you have all of the needed Modules ? colorama, selenium, requests, json,Google Search, and urllib2!!')
	time.sleep(1)
	yn = raw_input('Would You Like To Install Them Now? y/n: ')
	if yn == 'n': 
		sys.exit()
	if yn == 'y':
		os.system('pip install selenium')
		os.system('pip install colorama')
		os.system('pip install  gsearch')
		os.system('pip install json')
		os.system('pip install requests')
		os.system('pip install socket')
		os.system('pip install urllib2')
		os.system('pip install os')
		os.system('pip install sys')
		os.system('pip install time')
		os.system('pip install optparse')
		os.system('pip install ConfigParser')
		os.system('pip install urllib')
		os.system('pip install logging')
		os.system('pip install threading')
		os.system('pip install pygoogling')
	'''
	Allows the program to find the build and sats 

	'''
x = os.path.dirname(os.path.abspath(__file__))
builddata = open(x+'/Extra/Build.cfg','r')
config = ConfigParser.RawConfigParser() 
config.readfp(builddata)
build = config.get('mercury', 'build')
parser = optparse.OptionParser()
parser.add_option('-f', '--file', action="store", dest="file_path", help="Zip File Path", default=None)
parser.add_option('-w', '--word_list', action="store", dest="word_list", help="Word List Path", default=None)
headers_useragents=[]
init(convert=True)


termsAndConditions = Fore.RED + '''Don`t Use Mercury To:
create and share malicious viruses, illegally harm others computers, 
interrupt wifi / bluetooth signals without permission, violate security, 
and violate privacy

'''
#terms and condtions 
            
def extra_long():
	time.sleep(10) #Pause == 4 Secs
def long():
	time.sleep(5) #Pause == 3 Secs
def quick():
	time.sleep(2) #Pause == 2 Secs
def clear():
	os.system('cls') #Change To 'clear' If Running Linux ! 
def space():
	print ' '
	print ' '	

def agreement():
 afile = open(x+'/Extra/Mercury.txt','r+')
 term = afile.readlines() # Creates a list of lines called term
 for line in term: #for lines in term
     print(line) #prints line
     if 'yes' in line: #if you agreed skip to main menu
         found = True
         clear()
         mainmenu()
     if ' ' in line: #if not load up terms
         found = False
         clear()
         print(termsAndConditions)
         agree = raw_input(Fore.YELLOW + 'Type "yes" To Agree: ')
         if agree == 'yes': #saves agree
             file = open(x+'\Extra\Mercury.txt','w')
             afile.write('yes')
             file.close()
             afile.close()

	
		  
def readme():
	clear()
	readme = open(x+'/README!!!.md','r') #opens file
	license = open(x+'/License', 'r') #opens file
	file_contents = readme.read() #reads file
	file_contents2 = license.read() #reads file
	print (file_contents) #prints ReadMe
	space()
	extra_long()
	clear()
	print (file_contents2) #print License
	extra_long()
	mainmenu()

def pythoni():
	clear()
	try:
		os.system('python') #loads python
	except KeyboardInterrupt: #returns to main menu if ctrl C is used
		mainmenu()
def googledork():
	count3 = 1
	dork = open(x +'/Resources/GoogleDorks.txt','r') #opens in url
	try:
		while True:
			lines = dork.read(count3)
			google_search = GoogleSearch(lines)
			google_search.start_search(max_page=1) #searches
			print(google_search.search_result)  #prints seaches
			count3 += 1 #count +1 aka next inurl
			
	except IOError:
		mainmenu()
	except KeyboardInterrupt: #returns to main menu if ctrl C is used
		mainmenu()
	except UnicodeEncodeError: #There Is an error if the encoding is not utf 8 you can change pass to just keep going even after error
		extra_long()
		mainmenu()

def update():
	clear()
	print (Fore.CYAN + 'You have build ' +build)
	quick()
	os.system('git clone https://github.com/14dead/Mercury-14dead '+x+'/Update') #Just redownloads the repo
	sys.exit()
def helpme():
	print ('''
 command            	          Usage
===============            =================
helpme                     Shows this screen
source                     Source code of websites
bruteforce                 BruteForce a website
stop                       Exit
pips                       Pip installer
geoip                      GeoIP
github                     Installs Github repos
stop                       Returns to main menu		''')
	time.sleep(15)
	prompt()
def sourcecodep():
	try:
		name = raw_input('Enter the File Name [End It With .html !] ') #Save File
		URL1=raw_input(Fore.CYAN + 'Enter An Url ') #Url
		html1 = open(name, 'a+') #Writes The File
		html = open(name, 'w')
		response = urllib2.urlopen(URL1) #Opens Url
		page_source = response.read() #Reads URL
		space()
		print >>html,  page_source #Change to python3 Syntax aka file. write
		print ('Done ! saved under users! ') #%users%
		quick()
		prompt()
	except KeyboardInterrupt:
		print ('Stopped! ')
		prompt()
	except IOError: #very rare error dont worry
		print ('File was not found \: ')
		prompt()
def toolss():
	clear()
	print (Fore.WHITE + ''' d888888b  .d88b.   .d88b.  db      .d8888. 
 `~~88~~' .8P  Y8. .8P  Y8. 88      88'  YP 
    88    88    88 88    88 88      `8bo.   
   \033[96m 88    88    88 88    88 88        `Y8b. 
    88    `8b  d8' `8b  d8' 88booo. db   8D 
    YP     `Y88P'   `Y88P'  Y88888P `8888Y' 
                                           
                                           ''')
	space()
	print (Fore.WHITE + '''
	[0]\033[96m Metasploit\033[1;37;40m		[9]\033[96m Aircrack\033[1;37;40m
	[1]\033[96m WireShark \033[1;37;40m		[10]\033[96m Wifite\033[1;37;40m
	[2]\033[96m Nmap \033[1;37;40m      		[11]\033[96m Hammer\033[1;37;40m
	[3]\033[96m Lazy script \033[1;37;40m	[12]\033[96m Xerxes\033[1;37;40m
	[4]\033[96m fsociety \033[1;37;40m		[13]\033[96m XSStrike\033[1;37;40m
	[5]\033[96m Reaver \033[1;37;40m		[14]\033[96m Wpscan\033[1;37;40m
	[6]\033[96m InstaBrute \033[1;37;40m 	[15]\033[96m Cupp\033[1;37;40m
	[7]\033[96m Cl0neMas3r \033[1;37;40m 	[16]\033[96m Hydra\033[1;37;40m
	[8]\033[96m Sqlmap \033[1;37;40m		


	[100]\033[96m Install All\033[1;37;40m	[99]\033[96m Exit submenu\033[1;37;40m
								      
		                        ''')
	ans_2 = raw_input('Tools ~# ')
	if ans_2 == '0':
		try:
			os.system('git clone https://github.com/rapid7/metasploit-framework '+x+'/Tools/Metasploit')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '1':
		try:
			os.system('git clone https://github.com/wireshark/wireshark '+x+'/Tools/WireShark')
			toolss()
		except KeyboardInterrupt:
			toolss()	
	if ans_2 == '2':
		try:
			os.system('git clone https://github.com/nmap/nmap '+x+'/Tools/Nmap')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '3':
		try:
			os.system('git clone https://github.com/arismelachroinos/lscript '+x+'/Tools/LazyScript')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '4':
		try:
			os.system('git clone https://github.com/Manisso/fsociety '+x+'/Tools/Fsociety')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '5':
		try:
			os.system('git clone https://github.com/t6x/reaver-wps-fork-t6x '+x+'/Tools/Reaver')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '6':
		try:
			os.system('git clone https://github.com/N3TC4T/InstaBrute '+x+'/InstaBrute')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '7':
		try:
			os.system('git clone https://github.com/Abdulraheem30042/Cl0neMast3r '+x+'/Tools/CloneMaster')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '8':
		try:
			os.system('git clone https://github.com/sqlmapproject/sqlmap '+x+'/Tools/Sqlmap')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '9':
		try:
			os.system('git clone https://github.com/aircrack-ng/aircrack-ng '+x+'/Tools/aircrack-ng')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '10':
		try:
			os.system('git clone  https://github.com/derv82/wifite '+x+'/Tools/wifite')
			toolss()
		except KeyboardInterrupt:
			toolss()

	if ans_2 == '11':
		try:
			os.system('git clone https://github.com/cyweb/hammer '+x+'/Tools/hammer')
			toolss()
		except KeyboardInterrupt:
			toolss()

	if ans_2 == '12':
		try:
			os.system('git clone https://github.com/zanyarjamal/xerxes '+x+'/Tools/xerxes')
			toolss()
		except KeyboardInterrupt:
			toolss()

	if ans_2 == '13':
		try:
			os.system('git clone https://github.com/UltimateHackers/XSStrike '+x+'/Tools/XSStrike')
			toolss()
		except KeyboardInterrupt:
			toolss()

	if ans_2 == '14':
		try:
			os.system('git clone https://github.com/wpscanteam/wpscan '+x+'/Tools/wpscan')
			toolss()
		except KeyboardInterrupt:
			toolss()

	if ans_2 == '15':
		try:
			os.system('git clone https://github.com/Mebus/cupp '+x+'/Tools/cupp')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '16':
		try:
			os.system('git clone https://github.com/vanhauser-thc/thc-hydra '+x+'/Tools/thc-hydra')
			toolss()
		except KeyboardInterrupt:
			toolss()
	if ans_2 == '17':
		try:
			os.system('git clone https://github.com/bettercap/bettercap '+x+'/Tools/BetterCap')
			toolss()
		except KeyboardInterrupt:
			toolss()

	if ans_2 == '100':
		try:
			os.system('git clone https://github.com/vanhauser-thc/thc-hydra '+x+'/Tools/thc-hydra')
			os.system('git clone https://github.com/Mebus/cupp '+x+'/Tools/cupp ')
			os.system('git clone https://github.com/wpscanteam/wpscan '+x+'/Tools/wpscan')
			os.system('git clone https://github.com/UltimateHackers/XSStrike '+x+'/Tools/XSStrike')
			os.system('git clone https://github.com/zanyarjamal/xerxes '+x+'/Tools/xerxes')
			os.system('git clone https://github.com/cyweb/hammer '+x+'/Tools/hammer')
			os.system('git clone  https://github.com/derv82/wifite '+x+'/Tools/wifite')
			os.system('git clone https://github.com/aircrack-ng/aircrack-ng '+x+'/Tools/aircrack-ng')
			os.system('git clone https://github.com/sqlmapproject/sqlmap '+x+'/Tools/Sqlmap')
			os.system('git clone https://github.com/Abdulraheem30042/Cl0neMast3r '+x+'/Tools/CloneMaster')
			os.system('git clone https://github.com/N3TC4T/InstaBrute '+x+'/Tools/InstaBrute')
			os.system('git clone https://github.com/t6x/reaver-wps-fork-t6x '+x+'/Tools/Reaver')
			os.system('git clone https://github.com/Manisso/fsociety '+x+'/Tools/Fsociety')
			os.system('git clone https://github.com/arismelachroinos/lscript '+x+'/Tools/LazyScript')
			os.system('git clone https://github.com/nmap/nmap '+x+'/Tools/Nmap')
			os.system('git clone https://github.com/wireshark/wireshark '+x+'/Tools/WireShark')
			os.system('git clone https://github.com/rapid7/metasploit-framework '+x+'/Tools/Metasploit')

			toolss()
		except KeyboardInterrupt: #returns to main menu if ctrl C is used
			toolss()

	if ans_2 == '99':
		mainmenu()
	else:
		toolss()

def sourcecode():
	try:
		name = raw_input('Enter the file name [end it with .html !] ') #Save File
		URL1=raw_input(Fore.CYAN + 'Enter An Url ') #Url
		html1 = open(name, 'a+') #Writes The File
		html = open(name, 'w')
		response = urllib2.urlopen(URL1) #Opens Url
		page_source = response.read() #Reads URL
		space()
		print >>html,  page_source #Change to python3 Syntax
		print ('Done ! saved under "Users" ')
		quick()
		clear()
	except KeyboardInterrupt:
		print ('Stopped! ')
		mainmenu()
	except IOError:
		print ('File was not found \: ')
		mainmenu()
	mainmenu()
def brute_force(): #Declares Function
	f = open(x+'/Resources/passwords.txt', 'r')
	browser = webdriver.Chrome() #Opens Chrome
	username = raw_input(Fore.CYAN + '	What is the Username? ') #Username
	USS = raw_input('		What is the CSS Selector for the Username? ') #CSS Selector Username
	PSS = raw_input(' 			What is the CSS Selector for the Password? ') #CSS Selector Password
	SSS  = raw_input ('				What is the CSS Selector for the Submit Button? ') #CSS Selector Submit
	url4 = raw_input('					What is the Url? ') #URL Requests
	browser.get(url4)
	count = 1 #count
	while True:
		try:
			browser.get(url4)
			Sel_user = browser.find_element_by_css_selector(USS) #Finds Selector
			Sel_pas = browser.find_element_by_css_selector(PSS) #Finds Selector
			enter = browser.find_element_by_css_selector(SSS) #Finds Selector 
			quick() #Pause
			line = f.read(count) #Password Lines
			for line in f:
				Sel_user = browser.find_element_by_css_selector(USS) #Finds Selector
				Sel_pas = browser.find_element_by_css_selector(PSS) #Finds Selector
				enter = browser.find_element_by_css_selector(SSS) #Finds Selector 
				Sel_user.send_keys(username) #Sends Username
				quick()
				Sel_pas.send_keys(line) #Sends Password
				enter = browser.find_element_by_css_selector(SSS).click() #Clicks Enter
				space()
				print (Fore.CYAN + '#-----------------------------#')
				print (Fore.WHITE + 'Tried Password: ' +line+ 'For User:' +username) #Displays Data
				print (Fore.CYAN +'# ----------------------------#')
				count =+ 1 #Counts +1
		except IOError: #unknown error by me 
			print ('There was a random error sorry! ')
			quick()
			mainmenu()
		except selenium.common.exceptions.StaleElementReferenceException: #Selector wasnt found maybe a typo
			print (Fore.RED + 'SELECTOR NOT FOUND!!!')
			extra_long()
			mainmenu()
		except selenium.common.exceptions.WebDriverException: #Chrome was closed
			print (Fore.CYAN + 'Chrome was closed! ')
			extra_long()
			mainmenu()
		except KeyboardInterrupt: #returns to main menu if ctrl C is used
			mainmenu()
def pip_installep(): #change to p so it could by loaded in prompt
	try:
		pip = raw_input(Fore.CYAN + '	What Pip would you like to install: ')
		os.system('pip install ' +pip)
		time.sleep(1)
		clear()
		prompt()
	except KeyboardInterrupt:
		print ('Stopped! ')
		quick()
		prompt()
def ipaddress():
	try:
		url2 = raw_input(Fore.CYAN +"Enter a website url ") #User Input
		ip = socket.gethostbyname(url2) #Gets Ip Address
		print (Fore.CYAN + (ip)) #Prints Ip Address
		long()
		clear()
		mainmenu()
	except KeyboardInterrupt:
		mainmenu()
	except AttributeError: #enter link like www.google.com rather than https://www.google.com
		print ('Dont include https or http in the site link !')
		quick()
		mainmenu()

def networksweb():
	url3 = raw_input(Fore.CYAN + 'Enter a host name include https: ')
	count3 = 1
	while True: #loop
			try:
				urllib2 .urlopen(url3) #opens link
		    		status = "Connected" #if no error
		    	except KeyboardInterrupt: #returns to main menu if ctrl C is used
				mainmenu() #mainmenu
			except:
		    		status = "Not connected" #if you cant connect then:
		    		print (Fore.RED+'Attempt '+ Fore.RED +str( count3 )+ Fore.RED +  ' At Host: '+ Fore.RED +url3 + Fore.RED + ': OFFLINE')
				print (status)

			if status == "Connected":
				print (Fore.CYAN +'Attempt '+ Fore.CYAN +str( count3 )+ Fore.CYAN +  ' at host: '+ Fore.CYAN +url3 + Fore.GREEN + ': online')
				count3 += 1
def webbrowserfunc():
	surf = webdriver.Chrome() #opens chrome you can change to FireFox if you won`t like: surf = webdriver.Firefox()
	surf.get('https://www.googlecom')

def mac():
	os.system('getmac') #For Linux Change to ifconfig -a
	long()
	mainmenu()
def myip():
	print (	'Your ip is ' + Fore.CYAN + socket.gethostbyname(socket.gethostname())) #gets ip address from socket linux always returns 12.0.0.1
	long()
	mainmenu()
def pip_installer():
	try:
		pip = raw_input(Fore.CYAN + '	What Pip would you like to install: ') #what pip 
		os.system('pip install ' +pip) #installs pip
		time.sleep(1)
		clear()
		mainmenu()
	except KeyboardInterrupt: 
		print ('Stopped! ')
		quick()
		mainmenu()
def github():
	githublink = raw_input(Fore.CYAN + '	Enter an url to the GitHub repo: ')
	name = raw_input('		What is the name of the repo? ')
	try:
		os.system('git clone '+githublink+ ' '+x+'/'+name) #save file to Mercury/'name'
		time.sleep(1)
		long()
		clear()
		mainmenu()
	except KeyboardInterrupt:
		print ('Stopped! ')
		quick()
		mainmenu()
	else:
		print ('Fatal error ')
		mainmenu()
def githubp():
	githublink = raw_input(Fore.CYAN + '	Enter an url to the GitHub repo: ')
	name = raw_input('		What is the name of the repo? ')
	try:
		os.system('git clone '+githublink+ ' '+x+'/'+name)
		time.sleep(1)
		long()
		clear()
		prompt()
	except KeyboardInterrupt:
		print ('Stopped! ')
		quick()
		prompt()
	else:
		print ('Fatal Error ')
		prompt()      
def exit():
	sys.exit()
def geoLocationp(): 
	try:
		target = raw_input(Fore.CYAN + '	Enter an ip address: ') #User Input
		send_url = 'http://freegeoip.net/json/'+target #Finds Targets
		r = requests.get(send_url) #Sends Url
		j = json.loads(r.text) #Reads All Text
		cn = j['country_name'] #Reads Country
		rc = j['region_code'] #Reads Region Code
		city = j['city'] #Reads City
		lat = j['latitude'] #Read Latitiude
		lon = j['longitude'] #Read Longitude
		print (lat)
		print  (lon)
		print (city)
		print (rc)
		print (cn)
		long() #Pause
		prompt()
	except KeyboardInterrupt:
		prompt()

def geoLocation(): 
	try:
		target = raw_input(Fore.CYAN + '	Enter an ip address: ') #User Input
		send_url = 'http://freegeoip.net/json/'+target #Finds Targets
		r = requests.get(send_url) #Sends Url
		j = json.loads(r.text) #Reads All Text
		cn = j['country_name'] #Reads Country
		rc = j['region_code'] #Reads Region Code
		city = j['city'] #Reads City
		lat = j['latitude'] #Read Latitiude
		lon = j['longitude'] #Read Longitude
		print (lat)
		print  (lon)
		print (city)
		print (rc)
		print (cn)
		long() #Pause
		mainmenu()
	except ValueError:
		print ('Invalid ip address')
		quick()
		mainmenu()
	except KeyboardInterrupt:
		mainmenu()
def file():
	try:
		dirt = raw_input(Fore.CYAN + '		Enter a file location: ') 
		t = os.listdir(dirt) #Change To Ls For Linux Users
		print (t)
		extra_long()
		clear()
		mainmenu()
	except WindowsError:
		print ('Invalid location! ')
		quick()
		mainmenu()
def prompt():
	try:
		while True:
			print ('''Mercury Retrograde [Version 1.0.0]
(c) 2018 14Dead. All rights reserved: To quit type 'stop' and for help type helpme''')
			print (' ')
			command = raw_input("C:\users\Mercury> ")
			if command == ' ':
				clear()
				prompt()
			if command == '':
				clear()
				prompt()
			if command == 'stop':
				mainmenu()
			if command == 'github':
				githubp()
			if command == 'bruteforce':
				brute_force()
			if command == 'source':
				sourcecodep()
			if command == 'pips':
				pip_installerp()
			if command == 'helpme':
				print helpme()
			if command == 'geoip':
				geoLocationp()
			os.system(command)
			prompt()
	except KeyboardInterrupt:
		mainmenu()
def wordlist():
	clear()
	print (Fore.WHITE + '''
 Yb        dP  dP"Yb  88""Yb 88     8888b.  88     88 .dP"Y8 888888 
  Yb  db  dP  dP   Yb 88__dP 88      8I  Yb 88     88 `Ybo."   88   
 \033[96m  YbdPYbdP   Yb   dP 88"Yb  88  .o  8I  dY 88  .o 88 o.`Y8b   88   
    YP  YP     YbodP  88  Yb 88ood8 8888Y"  88ood8 88 8bodP'   88   

 ''')
	space()
	print (Fore.WHITE + '''
	[0]\033[96m 10m passwords 85MB \033[1;37;40m 	
	[1]\033[96m CrackStation 246MB \033[1;37;40m 		
	[2]\033[96m B0n3z Dictionary 3GB \033[1;37;40m             	
	[3]\033[96m 18_in_1 5GB \033[1;37;40m                
	[4]\033[96m B0n3z-wordlist-sorted 9GB \033[1;37;40m		

		              

        [99]\033[96m Exit submenu\033[1;37;40m''')
	ans_3 = raw_input('Wordlist ~# ')
	if ans_3 == '0':
		try:
			print ('Downloading 10m password 85MB this may take awhile...')
			requests.get('http://download.g0tmi1k.com/wordlists/large/10-million-combos.zip')
			print ('Saved Under Users!')
			long()
			wordlist()
		except KeyboardInterrupt:
			wordlist()
	if ans_3 == '1':
		try:
			print ('Downloading CrackStation 246MB this may take awhile...')
			requests.get('http://download.g0tmi1k.com/wordlists/large/crackstation-human-only.txt.gz')
			print ('Saved Under Users!')
			long()
			wordlist()
		except KeyboardInterrupt:
			wordlist()
	if ans_3 == '2':
		try:
			print ('Downloading Bon3z Dictionary 3GB this may take awhile...')
			requests.get('http://download.g0tmi1k.com/wordlists/large/b0n3z_dictionary-SPLIT-BY-LENGTH-34.6GB.7z')
			print ('Saved Under Users!')
			long()
			wordlist()
		except KeyboardInterrupt:
			wordlist()
	if ans_3 == '3':
		try:
			print ('Downloading 18_in_1 5GB this may take awhile...')
			requests.get('http://download.g0tmi1k.com/wordlists/large/36.4GB-18_in_1.lst.7z')
			print ('Saved Under Users!')
			long()
			wordlist()
		except KeyboardInterrupt:
			wordlist()
	if ans_3 == '3':
		try:
			print ('Downloading B03z Sorted  9GB this may take awhile...')
			requests.get('http://download.g0tmi1k.com/wordlists/large/b0n3z-wordlist-sorted_REPACK-69.3GB.7z')
			print ('Saved Under Users!')
			long()
			wordlist()
		except KeyboardInterrupt:
			wordlist()
	if ans_3 == '99': 
		mainmenu()
def mainmenu():
	clear()
	print (Fore.CYAN +'Dir = '+(x))
	space()
	print (Fore.WHITE + ''' 888b     d888                                                                                   
 8888b   d8888                                                                                   
 88888b.d88888                                                                                   
 888Y88888P888       .d88b.       888d888       .d8888b      888  888      888d888      888  888 
 888 Y888P 888      d8P  Y8b      888P"        d88P"         888  888      888P"        888  888 
\033[96m 888  Y8P  888      88888888      888          888           888  888      888          888  888 
 888   "   888      Y8b.          888          Y88b.         Y88b 888      888          Y88b 888 
 888       888       "Y8888       888           "Y8888P       "Y88888      888           "Y88888 
                                                                                            888 
                                                                                       Y8b d88P 
                                                                                        "Y88P"  
 ''')
	space()
	print (Fore.WHITE + '''
	[0]\033[96m ReadMe and license \033[1;37;40m 	[9]\033[96m SourceCode from website \033[1;37;40m
	[1]\033[96m Brute force \033[1;37;40m 		[10]\033[96m Ip address from website\033[1;37;40m
	[2]\033[96m Whats my Ip \033[1;37;40m             	[11]\033[96m Google dorks\033[1;37;40m
	[3]\033[96m GeoLocation \033[1;37;40m                [12]\033[96m \033[1;37;40m
	[4]\033[96m Show mac address \033[1;37;40m		[13]\033[96m Download tools\033[1;37;40m
	[5]\033[96m Website online/offline \033[1;37;40m	[14]\033[96m Wordlists\033[1;37;40m
	[6]\033[96m File explorer \033[1;37;40m		[15]\033[96m Python\033[1;37;40m
	[7]\033[96m GitHub cloner \033[1;37;40m		[16]\033[96m Prompt\033[1;37;40m
	[8]\033[96m Pip installer \033[1;37;40m 		[17]\033[96m Webbrowser\033[1;37;40m
		              

	[100]\033[96m Update\033[1;37;40m	[99]\033[96m Exit tool\033[1;37;40m	
	''')
	ans = raw_input(Fore.WHITE + 'Enter a choice  ~# ')
	if ans == '0':
		readme()
	if ans == '1':
		brute_force()
	if ans == '2':
		myip()
	if ans == '3':
		geoLocation()
	if ans == '4':
		mac()
	if ans == '5':
		networksweb()
	if ans == '6':
		file()
	if ans == '7':
		github()
	if ans == '8':
		pip_installer()
	if ans == '9':
		sourcecode()
	if ans == '10':
		ipaddress()
	if ans =='11':
		googledork()
	if ans == '12':
		ddos()
	if ans == '13':
		toolss()
	if ans == '14':
		wordlist()
	if ans == '15':
		pythoni()
	if ans == '16':
		clear()
		prompt()
	if ans == '17':
		webbrowserfunc()
	if ans == '99':
		exit()
	if ans == '100':
		update()
	else:
		mainmenu()
try:
	agreement()
	mainmenu()
except KeyboardInterrupt:
	mainmenu()
