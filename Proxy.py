import urllib.request
import random
useragents=["Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5"]
urlproxy = "http://free-proxy-list.net/"
try:
    req = urllib.request.Request(("%s") % (urlproxy))       
    req.add_header("User-Agent", random.choice(useragents)) 
    sourcecode = urllib.request.urlopen(req)                
    part = str(sourcecode.read())                           
    part = part.split("<tbody>")
    part = part[1].split("</tbody>")
    part = part[0].split("<tr><td>")
    proxies = ""
    for proxy in part:
        proxy = proxy.split("</td><td>")
        try:
            proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
        except:
            pass
    out_file = open("proxy.txt","w")
    out_file.write("")
    out_file.write(proxies)
    out_file.close()
    print ("Proxies downloaded successfully.")
except: # se succede qualche casino
    print ("\nERROR!\n")
