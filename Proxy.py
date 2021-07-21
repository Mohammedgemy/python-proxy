import requests
import urllib.request
import random

 
useragents=["Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5"]

urlproxy = "http://free-proxy-list.net/"

 # lo dice il nome, questa funzione scarica i proxies
req = urllib.request.Request(urlproxy)       # qua impostiamo il sito da dove scaricare.
req.add_header("User-Agent", random.choice(useragents)) # siccome il format del sito e' identico sia
sourcecode = urllib.request.urlopen(req)                # per free-proxy-list.net che per socks-proxy.net,
part = str(sourcecode.read())                           # imposto la variabile urlproxy in base a cosa si sceglie.
part = part.split("<tbody>")
part = part[1].split("</tbody>")
part = part[0].split("<tr><td>")
for proxy in part:
    proxy = proxy.split("</td><td>")

    print(proxy)