# Proxy parser

#
# Example
```
from proxy_parser import main
a = await main()
# "type " need for getting proxy string
#  change proxy type to "socks4" or "http" if you use not socks5 proxy.
print(a)
```
##Result :
```
 "socks5://ip:port".
```
#
# **Requirements**
```
Python 3.7+
BeautifulSoup
aiothttp
asyncio
```
