# This class is used to contained methods of calculating features' input

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import ssl
import urllib
import urllib.request
from urllib.parse import urlparse
from urllib.request import urlopen
import whois
import datetime
from tldextract import extract
# import dnspython as dns
import dns.resolver
import bs4
import regex
import socket
import threading
import requests
from model.functions import Functions
import numpy as np
import time

def url_is_internal(url,compare):
        # url is the param needed to be compared to compare
        if ".".join(extract(url)) == ".".join(extract(compare)) or (url[0:4] != "http" and url[0] != "#"):
            return True
        else:
            return False

class Checker():
    
    def check_connection(url):
        try:
            r = requests.get(url,timeout=7)
            return 1
        except:
            return 0

    def having_IP_Address(url):
        try:
            symbol = regex.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',url)
            if(len(symbol)!=0):
                having_ip = 1 
            else:
                having_ip = -1 
            return(having_ip)        
        except Exception as e:
            print("err_having_IP_Address",e)
            return 0
            
    def URL_Length(url):
        try:
            length=len(url)
            if(length<54):
                return -1
            elif(54<=length<=75):
                return 0
            else:
                return 1
        except Exception as e:
            print("err_URL_length",e)
            return 0

    def Shortining_Service(url):
        try:
            r = requests.get(url,timeout=7)
            if len(r.history) > 1:
                return 1
            else:
                return -1
        except Exception as e:
            print("err_shortining_Service",e)
            return 0
    
    def having_At_Symbol(url):
        try:
            symbol=regex.findall(r'@',url)
            if(len(symbol)==0):
                return -1
            else:
                return 1 
        except Exception as e:
            print("err_having_At_Symbol",e)
            return 0
    
    def double_slash_redirecting(url):
        return -1
    
    def Prefix_Suffix(url):
        try:
            subDomain, domain, suffix = extract(url)
            if(domain.count('-')):
                return 1
            else:
                return -1
        except Exception as e:
            print("err_Prefix_Suffix",e)
            return 0
    
    def having_Sub_Domain(url):
        try:
            subDomain, domain, suffix = extract(url)
            if(subDomain.count('.')==0):
                return -1
            elif(subDomain.count('.')==1):
                return 0
            else:
                return 1
        except Exception as e:
            print("err_having_Sub_Domain",e)
            return 0
    
    def SSLfinal_State(url):
        try:
            if(regex.search('^https',url)):
                usehttps = 1
            else:
                usehttps = 0
            subDomain, domain, suffix = extract(url)
            host_name = domain + "." + suffix
            context = ssl.create_default_context()
            sct = context.wrap_socket(socket.socket(), server_hostname = host_name)
            sct.connect((host_name, 443))
            certificate = sct.getpeercert()
            # print("CERTIFICATE:",certificate)
            startingDate = str(certificate['notBefore'])
            endingDate = str(certificate['notAfter'])
            startingYear = int(startingDate.split()[3])
            endingYear = int(endingDate.split()[3])
            Age_of_certificate = endingYear-startingYear
            if((usehttps==1) and (Age_of_certificate>=1) ):
                return -1 
            else:
                return 1 
        except Exception as e:
            print("err_SSLfinal_State",e)
            return 0  
    
    def Domain_registeration_length(url):
        try:
            w = whois.whois(url)
            updated = w.creation_date
            exp = w.expiration_date
            if type(updated) == list:
                updated = updated[-1]
            if type(exp) == list:
                exp = exp[-1]

            length = (exp-updated).days
            if(length<=365):
                return 1
            else:
                return -1
        except Exception as e:
            print("err_Domain_registration_length",e)
            return 0
    
    def Favicon(url):
        try:
            r = requests.get(url,timeout=7)
            html = r.text

            regex_favicon = '<link rel=".*?icon".*?href="(.*?)"'
            regex_result = regex.findall(regex_favicon,html)
            if len(regex_result) == 0:
                return 1
            
            favicon_url = regex_result[0]

            url_domain = ".".join(extract(url)[1:3])
            favicon_domain = ".".join(extract(favicon_url[1:3]))
            if url_domain == favicon_domain:
                return -1
            else:
                return 1
        except Exception as e:
            print("err_favicon",e)
            return 1
    
    def port(url):
        try:
            subDomain, domain, suffix = extract(url)
            host_name = domain + "." + suffix
            DEFAULT_TIMEOUT = 0.5
            open_port = []
            list_ports = [21,22,23,80,443,445,1433,1521,3306,3389]
            timeout=DEFAULT_TIMEOUT
            TCPsock = socket.socket()
            TCPsock.settimeout(timeout)
            TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                for i in list_ports:
                    result = TCPsock.connect((host_name, i))
                    if result == 0:
                        open_port.append(i)
            except:
                pass
            if (80,443 in open_port) and  len(list_ports) > 2:
                return 1
            elif (80,443 in open_port) and len(list_ports) == 2:
                return -1
            else:
                return 1
        except Exception as e:
            print("err_port",e)
            return 0
                            
    def HTTPS_token(url):
        try:
            subDomain, domain, suffix = extract(url)
            host =subDomain +'.' + domain + '.' + suffix 
            if(host.count('https')): 
                return 1
            else:
                return -1
        except Exception as e:
            print("err_HTTPS_token",e)
            return 0

    def Request_URL(url):
        try:
            r = requests.get(url,timeout=7)
            html = r.text
            url_elems = extract(url)
            domain = url_elems[1] + "." + url_elems[2]
            
            regex_external = "(href=|src=)(\"|')((https|http)://)"

            links = regex.findall(regex_external,html)

            regex_all = "(href=|src=)(\"|')(.*?)(\"|')"
            total_links = len(regex.findall(regex_all,html))
            
            count_diff = 0 # number of external domains
            for link in links:
                domain_of_link = urlparse(link[2])[1]
                domain_elements = domain_of_link.split(".")
                domain_of_link = ".".join(domain_elements[len(domain_elements)-2:len(domain_elements)])
                count_diff += domain_of_link != domain
            if (total_links == 0):
                return 1
            
            diff_rate = count_diff / total_links
            
            if diff_rate < 0.22:
                return -1
            elif diff_rate <= 0.61:
                return 0
            else:
                return 1
        except Exception as e:
            print("err_Request_url",e)
            return 0
    
    def URL_of_Anchor(url):
        try:
            t1 = time.time()
            regex_str = "<a href=\".*?\""
            html = requests.get(url,timeout=7).text
            links_list = regex.findall(regex_str,html)
            count_internal = 0

            for link in links_list:
                if url_is_internal(link,url):
                    count_internal += 1
            
            if len(links_list) == 0:
                return 1

            count_anchor = len(links_list) - count_internal
            rate = count_anchor / len(links_list)
            if (rate < 0.31):
                return -1
            elif (0.31 <= rate <= 0.67):
                return 0
            else:
                return 1
        except Exception as e:
            print("err_URL_of_Anchor",e)
            return 0
    
    def Links_in_tags(url):
        return -1
    
    def SFH(url):
        # MrNA
        return -1
    
    def Submitting_to_email(url):
        # MrNA
        return -1

    def Abnormal_URL(url):
        try:
            w = whois.whois(url)
            if w.domain_name == None:
                return 1
            else:
                return -1
        except Exception as e:
            print("err_abnormal_url",e)
            return 1
    
    def Redirect(url):
        try:
            r = requests.get(url,timeout=7)
            redirections = len(r.history)

            if redirections <= 1:
                return -1
            elif redirections < 4:
                return 0
            else:
                return 1
        # still need to validate client redirecting sites
        except Exception as e:
            print("err_redirect",e)
            return 0
    
    def on_mouseover(url):
        try:
            html = requests.get(url,timeout=7).text
            soup = BeautifulSoup(html, 'html.parser')
            p = soup.find_all('script')
            result = 1
            strr = ""
            for jss in p:
                strr = strr + jss.text
            if "window.status" in strr:
                result = -1
            return result
        except Exception as e:
            print("err_onmouseover",e)
            return 1
    
    def RightClick(url):
        try:
            html = requests.get(url,timeout=7).text
            soup = BeautifulSoup(html, 'html.parser')
            p = soup.find_all('script')
            result = 1
            strr = ""
            for jss in p:
                strr = strr + jss.text
            if "contextmenu" in strr:
                result = -1
            return result
        except Exception as e:
            print("err_RighClick",e)
            return 0
    
    def popUpWidnow(url):
        try:
            html = requests.get(url,timeout=7).text
            soup = BeautifulSoup(html, 'html.parser')
            p = soup.find_all('script')
            result = 1
            strr = ""
            for jss in p:
                strr = strr + jss.text
            if "window.open" in strr:
                result = -1
            return result
        except Exception as e:
            print("err_popUpWindow",e)
            return 0
    
    def Iframe(url):
        try:
            html = requests.get(url,timeout=7).text
            if "</iframe>" in html:
                return -1
            else:
                return 1
        except Exception as e:
            print("err_Iframe")
            return 0
    
    def age_of_domain (url):
        try:
            w = whois.whois(url)
            start_date = w.creation_date
            current_date = datetime.datetime.now()

            if type(start_date) == list:
                start_date = start_date[-1]
        
            age =(current_date-start_date).days

            if(age>=180):
                return -1
            else:
                return 1
        except Exception as e:
            print("err_age_of_domain",e)
            return 1

    def DNSRecord(url):
        try: 
            try:
                result = dns.resolver.query(url, 'A')
                for i in result:
                    if i:
                        return -1  
            except:
                return 1
        except Exception as e:
            print("err_DNSRecord")    
            return 0

    def web_traffic(url):
        try:
            soup = bs4.BeautifulSoup(urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url='+url).read(),features="html.parser")
            if not hasattr(soup.popularity,'text'):
                return 1

            rank = int(soup.popularity['text'])
            if rank < 100000:
                return -1
            else:
                return 1
        except Exception as e:
            print("err_web_traffic",e)
            return 0

    def Page_Rank(url):
        try:
            URL = "https://openpagerank.com/api/v1.0/getPageRank"
            PARAMS = {'domains[]':'google.com'} 
            r=requests.get(URL,params=PARAMS, headers={'API-OPR':'8044swwk8og00wwgc8ogo80cocs00o0o4008kkg0'}, timeout=7)
            json_data = r.json()
            domainarray = json_data['response']
            target = domainarray[0]
            rank = target['rank']
            if rank=="None" or float(rank or 0.1)<0.2:
                return -1
            else:
                return 1
        except Exception as e:
            print("err_Page_Rank",e)
            return 0

    def Google_Index(url):
        try:
            r = requests.head("https://webcache.googleusercontent.com/search?q=cache:" + url, timeout=7)
            if r.status_code == 404:
                return -1
            else:
                return 1
        except Exception as e:
            print("err_google_index",e)
            return 0

    def Links_pointing_to_page(url): # backlinks
        # proxyht
        return -1

    def Statistical_report(url):
        # proxyht
        f = open("model/data/urls.csv","r",encoding="UTF-8")
        data = f.read().split("\n")
        
        if url in data:
            return 1
        else: 
            return -1
    
    
