import mechanize
import urllib
from urllib import urlopen
import cookielib
import BeautifulSoup
import html2text
import re
import sys
import StringIO
from urllib2 import HTTPError
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import webbrowser
import pickle
import datetime

'''
myPhantomFolder = os.getcwd()
browser = webdriver.PhantomJS(executable_path=(str(myPhantomFolder)+'\\phantomjs.exe'))
browser.delete_all_cookies()
'''






br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)


br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br._ua_handlers['_cookies'].cookiejar
br.addheaders = [('User-agent', 'Chrome')]
loop = 1

myPhantomFolder = os.getcwd()

#browser = webdriver.Chrome()
browser = webdriver.PhantomJS(executable_path=(str(myPhantomFolder)+'\\phantomjs.exe'))
browser.delete_all_cookies()




SOL = ['failure', 'exceptions']
carted = 'success'
line = ['pil', 'ewt']
OOS = ['wait', 'nogood']

print'............................................................'
print'......77777......................................77777......'
print'.....777777...............:?+++??...............777777......'
print'...7 777777...........??+++++++++++++...........,7777777,...'
print'..777777777.........+++++++++++++++++++~........,77777777 ..'
print'..7777777777?.....?++.+?++++++++++++++.++......7777777777 ..'
print'...777.: 77777...++:.+.??.++++++++++.++.++...7777777.7777...'
print'.........777777.++++++++++++++++++++:++?~++..77777..........'
print'...........777.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~. 77~...........'
print'............,7.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.7.............'
print'..............:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...............'
print'.......?+????+++??++++++++++++++++++??+++++++?++??+??.......'
print'.......??????????????????????????????????????????????.......'
print'..............:7777777 7777777777777777777777...............'
print'...............7777 +......777777......777777...............'
print'...............77777........777 ........7777................'
print'................777,........777 ........777.................'
print'.................777.......77777........77..................'
print'..................777.....7777777?....I 7...................'
print'....................7777 777...7777 777.....................'
print'......................=777777 7777777.......................'
print'.....................777...........=77.~....................'
print'..................77.777I7 77.77 I7777+77...................'
print'................777.77...7777.7777.:.,7.777.................'
print'...............7777.7 77.77~...:77.777 .77777...............'
print'........777..777777.7..7.7777.7777.77...777777..77 .........'
print'.......7777777777 ..7777....+.I:...?777..77777777777~.......'
print'......,777777777....:777777777777777777....7777777777.......'
print'.......+7777777~.....7777777777777777 ......77777777........'
print'..........777777......777777777777777......777777...........'
print'..........:77777........77777777777........777777...........'
print'............,~...............................++.............\n'


print 'PID?'
pid=int(input(""))
print '\nSize?'
size=raw_input("")

print "\nLet's get your skus..."
skuPage='https://secure-store.nike.com/us/services/catalogService?action=loadSkus&productId='+str(pid)+'&catalog=1&lang_locale=en_US&rt=json'

'''
browser.get(skuPage)
browser.save_screenshot("skuPage.png")
'''


br.open(str(skuPage))
browser.get(skuPage)





#br.select_form(nr=0)
'''
regex='<body>(.+?)</body>'
pattern = re.compile(regex)
htmltext = br.open(str(skuPage)).read()
text = re.findall(pattern,htmltext)
'''
skuPageText=str(br.open(str(skuPage)).read())
#print skuPageText

if '"failure"' in skuPageText:
    print "\nSKUs are not loaded yet"
    #EXIT OR PROMPT USER FOR INFO HERE

if '"'+size+'"' in skuPageText:
    foundSku=skuPageText.split('"'+size+'"')[0].split('",')[len(skuPageText.split('"'+size+'"')[0].split('",'))-2].split('{"id" :"')[len(skuPageText.split('"'+size+'"')[0].split('",')[len(skuPageText.split('"'+size+'"')[0].split('",'))-2].split('{"id" :"'))-1]
    print "\nYour sku for size " + str(size) + " -> " +str(foundSku)
    time.sleep(2)
    browser.save_screenshot('skus.png')
    print "Now lets try adding to cart =) \n"
    addURL='http://store.nike.com/us/services/jcartService?callback=nike_Cart_hanleJCartResponse&action=addItem&lang_locale=en_US&country=US&catalogId=1&productId='+str(pid)+'&price=120.0&siteId=null&line1=Nike+Air+Max+1+Ultra+Moire&line2=Men%27s+Shoe&passcode=null&sizeType=null&skuAndSize='+str(foundSku)+'%3A10&qty=1&rt=json&view=3&skuId='+str(foundSku)+'&displaySize='+str(size)+'&_=142655682313'
    #print addURL
    '''
    browser.get(addURL)
    browser.save_screenshot("test.png")
    '''
    
    store_url = 'http://store.nike.com/us/en_us/'
    cart_url = 'https://secure-store.nike.com/us/checkout/html/cart.jsp'

    #for cookies
    response = br.open(store_url)
    browser.get(store_url)
    
    response = br.open(addURL)
    browser.get(addURL)
    data = response.read()
    #print data

    #while - include loop count
    if all(x in data for x in SOL):
        while all(x in data for x in SOL):
            now = datetime.datetime.now()
            print "Failed ("+str(data.split('"errorcode" :"')[1].split('",')[0])+")"
            print "Attempt: " +str(loop)+" ("+str(now.hour % 12)+":"+str(now.minute)+":"+str(now.second)+"."+str(now.microsecond)+")\n"
            #print "DATA HERE->"+str(data)
            #Retry code here
            #retry(addUrl)
            response = br.open(store_url)
            response = br.open(addURL)
            data = response.read()
            time.sleep(2)
            #filename="fail"+str(loop)+".png"
            #browser.save_screenshot(filename)
            loop+=1

    elif all(x in data for x in OOS):
        while all(x in data for x in OOS):
            now = datetime.datetime.now()
            print "Status: " + str(data.split('"status" :"')[1].split('",')[0])
            print "PIL: " + str(data.split('"pil" :"')[1].split('",')[0])
            print "CartID: " + str(data.split('"psh" :"')[1].split('","')[0])
            print "OOS. Sorry =("
            print "Attempt: " +str(loop)+" ("+str(now.hour % 12)+":"+str(now.minute)+":"+str(now.second)+"."+str(now.microsecond)+")\n"
            #print "DATA HERE->"+str(data)
            #Retry code here
            #retry(addUrl)
            response = br.open(store_url)
            response = br.open(addURL)
            data = response.read()
            time.sleep(2)
            #filename="fail"+str(loop)+".png"
            #browser.save_screenshot(filename)
            loop+=1
    

        
    elif carted in data:
        print "Success! " + str(data.split('"displayName" :"')[1].split('","description"')[0])+ " - Size: " + size +" add to cart!\nLemme get your cart so you can checkout =)\n"
        #webbrowser.open(str(addURL)) <- webbrowser too generic and doesn't support cookies?
        
        #response = br.open(cart_url)
        browser.get(cart_url)
        browser.save_screenshot("cart.png")
       
        pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
        browser = webdriver.Chrome()
        cookies = pickle.load(open("cookies.pkl", "rb"))
        #print cookies
        i=0
        
    
        browser.get(cart_url)
        print "\n"

        
        for cookie in cookies:
            browser.add_cookie(cookie)
        #print browser.get_cookies()

        browser.refresh()
        #browser.get(cart_url)
        print "\nHere, have some cookies"
        print cookies

        print "\n"


    
        
        #webbrowser.open('https://secure-store.nike.com/us/checkout/html/cart.jsp')
    elif all(x in data for x in line):
        now = datetime.datetime.now()
        print "\nIn line"
        print "========="
        print "PIL: " + str(data.split('"pil" :"')[1].split('",')[0])
        print "EWT: " + str(data.split('"ewt" :')[1].split(',"')[0])
        print "CartID: " + str(data.split('"psh" :"')[1].split('","')[0])+"\n"
        print "Opening cart - refresh intermittently, good luck!"




        
        '''HANDLE INLINE WAIT HERE'''
        '''Continue loop try with psh and pil in jCart call'''
        '''Scrape for different results then trigger open browser'''





        
        browser.save_screenshot("wait.png")
        pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
        browser = webdriver.Chrome()
        cookies = pickle.load(open("cookies.pkl", "rb"))
        i=0
        browser.get(addURL)
        print "\n"
        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()
        #print "\nHere, have some cookies"
        #print cookies

        print "\n"





    else:
        print "IDK - TIMEOUT?"


else:
    print "Your size sku isn't loaded.\nLemme pull up their inventory for you =)\n\n"
    browser.save_screenshot("sku1.png")
    print skuPageText
    #prompt user for different size and run from the top/get that sku and continue with program
    print "\n\n"
 
#os.system("pause")



