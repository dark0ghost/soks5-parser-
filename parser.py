from bs4 import BeautifulSoup
import requests
import time


def Proxy(type):
    if type == "socks":
        if str(requests.get('http://www.gatherproxy.com/ru/sockslist')) == "<Response [200]>":
            return  socks5()
        if str(requests.get("https://www.socks-proxy.net/")) == "<Response [200]>":
            return  socks4()
    elif type == "http":
        return http()
    else:
        return  socks5()


def  socks5():
    url = 'http://www.gatherproxy.com/ru/sockslist'
    lis = [(i * 7) + 2 for i in range(0, 24)]
    soup = request(url)

    td = soup.find('table', id='tblproxy').find_all('td')

    ip_list = []
    for i in lis:
        tds = td[i:i + 2]
        ip = str(tds[0].find_all('script'))
        port = str(tds[1].find_all('script'))
        ip = ip[53:67].replace("')", '').replace("'", '').replace('<', "")
        port = port[53:60].replace("')", "").replace("<", "")
        ip_list.append(f"socks5://{ip}:{port}")
    return check_proxy(ip_list)


def  socks4():
    try:
        url = 'https://www.socks-proxy.net/'
        ip_list = []
        soup = request(url)
        ip = soup.find_all('td')

        for i in [5, 192]:
            ips = str(ip)[i:i + 13]\
                .replace("<", "")\
                .replace("/", "")\
                .replace(">", "")\
                .replace("d", '')\
                .replace('t', "")
            port = str(ip)[i + 24:i + 30]\
                .replace("<", "")\
                .replace("/", "")\
                .replace('t', '')\
                .replace(">", "")\
                .replace("d", "")
            ip_list.append(f"socks4://{ips}:{port}")
        return check_proxy(ip_list)
    except:
        with open('log101.log','w') as f:
           f.write(f"{time.ctime(time.time())}:pars")
           f.close()


def request(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    except:
        with open('log101.log', 'w') as f:
          f.write(f"{time.ctime(time.time())}:req")
          f.close()


def check_proxy(list):
    for i in list:
        a = {'http://': i}
        try:
          print('оброботка прокси')
          r = requests.get('http://api.telegram.org', proxies=a)
          if r.status_code == 200:
              return str(i)
        except:

            print('не прошло:',i)
            continue
    else:
        print('снова')
        socks5()
   

def http():
    url = "https://free.proxy-sale.com/?port%5B0%5D=http"
    soup = request(url)
    ip=str(soup.findAll('td',{'class':'bg-data'}))

    ip_list = []
    for i in [153,526,894]:
        ips = ip[i:i+20]\
            .replace('"','')\
            .replace("\n",'')\
            .replace("[p",'')\
            .replace("o",'')
        ip_list.append(ips)

    return check_proxy( ip_list)
def  socks_list():
    url = 'http://www.gatherproxy.com/ru/sockslist'
    lis = [(i * 7) + 2 for i in range(0, 24)]
    soup = request(url)

    td = soup.find('table', id='tblproxy').find_all('td')
    p = []
    ip_list = []
    for i in lis:
        tds = td[i:i + 2]
        ip = str(tds[0].find_all('script'))
        port = str(tds[1].find_all('script'))
        ip = ip[53:67]\
            .replace("')", '')\
            .replace("'", '')\
            .replace('<', "")
        port = port[53:60]\
            .replace("')", "")\
            .replace("<", "")
        ip_list.append(f"socks5://{ip}:{port}")

    for g in ip_list:
        a = {'http://': g}
        try:
          print('оброботка')
          r = requests.get('http://api.telegram.org', proxies=a)
          if r.status_code == 200:
             p.append(g)
        except:

            print('не прошло:',i)
            continue
    else:
        print('снова')
        socks_list()

    return p
