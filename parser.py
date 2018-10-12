from bs4 import BeautifulSoup
import requests
def Proxy (type):

  if type == "socks5":
     a=pars()
     for i in a:
         a = {'http':i}
         try:
           requests.get("https://www.google.com/", proxies= a)
           return i
         except:
            continue
  elif type == "http":
      pass
  elif type == "https":
      pass
  else:
      a = pars()
      for i in a:
          a = {'http': i}
          try:
              requests.get("https://www.google.com/", proxies=a)
              return i
          except:
              continue

def  pars ():
    url = 'http://www.gatherproxy.com/ru/sockslist'
    #url = 'http://spys.one/socks/'
    r= requests.get(url)
    lis = [ (i*7)+2 for i  in  range(0,24)]

    try:


     soup = BeautifulSoup(r.text, 'html.parser')
    except:
        return 0

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


