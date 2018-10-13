from bs4 import BeautifulSoup
import requests
def Proxy (type):

  if type == "socks":


    if str( requests.get('http://www.gatherproxy.com/ru/sockslist')) == "<Response [200]>":
        a=pars()
        for i in a:
           a = {'http':i}
           try:
             requests.get("https://www.google.ru", proxies= a)
             return i
           except:
              continue



    if str(requests.get("https://www.socks-proxy.net/")) == "<Response [200]>":
         
         a = pars2()
         for i in a:
             a = {'http': i}
             try:
                 requests.get("https://www.google.ru", proxies=a)
                 return i
             except:
                 Proxy(type)

  elif type == "http":
      pass

def  pars ():
    url = 'http://www.gatherproxy.com/ru/sockslist'
    lis = [ (i*7)+2 for i  in  range(0,24)]
    try:
     r = requests.get(url)

     soup = BeautifulSoup(r.text, 'html.parser')

     td = soup.find('table', id='tblproxy').find_all('td')

     ip_list = []
     for  i in lis:

          tds = td[i:i+2]
          ip= str(tds[0].find_all('script'))
          port =str (tds[1].find_all('script'))
          ip=ip[53:67].replace("')",'').replace("'",'').replace('<',"")
          port = port[53:60].replace("')","").replace("<","")
          ip_list.append (f"soks5://{ip}:{port}")
     return ip_list
    except:
        pass


def pars2():
    try:
        url = 'https://www.socks-proxy.net/'
        ip_list = []
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

        except:
            return 'error1'
        ip = soup.find_all('td')

        for i in [5, 192]:
            ips = str(ip)[i:i + 13].replace("<", "").replace("/", "").replace(">", "").replace("d", '').replace('t', "")
            port = str(ip)[i + 24:i + 30].replace("<", "").replace("/", "").replace('t', '').replace(">", "").replace("d","")
            ip_list.append(f"socks4://{ips}:{port}")

        return ip_list

    except:
       return  ' error'
