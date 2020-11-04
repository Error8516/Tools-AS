import requests, builtwith
from colorama import Fore
import os
import sys
import time
import socket
import json
############################################################
def __start__():
      if os.name == "nt":
            os.system("cls")
            print("")
            __Banner__()
      elif os.name == "posix":
            os.system("clear")
            print("")
            __Banner__()            
############################################################
def __Banner__():      
      print(Fore.YELLOW+"""
 _____              _                  _____  ___   
(_   _)            (_ )               (  _  )(  _`\ 
  | |   _      _    | |   ___  ______ | (_) || (_(_)
  | | /'_`\  /'_`\  | | /',__)(______)|  _  |`\__ \ 
  | |( (_) )( (_) ) | | \__, \        | | | |( )_) |
  (_)`\___/'`\___/'(___)(____/        (_) (_)`\____)     
      """)
      print(Fore.CYAN+"=========================================================")
      print(Fore.CYAN+"|"+Fore.GREEN+"           ~~~ install best Tools-AS ~~~"+Fore.CYAN+"               |")           
      print(Fore.CYAN+"=========================================================")           
      print("")                                 
      time.sleep(1)
############################################################      
def pageone_tools():
      __start__()
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"01"+Fore.YELLOW+"]-"+Fore.GREEN+"information Gathering")    

      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"02"+Fore.YELLOW+"]-"+Fore.GREEN+"About Me")        

      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"03"+Fore.YELLOW+"]-"+Fore.GREEN+"Exit ...")  
      print("")

      try:
            targetAsle= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~"+Fore.WHITE+"# ")
      except:
            sys.exit()
            
      if targetAsle == "":
            time.sleep(1)
            pageone_tools()

############################################################
      if targetAsle == "1":
            __toolss__()
      elif targetAsle == "01":
            __toolss__()
      elif targetAsle == "2":
            AboutMe()
      elif targetAsle == "02":
            AboutMe()
      elif targetAsle == "3":
             time.sleep(1)
             sys.exit()
      elif targetAsle == "03":
             time.sleep(1)
             sys.exit()

############################################################

def __toolss__():
      __start__()  
         
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"01"+Fore.YELLOW+"]-"+Fore.GREEN+"Admin Page Finder")
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"02"+Fore.YELLOW+"]-"+Fore.GREEN+"Port Scan")
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"03"+Fore.YELLOW+"]-"+Fore.GREEN+"Cms Detect")
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"04"+Fore.YELLOW+"]-"+Fore.GREEN+"Ip Finder")
            
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"05"+Fore.YELLOW+"]-"+Fore.GREEN+"DNS Lookup")         
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"06"+Fore.YELLOW+"]-"+Fore.GREEN+"Show Http Header")         
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"07"+Fore.YELLOW+"]-"+Fore.GREEN+"Reverse Ip")   
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"08"+Fore.YELLOW+"]-"+Fore.GREEN+"Trace Route")
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"09"+Fore.YELLOW+"]-"+Fore.GREEN+"Whois")
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"10"+Fore.YELLOW+"]-"+Fore.GREEN+"Find Shared DNS")    
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"11"+Fore.YELLOW+"]-"+Fore.GREEN+"Robots Scanner")  
                  
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"12"+Fore.YELLOW+"]-"+Fore.GREEN+"Bypass Cloud Flare")  
      
      time.sleep(0.1)
      print(Fore.YELLOW+"["+Fore.RED+"13"+Fore.YELLOW+"]-"+Fore.GREEN+"Ip Location")  
      print("")                                                                                                                                                                            

      try:
            input_tools= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"InformationGathering"+Fore.WHITE+"# ")
      except:
            sys.exit()
            
      if input_tools == "":
            time.sleep(1)
            pageone_tools()
############################################################
      if input_tools == "1":
            Admin_Page_Finder()
      elif input_tools == "01":
            Admin_Page_Finder()
      elif input_tools == "2":
            port_scan()
      elif input_tools == "02":
            port_scan()
      elif input_tools == "3":
            Cms_Detect()
      elif input_tools == "03":
            Cms_Detect()
      elif input_tools == "4":
            Ip_Finder()
      elif input_tools == "04":
            Ip_Finder()
      elif input_tools == "5":
            DNS_Lookup()
      elif input_tools == "05":
            DNS_Lookup()
      elif input_tools == "6":
            Show_Http_Header()            
      elif input_tools == "06":
            Show_Http_Header()
      elif input_tools == "7":
            Reverse_Ip()            
      elif input_tools == "07":
            Reverse_Ip()             
      elif input_tools == "8":
            Trace_Route()            
      elif input_tools == "08":
            Trace_Route()            
      elif input_tools == "9":
            whois()            
      elif input_tools == "09":
            whois()
      elif input_tools == "10":
            Find_Shared_DNS()            
      elif input_tools == "11":
            Robots_Scanner()            
      elif input_tools == "12":
            Bypass_Cloud_Flare()                                              
      elif input_tools == "13":
            Ip_Location()
############################################################
def AboutMe():
      __start__()
      
      time.sleep(0.1)
      print(Fore.GREEN+"[!]-"+Fore.WHITE+"Developer: "+Fore.RED+"Error8516")
      print("")
      
      time.sleep(0.1)
      print(Fore.GREEN+"[!]-"+Fore.WHITE+"My Age: "+Fore.RED+"15 Yers Old")
      print("")      
      
      time.sleep(0.1)
      print(Fore.GREEN+"[!]-"+Fore.WHITE+"City: "+Fore.RED+"Qasr e Shirin")
      print("")      
      
      time.sleep(0.1)
      print(Fore.GREEN+"[!]-"+Fore.WHITE+"Country: "+Fore.RED+"Iran")
      print("")      
      
      time.sleep(0.1)
      print(Fore.GREEN+"[!]-"+Fore.WHITE+"Telegram: "+Fore.RED+"Error8516")
      print("")      

      time.sleep(0.1)
      print(Fore.GREEN+"[!]-"+Fore.WHITE+"Telegram Chanel: "+Fore.RED+"Programms_Termenaling_AS")
      print("") 
                    
      time.sleep(0.1)
      print(Fore.GREEN+"[!]-"+Fore.WHITE+"Instagram: "+Fore.RED+"ali_tanasan15")
      print("")   

      time.sleep(0.1)
      print(Fore.GREEN+"[!]-"+Fore.WHITE+"Github: "+Fore.RED+"https://github.com/Error8516")
      print("")
      
      try:
            print("")
            input(Fore.MAGENTA+"[!] "+Fore.YELLOW+"Go To Menu (press Enter ...) ")
            pageone_tools()
      except:
            sys.exit() 
############################################################
search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']  
def Robots_Scanner():
      __start__()
      
      try:
            print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
            print("")
            url = input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"RobotsScanner"+Fore.WHITE+"# ")
            print("")
            if 'http' in url:
                  pass
            elif 'http' != url:
                  url = ('http://'+url)
            
            for i in search:
                  time.sleep(0.1)
                  ur = (url+"/"+i)
                  reqs = requests.get(ur)
                  if reqs.status_code == 200 or reqs.status_code == 405:
                        print(Fore.GREEN+"[+] "+ ur)
            else:
                print(Fore.RED+"[-] "+ur)
            try:
                  print("")
                  input(Fore.RED+"[!] "+Fore.GREEN+"Go To Menu (Press Enter...) ")
                  pageone_tools()
            except:
                         print("")
                         sys.exit()  
      except:
                   sys.exit()
        
############################################################
def Find_Shared_DNS():
      __start__()
      
      try:
               print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
               print("")
               
               target_10= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"FindSharedDNS"+Fore.WHITE+"# ")         
               print("")
               
               try:
                     result = requests.get('https://api.hackertarget.com/whois/?q=' + target_10).text
                     print(Fore.BLUE+result)
               except:
                     Find_Shared_DNS()
                     
               try:
                      input(Fore.RED+" [!] "+Fore.GREEN+"Go To Menu (Press Enter...) "+Fore.WHITE+"")
                      pageone_tools()
               except:
                      sys.exit()  
      except:
            sys.exit()

      if target_10 == "":
            time.sleep(1)
            pageone_tools()
############################################################
def Ip_Location():
      __start__()
      
      print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
      print(Fore.RED+"\n [/] Or Press The Enter Key :))) \n")
    
      try:
           target_11= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"IpLocation"+Fore.WHITE+"# ")      
           source = ipapi.location(ip=site, key=None, field=None)
      except:
           sys.exit()
      try:
         print(Fore.GREEN+" [!]"+Fore.RED+" See your info")
         print (Fore.GREEN+" [!]"+Fore.BLUE+" ip = "+ source["ip"])
         print (Fore.GREEN+" [!]"+Fore.BLUE+" city = " + source["city"])
         print (Fore.GREEN+" [!]"+Fore.BLUE+" region = "+ source["region"])
         print (Fore.GREEN+" [!]"+Fore.BLUE+" id country = "+source["country"])
         print (Fore.GREEN+" [!]"+Fore.BLUE+" country = "+ source["country_name"])
         print (Fore.GREEN+" [!]"+Fore.BLUE+" Calling Code = "+source["country_calling_code"])
         print (Fore.GREEN+" [!]"+Fore.BLUE+" Languages = "+source["languages"])
         print (Fore.GREEN+" [!]"+Fore.BLUE+" org = "+ source["org"])
         try:
             print("")
             input(Fore.RED+" [!] "+Fore.GREEN+"Go To Menu (Press Enter...) ")
             pageone_tools()
         except:
             print("")
             sys.exit()  
      except:
          print(Fore.RED+"Sorry Please Enter IP Address")      
############################################################ 
def Bypass_Cloud_Flare():
      __start__()
      
      print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
      subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

      try:
            site = input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"BypassCloudFlare"+Fore.WHITE+"# ")
            print("")
      except:
            sys.exit()

      if site == "":
           try:
                 time.sleep(1)
                 pageone_tools()
           except:
            return
      for sub in subdom:
              try:
                    hosts = str(sub) + "." + str(site)
                    bypass = socket.gethostbyname(str(hosts))
                    print ("[!] CloudFlare Bypass " + str(bypass) + ' | ' + str(hosts))
              except Exception:
                        pass
      try:
            print("")
            input(Fore.GREEN+" [*] Go To Menu (Press Enter...) ")
            pageone_tools()
      except:
                  print("")
                  sys.exit()      
############################################################
def whois():
      __start__()
      
      try:
               print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
               print("")
               
               target_9= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"whois"+Fore.WHITE+"# ") 
               print("")
      except:
            sys.exit()                
      try:
               result = requests.get('https://api.hackertarget.com/whois/?q=' + target_9).text
               print(Fore.BLUE+result)
      except:
                  whois()
                     
      try:
              print("")
              input(Fore.RED+" [!] "+Fore.GREEN+"Go To Menu (Press Enter...) "+Fore.WHITE+"")
              pageone_tools()
      except:
                   sys.exit()  
                   
      if target_9 == "":
            time.sleep(1)
            pageone_tools()

############################################################ 
def Trace_Route():
      __start__()
      
      try:
              print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
              print("")
               
              target_8= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"TraceRoute"+Fore.WHITE+"# ")
              print("")
              
              try:
                    result = requests.get('https://api.hackertarget.com/mtr/?q=' + target_8).text
                    print(Fore.BLUE+result)
                    print("")
              except:
                    Trace_Route()
              
              try:
                      print("")
                      input(Fore.RED+"[!] "+Fore.GREEN+"Go To Menu (Press Enter...) ")
                      pageone_tools()
              except:
                       sys.exit()  
      except:
            sys.exit()

      if target_8 == "":
            time.sleep(1)
            pageone_tools()
      else:
            print("")
############################################################
def Reverse_Ip(): # target_7
      __start__()
      
#      try:
      print (Fore.RED+"\n [!] Enter The Domain/ip\n")
      website = input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"ReverseIp"+Fore.WHITE+"# ") 
      print("")
#      except:
#            sys.exit()

      mysite = {"remoteAddress":website}
      link = requests.post("https://domains.yougetsignal.com/domains.php" , mysite)
      source = json.loads(link.content)

      for data in source["domainArray"]:
              print(" "+data[0]+"\n")

      try:
              print("")
              input(Fore.RED+"[!] "+Fore.GREEN+"Go To Menu (Press Enter...) ")
              pageone_tools()
      except:
              print("")
              sys.exit()
############################################################
def Show_Http_Header():
      __start__()
      
      try:
              print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
              print("")
               
              target_6= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"ShowHttpHeader"+Fore.WHITE+"# ")
              print("")
              
              try:
                    result= requests.get("http://api.hackertarget.com/httpheaders/?q="+ target_6).text
                    print(Fore.BLUE+result)
                    print("")
              except:
                    Show_Http_Header()
              
              try:
                      print("")
                      input(Fore.RED+"[!] "+Fore.GREEN+"Go To Menu (Press Enter...) ")
                      pageone_tools()
              except:
                       sys.exit()  
      except:
            sys.exit()

      if target_6 == "":
            time.sleep(1)
            pageone_tools()
############################################################
def DNS_Lookup():
      __start__()

      try:
              print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
              print("")
               
              target_5= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"DNSLookup"+Fore.WHITE+"# ")
              print("")
              
              try:
                    result= requests.get("http://api.hackertarget.com/dnslookup/?q="+ target_5).text
                    print(Fore.BLUE+result)
                    print("")
              except:
                    Show_Http_Header()
              
              try:
                      print("")
                      input(Fore.RED+"[!] "+Fore.GREEN+"Go To Menu (Press Enter...) ")
                      pageone_tools()
              except:
                       sys.exit()  
      except:
            sys.exit()

      if target_5 == "":
            time.sleep(1)
            pageone_tools()
############################################################
def Ip_Finder():
      __start__()
      
      try:
            print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
            print("")

            target_4= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"IpFinder"+Fore.WHITE+"# ")
            print("")
      except:
            sys.exit()

      if target_4 == "":
            time.sleep(1)
            pageone_tools()

      ip= socket.gethostbyname(str(target_4))
      def tkrar():
            while True:
                  print(Fore.YELLOW+target_4+"    "+Fore.YELLOW+"("+Fore.YELLOW+ip+Fore.YELLOW+")")
                  time.sleep(0.5)
      tkrar()

############################################################
def Cms_Detect():
      __start__()

      try:
             print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
             print("")
             target_2 = input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"IpFinder"+Fore.WHITE+"# ")
             print("")
      except:
             sys.exit()
    
      if not 'https://' in target_2 or not 'http://' in target_2:
            target_2 = 'http://'+target_2
      info = builtwith.parse(target_2)
      for name in info:
            value = ''
            for val in info[str(name)]:
                  time.sleep(0.1)
                  name = name.replace('-',' ')
                  name = name.title()
                  value += str(val) 
            print(Fore.BLUE+"\n"+name+': '+value)
      try:
            print("")
            input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
      except:
            print("")
            sys.exit()
############################################################
def port_scan():
      __start__()
      
      try:
            print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
            print("")
            target_2= input(Fore.RED+"Root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"PortScan"+Fore.WHITE+"# ")
            print("")
      except:
            sys.exit()
            
      if target_2 == "":
            time.sleep(1)
            pageone_tools()
      
      try:
            result= requests.get("http://api.hackertarget.com/nmap/?q="+ target_2).text
            print(Fore.YELLOW+result)
      except:
            port_scan()
      
      try:
            print("")
            input(Fore.MAGENTA+"[!] "+Fore.YELLOW+"Go To Menu (press Enter ...) ")
            pageone_tools()
      except:
            sys.exit()
############################################################
def Admin_Page_Finder():
      __start__()
      
      try:
            print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.MAGENTA+"Please Enter URL.")
            print("")            
            target_1= input(Fore.RED+"root@Tools-AS"+Fore.WHITE+":"+Fore.BLUE+"~/"+Fore.BLUE+"AdminPageFinder"+Fore.WHITE+"# ")
            print("")
      except:
            sys.exit()
            
      if target_1 == "":
            time.sleep(1)
            pageone_tools()
            
      UserPanel= ['admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html']
      
      if "http://" in target_1:
            target_1= (target_1+"/")
            
      elif "https://" in target_1:
            target_1= (target_1+"/")
            
      else:
            target_1= ("http://"+target_1+"/")
            
      for i in UserPanel:
            r= requests.get(target_1+i)
            
            if r.status_code == 200:
                  print(Fore.GREEN+"[+] "+target_1+i+" Fount")
            else:
                  print(Fore.RED+"[-] "+target_1+i+" Not Fount")
      try:
            input(Fore.MAGENTA+"[!] "+Fore.YELLOW+"Go To Menu (press Enter ...) ")
            pageone_tools()
      except: 
            sys.exit()




pageone_tools()
